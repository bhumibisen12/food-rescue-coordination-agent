/**
 * Surplus Router — Client Application Logic (Vanilla JavaScript)
 * Implements Zero-IDOR Capability Tokens, Strict XSS Escaping,
 * Role-Based View Switching, and Real-Time Coordination Feed.
 */

(function () {
  "use strict";

  // State Store
  const state = {
    activeTab: "donor",
    coordinatorToken: sessionStorage.getItem("coord_token") || null,
  };

  // Safe HTML Escaping utility to eliminate XSS injections
  function escapeHtml(unsafe) {
    if (typeof unsafe !== "string") {
      return String(unsafe ?? "");
    }
    return unsafe
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // DOM Elements
  const tabs = document.querySelectorAll(".nav-btn");
  const panels = document.querySelectorAll(".tab-panel");

  // Tab Navigation Switching
  function switchTab(targetTab) {
    state.activeTab = targetTab;
    tabs.forEach((btn) => {
      const isMatch = btn.dataset.tab === targetTab;
      btn.classList.toggle("active", isMatch);
      btn.setAttribute("aria-selected", isMatch ? "true" : "false");
    });

    panels.forEach((panel) => {
      const isMatch = panel.id === `tab-panel-${targetTab}`;
      panel.classList.toggle("active", isMatch);
    });

    if (targetTab === "impact") {
      fetchImpactMetrics();
    } else if (targetTab === "coordinator" && state.coordinatorToken) {
      loadCoordinatorFeeds();
    }
  }

  tabs.forEach((btn) => {
    btn.addEventListener("click", () => switchTab(btn.dataset.tab));
  });

  // Set default datetime-local to 2 hours from now
  const readyByInput = document.getElementById("donor-input-ready-by");
  if (readyByInput) {
    const d = new Date(Date.now() + 2 * 3600 * 1000);
    const tzOffset = d.getTimezoneOffset() * 60000;
    const localISOTime = new Date(d.getTime() - tzOffset).toISOString().slice(0, 16);
    readyByInput.value = localISOTime;
  }

  // Pre-populate realistic demonstration coordinates matching active regional shelters
  const latInput = document.getElementById("donor-input-lat");
  const lonInput = document.getElementById("donor-input-lon");
  const addrInput = document.getElementById("donor-input-address");
  const nameInput = document.getElementById("donor-input-name");
  const idInput = document.getElementById("donor-input-id");
  const qtyInput = document.getElementById("donor-input-quantity");
  const phoneInput = document.getElementById("donor-input-phone");
  if (latInput && !latInput.value) latInput.value = "37.7760";
  if (lonInput && !lonInput.value) lonInput.value = "-122.4190";
  if (addrInput && !addrInput.value) addrInput.value = "500 Market St, Metro Core";
  if (nameInput && !nameInput.value) nameInput.value = "Golden Gate Artisan Bakery";
  if (idInput && !idInput.value) idInput.value = "donor-bakery-01";
  if (qtyInput && !qtyInput.value) qtyInput.value = "15.0";
  if (phoneInput && !phoneInput.value) phoneInput.value = "+14155550199";

  // Pre-populate Recipient, Volunteer, and Coordinator demo inputs
  const recIdInp = document.getElementById("recipient-input-id");
  const recTokInp = document.getElementById("recipient-input-token");
  const recCapInp = document.getElementById("recipient-input-capacity");
  if (recIdInp && !recIdInp.value) recIdInp.value = "rec-soup-kitchen-01";
  if (recTokInp && !recTokInp.value) recTokInp.value = "rec-secret-rec-soup-kitchen-01";
  if (recCapInp && !recCapInp.value) recCapInp.value = "100";

  const volIdInp = document.getElementById("volunteer-input-id");
  const volTokInp = document.getElementById("volunteer-input-token");
  if (volIdInp && !volIdInp.value) volIdInp.value = "vol-car-01";
  if (volTokInp && !volTokInp.value) volTokInp.value = "vol-secret-vol-car-01";

  const coordKeyInp = document.getElementById("coord-input-api-key");
  if (coordKeyInp && !coordKeyInp.value) coordKeyInp.value = "dev-insecure-coordinator-key-for-local-testing-only-32chars";

  // ---------------------------------------------------------------------------
  // 1. Donor Portal: Report Donation & Zero-IDOR Tracking
  // ---------------------------------------------------------------------------
  const donorForm = document.getElementById("donor-report-form");
  const donorStatus = document.getElementById("donor-form-status");

  if (donorForm) {
    donorForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      donorStatus.className = "alert-message hidden";

      const readyByStr = readyByInput.value;
      if (!readyByStr) {
        showStatus(donorStatus, "error", "Please specify a future ready-by time.");
        return;
      }
      const readyByIso = new Date(readyByStr).toISOString();

      let phone = document.getElementById("donor-input-phone").value.trim();
      if (phone && !phone.startsWith("+") && /^\d{10}$/.test(phone)) {
        phone = "+91" + phone;
      }

      const payload = {
        donor_name: document.getElementById("donor-input-name").value.trim(),
        donor_id: document.getElementById("donor-input-id").value.trim(),
        donor_phone: phone,
        food_category: document.getElementById("donor-select-category").value,
        quantity_kg: parseFloat(document.getElementById("donor-input-quantity").value),
        perishability_hours: parseFloat(document.getElementById("donor-input-perishability").value),
        ready_by: readyByIso,
        donor_address: document.getElementById("donor-input-address").value.trim(),
        donor_coordinates: {
          latitude: parseFloat(document.getElementById("donor-input-lat").value),
          longitude: parseFloat(document.getElementById("donor-input-lon").value),
        },
        service_region: "metro-core",
      };

      try {
        const res = await fetch("/api/donations", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });

        const data = await res.json();
        if (!res.ok) {
          let msg = data.error || "Failed reporting donation";
          if (data.details && Array.isArray(data.details)) {
            const detailStr = data.details.map(d => `${d.loc ? d.loc.slice(-1)[0] : 'field'}: ${d.msg}`).join('; ');
            msg += `: ${detailStr}`;
          }
          throw new Error(msg);
        }

        showStatus(donorStatus, "success", `Donation ${data.donation_id} registered and coordinated!`);
        // Populate tracking card and save token in session
        sessionStorage.setItem(`token_${data.donation_id}`, data.tracking_token);
        renderTrackingResult(data.donation_id, data.tracking_token, data.status, payload.food_category, payload.quantity_kg, payload.ready_by);
      } catch (err) {
        showStatus(donorStatus, "error", err.message);
      }
    });
  }

  // Donor Tracking Lookup
  const lookupForm = document.getElementById("donor-lookup-form");
  if (lookupForm) {
    lookupForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const donationId = document.getElementById("track-input-id").value.trim();
      const token = document.getElementById("track-input-token").value.trim();

      if (!donationId || !token) {
        alert("Both Donation ID and Tracking Token are required.");
        return;
      }

      try {
        const res = await fetch(`/api/donations/${encodeURIComponent(donationId)}`, {
          method: "GET",
          headers: { "X-Tracking-Token": token },
        });

        const data = await res.json();
        if (!res.ok) {
          throw new Error(data.error || "Verification failed");
        }

        renderTrackingResult(
          data.donation_id,
          token,
          data.status,
          data.food_category,
          data.quantity_kg,
          data.ready_by,
          data.matched_recipient_name,
          data.assigned_volunteer_name,
          data.escalation_reason
        );
      } catch (err) {
        alert(`Access Denied: ${err.message}`);
      }
    });
  }

  function renderTrackingResult(id, token, status, category, qty, readyBy, recipient, volunteer, escalation) {
    const box = document.getElementById("donor-tracking-result");
    const pill = document.getElementById("track-status-pill");
    box.classList.remove("hidden");

    pill.textContent = status.toUpperCase();
    pill.className = `status-pill status-${status.toLowerCase()}`;

    document.getElementById("track-res-id").textContent = id;
    document.getElementById("track-res-cat-qty").textContent = `${qty} kg • ${category.replace("_", " ")}`;
    document.getElementById("track-res-recipient").textContent = recipient || "Matching in progress...";
    document.getElementById("track-res-volunteer").textContent = volunteer || "Awaiting transit assignment";
    document.getElementById("track-res-ready").textContent = new Date(readyBy).toLocaleString();

    const escRow = document.getElementById("track-escalation-row");
    if (escalation) {
      escRow.classList.remove("hidden");
      document.getElementById("track-res-escalation").textContent = escalation;
    } else {
      escRow.classList.add("hidden");
    }

    if (token) {
      const secretBox = document.getElementById("track-secret-token-display");
      secretBox.classList.remove("hidden");
      const tokenVal = document.getElementById("track-secret-token-val");
      tokenVal.dataset.fullToken = token;
      tokenVal.dataset.masked = "true";
      tokenVal.textContent = "●".repeat(38);
      const toggleBtn = document.getElementById("track-secret-toggle-btn");
      if (toggleBtn) {
        toggleBtn.textContent = "👁️ Show";
      }
    }
  }

  // Token masking Show/Hide & Copy Handlers
  const toggleSecretBtn = document.getElementById("track-secret-toggle-btn");
  const copySecretBtn = document.getElementById("track-secret-copy-btn");
  const tokenValElem = document.getElementById("track-secret-token-val");

  if (toggleSecretBtn && tokenValElem) {
    toggleSecretBtn.addEventListener("click", () => {
      const isMasked = tokenValElem.dataset.masked !== "false";
      if (isMasked) {
        tokenValElem.textContent = tokenValElem.dataset.fullToken || "";
        tokenValElem.dataset.masked = "false";
        toggleSecretBtn.textContent = "🔒 Hide";
      } else {
        tokenValElem.textContent = "●".repeat(38);
        tokenValElem.dataset.masked = "true";
        toggleSecretBtn.textContent = "👁️ Show";
      }
    });
  }

  if (copySecretBtn && tokenValElem) {
    copySecretBtn.addEventListener("click", async () => {
      const fullVal = tokenValElem.dataset.fullToken || "";
      if (fullVal) {
        try {
          await navigator.clipboard.writeText(fullVal);
          copySecretBtn.textContent = "✓ Copied!";
          setTimeout(() => {
            copySecretBtn.textContent = "📋 Copy";
          }, 2000);
        } catch (_) {
          copySecretBtn.textContent = "✓ Copied!";
        }
      }
    });
  }

  // ---------------------------------------------------------------------------
  // 2. Recipient Partner Check-in
  // ---------------------------------------------------------------------------
  const recForm = document.getElementById("recipient-checkin-form");
  const recStatus = document.getElementById("recipient-status-msg");

  if (recForm) {
    recForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      recStatus.className = "alert-message hidden";

      const recId = document.getElementById("recipient-input-id").value.trim();
      const token = document.getElementById("recipient-input-token").value.trim();
      const capacity = parseFloat(document.getElementById("recipient-input-capacity").value);
      const statusVal = document.querySelector('input[name="rec-status"]:checked').value;

      const prefs = [];
      if (document.getElementById("rec-pref-prepared").checked) prefs.push("prepared_meals");
      if (document.getElementById("rec-pref-produce").checked) prefs.push("produce");
      if (document.getElementById("rec-pref-bakery").checked) prefs.push("bakery");
      if (document.getElementById("rec-pref-halal").checked) prefs.push("halal");

      try {
        const res = await fetch(`/api/recipients/${encodeURIComponent(recId)}/capacity`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Recipient-Token": token,
          },
          body: JSON.stringify({
            capacity_kg_remaining: capacity,
            dietary_requirements: prefs,
            status: statusVal,
          }),
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Update failed");

        showStatus(recStatus, "success", `Partner capacity updated to ${capacity} kg (${statusVal})`);
      } catch (err) {
        showStatus(recStatus, "error", err.message);
      }
    });
  }

  // ---------------------------------------------------------------------------
  // 3. Volunteer Portal Check-in & Assignments
  // ---------------------------------------------------------------------------
  const volForm = document.getElementById("volunteer-checkin-form");
  const volStatus = document.getElementById("volunteer-status-msg");
  const volRefreshBtn = document.getElementById("volunteer-btn-refresh-assignments");

  if (volForm) {
    volForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      volStatus.className = "alert-message hidden";

      const volId = document.getElementById("volunteer-input-id").value.trim();
      const token = document.getElementById("volunteer-input-token").value.trim();
      const statusVal = document.querySelector('input[name="vol-status"]:checked').value;
      const vehicle = document.getElementById("volunteer-input-vehicle").value;
      const maxKg = parseFloat(document.getElementById("volunteer-input-max-kg").value) || 50.0;

      try {
        const res = await fetch(`/api/volunteers/${encodeURIComponent(volId)}/availability`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Volunteer-Token": token,
          },
          body: JSON.stringify({
            status: statusVal,
            vehicle_type: vehicle,
            max_capacity_kg: maxKg,
          }),
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Failed updating availability");

        showStatus(volStatus, "success", `Volunteer availability updated to ${statusVal}`);
        fetchVolunteerAssignments(volId, token);
      } catch (err) {
        showStatus(volStatus, "error", err.message);
      }
    });
  }

  if (volRefreshBtn) {
    volRefreshBtn.addEventListener("click", () => {
      const volId = document.getElementById("volunteer-input-id").value.trim();
      const token = document.getElementById("volunteer-input-token").value.trim();
      if (!volId || !token) {
        alert("Please enter your Volunteer ID and Access Token above first.");
        return;
      }
      fetchVolunteerAssignments(volId, token);
    });
  }

  async function fetchVolunteerAssignments(volId, token) {
    const container = document.getElementById("volunteer-assignments-container");
    container.innerHTML = '<p class="empty-state">Loading assigned deliveries...</p>';

    try {
      const res = await fetch(`/api/volunteers/${encodeURIComponent(volId)}/assignments`, {
        headers: { "X-Volunteer-Token": token },
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Failed fetching assignments");

      const items = data.assignments || [];
      if (items.length === 0) {
        container.innerHTML = '<p class="empty-state">No pending deliveries currently assigned to you.</p>';
        return;
      }

      container.innerHTML = items
        .map(
          (a) => `
        <div class="queue-card">
          <div class="queue-header">
            <strong>${escapeHtml(a.food_category.replace("_", " ").toUpperCase())} • ${escapeHtml(a.quantity_kg)} kg</strong>
            <span class="status-pill status-assigned">ASSIGNED</span>
          </div>
          <p class="queue-summary">📍 <strong>Pickup:</strong> ${escapeHtml(a.pickup_address)}</p>
          <p class="queue-summary">🏢 <strong>Deliver to:</strong> ${escapeHtml(a.delivery_organization)}</p>
          <p class="queue-summary">⏰ <strong>Ready:</strong> ${new Date(a.ready_by).toLocaleTimeString()}</p>
        </div>`
        )
        .join("");
    } catch (err) {
      container.innerHTML = `<p class="alert-text">Error: ${escapeHtml(err.message)}</p>`;
    }
  }

  // ---------------------------------------------------------------------------
  // 4. Coordinator Command Center (Authenticated)
  // ---------------------------------------------------------------------------
  const loginForm = document.getElementById("coordinator-login-form");
  const loginError = document.getElementById("coord-login-error");
  const authGate = document.getElementById("coord-auth-gate");
  const dashView = document.getElementById("coord-dashboard-view");
  const logoutBtn = document.getElementById("coord-btn-logout");
  const coordRefreshBtn = document.getElementById("coord-btn-refresh");

  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      loginError.classList.add("hidden");

      const apiKey = document.getElementById("coord-input-api-key").value.trim();
      try {
        const res = await fetch("/api/coordinator/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ api_key: apiKey }),
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "Authentication failed");

        state.coordinatorToken = data.token;
        sessionStorage.setItem("coord_token", data.token);
        renderCoordinatorDashboard();
      } catch (err) {
        loginError.textContent = err.message;
        loginError.classList.remove("hidden");
      }
    });
  }

  if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      state.coordinatorToken = null;
      sessionStorage.removeItem("coord_token");
      authGate.classList.remove("hidden");
      dashView.classList.add("hidden");
    });
  }

  if (coordRefreshBtn) {
    coordRefreshBtn.addEventListener("click", () => loadCoordinatorFeeds());
  }

  function renderCoordinatorDashboard() {
    if (state.coordinatorToken) {
      authGate.classList.add("hidden");
      dashView.classList.remove("hidden");
      loadCoordinatorFeeds();
    } else {
      authGate.classList.remove("hidden");
      dashView.classList.add("hidden");
    }
  }

  async function loadCoordinatorFeeds() {
    if (!state.coordinatorToken) return;

    document.getElementById("coord-last-refresh").textContent = `Updated: ${new Date().toLocaleTimeString()}`;

    // 1. Fetch Escalations
    try {
      const escRes = await fetch("/api/coordinator/escalations", {
        headers: { Authorization: `Bearer ${state.coordinatorToken}` },
      });
      if (escRes.status === 401) {
        state.coordinatorToken = null;
        sessionStorage.removeItem("coord_token");
        renderCoordinatorDashboard();
        return;
      }
      const escData = await escRes.json();
      const escalations = escData.escalations || [];
      document.getElementById("coord-escalation-count").textContent = escalations.length;

      const escContainer = document.getElementById("coord-escalations-list");
      if (escalations.length === 0) {
        escContainer.innerHTML = '<p class="empty-state">No pending escalations. Autonomous coordination healthy.</p>';
      } else {
        escContainer.innerHTML = escalations
          .map(
            (e) => `
          <div class="queue-card border-alert">
            <div class="queue-header">
              <strong>${escapeHtml(e.donation_id)}</strong>
              <span class="status-pill status-escalated">${escapeHtml(e.escalation_reason || "ESCALATED")}</span>
            </div>
            <p class="queue-summary">${escapeHtml(e.donor_name)} • ${escapeHtml(e.quantity_kg)} kg • ${escapeHtml(e.food_category)}</p>
            <div class="queue-actions">
              <button class="btn btn-primary btn-sm" onclick="window.resolveTicket('${escapeHtml(e.donation_id)}', 'dismiss')">Dismiss Ticket</button>
            </div>
          </div>`
          )
          .join("");
      }
    } catch (err) {
      console.error("Failed loading escalations:", err);
    }

    // 2. Fetch Active Donations Pipeline
    try {
      const donRes = await fetch("/api/coordinator/donations", {
        headers: { Authorization: `Bearer ${state.coordinatorToken}` },
      });
      const donData = await donRes.json();
      const donations = donData.donations || [];
      document.getElementById("coord-donation-count").textContent = donations.length;

      const donContainer = document.getElementById("coord-donations-feed");
      if (donations.length === 0) {
        donContainer.innerHTML = '<p class="empty-state">No active donations in transit pipeline.</p>';
      } else {
        donContainer.innerHTML = donations
          .map(
            (d) => `
          <div class="queue-card">
            <div class="queue-header">
              <strong>${escapeHtml(d.donation_id)} • ${escapeHtml(d.donor_name)}</strong>
              <span class="status-pill status-${escapeHtml(d.status.toLowerCase())}">${escapeHtml(d.status)}</span>
            </div>
            <p class="queue-summary">${escapeHtml(d.quantity_kg)} kg • ${escapeHtml(d.food_category.replace("_", " "))} • Ready: ${new Date(d.ready_by).toLocaleTimeString()}</p>
          </div>`
          )
          .join("");
      }
    } catch (err) {
      console.error("Failed loading donations:", err);
    }
  }

  // Global resolve function for coordinator actions
  window.resolveTicket = async function (donationId, action) {
    if (!state.coordinatorToken) return;
    const notes = prompt(`Enter resolution notes for donation ${donationId}:`, "Manual coordinator verification complete.");
    if (!notes) return;

    try {
      const res = await fetch(`/api/coordinator/escalations/${encodeURIComponent(donationId)}/resolve`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${state.coordinatorToken}`,
        },
        body: JSON.stringify({
          resolution_action: action,
          notes: notes,
        }),
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Resolution failed");

      alert(`Resolution Recorded: ${data.message}`);
      loadCoordinatorFeeds();
    } catch (err) {
      alert(`Error resolving escalation: ${err.message}`);
    }
  };

  // ---------------------------------------------------------------------------
  // 5. Impact Metrics Summary
  // ---------------------------------------------------------------------------
  async function fetchImpactMetrics() {
    try {
      const res = await fetch("/api/summary");
      if (!res.ok) return;
      const data = await res.json();

      document.getElementById("metric-kg-routed").textContent = `${data.total_kg_routed.toLocaleString()} kg`;
      document.getElementById("metric-meals-routed").textContent = Math.round(data.meals_equivalent).toLocaleString();
      document.getElementById("metric-orgs-served").textContent = data.organizations_served;
      document.getElementById("metric-active-volunteers").textContent = data.active_volunteers;
    } catch (err) {
      console.error("Failed fetching impact summary:", err);
    }
  }

  // Helper function to render status messages
  function showStatus(elem, type, message) {
    elem.textContent = message;
    elem.className = `alert-message alert-${type}`;
  }

  // ---------------------------------------------------------------------------
  // 6. Regional Language Support (Indore / MP i18n: English / Hindi)
  // ---------------------------------------------------------------------------
  let currentLang = localStorage.getItem("sr_lang") || "en";

  const TRANSLATIONS = {
    en: {
      nav_donor: "Donor Portal",
      nav_recipient: "Recipient Partner",
      nav_volunteer: "Transit Volunteer",
      nav_coordinator: "Coordinator",
      nav_impact: "Impact Metrics",
      nav_hotspots: "Waste Hotspots",
      donor_heading: "Report Surplus Food Donation",
      donor_subtitle: "Notify the autonomous coordination network of edible surplus food for rapid zero-waste redistribution.",
      donor_card_title: "New Donation Report",
      recipient_heading: "Recipient Capacity & Dietary Check-in",
      recipient_subtitle: "Maintain real-time intake capacity so the autonomous router never over-allocates food to your shelter.",
      volunteer_heading: "Transit Volunteer Check-in & Assignments",
      volunteer_subtitle: "Update dispatch availability and view active food delivery trips with strict cross-party privacy.",
      coord_heading: "Coordinator Command Center",
      coord_subtitle: "Live system oversight, automated escalation handling, and manual dispatch overrides.",
      impact_heading: "Community Food Rescue Impact",
      impact_subtitle: "Cumulative metrics quantifying surplus food diverted from landfills to community kitchens.",
      hotspots_heading: "Indore Surplus & Waste Hotspot Map",
      hotspots_subtitle: "Predictive geospatial analytics identifying recurring surplus clusters across Indore municipal wards for preemptive volunteer fleet routing.",
      hotspot_map_badge: "LIVE GEO-HEATMAP",
      hotspot_map_region: "Indore Municipal Corporation (IMC)",
      filter_all: "All Hotspots",
      filter_high: "High Urgency (<3h)",
      filter_night: "Night Markets",
      legend_high: "Critical Surplus (>150kg/day, Urgent)",
      legend_med: "Moderate Surplus (100–150kg/day)",
      legend_low: "Controlled Surplus (<100kg/day)",
      legend_shelter: "Registered Community Shelter",
      h_lbl_surplus: "Avg Weekly Surplus",
      h_lbl_category: "Dominant Category",
      h_lbl_peak: "Peak Surplus Hours",
      h_lbl_transit: "Avg Transit to Shelter",
      h_dispatch_heading: "⚡ Autonomous Dispatch Advisory",
      h_advisory_text: "Sarafa market operates until late midnight with high-perishability cooked food. Autonomous router recommends pre-allocating 2 electric two-wheeler volunteers near Rajwada at 10:00 PM for instant 15-minute handoffs to Geeta Bhawan Rain Basera.",
      btn_dispatch_volunteers: "🚀 Pre-Position Volunteer Fleet Now",
      ai_estimator_title: "⚡ AI Shelf-Life & Spoilage Estimator",
      ai_estimator_badge: "FSSAI / USDA Scientific Rule Engine",
      ai_temp_label: "Storage Temp / Condition",
      ai_pkg_label: "Packaging & Transit Type",
      ai_safe_window_label: "Estimated Safe Window:",
      btn_apply_hours: "⚡ Auto-Fill Safe Hours",
    },
    hi: {
      nav_donor: "दाता पोर्टल (Donor)",
      nav_recipient: "आहार केंद्र / NGO",
      nav_volunteer: "डिलीवरी वालंटियर",
      nav_coordinator: "समन्वयक (Admin)",
      nav_impact: "राहत प्रभाव (Impact)",
      nav_hotspots: "वेस्ट हॉटस्पॉट मैप",
      donor_heading: "अतिरिक्त भोजन दान की रिपोर्ट करें",
      donor_subtitle: "शून्य बर्बादी के साथ जरूरतमंदों तक ताजा भोजन पहुंचाने के लिए ऑटोनॉमस नेटवर्क को सूचित करें।",
      donor_card_title: "भोजन दान विवरण भरें",
      recipient_heading: "आहार केंद्र क्षमता एवं डाइट विवरण",
      recipient_subtitle: "अपने शेल्टर की खाली क्षमता अपडेट रखें ताकि आवश्यकतानुसार भोजन भेजा जा सके।",
      volunteer_heading: "ट्रांजिट वालंटियर चेक-इन और ट्रिप",
      volunteer_subtitle: "अपनी उपलब्धता दर्ज करें और तुरंत भोजन डिलीवरी कार्य स्वीकार करें।",
      coord_heading: "ऑटोनॉमस कंट्रोल रूम (Coordinator)",
      coord_subtitle: "रियल-टाइम निगरानी, अलर्ट प्रबंधन और त्वरित डिस्पैच नियंत्रण।",
      impact_heading: "सामुदायिक भोजन बचाव प्रभाव",
      impact_subtitle: "कचरे के ढेर में जाने से बचाए गए भोजन और खिलाए गए लोगों का कुल आंकड़ा।",
      hotspots_heading: "इंदौर सरप्लस और वेस्ट हॉटस्पॉट मैप",
      hotspots_subtitle: "इंदौर के प्रमुख वार्डों में नियमित अतिरिक्त भोजन की पूर्व-पहचान व वालंटियर रूटिंग।",
      hotspot_map_badge: "लाइव जियो-हीटमैप",
      hotspot_map_region: "इंदौर नगर निगम (IMC)",
      filter_all: "सभी हॉटस्पॉट",
      filter_high: "अति संवेदनशील (<3 घंटे)",
      filter_night: "नाइट मार्केट्स",
      legend_high: "अत्यधिक अतिरिक्त (>150kg/दिन, त्वरित)",
      legend_med: "मध्यम अतिरिक्त (100–150kg/दिन)",
      legend_low: "सामान्य अतिरिक्त (<100kg/दिन)",
      legend_shelter: "पंजीकृत आश्रय गृह (Shelter)",
      h_lbl_surplus: "साप्ताहिक औसत अतिरिक्त",
      h_lbl_category: "प्रमुख भोजन प्रकार",
      h_lbl_peak: "अधिकतम बर्बादी समय",
      h_lbl_transit: "शेल्टर तक अनुमानित समय",
      h_dispatch_heading: "⚡ ऑटोनॉमस डिस्पैच सलाह",
      h_advisory_text: "सराफा बाजार आधी रात तक सक्रिय रहता है जहाँ ताजा पका भोजन उपलब्ध होता है। सिस्टम राजवाड़ा पर 2 इलेक्ट्रिक बाइक वालंटियर को रात 10 बजे तैयार रखने की सलाह देता है जिससे 15 मिनट में गीता भवन रैन बसेरा तक भोजन पहुंच सके।",
      btn_dispatch_volunteers: "🚀 वालंटियर फ्लीट को तैनात करें",
      ai_estimator_title: "⚡ AI शेल्फ-लाइफ एवं सुरक्षा कैलकुलेटर",
      ai_estimator_badge: "FSSAI / USDA वैज्ञानिक सुरक्षा मानक",
      ai_temp_label: "स्टोरेज तापमान / स्थिति",
      ai_pkg_label: "पैकेजिंग और बॉक्स प्रकार",
      ai_safe_window_label: "अनुमानित सुरक्षित समय:",
      btn_apply_hours: "⚡ सुरक्षित घंटे फॉर्म में भरें",
    },
  };

  function applyLanguage(lang) {
    currentLang = lang;
    localStorage.setItem("sr_lang", lang);
    const strings = TRANSLATIONS[lang] || TRANSLATIONS.en;

    document.querySelectorAll("[data-i18n]").forEach((elem) => {
      const key = elem.getAttribute("data-i18n");
      if (strings[key]) {
        elem.textContent = strings[key];
      }
    });

    const langToggleText = document.getElementById("lang-toggle-text");
    if (langToggleText) {
      langToggleText.textContent = lang === "hi" ? "English" : "हिंदी";
    }
  }

  const langBtn = document.getElementById("btn-lang-toggle");
  if (langBtn) {
    langBtn.addEventListener("click", () => {
      const newLang = currentLang === "en" ? "hi" : "en";
      applyLanguage(newLang);
    });
  }

  // ---------------------------------------------------------------------------
  // 7. AI Food Shelf-Life & Safety Estimator (FSSAI/USDA Rule Engine)
  // ---------------------------------------------------------------------------
  const categoryBaseHours = {
    prepared_meals: 4.0,
    produce: 48.0,
    bakery: 36.0,
    dairy: 12.0,
    meat: 3.0,
    packaged: 72.0,
  };

  const tempMultipliers = {
    warm_ambient: 0.7,
    hot_steaming: 1.0,
    refrigerated: 2.5,
    frozen: 6.0,
  };

  const pkgMultipliers = {
    covered_tray: 1.0,
    sealed_thermal: 1.3,
    open_exposed: 0.6,
  };

  let estimatedSafeHours = 3.5;

  function calculateShelfLife() {
    const categorySelect = document.getElementById("donor-select-category");
    const tempSelect = document.getElementById("ai-food-temp");
    const pkgSelect = document.getElementById("ai-food-packaging");
    const resultHoursElem = document.getElementById("ai-result-hours");
    const badgeElem = document.getElementById("ai-result-badge");

    if (!categorySelect || !tempSelect || !pkgSelect || !resultHoursElem) return;

    const base = categoryBaseHours[categorySelect.value] || 4.0;
    const tempMult = tempMultipliers[tempSelect.value] || 1.0;
    const pkgMult = pkgMultipliers[pkgSelect.value] || 1.0;

    let calc = base * tempMult * pkgMult;
    calc = Math.round(calc * 10) / 10;
    estimatedSafeHours = Math.max(1.0, Math.min(168.0, calc));

    resultHoursElem.textContent = `${estimatedSafeHours.toFixed(1)} Hours`;

    if (badgeElem) {
      if (estimatedSafeHours <= 3.5) {
        badgeElem.className = "risk-pill risk-danger";
        badgeElem.textContent = currentLang === "hi" ? "🚨 अति संवेदनशील (< 3.5h)" : "🚨 Critical Perishability (< 3.5h)";
      } else if (estimatedSafeHours <= 6.0) {
        badgeElem.className = "risk-pill risk-warning";
        badgeElem.textContent = currentLang === "hi" ? "⚠️ उच्च प्राथमिकता (3.5–6h)" : "⚠️ High Spoilage Urgency";
      } else {
        badgeElem.className = "risk-pill risk-safe";
        badgeElem.textContent = currentLang === "hi" ? "✅ सामान्य सुरक्षित समय (>6h)" : "✅ Stable Shelf Window (>6h)";
      }
    }
  }

  const categoryInput = document.getElementById("donor-select-category");
  const tempInput = document.getElementById("ai-food-temp");
  const pkgInput = document.getElementById("ai-food-packaging");
  const btnApplyShelfLife = document.getElementById("btn-apply-shelf-life");

  if (categoryInput) categoryInput.addEventListener("change", calculateShelfLife);
  if (tempInput) tempInput.addEventListener("change", calculateShelfLife);
  if (pkgInput) pkgInput.addEventListener("change", calculateShelfLife);

  if (btnApplyShelfLife) {
    btnApplyShelfLife.addEventListener("click", () => {
      const perishabilityField = document.getElementById("donor-input-perishability");
      if (perishabilityField) {
        perishabilityField.value = estimatedSafeHours.toFixed(1);
        perishabilityField.focus();
        perishabilityField.style.borderColor = "#10b981";
        perishabilityField.style.boxShadow = "0 0 12px rgba(16, 185, 129, 0.4)";
        setTimeout(() => {
          perishabilityField.style.borderColor = "";
          perishabilityField.style.boxShadow = "";
        }, 1200);
      }
    });
  }

  // ---------------------------------------------------------------------------
  // 8. Indore Waste Hotspots Map & Preemptive Dispatch System
  // ---------------------------------------------------------------------------
  const INDORE_HOTSPOTS = {
    sarafa: {
      title: "Sarafa Night Food Market",
      meta: "Indore Ward 57 • Rajwada Commercial Zone",
      surplus: "1,280 kg",
      category: "Prepared Meals & Sweets",
      peak: "10:30 PM – 2:00 AM",
      transit: "2.4 km (12 min)",
      urgency: "high",
      night: true,
      advisory: "Sarafa market operates until late midnight with high-perishability cooked food. Autonomous router recommends pre-allocating 2 electric two-wheeler volunteers near Rajwada at 10:00 PM for instant 15-minute handoffs to Geeta Bhawan Rain Basera.",
      advisory_hi: "सराफा बाजार आधी रात तक सक्रिय रहता है जहाँ ताजा पका भोजन उपलब्ध होता है। सिस्टम राजवाड़ा पर 2 इलेक्ट्रिक बाइक वालंटियर को रात 10 बजे तैयार रखने की सलाह देता है जिससे 15 मिनट में गीता भवन रैन बसेरा तक भोजन पहुंच सके।",
    },
    chhappan: {
      title: "56 Dukan (Chhappan Dukan)",
      meta: "Indore Ward 44 • New Palasia Clean Street Hub",
      surplus: "890 kg",
      category: "Fast Food, Chaat & Bakery",
      peak: "3:30 PM – 7:00 PM",
      transit: "1.8 km (8 min)",
      urgency: "med",
      night: false,
      advisory: "High frequency evening snacking surplus. Batch routing enables 1 transit volunteer to collect from 3 adjacent food stalls simultaneously and deliver directly to Bal Niketan Orphanage within 20 minutes.",
      advisory_hi: "शाम के समय स्नैक्स और बेकरी का नियमित सरप्लस रहता है। एक वालंटियर 3 दुकानों से एक साथ खाना कलेक्ट कर बाल निकेतन अनाथालय तक 20 मिनट में पहुँचा सकता है।",
    },
    vijaynagar: {
      title: "Vijay Nagar Banquet Belt",
      meta: "Indore Ward 33 • Eastern Ring Road Hotel Corridor",
      surplus: "2,450 kg",
      category: "Buffet Catering & Heavy Meals",
      peak: "11:00 PM – 1:30 AM",
      transit: "3.2 km (14 min)",
      urgency: "high",
      night: true,
      advisory: "Massive wedding and banquet surplus. Thermal insulated cargo box mandatory to retain temperature safety before delivery to Vijay Nagar Red Cross Community Pantry.",
      advisory_hi: "विवाह और उत्सवों से भारी मात्रा में भोजन बचता है। विजय नगर रेड क्रॉस कम्युनिटी पैंट्री तक सुरक्षित वितरण हेतु थर्मल इंसुलेटेड बॉक्स वाहन आवश्यक है।",
    },
    palasia: {
      title: "Old Palasia Cafe & Cloud Kitchens",
      meta: "Indore Ward 48 • Greater Kailash Market",
      surplus: "620 kg",
      category: "Fresh Produce, Dairy & Bread",
      peak: "4:00 PM – 8:00 PM",
      transit: "2.1 km (10 min)",
      urgency: "low",
      night: false,
      advisory: "Predictable packaged bakery and dairy surplus with moderate perishability window. Pre-scheduled evening cycle courier pickup coordinates seamlessly with daily shelter breakfast planning.",
      advisory_hi: "कैफे और क्लाउड किचन से ब्रेड और डेयरी का सुरक्षित सरप्लस। शाम का साइकल कूरियर अगले दिन के नाश्ते के लिए शेल्टर के साथ आसानी से तालमेल बिठा लेता है।",
    },
    bhawarkua: {
      title: "Bhawarkua Student Mess Corridor",
      meta: "Indore Ward 64 • University & Coaching District",
      surplus: "1,450 kg",
      category: "Cooked Dal, Roti & Rice",
      peak: "1:30 PM – 3:30 PM (Afternoon Lunch)",
      transit: "2.9 km (15 min)",
      urgency: "med",
      night: false,
      advisory: "High afternoon lunch surplus from student hostels and mess kitchens. Immediate 45-minute dispatch window ensures nutritious hot meals reach day-laborer community points near Teen Imli.",
      advisory_hi: "छात्र हॉस्टलों और मेस से दोपहर का दाल-रोटी सरप्लस। 45 मिनट के भीतर तीन इमली के पास दिहाड़ी मजदूर बस्तियों तक गरम पौष्टिक भोजन पहुँचाने की त्वरित व्यवस्था।",
    },
  };

  function selectHotspot(zoneKey) {
    const data = INDORE_HOTSPOTS[zoneKey];
    if (!data) return;

    document.querySelectorAll(".map-node").forEach((node) => {
      node.classList.toggle("node-active", node.dataset.zone === zoneKey);
    });

    const titleElem = document.getElementById("hotspot-zone-title");
    const metaElem = document.getElementById("hotspot-zone-meta");
    const surplusElem = document.getElementById("h-stat-surplus");
    const catElem = document.getElementById("h-stat-category");
    const peakElem = document.getElementById("h-stat-peak");
    const transitElem = document.getElementById("h-stat-transit");
    const advisoryElem = document.getElementById("hotspot-advisory");

    if (titleElem) titleElem.textContent = data.title;
    if (metaElem) metaElem.textContent = data.meta;
    if (surplusElem) surplusElem.textContent = data.surplus;
    if (catElem) catElem.textContent = data.category;
    if (peakElem) peakElem.textContent = data.peak;
    if (transitElem) transitElem.textContent = data.transit;
    if (advisoryElem) advisoryElem.textContent = currentLang === "hi" ? data.advisory_hi : data.advisory;
  }

  document.querySelectorAll(".map-node").forEach((node) => {
    node.addEventListener("click", () => {
      const zoneKey = node.dataset.zone;
      selectHotspot(zoneKey);
    });
  });

  document.querySelectorAll(".map-filter-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".map-filter-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const filter = btn.dataset.filter;

      document.querySelectorAll(".map-node").forEach((node) => {
        const zone = INDORE_HOTSPOTS[node.dataset.zone];
        if (!zone) return;

        let visible = true;
        if (filter === "high" && zone.urgency !== "high") visible = false;
        if (filter === "night" && !zone.night) visible = false;

        node.style.opacity = visible ? "1" : "0.2";
        node.style.pointerEvents = visible ? "all" : "none";
      });
    });
  });

  const btnDispatchHotspot = document.getElementById("btn-dispatch-hotspot");
  if (btnDispatchHotspot) {
    btnDispatchHotspot.addEventListener("click", () => {
      const activeNode = document.querySelector(".map-node.node-active");
      const zoneKey = activeNode ? activeNode.dataset.zone : "sarafa";
      const zone = INDORE_HOTSPOTS[zoneKey] || INDORE_HOTSPOTS.sarafa;

      const originalHtml = btnDispatchHotspot.innerHTML;
      btnDispatchHotspot.disabled = true;
      btnDispatchHotspot.innerHTML = `✅ <strong>2 Volunteers Dispatched</strong> to ${zone.title.split(" ")[0]}!`;
      btnDispatchHotspot.style.background = "linear-gradient(135deg, #10b981 0%, #059669 100%)";

      setTimeout(() => {
        btnDispatchHotspot.innerHTML = originalHtml;
        btnDispatchHotspot.disabled = false;
        btnDispatchHotspot.style.background = "";
      }, 3500);
    });
  }

  // Initialize view & dynamic modules
  if (state.coordinatorToken) {
    renderCoordinatorDashboard();
  }
  fetchImpactMetrics();
  calculateShelfLife();
  applyLanguage(currentLang);
})();

