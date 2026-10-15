"""Unit tests for the 5 AI/ML upgrades in agent.ml_services."""

import pytest
from agent.ml_services import (
    ANOMALY_DETECTOR,
    ROUTE_OPTIMIZER,
    SHELF_LIFE_PREDICTOR,
    SMART_MATCHING_RANKER,
    SURPLUS_FORECASTER,
)


def test_surplus_forecasting_normal():
    """Verify surplus forecaster outputs valid kg prediction and confidence intervals."""
    res = SURPLUS_FORECASTER.forecast(
        donor_id="donor-banquet-01",
        donor_category="banquet",
        rolling_7d_avg=60.0,
        event_intensity=1.5,
    )
    assert res.predicted_kg > 0
    assert res.confidence_interval_lower_kg <= res.predicted_kg <= res.confidence_interval_upper_kg
    assert res.confidence_score >= 0.80
    assert res.advance_notice_tier in ("HIGH_SURPLUS", "NORMAL", "LOW")


def test_shelf_life_danger_zone_and_escalation():
    """Verify shelf-life predictor triggers escalation when cooked food enters critical spoilage."""
    # Warm room temp, cooked food prepared 4 hours ago -> should breach safety threshold
    res = SHELF_LIFE_PREDICTOR.predict(
        food_type="prepared_meals",
        storage_temp_c=36.0,
        prep_elapsed_hours=4.0,
        packaging="open_exposed",
    )
    assert res.predicted_safe_hours < 1.0
    assert res.escalation_required is True
    assert "below mandatory safety threshold" in (res.escalation_reason or "")
    assert res.is_safe_for_dispatch is False


def test_shelf_life_refrigerated_safe():
    """Verify refrigerated food stays safe with no escalation required."""
    res = SHELF_LIFE_PREDICTOR.predict(
        food_type="dairy",
        storage_temp_c=3.0,
        prep_elapsed_hours=1.0,
        packaging="sealed_thermal",
        is_refrigerated=True,
    )
    assert res.predicted_safe_hours >= 10.0
    assert res.escalation_required is False
    assert res.is_safe_for_dispatch is True


def test_smart_matching_hybrid_score():
    """Verify smart matching blends deterministic factors with ML acceptance probability."""
    cand = SMART_MATCHING_RANKER.score_candidate(
        recipient_id="rec-shelter-01",
        recipient_name="Community Food Pantry",
        distance_km=2.5,
        donation_kg=30.0,
        recipient_capacity_kg=100.0,
        dietary_match=True,
        past_acceptance_rate=0.95,
    )
    assert 0.0 <= cand.ml_acceptance_probability <= 1.0
    assert 0.0 <= cand.deterministic_score <= 1.0
    assert 0.0 <= cand.hybrid_score <= 1.0
    # Close distance + high capacity should result in a high hybrid score
    assert cand.hybrid_score > 0.60


def test_route_optimizer_multi_stop():
    """Verify route optimizer solves pickup and dropoff sequencing with spoilage index."""
    pickups = [
        {"name": "Sarafa Vendor A", "lat": 22.7180, "lon": 75.8560, "quantity_kg": 20.0, "perishability_hours": 2.5},
        {"name": "56 Dukan Cafe", "lat": 22.7240, "lon": 75.8820, "quantity_kg": 15.0, "perishability_hours": 3.0},
    ]
    dropoffs = [
        {"name": "Geeta Bhawan Shelter", "lat": 22.7210, "lon": 75.8750, "capacity_kg": 50.0},
    ]

    res = ROUTE_OPTIMIZER.optimize_route(
        volunteer_start_lat=22.7196,
        volunteer_start_lon=75.8577,
        pickups=pickups,
        dropoffs=dropoffs,
        vehicle_max_capacity_kg=80.0,
    )
    assert len(res.ordered_stops) == 3
    assert res.total_distance_km > 0
    assert res.total_travel_time_minutes > 0
    assert 0.0 <= res.spoilage_risk_index <= 1.0


def test_anomaly_detection_normal_vs_abnormal():
    """Verify anomaly detector flags severe quantity spikes and unrealistic claims."""
    # Normal donation
    normal_eval = ANOMALY_DETECTOR.evaluate_donation(
        quantity_kg=25.0,
        perishability_hours=4.0,
        food_category="produce",
    )
    assert normal_eval.is_anomaly is False
    assert normal_eval.action in ("AUTO_APPROVE", "COORDINATOR_REVIEW")

    # Fraudulent / massive spike donation
    fraud_eval = ANOMALY_DETECTOR.evaluate_donation(
        quantity_kg=2500.0,  # 2500kg reported by 30kg average donor
        perishability_hours=96.0,  # cooked food claiming 96h
        food_category="prepared_meals",
        donor_historical_mean_kg=25.0,
        donor_historical_std_kg=5.0,
        reports_last_hour=8,
    )
    assert fraud_eval.is_anomaly is True
    assert fraud_eval.action == "FLAG_FOR_HUMAN"
    assert len(fraud_eval.flagged_reasons) >= 2
