"""Generate a 12-slide PowerPoint presentation matching the Metaverse Cyber-Stage Neon template.

Features exact template styling:
- Midnight dark background with glowing 3D podium stage and neon purple/magenta ambient lighting
- Floating iridescent ribbons and starry sky
- Slide 1 presenter profile for Bhumeshwari Bisen (Machine Learning & Applied AI Intern, IIST)
- 12 slide layouts corresponding directly to the template slides
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Template Color Palette
COLOR_PURE_WHITE = RGBColor(255, 255, 255)
COLOR_NEON_PURPLE = RGBColor(192, 132, 252)    # #C084FC
COLOR_NEON_VIOLET = RGBColor(147, 51, 234)     # #9333EA
COLOR_NEON_MAGENTA = RGBColor(232, 121, 249)   # #E879F9
COLOR_NEON_CYAN = RGBColor(56, 189, 248)       # #38BDF8
COLOR_LAVENDER = RGBColor(233, 213, 255)       # #E9D5FF
COLOR_MUTED_SLATE = RGBColor(148, 163, 184)    # #94A3B8

COLOR_CARD_DARK = RGBColor(13, 10, 24)         # #0D0A18
COLOR_CARD_BORDER = RGBColor(88, 28, 135)      # #581C87 Deep Purple
COLOR_BORDER_CYAN = RGBColor(14, 116, 144)     # #0E7490

FONT_NAME = "Segoe UI"

BG_STAGE_PATH = "cyber_stage_bg.jpg"
BG_CONTENT_PATH = "cyber_content_bg.jpg"


class CyberDeckBuilder:
    """Builder for the Metaverse Cyber-Stage PowerPoint Presentation."""

    def __init__(self, filename="Surplus_Router_Metaverse_Presentation.pptx"):
        self.filename = filename
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]

    def add_cyber_slide(self, use_stage_bg=False):
        """Add a slide with high-res cyberpunk background image."""
        slide = self.prs.slides.add_slide(self.blank_layout)
        bg_path = BG_STAGE_PATH if use_stage_bg else BG_CONTENT_PATH
        if os.path.exists(bg_path):
            slide.shapes.add_picture(bg_path, Inches(0), Inches(0), width=Inches(13.333), height=Inches(7.5))
        else:
            # Fallback solid dark
            bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
            bg.fill.solid()
            bg.fill.fore_color.rgb = RGBColor(8, 7, 13)
            bg.line.fill.background()

        # Add Template Accents: Top-right star sparkle and bottom-right double chevrons
        star = slide.shapes.add_textbox(Inches(12.3), Inches(0.4), Inches(0.6), Inches(0.6))
        star.text_frame.word_wrap = False
        sp = star.text_frame.paragraphs[0]
        sp.text = "✦"
        sp.font.name = FONT_NAME
        sp.font.size = Pt(16)
        sp.font.bold = True
        sp.font.color.rgb = COLOR_NEON_PURPLE

        chev = slide.shapes.add_textbox(Inches(12.3), Inches(6.6), Inches(0.7), Inches(0.6))
        chev.text_frame.word_wrap = False
        cp = chev.text_frame.paragraphs[0]
        cp.text = ">>"
        cp.font.name = FONT_NAME
        cp.font.size = Pt(18)
        cp.font.bold = True
        cp.font.color.rgb = COLOR_NEON_CYAN

        return slide

    def add_top_badge(self, slide, text="AWS HACKATHON 2026"):
        """Add small top-left pill badge matching template."""
        badge = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.5), Inches(2.5), Inches(0.32)
        )
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_CARD_DARK
        badge.line.color.rgb = COLOR_NEON_VIOLET
        badge.line.width = Pt(1.0)
        
        tf = badge.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = text.upper()
        p.font.name = FONT_NAME
        p.font.size = Pt(8.0)
        p.font.bold = True
        p.font.color.rgb = COLOR_NEON_PURPLE
        p.alignment = PP_ALIGN.CENTER
        return badge

    def add_cyber_card(self, slide, left, top, width, height, border_color=COLOR_CARD_BORDER):
        """Create a sleek dark glass card with glowing cyber border."""
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
        )
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    def save(self):
        """Save presentation."""
        self.prs.save(self.filename)
        print(f"Cyber presentation saved to: {self.filename}")


def build_metaverse_deck():
    builder = CyberDeckBuilder("Surplus_Router_Metaverse_Presentation.pptx")

    # =========================================================================
    # SLIDE 1: HERO TITLE SLIDE (Matches Template Slide 1: METAVERSE)
    # =========================================================================
    s1 = builder.add_cyber_slide(use_stage_bg=True)
    builder.add_top_badge(s1, "AWS AGENTS FOR HUMANS 2026")

    # Hero Main Title
    tb_title = s1.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.3), Inches(2.2))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True

    p_t = tf_t.paragraphs[0]
    p_t.text = "SURPLUS ROUTER"
    p_t.font.name = FONT_NAME
    p_t.font.size = Pt(50)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_PURE_WHITE
    p_t.alignment = PP_ALIGN.CENTER
    p_t.space_after = Pt(4)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "AUTONOMOUS FOOD RESCUE COORDINATION AGENT"
    p_sub.font.name = FONT_NAME
    p_sub.font.size = Pt(14)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_NEON_CYAN
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.space_after = Pt(6)

    p_tag = tf_t.add_paragraph()
    p_tag.text = "Strands Agents SDK | Amazon Bedrock AgentCore | Amazon DynamoDB ACID"
    p_tag.font.name = FONT_NAME
    p_tag.font.size = Pt(10.5)
    p_tag.font.color.rgb = COLOR_LAVENDER
    p_tag.alignment = PP_ALIGN.CENTER

    # Presenter Podium Card (Positioned directly over the 3D glowing stage!)
    card_stage = builder.add_cyber_card(
        s1, Inches(3.2), Inches(3.6), Inches(6.9), Inches(2.4), border_color=COLOR_NEON_PURPLE
    )
    tb_stage = s1.shapes.add_textbox(Inches(3.4), Inches(3.75), Inches(6.5), Inches(2.1))
    tf_s = tb_stage.text_frame
    tf_s.word_wrap = True

    ps_tag = tf_s.paragraphs[0]
    ps_tag.text = "PROJECT LEAD & PRESENTER"
    ps_tag.font.name = FONT_NAME
    ps_tag.font.size = Pt(9.0)
    ps_tag.font.bold = True
    ps_tag.font.color.rgb = COLOR_NEON_MAGENTA
    ps_tag.alignment = PP_ALIGN.CENTER
    ps_tag.space_after = Pt(4)

    ps_name = tf_s.add_paragraph()
    ps_name.text = "Bhumeshwari Bisen"
    ps_name.font.name = FONT_NAME
    ps_name.font.size = Pt(24)
    ps_name.font.bold = True
    ps_name.font.color.rgb = COLOR_PURE_WHITE
    ps_name.alignment = PP_ALIGN.CENTER
    ps_name.space_after = Pt(2)

    ps_pos = tf_s.add_paragraph()
    ps_pos.text = "Machine Learning & Applied AI Intern"
    ps_pos.font.name = FONT_NAME
    ps_pos.font.size = Pt(13)
    ps_pos.font.bold = True
    ps_pos.font.color.rgb = COLOR_NEON_CYAN
    ps_pos.alignment = PP_ALIGN.CENTER
    ps_pos.space_after = Pt(6)

    ps_inst = tf_s.add_paragraph()
    ps_inst.text = "Indore Institute of Science & Technology"
    ps_inst.font.name = FONT_NAME
    ps_inst.font.size = Pt(11)
    ps_inst.font.color.rgb = COLOR_LAVENDER
    ps_inst.alignment = PP_ALIGN.CENTER

    # Year tag at bottom left
    yr = s1.shapes.add_textbox(Inches(0.8), Inches(6.7), Inches(1.5), Inches(0.4))
    yr.text_frame.paragraphs[0].text = "2026"
    yr.text_frame.paragraphs[0].font.name = FONT_NAME
    yr.text_frame.paragraphs[0].font.size = Pt(11)
    yr.text_frame.paragraphs[0].font.bold = True
    yr.text_frame.paragraphs[0].font.color.rgb = COLOR_MUTED_SLATE

    # =========================================================================
    # SLIDE 2: EXECUTIVE OVERVIEW (Matches Template Slide 2: Metaverse Overview)
    # =========================================================================
    s2 = builder.add_cyber_slide(use_stage_bg=True)
    builder.add_top_badge(s2, "EXECUTIVE SUMMARY")

    tb2 = s2.shapes.add_textbox(Inches(1.5), Inches(1.2), Inches(10.3), Inches(2.2))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p2_h = tf2.paragraphs[0]
    p2_h.text = "Autonomous Coordination Engine"
    p2_h.font.name = FONT_NAME
    p2_h.font.size = Pt(32)
    p2_h.font.bold = True
    p2_h.font.color.rgb = COLOR_PURE_WHITE
    p2_h.space_after = Pt(12)

    p2_body = tf2.add_paragraph()
    p2_body.text = (
        "Surplus Router transforms commercial surplus food recovery from an exhausting, 3-to-5 hour manual "
        "logistics nightmare into an autonomous background intelligence network. Built upon the Strands Agents SDK "
        "and deployed on Amazon Bedrock AgentCore, the agent continuously matches surplus reports with verified recipient "
        "shelters, reserves intake capacity via DynamoDB ACID transactions, and dispatches volunteer drivers within milliseconds."
    )
    p2_body.font.name = FONT_NAME
    p2_body.font.size = Pt(12)
    p2_body.font.color.rgb = COLOR_LAVENDER

    # 3 Stat Cards on the stage
    stat_items = [
        ("< 1.0s", "Autonomous Latency", COLOR_NEON_CYAN),
        ("100% ACID", "Zero Double-Allocations", COLOR_NEON_PURPLE),
        ("3-5 Hours", "Coordinator Time Saved Daily", COLOR_NEON_MAGENTA),
    ]
    for i, (val, lbl, col) in enumerate(stat_items):
        cx = Inches(1.8) + i * Inches(3.4)
        builder.add_cyber_card(s2, cx, Inches(3.7), Inches(3.0), Inches(1.5), border_color=col)
        tx = s2.shapes.add_textbox(cx + Inches(0.2), Inches(3.85), Inches(2.6), Inches(1.2))
        tfx = tx.text_frame
        tfx.word_wrap = True
        pv = tfx.paragraphs[0]
        pv.text = val
        pv.font.name = FONT_NAME
        pv.font.size = Pt(22)
        pv.font.bold = True
        pv.font.color.rgb = col
        pv.space_after = Pt(3)

        pl = tfx.add_paragraph()
        pl.text = lbl
        pl.font.name = FONT_NAME
        pl.font.size = Pt(9.5)
        pl.font.color.rgb = COLOR_MUTED_SLATE

    # =========================================================================
    # SLIDE 3: HISTORICAL CONTEXT -> THE CRISIS (Matches Template Slide 3)
    # =========================================================================
    s3 = builder.add_cyber_slide(use_stage_bg=True)
    builder.add_top_badge(s3, "THE CRISIS")

    tb3 = s3.shapes.add_textbox(Inches(1.5), Inches(1.3), Inches(10.3), Inches(4.5))
    tf3 = tb3.text_frame
    tf3.word_wrap = True

    p3_h = tf3.paragraphs[0]
    p3_h.text = "The Food Recovery Paradox"
    p3_h.font.name = FONT_NAME
    p3_h.font.size = Pt(34)
    p3_h.font.bold = True
    p3_h.font.color.rgb = COLOR_PURE_WHITE
    p3_h.alignment = PP_ALIGN.CENTER
    p3_h.space_after = Pt(14)

    p3_b1 = tf3.add_paragraph()
    p3_b1.text = (
        "Every single day, restaurants, bakeries, and corporate cafeterias produce tons of wholesome, safe surplus food. "
        "Simultaneously, nearby community shelters and soup kitchens face severe meal deficits."
    )
    p3_b1.font.name = FONT_NAME
    p3_b1.font.size = Pt(12)
    p3_b1.font.color.rgb = COLOR_LAVENDER
    p3_b1.alignment = PP_ALIGN.CENTER
    p3_b1.space_after = Pt(16)

    # Crisis Highlight Box on Stage
    card_crisis = builder.add_cyber_card(
        s3, Inches(2.0), Inches(3.2), Inches(9.3), Inches(2.2), border_color=COLOR_NEON_MAGENTA
    )
    tb_cbox = s3.shapes.add_textbox(Inches(2.3), Inches(3.35), Inches(8.7), Inches(1.9))
    tf_cb = tb_cbox.text_frame
    tf_cb.word_wrap = True

    pc_h = tf_cb.paragraphs[0]
    pc_h.text = "THE FATAL 3-TO-4 HOUR SPOILAGE CLOCK"
    pc_h.font.name = FONT_NAME
    pc_h.font.size = Pt(11)
    pc_h.font.bold = True
    pc_h.font.color.rgb = COLOR_NEON_MAGENTA
    pc_h.space_after = Pt(6)

    pc_desc = tf_cb.add_paragraph()
    pc_desc.text = (
        "• Perishable food degrades in 3-4 hours without rapid cold-chain transport.\n"
        "• Non-profit coordinators lose 3-5 hours on phone calls, chaotic WhatsApp groups, and spreadsheets.\n"
        "• When coordination lags, edible food is discarded into landfills, releasing harmful methane."
    )
    pc_desc.font.name = FONT_NAME
    pc_desc.font.size = Pt(10.5)
    pc_desc.font.color.rgb = COLOR_PURE_WHITE

    # =========================================================================
    # SLIDE 4: CORE TECHNOLOGIES (Matches Template Slide 4: Core Technologies)
    # =========================================================================
    s4 = builder.add_cyber_slide(use_stage_bg=False)
    builder.add_top_badge(s4, "INFRASTRUCTURE")

    tb4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(5.0), Inches(2.0))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    p4_h = tf4.paragraphs[0]
    p4_h.text = "Core Technologies"
    p4_h.font.name = FONT_NAME
    p4_h.font.size = Pt(36)
    p4_h.font.bold = True
    p4_h.font.color.rgb = COLOR_PURE_WHITE
    p4_h.space_after = Pt(8)

    p4_sub = tf4.add_paragraph()
    p4_sub.text = "Autonomous Multi-Agent Architecture built on Enterprise AWS Foundations."
    p4_sub.font.name = FONT_NAME
    p4_sub.font.size = Pt(11.5)
    p4_sub.font.color.rgb = COLOR_MUTED_SLATE

    # Two Horizontal Technology Cards on Right (matching template layout!)
    tech_cards = [
        ("AMAZON BEDROCK & STRANDS AGENTS SDK", 
         "Autonomous reasoning runtime executing dynamic prompt isolation, intent classification, and deterministic tool invocations (classify_donation, find_best_match, assign_volunteer).",
         COLOR_NEON_PURPLE),
        ("AMAZON DYNAMODB ACID TRANSACTIONS", 
         "Five dedicated high-performance tables with TransactWriteItems and conditional expressions (remaining_capacity >= :claimed) mathematically preventing double-allocations.",
         COLOR_NEON_CYAN),
    ]
    for i, (ttitle, tdesc, tcol) in enumerate(tech_cards):
        cy = Inches(1.4) + i * Inches(2.5)
        builder.add_cyber_card(s4, Inches(5.8), cy, Inches(6.7), Inches(2.1), border_color=tcol)
        
        # Pill badge inside card
        pb = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.1), cy + Inches(0.2), Inches(3.6), Inches(0.3))
        pb.fill.solid()
        pb.fill.fore_color.rgb = COLOR_CARD_DARK
        pb.line.color.rgb = tcol
        pb.line.width = Pt(1.0)
        pbp = pb.text_frame.paragraphs[0]
        pbp.text = ttitle
        pbp.font.name = FONT_NAME
        pbp.font.size = Pt(7.5)
        pbp.font.bold = True
        pbp.font.color.rgb = tcol
        pbp.alignment = PP_ALIGN.CENTER

        tx = s4.shapes.add_textbox(Inches(6.1), cy + Inches(0.65), Inches(6.1), Inches(1.2))
        tf = tx.text_frame
        tf.word_wrap = True
        ptd = tf.paragraphs[0]
        ptd.text = tdesc
        ptd.font.name = FONT_NAME
        ptd.font.size = Pt(10)
        ptd.font.color.rgb = COLOR_LAVENDER

    # =========================================================================
    # SLIDE 5: KEY PLAYERS (Matches Template Slide 5: Key Players with 3 Bracket Cards)
    # =========================================================================
    s5 = builder.add_cyber_slide(use_stage_bg=True)
    builder.add_top_badge(s5, "ECOSYSTEM")

    tb5 = s5.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.3), Inches(1.0))
    tf5 = tb5.text_frame
    p5_h = tf5.paragraphs[0]
    p5_h.text = "Key Ecosystem Players"
    p5_h.font.name = FONT_NAME
    p5_h.font.size = Pt(32)
    p5_h.font.bold = True
    p5_h.font.color.rgb = COLOR_PURE_WHITE
    p5_h.alignment = PP_ALIGN.CENTER

    players = [
        ("Commercial Donors", "Restaurants & Caterers", [
            "• 30-second surplus report portal.",
            "• Zero password or registration required.",
            "• 256-bit cryptographic tracking token.",
            "• Automated tax & ESG diversion receipts.",
        ], COLOR_NEON_PURPLE),
        ("Recipient Shelters", "Soup Kitchens & Food Banks", [
            "• Pre-vetted health safety accreditation.",
            "• 1-click capacity adjustment slider.",
            "• Atomic reservation guarantees.",
            "• Zero unexpected food waste dumps.",
        ], COLOR_NEON_CYAN),
        ("Transit Volunteers", "Drivers & Cargo Cyclists", [
            "• Shift toggle (Available / Offline).",
            "• Vehicle-matched cargo capacity.",
            "• Turn-by-turn route dispatch cards.",
            "• Zero-IDOR masked phone call privacy.",
        ], COLOR_NEON_MAGENTA),
    ]

    for i, (title, sub, bullets, col) in enumerate(players):
        cx = Inches(1.0) + i * Inches(3.9)
        builder.add_cyber_card(s5, cx, Inches(2.2), Inches(3.6), Inches(4.3), border_color=col)

        tx = s5.shapes.add_textbox(cx + Inches(0.25), Inches(2.4), Inches(3.1), Inches(3.9))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_NAME
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_PURE_WHITE
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.name = FONT_NAME
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = col
        p2.space_after = Pt(12)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = b
            pb.font.name = FONT_NAME
            pb.font.size = Pt(9.0)
            pb.font.color.rgb = COLOR_LAVENDER
            pb.space_after = Pt(6)

    # =========================================================================
    # SLIDE 6: SOCIAL IMPACT (Matches Template Slide 6: Social Impact)
    # =========================================================================
    s6 = builder.add_cyber_slide(use_stage_bg=False)
    builder.add_top_badge(s6, "COMMUNITY VALUE")

    tb6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(6.0), Inches(5.5))
    tf6 = tb6.text_frame
    tf6.word_wrap = True

    p6_h = tf6.paragraphs[0]
    p6_h.text = "Social & Community Impact"
    p6_h.font.name = FONT_NAME
    p6_h.font.size = Pt(32)
    p6_h.font.bold = True
    p6_h.font.color.rgb = COLOR_PURE_WHITE
    p6_h.space_after = Pt(12)

    impact_points = [
        "• Human Dignity: Converts commercial culinary excess into hot, dignified meals for families and children experiencing homelessness.",
        "• Operational Relief: Saves 20 to 25 hours per week for non-profit coordinators, eliminating phone burnout.",
        "• Methane Abatement: Organic waste in landfills produces potent methane; diverting surplus directly reduces municipal carbon emissions.",
        "• Transparent Trust: Public impact ticker tracks cumulative kg diverted and meals served equivalent in real-time.",
    ]
    for ip in impact_points:
        pip = tf6.add_paragraph()
        pip.text = ip
        pip.font.name = FONT_NAME
        pip.font.size = Pt(10.5)
        pip.font.color.rgb = COLOR_LAVENDER
        pip.space_after = Pt(10)

    # Right Card: Holographic Impact Badge Container
    builder.add_cyber_card(s6, Inches(7.3), Inches(1.5), Inches(5.2), Inches(4.8), border_color=COLOR_NEON_CYAN)
    tx_right = s6.shapes.add_textbox(Inches(7.6), Inches(1.8), Inches(4.6), Inches(4.2))
    tfr = tx_right.text_frame
    tfr.word_wrap = True

    pr_h = tfr.paragraphs[0]
    pr_h.text = "REAL-TIME IMPACT METRICS"
    pr_h.font.name = FONT_NAME
    pr_h.font.size = Pt(11)
    pr_h.font.bold = True
    pr_h.font.color.rgb = COLOR_NEON_CYAN
    pr_h.space_after = Pt(16)

    m_items = [
        ("2.0x Multiplier", "Meals Equivalent Conversion per kg"),
        ("> 96% Success", "Rescue Rate Before Shelf-Life Expiry"),
        ("< 1.0 Second", "Autonomous Decision Latency"),
        ("Zero IDOR", "Constant-Time Salted SHA-256 Privacy"),
    ]
    for v, l in m_items:
        pv = tfr.add_paragraph()
        pv.text = v
        pv.font.name = FONT_NAME
        pv.font.size = Pt(18)
        pv.font.bold = True
        pv.font.color.rgb = COLOR_PURE_WHITE
        pv.space_after = Pt(1)

        pl = tfr.add_paragraph()
        pl.text = l
        pl.font.name = FONT_NAME
        pl.font.size = Pt(9.5)
        pl.font.color.rgb = COLOR_MUTED_SLATE
        pl.space_after = Pt(10)

    # =========================================================================
    # SLIDE 7: ECONOMIC POTENTIAL (Matches Template Slide 7: Economic Potential)
    # =========================================================================
    s7 = builder.add_cyber_slide(use_stage_bg=True)
    builder.add_top_badge(s7, "SUSTAINABILITY")

    tb7 = s7.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.3), Inches(1.0))
    tf7 = tb7.text_frame
    p7_h = tf7.paragraphs[0]
    p7_h.text = "Economic Potential & Sustainability"
    p7_h.font.name = FONT_NAME
    p7_h.font.size = Pt(32)
    p7_h.font.bold = True
    p7_h.font.color.rgb = COLOR_PURE_WHITE
    p7_h.alignment = PP_ALIGN.CENTER

    # 2 Comparison Columns (Matching Template Slide 7!)
    builder.add_cyber_card(s7, Inches(1.5), Inches(2.2), Inches(4.9), Inches(4.3), border_color=COLOR_NEON_PURPLE)
    tx7_1 = s7.shapes.add_textbox(Inches(1.8), Inches(2.4), Inches(4.3), Inches(3.9))
    tf7_1 = tx7_1.text_frame
    tf7_1.word_wrap = True

    p71 = tf7_1.paragraphs[0]
    p71.text = "B2B CORPORATE ESG SAAS"
    p71.font.name = FONT_NAME
    p71.font.size = Pt(12)
    p71.font.bold = True
    p71.font.color.rgb = COLOR_NEON_PURPLE
    p71.space_after = Pt(10)

    e1_points = [
        "• Tiered monthly subscriptions for catering chains and corporate cafeterias.",
        "• Automated tax deduction & donation receipts compliant with tax regulations.",
        "• Audited Scope-3 waste diversion reporting for corporate ESG filings.",
        "• Enterprise food waste reduction certificates for brand sustainability.",
    ]
    for ep in e1_points:
        pep = tf7_1.add_paragraph()
        pep.text = ep
        pep.font.name = FONT_NAME
        pep.font.size = Pt(9.5)
        pep.font.color.rgb = COLOR_LAVENDER
        pep.space_after = Pt(8)

    builder.add_cyber_card(s7, Inches(6.9), Inches(2.2), Inches(4.9), Inches(4.3), border_color=COLOR_NEON_CYAN)
    tx7_2 = s7.shapes.add_textbox(Inches(7.2), Inches(2.4), Inches(4.3), Inches(3.9))
    tf7_2 = tx7_2.text_frame
    tf7_2.word_wrap = True

    p72 = tf7_2.paragraphs[0]
    p72.text = "MUNICIPAL & CLIMATE GRANTS"
    p72.font.name = FONT_NAME
    p72.font.size = Pt(12)
    p72.font.bold = True
    p72.font.color.rgb = COLOR_NEON_CYAN
    p72.space_after = Pt(10)

    e2_points = [
        "• Smart city organic waste reduction & methane mitigation public funds.",
        "• Municipal solid waste diversion subsidies.",
        "• Civic innovation tech endowments and food security grants.",
        "• Future carbon credit marketplace trading based on verifiable diversion.",
    ]
    for ep in e2_points:
        pep = tf7_2.add_paragraph()
        pep.text = ep
        pep.font.name = FONT_NAME
        pep.font.size = Pt(9.5)
        pep.font.color.rgb = COLOR_LAVENDER
        pep.space_after = Pt(8)

    # =========================================================================
    # SLIDE 8: CULTURAL SHIFTS -> PARADIGM SHIFT (Matches Template Slide 8)
    # =========================================================================
    s8 = builder.add_cyber_slide(use_stage_bg=False)
    builder.add_top_badge(s8, "PARADIGM SHIFT")

    tb8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(1.1))
    tf8 = tb8.text_frame
    p8_h = tf8.paragraphs[0]
    p8_h.text = "Operational Paradigm Shift"
    p8_h.font.name = FONT_NAME
    p8_h.font.size = Pt(32)
    p8_h.font.bold = True
    p8_h.font.color.rgb = COLOR_PURE_WHITE
    p8_h.space_after = Pt(4)

    p8_sub = tf8.add_paragraph()
    p8_sub.text = "Transitioning community logistics from reactive chaos to proactive background intelligence."
    p8_sub.font.name = FONT_NAME
    p8_sub.font.size = Pt(11.5)
    p8_sub.font.color.rgb = COLOR_LAVENDER

    # 2 Comparison Cards (Old vs New Paradigm)
    builder.add_cyber_card(s8, Inches(0.8), Inches(2.2), Inches(5.6), Inches(4.7), border_color=COLOR_CARD_BORDER)
    tx8_1 = s8.shapes.add_textbox(Inches(1.1), Inches(2.4), Inches(5.0), Inches(4.3))
    tf8_1 = tx8_1.text_frame
    tf8_1.word_wrap = True

    p81_h = tf8_1.paragraphs[0]
    p81_h.text = "TRADITIONAL MODEL: REACTIVE & CHAOTIC"
    p81_h.font.name = FONT_NAME
    p81_h.font.size = Pt(12)
    p81_h.font.bold = True
    p81_h.font.color.rgb = COLOR_MUTED_SLATE
    p81_h.space_after = Pt(12)

    old_points = [
        "• Manual phone trees and endless WhatsApp notifications.",
        "• No central real-time view of shelter refrigeration space.",
        "• High coordinator burnout with high volunteer dropout.",
        "• Food spoils while coordinators hunt for available drivers.",
        "• Frequent double allocations and wasted vehicle trips.",
    ]
    for op in old_points:
        pop = tf8_1.add_paragraph()
        pop.text = op
        pop.font.name = FONT_NAME
        pop.font.size = Pt(10)
        pop.font.color.rgb = COLOR_MUTED_SLATE
        pop.space_after = Pt(10)

    builder.add_cyber_card(s8, Inches(6.9), Inches(2.2), Inches(5.6), Inches(4.7), border_color=COLOR_NEON_PURPLE)
    tx8_2 = s8.shapes.add_textbox(Inches(7.2), Inches(2.4), Inches(5.0), Inches(4.3))
    tf8_2 = tx8_2.text_frame
    tf8_2.word_wrap = True

    p82_h = tf8_2.paragraphs[0]
    p82_h.text = "SURPLUS ROUTER: PROACTIVE & AUTONOMOUS"
    p82_h.font.name = FONT_NAME
    p82_h.font.size = Pt(12)
    p82_h.font.bold = True
    p82_h.font.color.rgb = COLOR_NEON_PURPLE
    p82_h.space_after = Pt(12)

    new_points = [
        "• Sub-second deterministic matching executed entirely in background.",
        "• Real-time DynamoDB intake tracking prevents fridge overload.",
        "• Coordinators act purely as exception managers.",
        "• Volunteers receive turn-by-turn routes matching cargo capacity.",
        "• Mathematical ACID transactions guarantee zero double claims.",
    ]
    for np in new_points:
        pnp = tf8_2.add_paragraph()
        pnp.text = np
        pnp.font.name = FONT_NAME
        pnp.font.size = Pt(10)
        pnp.font.color.rgb = COLOR_PURE_WHITE
        pnp.space_after = Pt(10)

    # =========================================================================
    # SLIDE 9: EDUCATION / TRANSFORMATION -> DECISION FORMULA (Matches Slide 9)
    # =========================================================================
    s9 = builder.add_cyber_slide(use_stage_bg=True)
    builder.add_top_badge(s9, "ALGORITHMIC LOGISTICS")

    tb9 = s9.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.3), Inches(1.0))
    tf9 = tb9.text_frame
    p9_h = tf9.paragraphs[0]
    p9_h.text = "Multi-Factor Decision Architecture"
    p9_h.font.name = FONT_NAME
    p9_h.font.size = Pt(32)
    p9_h.font.bold = True
    p9_h.font.color.rgb = COLOR_PURE_WHITE
    p9_h.alignment = PP_ALIGN.CENTER

    # Formula Callout Banner
    builder.add_cyber_card(s9, Inches(1.2), Inches(2.2), Inches(10.9), Inches(1.2), border_color=COLOR_NEON_CYAN)
    tx9_f = s9.shapes.add_textbox(Inches(1.5), Inches(2.35), Inches(10.3), Inches(0.9))
    tf9_f = tx9_f.text_frame
    tf9_f.word_wrap = True
    pf_h = tf9_f.paragraphs[0]
    pf_h.text = "COMPOSITE MATCH FORMULA"
    pf_h.font.name = FONT_NAME
    pf_h.font.size = Pt(9.5)
    pf_h.font.bold = True
    pf_h.font.color.rgb = COLOR_NEON_CYAN
    pf_h.space_after = Pt(2)

    pf_eq = tf9_f.add_paragraph()
    pf_eq.text = "Score = (0.40 × Road_Distance) + (0.30 × Capacity_Fit) + (0.20 × Urgency) + (0.10 × Dietary_Fit)"
    pf_eq.font.name = FONT_NAME
    pf_eq.font.size = Pt(15)
    pf_eq.font.bold = True
    pf_eq.font.color.rgb = COLOR_PURE_WHITE

    # 4 Factor Breakdown Cards on Stage
    f_cards = [
        ("Distance (40%)", "Amazon Location Service matrix routing within 25km radius.", COLOR_NEON_CYAN),
        ("Capacity (30%)", "DynamoDB atomic storage availability ratio matching.", COLOR_NEON_PURPLE),
        ("Urgency (20%)", "Fast-tracks food with <2h shelf-life remaining.", COLOR_NEON_MAGENTA),
        ("Dietary (10%)", "Binary gatekeeper for Halal, Vegetarian, & Allergen rules.", COLOR_LAVENDER),
    ]
    for i, (f_title, f_desc, f_col) in enumerate(f_cards):
        fx = Inches(1.2) + i * Inches(2.8)
        builder.add_cyber_card(s9, fx, Inches(3.6), Inches(2.6), Inches(2.9), border_color=f_col)
        tx = s9.shapes.add_textbox(fx + Inches(0.2), Inches(3.8), Inches(2.2), Inches(2.5))
        tf = tx.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = f_title
        pt.font.name = FONT_NAME
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = f_col
        pt.space_after = Pt(8)

        pd = tf.add_paragraph()
        pd.text = f_desc
        pd.font.name = FONT_NAME
        pd.font.size = Pt(9.5)
        pd.font.color.rgb = COLOR_PURE_WHITE

    # =========================================================================
    # SLIDE 10: BUSINESS APPLICATIONS (Matches Template Slide 10: Tablet Screen + Text)
    # =========================================================================
    s10 = builder.add_cyber_slide(use_stage_bg=False)
    builder.add_top_badge(s10, "ENTERPRISE VALUE")

    # Left: Cyber Screen Container
    builder.add_cyber_card(s10, Inches(0.8), Inches(1.4), Inches(5.2), Inches(5.4), border_color=COLOR_NEON_PURPLE)
    tx10_l = s10.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(4.6), Inches(4.8))
    tf10_l = tx10_l.text_frame
    tf10_l.word_wrap = True

    pl_h = tf10_l.paragraphs[0]
    pl_h.text = "ZERO-IDOR CLIENT PORTALS"
    pl_h.font.name = FONT_NAME
    pl_h.font.size = Pt(12)
    pl_h.font.bold = True
    pl_h.font.color.rgb = COLOR_NEON_MAGENTA
    pl_h.space_after = Pt(12)

    portal_points = [
        "1. Donor Report Portal:\nFrictionless 30-sec form without password walls; generates SHA-256 capability token.",
        "2. Status Tracker:\nZero-IDOR tracking page allowing donors to view live driver ETA without login.",
        "3. Shelter Check-in:\n1-click capacity slider updating DynamoDB remaining kg atomically.",
        "4. Volunteer Dispatch:\nTurn-by-turn mission cards with auto-masked phone numbers.",
    ]
    for pt in portal_points:
        ppt = tf10_l.add_paragraph()
        ppt.text = pt
        ppt.font.name = FONT_NAME
        ppt.font.size = Pt(9.2)
        ppt.font.color.rgb = COLOR_LAVENDER
        ppt.space_after = Pt(8)

    # Right: Enterprise Analytics Text
    tb10_r = s10.shapes.add_textbox(Inches(6.5), Inches(1.4), Inches(6.0), Inches(5.4))
    tf10_r = tb10_r.text_frame
    tf10_r.word_wrap = True

    pr10_h = tf10_r.paragraphs[0]
    pr10_h.text = "Enterprise Applications"
    pr10_h.font.name = FONT_NAME
    pr10_h.font.size = Pt(32)
    pr10_h.font.bold = True
    pr10_h.font.color.rgb = COLOR_PURE_WHITE
    pr10_h.space_after = Pt(10)

    app_bullets = [
        "• Automated Tax Invoicing: Generates auditable food donation tax exemption receipts under Section 170e.",
        "• Scope-3 Carbon Accounting: Provides enterprises with verifiable carbon offset metrics for global ESG reporting.",
        "• Kitchen Waste Intelligence: Highlights recurring over-prep patterns to help commercial kitchens reduce procurement costs.",
        "• Municipal Integration: Integrates directly with city smart-waste tracking dashboards for landfill diversion benchmarks.",
    ]
    for ab in app_bullets:
        pab = tf10_r.add_paragraph()
        pab.text = ab
        pab.font.name = FONT_NAME
        pab.font.size = Pt(10.5)
        pab.font.color.rgb = COLOR_PURE_WHITE
        pab.space_after = Pt(10)

    # =========================================================================
    # SLIDE 11: CHALLENGES FACED -> SAFETY GUARDRAILS (Matches Template Slide 11)
    # =========================================================================
    s11 = builder.add_cyber_slide(use_stage_bg=True)
    builder.add_top_badge(s11, "SAFETY GUARDRAILS")

    tb11 = s11.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.3), Inches(1.0))
    tf11 = tb11.text_frame
    p11_h = tf11.paragraphs[0]
    p11_h.text = "Ethical AI & Concurrency Guardrails"
    p11_h.font.name = FONT_NAME
    p11_h.font.size = Pt(32)
    p11_h.font.bold = True
    p11_h.font.color.rgb = COLOR_PURE_WHITE
    p11_h.alignment = PP_ALIGN.CENTER

    # 2 Radar/Node Containers on Stage (matching template slide 11!)
    builder.add_cyber_card(s11, Inches(1.5), Inches(2.2), Inches(4.9), Inches(4.3), border_color=COLOR_NEON_MAGENTA)
    tx11_1 = s11.shapes.add_textbox(Inches(1.8), Inches(2.4), Inches(4.3), Inches(3.9))
    tf11_1 = tx11_1.text_frame
    tf11_1.word_wrap = True

    p111_h = tf11_1.paragraphs[0]
    p111_h.text = "60-MINUTE SAFETY FLOOR"
    p111_h.font.name = FONT_NAME
    p111_h.font.size = Pt(12)
    p111_h.font.bold = True
    p111_h.font.color.rgb = COLOR_NEON_MAGENTA
    p111_h.space_after = Pt(8)

    g1_points = [
        "• Food Safety Regulations: Prepared meals with <60m shelf-life are halted from autonomous dispatch.",
        "• Human Escalation: Flags an emergency ticket to the human coordinator queue.",
        "• Prevents Legal Liability: Ensures spoiled food is never delivered to vulnerable shelter residents.",
        "• Capacity Deficit Guardrail: Escalates if all regional shelters report 0kg cold capacity.",
    ]
    for gp in g1_points:
        pgp = tf11_1.add_paragraph()
        pgp.text = gp
        pgp.font.name = FONT_NAME
        pgp.font.size = Pt(9.5)
        pgp.font.color.rgb = COLOR_LAVENDER
        pgp.space_after = Pt(7)

    builder.add_cyber_card(s11, Inches(6.9), Inches(2.2), Inches(4.9), Inches(4.3), border_color=COLOR_NEON_CYAN)
    tx11_2 = s11.shapes.add_textbox(Inches(7.2), Inches(2.4), Inches(4.3), Inches(3.9))
    tf11_2 = tx11_2.text_frame
    tf11_2.word_wrap = True

    p112_h = tf11_2.paragraphs[0]
    p112_h.text = "CONCURRENCY & CHAOS RESILIENCE"
    p112_h.font.name = FONT_NAME
    p112_h.font.size = Pt(12)
    p112_h.font.bold = True
    p112_h.font.color.rgb = COLOR_NEON_CYAN
    p112_h.space_after = Pt(8)

    g2_points = [
        "• 50-Thread Adversarial Gate: 50 concurrent requests competing for 50kg capacity resulted in exactly 1 claim.",
        "• 49 Graceful Reroutes: Eliminated double allocations through TransactWriteItems condition expressions.",
        "• Mid-Flight Crash Recovery: Replays uncompleted transit items without duplicate driver assignment.",
        "• 157 Passing Tests: 100% test pass rate with 0 Ruff linting errors.",
    ]
    for gp in g2_points:
        pgp = tf11_2.add_paragraph()
        pgp.text = gp
        pgp.font.name = FONT_NAME
        pgp.font.size = Pt(9.5)
        pgp.font.color.rgb = COLOR_LAVENDER
        pgp.space_after = Pt(7)

    # =========================================================================
    # SLIDE 12: FUTURE PROSPECTS -> ROADMAP & ACCESS (Matches Template Slide 12)
    # =========================================================================
    s12 = builder.add_cyber_slide(use_stage_bg=False)
    builder.add_top_badge(s12, "FUTURE VISION")

    # Left Column: Future Prospects Phases
    tb12_l = s12.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(5.8), Inches(5.7))
    tf12_l = tb12_l.text_frame
    tf12_l.word_wrap = True

    p12_h = tf12_l.paragraphs[0]
    p12_h.text = "Future Prospects"
    p12_h.font.name = FONT_NAME
    p12_h.font.size = Pt(34)
    p12_h.font.bold = True
    p12_h.font.color.rgb = COLOR_PURE_WHITE
    p12_h.space_after = Pt(10)

    phases = [
        ("Phase 1: Present (v1 Core Agent)", "1-to-1 autonomous matching, Location Service routing, DynamoDB ACID transactions, and 6-tab unified web portal. (LIVE)"),
        ("Phase 2: Near-Term (v2 Route Chaining)", "Multi-stop pickup route optimization, WhatsApp Business API conversational donor bot, and smart volunteer push notifications."),
        ("Phase 3: Long-Term (v3 IoT Telemetry)", "BLE / LoRaWAN cold-chain temperature monitoring, automated municipal health verification, and carbon credit marketplace."),
    ]
    for p_title, p_desc in phases:
        pt = tf12_l.add_paragraph()
        pt.text = p_title
        pt.font.name = FONT_NAME
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_NEON_MAGENTA
        pt.space_after = Pt(2)

        pd = tf12_l.add_paragraph()
        pd.text = p_desc
        pd.font.name = FONT_NAME
        pd.font.size = Pt(9.5)
        pd.font.color.rgb = COLOR_LAVENDER
        pd.space_after = Pt(10)

    # Right Column: Access & Presenter Card
    builder.add_cyber_card(s12, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.2), border_color=COLOR_NEON_PURPLE)
    tx12_r = s12.shapes.add_textbox(Inches(7.2), Inches(1.7), Inches(5.0), Inches(4.6))
    tf12_r = tx12_r.text_frame
    tf12_r.word_wrap = True

    pr12_tag = tf12_r.paragraphs[0]
    pr12_tag.text = "PROJECT REPOSITORY & DEMO ACCESS"
    pr12_tag.font.name = FONT_NAME
    pr12_tag.font.size = Pt(10)
    pr12_tag.font.bold = True
    pr12_tag.font.color.rgb = COLOR_NEON_CYAN
    pr12_tag.space_after = Pt(12)

    links = [
        ("Presenter:", "Bhumeshwari Bisen\nMachine Learning & Applied AI Intern\nIndore Institute of Science & Technology"),
        ("GitHub Repository:", "https://github.com/kuldeep-poonia/food-rescue-coordination-agent"),
        ("Local Dashboard:", "http://localhost:8080 (python server.py --port 8080 --mock)"),
        ("Demo Coordinator Key:", "dev-insecure-coordinator-key-for-local-testing-only-32chars"),
    ]
    for lt, ld in links:
        pt = tf12_r.add_paragraph()
        pt.text = lt
        pt.font.name = FONT_NAME
        pt.font.size = Pt(9.5)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_PURE_WHITE
        pt.space_after = Pt(1)

        pd = tf12_r.add_paragraph()
        pd.text = ld
        pd.font.name = FONT_NAME
        pd.font.size = Pt(9.0)
        pd.font.color.rgb = COLOR_MUTED_SLATE
        pd.space_after = Pt(8)

    builder.save()


if __name__ == "__main__":
    build_metaverse_deck()
