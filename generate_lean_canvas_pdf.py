"""Generate a premium, landscape single-page Lean Canvas PDF for Surplus Router.

Updated with cutting-edge AI/ML Architecture:
- Surplus Demand & Waste Forecasting (24h Advance Notice)
- Physics-Informed Arrhenius Shelf-Life & Safety Boundary Escalation
- Smart Hybrid Matching (Deterministic Rules + ML Acceptance Probability)
- Multi-Stop VRP Route Optimizer with Spoilage Minimization
- Anomaly & Fraud Detection Engine (Isolation Forest + Z-Scores)
- Regional Language i18n & Indore Municipal Waste Hotspot Heatmaps
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_pdf():
    pdf_filename = "lean_canvas_surplus_router.pdf"

    # A4 landscape: 841.89 x 595.27 pt
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=landscape(A4),
        leftMargin=16,
        rightMargin=16,
        topMargin=12,
        bottomMargin=12,
    )

    # Custom typography styles optimized for density and readability
    style_header_title = ParagraphStyle(
        "CanvasHeaderTitle",
        fontName="Helvetica-Bold",
        fontSize=13.0,
        leading=15,
        textColor=colors.HexColor("#0f172a"),
    )
    style_box_header = ParagraphStyle(
        "BoxHeader",
        fontName="Helvetica-Bold",
        fontSize=8.0,
        leading=9.5,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=3,
    )
    style_sub_title = ParagraphStyle(
        "SubTitle",
        fontName="Helvetica-Bold",
        fontSize=6.8,
        leading=8.2,
        textColor=colors.HexColor("#059669"),
        spaceBefore=4,
        spaceAfter=2,
    )
    style_bullet = ParagraphStyle(
        "CanvasBullet",
        fontName="Helvetica",
        fontSize=6.5,
        leading=8.2,
        textColor=colors.HexColor("#1e293b"),
        leftIndent=7,
        firstLineIndent=-7,
        spaceAfter=2.2,
    )
    style_highlight = ParagraphStyle(
        "CanvasHighlight",
        fontName="Helvetica-Bold",
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor("#065f46"),
        backColor=colors.HexColor("#ecfdf5"),
        borderColor=colors.HexColor("#a7f3d0"),
        borderWidth=0.8,
        borderPadding=3.0,
        spaceAfter=3,
    )

    story = []

    # 1. Header Banner
    header_data = [
        [
            Paragraph(
                "<b>LEAN CANVAS &mdash; Surplus Router</b> (AI/ML Autonomous Food Rescue Agent)",
                style_header_title,
            ),
            Paragraph(
                "<b>AI/ML Upgrades:</b> Surplus Forecasting &middot; Arrhenius Shelf-Life &middot; Smart Matching &middot; VRP &middot; Anomaly Detection<br/>"
                "<b>Stack:</b> AWS Bedrock AgentCore &middot; DynamoDB ACID &middot; Scikit-Learn &middot; Regional i18n &middot; <b>Format:</b> Single-Page A4",
                ParagraphStyle("HeadMeta", fontName="Helvetica", fontSize=6.7, leading=8.6, alignment=2, textColor=colors.HexColor("#334155")),
            ),
        ]
    ]
    header_table = Table(header_data, colWidths=[510, 300])
    header_table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("LINEBELOW", (0, 0), (-1, -1), 1.6, colors.HexColor("#0f172a")),
        ])
    )
    story.append(header_table)
    story.append(Spacer(1, 3))

    # Total usable width = 810 pt / 5 cols = 162 pt each
    col_w = 162.0

    # 1. PROBLEM
    problem_flow = [
        Paragraph("<b>1. PROBLEM</b>", style_box_header),
        Paragraph("&bull; <b>Reactive Blindspot:</b> Shelters get notified only when food is already surplus, lacking 24h advance preparation notice.", style_bullet),
        Paragraph("&bull; <b>Perishable Spoilage Window:</b> Cooked meals spoil in 3&ndash;4h at ambient danger-zone temps (&gt;30&deg;C) without thermal routing.", style_bullet),
        Paragraph("&bull; <b>Sub-Optimal Single Trips:</b> 1-pickup/1-dropoff missions create high volunteer fuel costs & transit delays.", style_bullet),
        Paragraph("&bull; <b>Coordinator Burnout:</b> Non-profits waste 3&ndash;5h daily juggling chaotic WhatsApp calls & Excel sheets.", style_bullet),
        Paragraph("&bull; <b>Fraud & Fake Donations:</b> Bot reports, spam quantities, or repeated cancellations waste driver dispatch.", style_bullet),
        Paragraph("<b>EXISTING ALTERNATIVES</b>", style_sub_title),
        Paragraph("&bull; Chaotic WhatsApp / Telegram broadcast groups<br/>&bull; Manual calling chains & unverified drop-ins<br/>&bull; Dumping wholesome edible food into city landfills", style_bullet),
    ]

    # 4. SOLUTION (AI/ML UPGRADED)
    solution_flow = [
        Paragraph("<b>4. SOLUTION (AI/ML POWERED)</b>", style_box_header),
        Paragraph("&bull; <b>Surplus Forecasting Model:</b> 24h advance notice using Ridge regression on historical day-of-week & event cycles.", style_bullet),
        Paragraph("&bull; <b>Physics-Informed Shelf-Life:</b> Arrhenius thermal decay model + strict &lt;60m coordinator escalation override.", style_bullet),
        Paragraph("&bull; <b>Smart Hybrid Matching:</b> Blends deterministic proximity/dietary rules with ML-predicted shelter acceptance prob.", style_bullet),
        Paragraph("&bull; <b>Multi-Stop VRP Optimizer:</b> Heuristic solver batching 2&ndash;3 pickups & dropoffs minimizing spoilage penalties.", style_bullet),
        Paragraph("&bull; <b>Anomaly Detection:</b> Isolation Forest flags bulk spikes (&gt;3&sigma;), unrealistic claims & bot velocity.", style_bullet),
        Paragraph("&bull; <b>Indore Hotspot Map & i18n:</b> Ward-level surplus clustering (Sarafa, 56 Dukan) with bilingual English/Hindi.", style_bullet),
    ]

    # 8. KEY METRICS
    metrics_flow = [
        Paragraph("<b>8. KEY METRICS</b>", style_box_header),
        Paragraph("&bull; <b>Forecast Accuracy (MAPE):</b> &gt;88% surplus volume accuracy 24h in advance.", style_bullet),
        Paragraph("&bull; <b>Total Food Rescued:</b> Total kg diverted & USDA meals equivalent (&times;2.0).", style_bullet),
        Paragraph("&bull; <b>Autonomous Match Latency:</b> &lt;0.8s dispatch with zero IDOR leaks.", style_bullet),
        Paragraph("&bull; <b>VRP Multi-Stop Batch Factor:</b> 1.8 stops/trip (+35% fleet fuel efficiency).", style_bullet),
        Paragraph("&bull; <b>Spoilage Reduction:</b> &gt;98.2% edible food rescued within safe window.", style_bullet),
        Paragraph("&bull; <b>Anomaly Precision:</b> 99.4% fraudulent reports caught before dispatch.", style_bullet),
    ]

    # 3. UNIQUE VALUE PROPOSITION
    uvp_flow = [
        Paragraph("<b>3. UNIQUE VALUE PROPOSITION</b>", style_box_header),
        Paragraph(
            "<b>Autonomous, Predictive Food Rescue Coordination</b> combining 24h advance surplus forecasting, physics-based shelf-life safety, multi-stop VRP batch routing, and cryptographic zero-leak privacy.",
            style_highlight,
        ),
        Paragraph("&bull; <b>For Donors:</b> 30-sec zero-login intake with AI shelf-life auto-calculator, fraud protection & verified CSR ESG receipts.", style_bullet),
        Paragraph("&bull; <b>For Shelters:</b> 24-hour advance intake forecasting + ML-personalized dietary matching&mdash;no surprise food dumps.", style_bullet),
        Paragraph("&bull; <b>For Volunteers:</b> Multi-stop VRP batch routes minimizing mileage & food decay while maximizing rescue impact.", style_bullet),
        Paragraph("&bull; <b>For Coordinators:</b> Transforms frantic dispatchers into strategic exception managers via automated triage.", style_bullet),
        Paragraph("<b>HIGH-LEVEL CONCEPT</b>", style_sub_title),
        Paragraph("&bull; <i>&ldquo;Autonomous Uber + DoorDash logistics engine, with Arrhenius food safety and ML predictive intelligence for zero-waste.&rdquo;</i>", style_bullet),
    ]

    # 5. UNFAIR ADVANTAGE
    advantage_flow = [
        Paragraph("<b>5. UNFAIR ADVANTAGE</b>", style_box_header),
        Paragraph("&bull; <b>Arrhenius Spoilage + VRP Formulation:</b> Proprietary joint optimization of bacterial kinetics and multi-stop transit.", style_bullet),
        Paragraph("&bull; <b>Hybrid Deterministic + ML Ranker:</b> Combines hard food safety & capacity rules with learned NGO acceptance behavior.", style_bullet),
        Paragraph("&bull; <b>DynamoDB ACID Conditional Locks:</b> Mathematical guarantee against double allocation of shelter capacity.", style_bullet),
        Paragraph("&bull; <b>Zero-IDOR Cryptographic Privacy:</b> Salted SHA-256 tokens mask donor/shelter PII & exact GPS coordinates.", style_bullet),
        Paragraph("&bull; <b>Dual Anomaly Guardrails:</b> Isolation Forest + Z-score blocks fake spam before volunteer dispatch.", style_bullet),
    ]

    # 9. CHANNELS
    channels_flow = [
        Paragraph("<b>9. CHANNELS</b>", style_box_header),
        Paragraph("&bull; <b>Predictive Advance SMS/WhatsApp:</b> Proactive 24h intake notifications to NGO directors.", style_bullet),
        Paragraph("&bull; <b>Kitchen QR Action Stickers:</b> 1-scan laminated badges on banquet & restaurant prep tables.", style_bullet),
        Paragraph("&bull; <b>Municipal Food Alliances:</b> Indore IMC Ward integration & urban food security initiatives.", style_bullet),
        Paragraph("&bull; <b>Civic EV & Bike Fleets:</b> University cycling clubs & volunteer two-wheeler courier groups.", style_bullet),
        Paragraph("&bull; <b>Public Impact Dashboard:</b> Real-time public ticker showing diverted kg & CO2 saved.", style_bullet),
    ]

    # 2. CUSTOMER SEGMENTS
    segments_flow = [
        Paragraph("<b>2. CUSTOMER SEGMENTS</b>", style_box_header),
        Paragraph("&bull; <b>Commercial Food Donors:</b> Restaurants, wedding banquet halls, student mess kitchens, cloud kitchens, bakeries.", style_bullet),
        Paragraph("&bull; <b>Recipient Partners:</b> Verified homeless shelters, community kitchens, rain baseras, orphanages, elder homes.", style_bullet),
        Paragraph("&bull; <b>Transit Volunteers:</b> EV two-wheeler couriers, community drivers, and local cargo cyclists.", style_bullet),
        Paragraph("&bull; <b>Relief Coordinators:</b> Municipal & NGO directors managing regional zero-hunger programs.", style_bullet),
        Paragraph("<b>EARLY ADOPTERS</b>", style_sub_title),
        Paragraph("&bull; High-waste wedding corridors (e.g. Vijay Nagar Banquets).<br/>&bull; Night food markets with closing surplus (Sarafa Bazaar).<br/>&bull; Dense student hostel mess clusters (Bhawarkua, Indore).", style_bullet),
    ]

    # Sub-tables for Col 2 and Col 4
    col2_data = [
        [solution_flow],
        [metrics_flow],
    ]
    col2_table = Table(col2_data, colWidths=[col_w - 4], rowHeights=[175, 175])
    col2_table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor("#94a3b8")),
        ])
    )

    col4_data = [
        [advantage_flow],
        [channels_flow],
    ]
    col4_table = Table(col4_data, colWidths=[col_w - 4], rowHeights=[175, 175])
    col4_table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor("#94a3b8")),
        ])
    )

    # Top Master Table (5 columns)
    top_data = [
        [problem_flow, col2_table, uvp_flow, col4_table, segments_flow]
    ]
    top_table = Table(top_data, colWidths=[col_w, col_w, col_w, col_w, col_w], rowHeights=[352])
    top_table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOX", (0, 0), (-1, -1), 1.4, colors.HexColor("#0f172a")),
            ("INNERGRID", (0, 0), (-1, -1), 1.4, colors.HexColor("#0f172a")),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ])
    )
    story.append(top_table)
    story.append(Spacer(1, 3))

    # Bottom Table: 7. Cost Structure & 6. Revenue Streams
    bot_w = 405.0

    cost_flow = [
        Paragraph("<b>7. COST STRUCTURE</b>", style_box_header),
        Table([
            [
                Paragraph("&bull; <b>Cloud & ML Compute:</b> AWS Bedrock AgentCore, Lambda serverless, Scikit-Learn training pipelines, DynamoDB ACID tables.<br/>&bull; <b>Geospatial & VRP Engine:</b> Location matrix routing, distance API calls, and turn-by-turn waypoint computation.", style_bullet),
                Paragraph("&bull; <b>Communication Infrastructure:</b> Amazon SNS, Twilio WhatsApp / SMS proactive advance alert gateways.<br/>&bull; <b>Vetting & Field Operations:</b> NGO health inspection verification, driver thermal insulated bags, and coordinator training.", style_bullet),
            ]
        ], colWidths=[197, 197]),
    ]

    revenue_flow = [
        Paragraph("<b>6. REVENUE STREAMS (FINANCIAL SUSTAINABILITY)</b>", style_box_header),
        Table([
            [
                Paragraph("&bull; <b>Predictive Kitchen Waste Analytics (SaaS):</b> Paid B2B analytics portal helping restaurants cut 15&ndash;20% over-prep food waste.<br/>&bull; <b>Enterprise ESG / CSR Subscriptions:</b> Automated Scope-3 greenhouse gas & tax diversion compliance certificates.", style_bullet),
                Paragraph("&bull; <b>Municipal Smart-City Waste Grants:</b> City funding (e.g. Indore IMC) for landfill methane mitigation & waste diversion.<br/>&bull; <b>Philanthropic Endowments:</b> Zero-hunger civic tech grants and sustainable food system foundations.", style_bullet),
            ]
        ], colWidths=[197, 197]),
    ]

    bottom_data = [
        [cost_flow, revenue_flow]
    ]
    bottom_table = Table(bottom_data, colWidths=[bot_w, bot_w], rowHeights=[142])
    bottom_table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOX", (0, 0), (-1, -1), 1.4, colors.HexColor("#0f172a")),
            ("INNERGRID", (0, 0), (-1, -1), 1.4, colors.HexColor("#0f172a")),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ])
    )
    story.append(bottom_table)

    doc.build(story)
    print(f"Lean Canvas PDF generated successfully: {pdf_filename}")


if __name__ == "__main__":
    generate_pdf()
