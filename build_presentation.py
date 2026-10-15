"""Generate an executive-level, professional 12-slide PowerPoint presentation for Surplus Router.

Includes personalized intro slide for Bhumeshwari Bisen, Machine Learning & Applied AI Intern.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Refined Executive Color Palette
COLOR_DARK_BG = RGBColor(11, 19, 43)        # Deep Midnight Navy (#0B132B)
COLOR_DARK_CARD = RGBColor(23, 37, 68)      # Elevated Dark Slate (#172544)
COLOR_DARK_BORDER = RGBColor(46, 64, 104)   # Subtle Border (#2E4068)

COLOR_LIGHT_BG = RGBColor(248, 250, 252)    # Slate 50 (#F8FAFC)
COLOR_WHITE = RGBColor(255, 255, 255)       # Pure White
COLOR_LIGHT_BORDER = RGBColor(226, 232, 240)# Slate 200

COLOR_EMERALD = RGBColor(16, 185, 129)      # Vibrant Emerald (#10B981)
COLOR_EMERALD_DARK = RGBColor(5, 150, 105)  # Dark Emerald (#059669)
COLOR_EMERALD_LIGHT = RGBColor(209, 250, 229)# Soft Mint (#D1FAE5)
COLOR_EMERALD_TEXT = RGBColor(6, 95, 70)    # Deep Mint Text (#065F46)

COLOR_CYAN = RGBColor(14, 165, 233)         # Sky Blue (#0EA5E9)
COLOR_CYAN_LIGHT = RGBColor(224, 242, 254)  # Light Sky (#E0F2FE)
COLOR_CYAN_TEXT = RGBColor(3, 105, 161)     # Deep Sky Text (#0369A1)

COLOR_INDIGO = RGBColor(99, 102, 241)       # Indigo (#6366F1)
COLOR_AMBER = RGBColor(245, 158, 11)        # Warm Amber (#F59E0B)
COLOR_CORAL = RGBColor(239, 68, 68)         # Crimson Coral (#EF4444)

COLOR_TEXT_MAIN = RGBColor(15, 23, 42)      # Slate 900
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)  # Slate 500
COLOR_TEXT_LIGHT = RGBColor(248, 250, 252)  # Slate 50
COLOR_TEXT_MUTED_LIGHT = RGBColor(148, 163, 184) # Slate 400

FONT_NAME = "Segoe UI"


class DeckBuilder:
    """Helper class to construct stylish, consistent widescreen PowerPoint slides."""

    def __init__(self, filename="Surplus_Router_Presentation.pptx"):
        self.filename = filename
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]

    def add_blank_slide(self, dark=False):
        """Add a slide with clean background color."""
        slide = self.prs.slides.add_slide(self.blank_layout)
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5)
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_DARK_BG if dark else COLOR_LIGHT_BG
        bg.line.fill.background()
        return slide

    def add_header(self, slide, category, title, subtitle, dark=False):
        """Add modern executive header banner."""
        # Top Accent Line
        accent = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.35), Inches(0.6), Inches(0.06)
        )
        accent.fill.solid()
        accent.fill.fore_color.rgb = COLOR_EMERALD
        accent.line.fill.background()

        # Category Pill
        pill = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(0.28), Inches(2.6), Inches(0.32)
        )
        pill.fill.solid()
        pill.fill.fore_color.rgb = COLOR_DARK_CARD if dark else COLOR_EMERALD_LIGHT
        pill.line.fill.background()
        
        tf_pill = pill.text_frame
        tf_pill.word_wrap = True
        tf_pill.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_pill = tf_pill.paragraphs[0]
        p_pill.text = category.upper()
        p_pill.font.name = FONT_NAME
        p_pill.font.size = Pt(8.5)
        p_pill.font.bold = True
        p_pill.font.color.rgb = COLOR_EMERALD if dark else COLOR_EMERALD_TEXT
        p_pill.alignment = PP_ALIGN.CENTER

        # Main Title & Subtitle in single text box to prevent overlap
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(1.1))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0

        p_t = tf_title.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_NAME
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_LIGHT if dark else COLOR_TEXT_MAIN
        p_t.space_after = Pt(2)

        p_s = tf_title.add_paragraph()
        p_s.text = subtitle
        p_s.font.name = FONT_NAME
        p_s.font.size = Pt(10.5)
        p_s.font.color.rgb = COLOR_TEXT_MUTED_LIGHT if dark else COLOR_TEXT_MUTED

    def add_card(self, slide, left, top, width, height, dark=False, highlight_border=None, fill_color=None):
        """Create a rounded rectangular card container with optional custom fill."""
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
        )
        card.fill.solid()
        if fill_color:
            card.fill.fore_color.rgb = fill_color
        else:
            card.fill.fore_color.rgb = COLOR_DARK_CARD if dark else COLOR_WHITE
        
        if highlight_border:
            card.line.color.rgb = highlight_border
            card.line.width = Pt(1.5)
        else:
            card.line.color.rgb = COLOR_DARK_BORDER if dark else COLOR_LIGHT_BORDER
            card.line.width = Pt(1.0)
        return card

    def save(self):
        """Save PowerPoint deck to disk."""
        self.prs.save(self.filename)
        print(f"Presentation saved successfully to: {self.filename}")


def build_full_deck():
    builder = DeckBuilder("Surplus_Router_Presentation.pptx")

    # =========================================================================
    # SLIDE 1: INTRO & PRESENTER TITLE SLIDE (Personalized for Bhumeshwari Bisen)
    # =========================================================================
    s1 = builder.add_blank_slide(dark=True)

    # Top Brand Bar
    brand_pill = s1.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(4.5), Inches(0.35)
    )
    brand_pill.fill.solid()
    brand_pill.fill.fore_color.rgb = COLOR_DARK_CARD
    brand_pill.line.color.rgb = COLOR_EMERALD
    brand_pill.line.width = Pt(1.0)
    bp_tf = brand_pill.text_frame
    bp_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    bp_p = bp_tf.paragraphs[0]
    bp_p.text = "AWS 'AGENTS FOR HUMANS' HACKATHON | GOOD NEIGHBOR TRACK"
    bp_p.font.name = FONT_NAME
    bp_p.font.size = Pt(8.5)
    bp_p.font.bold = True
    bp_p.font.color.rgb = COLOR_EMERALD
    bp_p.alignment = PP_ALIGN.CENTER

    # Left Column: Project Title & Value Proposition (Width = 7.2 in)
    tb_left = s1.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(7.2), Inches(3.8))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True

    p_proj = tf_l.paragraphs[0]
    p_proj.text = "Surplus Router"
    p_proj.font.name = FONT_NAME
    p_proj.font.size = Pt(44)
    p_proj.font.bold = True
    p_proj.font.color.rgb = COLOR_TEXT_LIGHT
    p_proj.space_after = Pt(4)

    p_sub = tf_l.add_paragraph()
    p_sub.text = "Autonomous Food Rescue Coordination Agent"
    p_sub.font.name = FONT_NAME
    p_sub.font.size = Pt(19)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_CYAN
    p_sub.space_after = Pt(14)

    p_desc = tf_l.add_paragraph()
    p_desc.text = "An autonomous background agent that diverts commercial food surplus to community shelters before it spoils -- executing sub-second multi-factor routing, atomic DynamoDB capacity reservations, and zero-IDOR privacy protection."
    p_desc.font.name = FONT_NAME
    p_desc.font.size = Pt(11.5)
    p_desc.font.color.rgb = COLOR_TEXT_MUTED_LIGHT
    p_desc.space_after = Pt(20)

    # Core Capabilities row on left
    caps = [
        ("< 1.0s Latency", COLOR_EMERALD),
        ("100% ACID Locks", COLOR_CYAN),
        ("Zero Double-Claims", COLOR_AMBER),
    ]
    for idx, (cap_text, cap_color) in enumerate(caps):
        cpill = s1.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + idx * Inches(2.35), Inches(4.5), Inches(2.2), Inches(0.4)
        )
        cpill.fill.solid()
        cpill.fill.fore_color.rgb = COLOR_DARK_CARD
        cpill.line.color.rgb = cap_color
        cpill.line.width = Pt(1.0)
        c_tf = cpill.text_frame
        c_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        c_p = c_tf.paragraphs[0]
        c_p.text = cap_text
        c_p.font.name = FONT_NAME
        c_p.font.size = Pt(9.5)
        c_p.font.bold = True
        c_p.font.color.rgb = cap_color
        c_p.alignment = PP_ALIGN.CENTER

    # Right Column: Presenter Profile Card (Width = 4.3 in)
    p_card = builder.add_card(
        s1, Inches(8.3), Inches(0.6), Inches(4.2), Inches(4.3),
        dark=True, highlight_border=COLOR_EMERALD
    )

    tb_pres = s1.shapes.add_textbox(Inches(8.6), Inches(0.85), Inches(3.6), Inches(3.8))
    tf_p = tb_pres.text_frame
    tf_p.word_wrap = True

    # Presenter Tag
    pp_tag = tf_p.paragraphs[0]
    pp_tag.text = "PROJECT LEAD & PRESENTER"
    pp_tag.font.name = FONT_NAME
    pp_tag.font.size = Pt(9)
    pp_tag.font.bold = True
    pp_tag.font.color.rgb = COLOR_EMERALD
    pp_tag.space_after = Pt(10)

    # Name
    pp_name = tf_p.add_paragraph()
    pp_name.text = "Bhumeshwari Bisen"
    pp_name.font.name = FONT_NAME
    pp_name.font.size = Pt(23)
    pp_name.font.bold = True
    pp_name.font.color.rgb = COLOR_TEXT_LIGHT
    pp_name.space_after = Pt(4)

    # Position
    pp_pos = tf_p.add_paragraph()
    pp_pos.text = "Machine Learning & Applied AI Intern"
    pp_pos.font.name = FONT_NAME
    pp_pos.font.size = Pt(12)
    pp_pos.font.bold = True
    pp_pos.font.color.rgb = COLOR_CYAN
    pp_pos.space_after = Pt(12)

    # College / Institution
    pp_inst_label = tf_p.add_paragraph()
    pp_inst_label.text = "INSTITUTION:"
    pp_inst_label.font.name = FONT_NAME
    pp_inst_label.font.size = Pt(8.5)
    pp_inst_label.font.bold = True
    pp_inst_label.font.color.rgb = COLOR_TEXT_MUTED_LIGHT

    pp_inst = tf_p.add_paragraph()
    pp_inst.text = "Indore Institute of Science & Technology"
    pp_inst.font.name = FONT_NAME
    pp_inst.font.size = Pt(11)
    pp_inst.font.color.rgb = COLOR_TEXT_LIGHT
    pp_inst.space_after = Pt(16)

    # Core Stack Tagline
    pp_focus_label = tf_p.add_paragraph()
    pp_focus_label.text = "TECHNICAL ARCHITECTURE:"
    pp_focus_label.font.name = FONT_NAME
    pp_focus_label.font.size = Pt(8.5)
    pp_focus_label.font.bold = True
    pp_focus_label.font.color.rgb = COLOR_TEXT_MUTED_LIGHT

    pp_focus = tf_p.add_paragraph()
    pp_focus.text = "Amazon Bedrock | Strands Agents SDK | DynamoDB ACID"
    pp_focus.font.name = FONT_NAME
    pp_focus.font.size = Pt(9.5)
    pp_focus.font.bold = True
    pp_focus.font.color.rgb = COLOR_EMERALD

    # Bottom Full-Width Metric Banner
    banner = builder.add_card(s1, Inches(0.8), Inches(5.25), Inches(11.7), Inches(1.6), dark=True, highlight_border=COLOR_DARK_BORDER)
    b_metrics = [
        ("< 1.0s", "Autonomous Dispatch Latency", COLOR_EMERALD),
        ("157 / 157", "Tests Passing (100% Quality Gate)", COLOR_CYAN),
        ("3 to 5 Hours", "Daily Coordinator Time Saved", COLOR_AMBER),
        ("Zero-IDOR", "Cryptographic Privacy Engine", COLOR_TEXT_LIGHT),
    ]
    mw = Inches(2.7)
    for i, (m_val, m_lbl, m_col) in enumerate(b_metrics):
        mx = Inches(1.0) + i * Inches(2.9)
        tb_m = s1.shapes.add_textbox(mx, Inches(5.45), Inches(2.6), Inches(1.2))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        
        pm1 = tf_m.paragraphs[0]
        pm1.text = m_val
        pm1.font.name = FONT_NAME
        pm1.font.size = Pt(22)
        pm1.font.bold = True
        pm1.font.color.rgb = m_col
        pm1.space_after = Pt(2)

        pm2 = tf_m.add_paragraph()
        pm2.text = m_lbl
        pm2.font.name = FONT_NAME
        pm2.font.size = Pt(9.5)
        pm2.font.color.rgb = COLOR_TEXT_MUTED_LIGHT

    # =========================================================================
    # SLIDE 2: THE HUMANITARIAN & LOGISTICS CRISIS (Problem)
    # =========================================================================
    s2 = builder.add_blank_slide(dark=False)
    builder.add_header(s2, "The Real-World Crisis", "The Food Recovery Paradox: Food Decays While Shelters Starve", "Why manual coordination fails in the critical 3-to-4 hour perishable safety window")

    cards_p = [
        ("The Spoilage Clock", "3–4 Hours Perishability Window", 
         "Commercial kitchens produce hot prepared meals and dairy daily. If not picked up and cold-stored within 3-4 hours, food health regulations require dumping it in landfills.",
         COLOR_CORAL, "CRITICAL WINDOW"),
        ("The Coordination Grind", "3–5 Hours Lost per Coordinator", 
         "Non-profit coordinators frantically juggle WhatsApp groups, phone trees, and Excel sheets trying to find an open shelter and an available driver before food spoils.",
         COLOR_AMBER, "OPERATIONAL BURNOUT"),
        ("Zero Real-Time Visibility", "Double Allocations & Food Dumps", 
         "Shelters lack real-time intake tracking. Uncoordinated volunteer drops lead to overloaded fridges, rejected donations, or simultaneous double-claims.",
         COLOR_CYAN, "BLIND LOGISTICS"),
    ]
    cw = Inches(3.7)
    cgap = Inches(0.3)
    cy = Inches(1.9)

    for i, (title, highlight, desc, col, badge_text) in enumerate(cards_p):
        cx = Inches(0.8) + i * (cw + cgap)
        builder.add_card(s2, cx, cy, cw, Inches(4.9), dark=False, highlight_border=col)
        
        # Pill badge
        badge = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.3), cy + Inches(0.3), Inches(2.2), Inches(0.32))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.fill.background()
        bp = badge.text_frame.paragraphs[0]
        bp.text = badge_text
        bp.font.name = FONT_NAME
        bp.font.size = Pt(8)
        bp.font.bold = True
        bp.font.color.rgb = COLOR_WHITE
        bp.alignment = PP_ALIGN.CENTER

        tx = s2.shapes.add_textbox(cx + Inches(0.3), cy + Inches(0.8), cw - Inches(0.6), Inches(3.8))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_NAME
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MAIN
        p1.space_after = Pt(6)

        p2 = tf.add_paragraph()
        p2.text = highlight
        p2.font.name = FONT_NAME
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = col
        p2.space_after = Pt(12)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_NAME
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = COLOR_TEXT_MUTED
        p3.space_after = Pt(10)

    # =========================================================================
    # SLIDE 3: INTRODUCING SURPLUS ROUTER (The Solution)
    # =========================================================================
    s3 = builder.add_blank_slide(dark=False)
    builder.add_header(s3, "The Autonomous Solution", "Surplus Router: Background AI Dispatch Engine", "Autonomous multi-factor matching, instant driver routing, and human-in-the-loop exception handling")

    # Left: Traditional Flow (Red/Grey Card)
    builder.add_card(s3, Inches(0.8), Inches(1.9), Inches(5.6), Inches(5.0), highlight_border=COLOR_CORAL)
    tx_old = s3.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.5))
    tf_old = tx_old.text_frame
    tf_old.word_wrap = True

    p_old_h = tf_old.paragraphs[0]
    p_old_h.text = "Traditional Manual Process (3-5 Hours):"
    p_old_h.font.name = FONT_NAME
    p_old_h.font.size = Pt(14)
    p_old_h.font.bold = True
    p_old_h.font.color.rgb = COLOR_CORAL
    p_old_h.space_after = Pt(10)

    steps_old = [
        "1. Restaurant reports surplus via WhatsApp text.",
        "2. Coordinator calls Shelter A -> No answer.",
        "3. Coordinator calls Shelter B -> Walk-in fridge is full.",
        "4. Coordinator calls Shelter C -> Can take 15kg, but vegetarian only.",
        "5. Coordinator texts 6 drivers to find who is available.",
        "6. Result: 2.5 hours elapse -> Shelf-life window expires! ❌ Food Wasted.",
    ]
    for step in steps_old:
        ps = tf_old.add_paragraph()
        ps.text = step
        ps.font.name = FONT_NAME
        ps.font.size = Pt(10)
        ps.font.color.rgb = COLOR_TEXT_MUTED
        ps.space_after = Pt(8)

    # Right: Autonomous Surplus Router Flow (Emerald Green Card)
    builder.add_card(s3, Inches(6.9), Inches(1.9), Inches(5.6), Inches(5.0), highlight_border=COLOR_EMERALD)
    tx_new = s3.shapes.add_textbox(Inches(7.2), Inches(2.1), Inches(5.0), Inches(4.5))
    tf_new = tx_new.text_frame
    tf_new.word_wrap = True

    p_new_h = tf_new.paragraphs[0]
    p_new_h.text = "Surplus Router Autonomous Engine (< 1.0s):"
    p_new_h.font.name = FONT_NAME
    p_new_h.font.size = Pt(14)
    p_new_h.font.bold = True
    p_new_h.font.color.rgb = COLOR_EMERALD_DARK
    p_new_h.space_after = Pt(10)

    steps_new = [
        "1. Frictionless 30-sec intake (no password, cryptographic token).",
        "2. Strands Agent evaluates live shelter cold-storage capacity.",
        "3. Evaluates real-time driving times via Amazon Location Service.",
        "4. Computes multi-factor score: Capacity + Distance + Dietary + Urgency.",
        "5. DynamoDB TransactWriteItems atomically locks capacity (zero race condition).",
        "6. Auto-dispatches nearest volunteer driver with turn-by-turn route.",
        "7. Coordinator alerted ONLY if an unresolvable exception occurs! ✅ Food Rescued.",
    ]
    for step in steps_new:
        ps = tf_new.add_paragraph()
        ps.text = step
        ps.font.name = FONT_NAME
        ps.font.size = Pt(10)
        ps.font.color.rgb = COLOR_TEXT_MAIN
        ps.space_after = Pt(7)

    # =========================================================================
    # SLIDE 4: SYSTEM ARCHITECTURE & CLOUD CORE
    # =========================================================================
    s4 = builder.add_blank_slide(dark=True)
    builder.add_header(s4, "Cloud Native Architecture", "Enterprise-Grade Architecture on Amazon Web Services", "Built with Strands Agents SDK, Amazon Bedrock AgentCore, and DynamoDB ACID Transactions", dark=True)

    arch_layers = [
        ("Layer 1: Zero-IDOR Gateway", "Client Edge & Privacy Protection", [
            "• 256-bit unguessable capability tokens.",
            "• Constant-time verification prevents ID enumeration.",
            "• Automatic phone number & coordinate sanitization.",
            "• Distributed two-tier IP rate limiting against brute force.",
        ], COLOR_CYAN),
        ("Layer 2: Strands AgentCore", "Autonomous Decision Engine", [
            "• Bedrock AgentCore Foundation Model runtime.",
            "• Dynamic prompt isolation & food safety boundaries.",
            "• Tool: classify_donation (perishability category).",
            "• Tool: find_best_match (multi-factor mathematical scoring).",
        ], COLOR_EMERALD),
        ("Layer 3: Persistence Layer", "Amazon DynamoDB (ACID Transactions)", [
            "• TransactWriteItems guarantees zero double-allocations.",
            "• Atomic capacity reservations: remaining >= :claimed.",
            "• Global Secondary Indexes (GSI) for sub-second status lookups.",
            "• TTL-enabled audit logging and short-term operational cache.",
        ], COLOR_AMBER),
        ("Layer 4: Managed Services", "Amazon Location & Notification Services", [
            "• Amazon Location Service road route & matrix distance calculations.",
            "• Enforces strict 25km regional operational boundaries.",
            "• Amazon SNS transactional SMS/Push volunteer dispatch.",
            "• SQS Dead-Letter Queues (DLQ) for fail-safe coordinator alerts.",
        ], COLOR_CORAL),
    ]

    for i, (layer_title, layer_sub, bullets, border_col) in enumerate(arch_layers):
        cx = Inches(0.8) + i * Inches(2.95)
        builder.add_card(s4, cx, Inches(1.9), Inches(2.8), Inches(5.0), dark=True, highlight_border=border_col)

        tx = s4.shapes.add_textbox(cx + Inches(0.2), Inches(2.1), Inches(2.4), Inches(4.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = layer_title
        p1.font.name = FONT_NAME
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = border_col
        p1.space_after = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = layer_sub
        p2.font.name = FONT_NAME
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED_LIGHT
        p2.space_after = Pt(12)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.name = FONT_NAME
            pb.font.size = Pt(9.0)
            pb.font.color.rgb = COLOR_TEXT_LIGHT
            pb.space_after = Pt(7)

    # =========================================================================
    # SLIDE 5: AUTONOMOUS DECISION ENGINE (Scoring Formula)
    # =========================================================================
    s5 = builder.add_blank_slide(dark=False)
    builder.add_header(s5, "Multi-Factor Scoring", "Deterministic Matching Engine: Sub-Second Precision", "How Surplus Router mathematically optimizes destination shelters and transit drivers")

    # Formula Card Across Top
    formula_card = builder.add_card(s5, Inches(0.8), Inches(1.9), Inches(11.7), Inches(1.3), dark=False, highlight_border=COLOR_EMERALD)
    tx_f = s5.shapes.add_textbox(Inches(1.1), Inches(2.05), Inches(11.1), Inches(1.0))
    tf_f = tx_f.text_frame
    tf_f.word_wrap = True

    pf1 = tf_f.paragraphs[0]
    pf1.text = "COMPOSITE MATCH SCORE FORMULA"
    pf1.font.name = FONT_NAME
    pf1.font.size = Pt(10)
    pf1.font.bold = True
    pf1.font.color.rgb = COLOR_EMERALD_DARK
    pf1.space_after = Pt(3)

    pf2 = tf_f.add_paragraph()
    pf2.text = "Score = (0.40 × Distance_Score) + (0.30 × Capacity_Fit) + (0.20 × Urgency_Alignment) + (0.10 × Dietary_Bonus)"
    pf2.font.name = FONT_NAME
    pf2.font.size = Pt(16)
    pf2.font.bold = True
    pf2.font.color.rgb = COLOR_TEXT_MAIN

    # 4 Factor Breakdown Cards
    factors = [
        ("Distance Score (40%)", "Amazon Location Service", "Enforces a strict 25km radius. Road network travel time is prioritized over straight-line aerial distance to ensure food arrives hot and safe.", COLOR_CYAN),
        ("Capacity Fit (30%)", "DynamoDB Real-Time Intake", "Calculates storage efficiency ratio. Shelters with verified walk-in refrigeration matching the exact cargo volume are prioritized.", COLOR_EMERALD),
        ("Urgency Alignment (20%)", "Perishability Guardrail", "Meals with <2 hours remaining shelf-life are accelerated to closest recipient, preventing spoilage before intake processing.", COLOR_AMBER),
        ("Dietary Match (10%)", "Strict Exclusion Filter", "Halal, vegetarian, and allergen requirements act as binary gatekeepers. Shelters rejecting non-veg are cleanly eliminated from candidate pool.", COLOR_CORAL),
    ]

    for i, (ftitle, fsub, fdesc, fcol) in enumerate(factors):
        fx = Inches(0.8) + i * Inches(2.95)
        builder.add_card(s5, fx, Inches(3.4), Inches(2.8), Inches(3.5), dark=False, highlight_border=fcol)

        tx = s5.shapes.add_textbox(fx + Inches(0.2), Inches(3.55), Inches(2.4), Inches(3.1))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = ftitle
        p1.font.name = FONT_NAME
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = fcol
        p1.space_after = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = fsub
        p2.font.name = FONT_NAME
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_after = Pt(8)

        p3 = tf.add_paragraph()
        p3.text = fdesc
        p3.font.name = FONT_NAME
        p3.font.size = Pt(9.0)
        p3.font.color.rgb = COLOR_TEXT_MAIN

    # =========================================================================
    # SLIDE 6: TARGET PERSONAS & UNIFIED EXPERIENCE
    # =========================================================================
    s6 = builder.add_blank_slide(dark=False)
    builder.add_header(s6, "Ecosystem Stakeholders", "Built for 4 Core Personas: Frictionless & Secure", "How each stakeholder interacts with the 6-tab unified web application")

    personas = [
        ("📦 Commercial Donors", "Restaurants, Bakeries, Caterers", [
            "• Frictionless 30-sec surplus intake.",
            "• No password or account setup needed.",
            "• Instant cryptographic tracking token.",
            "• Automated tax & ESG donation receipt.",
        ], COLOR_EMERALD),
        ("🏢 Recipient Shelters", "Verified Food Banks & Soup Kitchens", [
            "• Pre-vetted health safety verification.",
            "• 1-click intake capacity update slider.",
            "• Live incoming delivery mission manifest.",
            "• Guaranteed cold-chain storage compliance.",
        ], COLOR_CYAN),
        ("🚲 Transit Volunteers", "Community Drivers & Cargo Cyclists", [
            "• Shift availability toggle (Active/Offline).",
            "• Vehicle cargo matching (Bike, Car, Van).",
            "• Turn-by-turn pickup & dropoff instructions.",
            "• Zero-IDOR masked phone call privacy.",
        ], COLOR_AMBER),
        ("🛡️ City Coordinators", "Non-Profit Operations Directors", [
            "• Transition from dispatchers to exception managers.",
            "• Real-time pipeline & capacity dashboard.",
            "• 1-click resolution for safety boundary tickets.",
            "• Tamper-proof DynamoDB audit trail.",
        ], COLOR_CORAL),
    ]

    for i, (ptitle, psub, pbullets, pcol) in enumerate(personas):
        px = Inches(0.8) + i * Inches(2.95)
        builder.add_card(s6, px, Inches(1.9), Inches(2.8), Inches(5.0), dark=False, highlight_border=pcol)

        tx = s6.shapes.add_textbox(px + Inches(0.2), Inches(2.1), Inches(2.4), Inches(4.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = ptitle
        p1.font.name = FONT_NAME
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MAIN
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = psub
        p2.font.name = FONT_NAME
        p2.font.size = Pt(9)
        p2.font.color.rgb = pcol
        p2.space_after = Pt(12)

        for b in pbullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.name = FONT_NAME
            pb.font.size = Pt(9.0)
            pb.font.color.rgb = COLOR_TEXT_MAIN
            pb.space_after = Pt(7)

    # =========================================================================
    # SLIDE 7: SAFETY GUARDRAILS & HUMAN-IN-THE-LOOP
    # =========================================================================
    s7 = builder.add_blank_slide(dark=True)
    builder.add_header(s7, "Safety Guardrails", "Human-in-the-Loop: Ethical & Compliant AI", "The agent acts autonomously on routine logistics, but escalates safety-critical decisions to human coordinators", dark=True)

    guards = [
        ("60-Minute Expiration Floor", "Food Safety Threshold", 
         "Perishable food with less than 60 minutes shelf-life remaining is strictly halted from autonomous dispatch. The agent flags a coordinator ticket to confirm immediate recipient consumption readiness before transit.",
         COLOR_CORAL),
        ("Regional Capacity Deficit", "Intake Overload Prevention",
         "If all regional verified recipient shelters within the 25km radius report 0kg cold storage capacity, the system does not dump food blindly; it alerts the human coordinator to authorize emergency expansion.",
         COLOR_AMBER),
        ("Zero-IDOR Privacy Sandbox", "PII & Address Masking",
         "Exact donor and recipient contact phone numbers and residential addresses are masked using salted SHA-256 tokens. Drivers only receive transient trip instructions, preventing data scraping and enumeration.",
         COLOR_CYAN),
    ]

    for i, (gtitle, gsub, gdesc, gcol) in enumerate(guards):
        gx = Inches(0.8) + i * Inches(3.95)
        builder.add_card(s7, gx, Inches(1.9), Inches(3.7), Inches(5.0), dark=True, highlight_border=gcol)

        tx = s7.shapes.add_textbox(gx + Inches(0.3), Inches(2.1), Inches(3.1), Inches(4.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = gtitle
        p1.font.name = FONT_NAME
        p1.font.size = Pt(15)
        p1.font.bold = True
        p1.font.color.rgb = gcol
        p1.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = gsub
        p2.font.name = FONT_NAME
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT_MUTED_LIGHT
        p2.space_after = Pt(14)

        p3 = tf.add_paragraph()
        p3.text = gdesc
        p3.font.name = FONT_NAME
        p3.font.size = Pt(9.8)
        p3.font.color.rgb = COLOR_TEXT_LIGHT
        p3.space_after = Pt(10)

    # =========================================================================
    # SLIDE 8: CONCURRENCY CHAOS & QUALITY GATES
    # =========================================================================
    s8 = builder.add_blank_slide(dark=False)
    builder.add_header(s8, "Production Reliability", "157 Passing Tests & Adversarial Verification", "Proven deterministic resilience under 50-thread concurrent multi-day simulation")

    tests_metrics = [
        ("157 / 157", "Automated Passing Tests (100%)", COLOR_EMERALD),
        ("50 Threads", "Concurrent Chaos Stress Test", COLOR_CYAN),
        ("0 Double Claims", "Mathematically Enforced by ACID", COLOR_AMBER),
        ("0 Ruff Errors", "Clean Enterprise Python Linter", COLOR_EMERALD_DARK),
    ]

    for i, (val, lbl, col) in enumerate(tests_metrics):
        cx = Inches(0.8) + i * Inches(2.95)
        builder.add_card(s8, cx, Inches(1.9), Inches(2.8), Inches(1.5), highlight_border=col)
        
        tx = s8.shapes.add_textbox(cx + Inches(0.2), Inches(2.05), Inches(2.4), Inches(1.1))
        tf = tx.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = val
        p1.font.name = FONT_NAME
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = lbl
        p2.font.name = FONT_NAME
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED

    # Bottom Details Card
    builder.add_card(s8, Inches(0.8), Inches(3.7), Inches(11.7), Inches(3.2), highlight_border=COLOR_LIGHT_BORDER)
    tx_detail = s8.shapes.add_textbox(Inches(1.1), Inches(3.9), Inches(11.1), Inches(2.8))
    tf_detail = tx_detail.text_frame
    tf_detail.word_wrap = True

    p_dh = tf_detail.paragraphs[0]
    p_dh.text = "HARDENED TEST GATES & ADVERSARIAL VALIDATION SUMMARY"
    p_dh.font.name = FONT_NAME
    p_dh.font.size = Pt(11)
    p_dh.font.bold = True
    p_dh.font.color.rgb = COLOR_TEXT_MAIN
    p_dh.space_after = Pt(8)

    test_bullets = [
        "• Concurrency Stress Gate (test_e2e_adversarial.py): 50 simultaneous threads claiming the same 50kg shelter allocation resulted in exactly 1 successful claim and 49 clean graceful reroutes.",
        "• Multi-Day Lifecycle Simulation (test_e2e_multi_day.py): 7-day operational cycle with dynamic intake shifts, volunteer check-ins, and variable donation perishability windows.",
        "• Mid-Flight Crash & Recovery (test_e2e_crash_recovery.py): Simulated container crashes mid-transit; event-sourcing safely restored pending dispatches without double-booking.",
        "• Security Invariant Suite (test_agent_guardrail.py): Validated constant-time token comparison, phone number sanitization, and strict regional boundary enforcement.",
    ]
    for b in test_bullets:
        pb = tf_detail.add_paragraph()
        pb.text = b
        pb.font.name = FONT_NAME
        pb.font.size = Pt(9.5)
        pb.font.color.rgb = COLOR_TEXT_MUTED
        pb.space_after = Pt(5)

    # =========================================================================
    # SLIDE 9: MEASURABLE COMMUNITY & ENVIRONMENTAL IMPACT
    # =========================================================================
    s9 = builder.add_blank_slide(dark=False)
    builder.add_header(s9, "Impact & Metrics", "Diverting Landfill Waste, Feeding Communities", "Measurable ESG metrics derived from real-world food rescue conversions")

    impact_data = [
        ("Surplus Diverted", "Hundreds of kg rescued", "Each kg of commercial surplus rescued prevents edible food from degrading into harmful methane in municipal landfills.", COLOR_EMERALD),
        ("Meals Served", "2.0 Meals per kg Factor", "Standard USDA and Feeding America conversion metric. 50kg surplus directly translates into 100 wholesome community meals.", COLOR_CYAN),
        ("Time Returned", "20-25 Hours / Week", "Replaces frantic manual dispatching with automated routing, freeing non-profit directors for community outreach and fundraising.", COLOR_AMBER),
        ("Landfill Emissions", "Scope-3 Carbon Abatement", "Provides corporate donors with verifiable carbon offset certificates for ESG compliance and tax deduction reporting.", COLOR_CORAL),
    ]

    for i, (title, highlight, desc, col) in enumerate(impact_data):
        cx = Inches(0.8) + i * Inches(2.95)
        builder.add_card(s9, cx, Inches(1.9), Inches(2.8), Inches(5.0), highlight_border=col)

        tx = s9.shapes.add_textbox(cx + Inches(0.2), Inches(2.1), Inches(2.4), Inches(4.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_NAME
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MAIN
        p1.space_after = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = highlight
        p2.font.name = FONT_NAME
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = col
        p2.space_after = Pt(12)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_NAME
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = COLOR_TEXT_MUTED

    # =========================================================================
    # SLIDE 10: BUSINESS MODEL & SUSTAINABILITY (Lean Canvas)
    # =========================================================================
    s10 = builder.add_blank_slide(dark=False)
    builder.add_header(s10, "Economic Sustainability", "Lean Canvas: Self-Sustaining Financial Model", "Balancing humanitarian mission with financial sustainability through B2B ESG SaaS and civic grants")

    cols_biz = [
        ("B2B Corporate ESG SaaS", "Recurring Enterprise Subscriptions", [
            "• Automated tax deduction & donation receipts.",
            "• Audited Scope-3 waste diversion reporting.",
            "• Corporate sustainability dashboard for ESG filings.",
            "• Tiered monthly subscriptions for catering chains.",
        ], COLOR_EMERALD),
        ("Municipal Waste Grants", "Smart City Climate Funding", [
            "• City-level organic waste reduction incentives.",
            "• Landfill diversion public infrastructure grants.",
            "• Municipal social welfare department tech sponsorships.",
            "• Green urban logistics carbon credits.",
        ], COLOR_CYAN),
        ("Predictive Waste Analytics", "Enterprise Kitchen Optimization", [
            "• AI-driven surplus prediction for commercial bakeries.",
            "• Highlights recurring over-prep patterns.",
            "• Helps executive chefs optimize purchasing costs.",
            "• Premium B2B subscription tier.",
        ], COLOR_AMBER),
    ]

    for i, (btitle, bsub, bbullets, bcol) in enumerate(cols_biz):
        bx = Inches(0.8) + i * Inches(3.95)
        builder.add_card(s10, bx, Inches(1.9), Inches(3.7), Inches(5.0), highlight_border=bcol)

        tx = s10.shapes.add_textbox(bx + Inches(0.3), Inches(2.1), Inches(3.1), Inches(4.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = btitle
        p1.font.name = FONT_NAME
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MAIN
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = bsub
        p2.font.name = FONT_NAME
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = bcol
        p2.space_after = Pt(12)

        for b in bbullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.name = FONT_NAME
            pb.font.size = Pt(9.5)
            pb.font.color.rgb = COLOR_TEXT_MAIN
            pb.space_after = Pt(7)

    # =========================================================================
    # SLIDE 11: VISION & PRODUCT ROADMAP
    # =========================================================================
    s11 = builder.add_blank_slide(dark=True)
    builder.add_header(s11, "Product Roadmap", "The Future of Autonomous Food Rescue", "From single-point dispatch to multi-stop autonomous fleet coordination", dark=True)

    roadmap_phases = [
        ("Phase 1: Present (v1)", "Core Strands Engine", [
            "• 1-to-1 autonomous matching engine.",
            "• Amazon Location Service road routing.",
            "• Zero-IDOR capability token security.",
            "• 6-tab unified web application & mock mode.",
            "• Production DynamoDB ACID conditional transactions.",
        ], COLOR_EMERALD, "COMPLETED & LIVE"),
        ("Phase 2: Near-Term (v2)", "Fleet Route Chaining", [
            "• Multi-stop pickup route optimization.",
            "• WhatsApp Business API conversational donor bot.",
            "• Smart volunteer push notification dispatch.",
            "• Cross-neighborhood capacity pooling.",
            "• Automated tax compliance e-invoicing.",
        ], COLOR_CYAN, "IN DEVELOPMENT"),
        ("Phase 3: Long-Term (v3)", "IoT & Smart Cities", [
            "• BLE & LoRaWAN cold-chain temperature telemetry.",
            "• Automated municipal health-code verification.",
            "• Predictive prep surplus forecasting for kitchens.",
            "• Nationwide network of autonomous rescue hubs.",
            "• Carbon credit marketplace integration.",
        ], COLOR_AMBER, "FUTURE VISION"),
    ]

    for i, (rtitle, rsub, rbullets, rcol, rbadge) in enumerate(roadmap_phases):
        rx = Inches(0.8) + i * Inches(3.95)
        builder.add_card(s11, rx, Inches(1.9), Inches(3.7), Inches(5.0), dark=True, highlight_border=rcol)

        # Status badge
        badge = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx + Inches(0.3), Inches(2.1), Inches(2.3), Inches(0.32))
        badge.fill.solid()
        badge.fill.fore_color.rgb = rcol
        badge.line.fill.background()
        bp = badge.text_frame.paragraphs[0]
        bp.text = rbadge
        bp.font.name = FONT_NAME
        bp.font.size = Pt(8)
        bp.font.bold = True
        bp.font.color.rgb = COLOR_WHITE
        bp.alignment = PP_ALIGN.CENTER

        tx = s11.shapes.add_textbox(rx + Inches(0.3), Inches(2.6), Inches(3.1), Inches(4.0))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = rtitle
        p1.font.name = FONT_NAME
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_LIGHT
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = rsub
        p2.font.name = FONT_NAME
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED_LIGHT
        p2.space_after = Pt(10)

        for b in rbullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.name = FONT_NAME
            pb.font.size = Pt(9.0)
            pb.font.color.rgb = COLOR_TEXT_LIGHT
            pb.space_after = Pt(6)

    # =========================================================================
    # SLIDE 12: CONCLUSION & CALL TO ACTION (Dark Theme)
    # =========================================================================
    s12 = builder.add_blank_slide(dark=True)

    # Central Impact Box
    c_box = s12.shapes.add_textbox(Inches(1.5), Inches(1.1), Inches(10.3), Inches(4.0))
    tf_c = c_box.text_frame
    tf_c.word_wrap = True

    pc0 = tf_c.paragraphs[0]
    pc0.text = "AUTONOMOUS | COMPASSIONATE | PRODUCTION-READY"
    pc0.font.name = FONT_NAME
    pc0.font.size = Pt(11)
    pc0.font.bold = True
    pc0.font.color.rgb = COLOR_EMERALD
    pc0.alignment = PP_ALIGN.CENTER
    pc0.space_after = Pt(10)

    pc1 = tf_c.add_paragraph()
    pc1.text = "From Dumpsters to Dinner Tables -- Autonomously."
    pc1.font.name = FONT_NAME
    pc1.font.size = Pt(36)
    pc1.font.bold = True
    pc1.font.color.rgb = COLOR_TEXT_LIGHT
    pc1.alignment = PP_ALIGN.CENTER
    pc1.space_after = Pt(14)

    pc2 = tf_c.add_paragraph()
    pc2.text = "Surplus Router proves that agentic AI can solve humanity's most urgent community logistical challenges with sub-second precision, rigorous safety boundaries, and uncompromising privacy."
    pc2.font.name = FONT_NAME
    pc2.font.size = Pt(13)
    pc2.font.color.rgb = COLOR_TEXT_MUTED_LIGHT
    pc2.alignment = PP_ALIGN.CENTER
    pc2.space_after = Pt(20)

    # Project Links / Credentials Container
    builder.add_card(s12, Inches(2.2), Inches(4.5), Inches(8.9), Inches(2.2), dark=True, highlight_border=COLOR_EMERALD)
    tx_links = s12.shapes.add_textbox(Inches(2.5), Inches(4.65), Inches(8.3), Inches(1.8))
    tf_l = tx_links.text_frame
    tf_l.word_wrap = True

    pl0 = tf_l.paragraphs[0]
    pl0.text = "PROJECT ARTIFACTS & QUICK-TEST ACCESS:"
    pl0.font.name = FONT_NAME
    pl0.font.size = Pt(10)
    pl0.font.bold = True
    pl0.font.color.rgb = COLOR_CYAN
    pl0.space_after = Pt(6)

    links_text = [
        "• Presenter: Bhumeshwari Bisen (Indore Institute of Science & Technology)",
        "• GitHub Repository: https://github.com/kuldeep-poonia/food-rescue-coordination-agent",
        "• Local Dashboard: http://localhost:8080 (Run: python server.py --port 8080 --mock)",
        "• Coordinator Demo Key: dev-insecure-coordinator-key-for-local-testing-only-32chars",
    ]
    for lt in links_text:
        plt = tf_l.add_paragraph()
        plt.text = lt
        plt.font.name = FONT_NAME
        plt.font.size = Pt(9.5)
        plt.font.color.rgb = COLOR_TEXT_LIGHT
        plt.space_after = Pt(3)

    builder.save()


if __name__ == "__main__":
    build_full_deck()
