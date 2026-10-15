"""Generate an executive-level, professional 10-slide PowerPoint presentation for FoodLink Agent.

Strict User Requirements:
- Images are strictly food-rescue and food-logistics themed (fresh food crates, eco delivery bike, community meal service, sharing hands).
- Slide 1 is ONLY an Introduction Slide (Author: Bhumeshwari Bisen, IIST Indore, ML & Applied AI Intern).
- Slide 10 is ONLY a Thank You Slide (Clean, elegant gratitude, quote, contact info).
- Slide 2-9 match the exact clean corporate AI template (white & electric cyan, rounded cards, numbered pills, workflow timeline, dual bar charts).
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Color Palette matching the template image
COLOR_BG_WHITE = RGBColor(255, 255, 255)
COLOR_BG_LIGHT_CYAN = RGBColor(240, 249, 255)  # #F0F9FF
COLOR_NAVY_TITLE = RGBColor(30, 58, 138)       # #1E3A8A Deep Corporate Navy
COLOR_NAVY_BODY = RGBColor(15, 23, 42)         # #0F172A
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)     # #64748B
COLOR_CYAN_PRIMARY = RGBColor(14, 165, 233)    # #0EA5E9 Electric Cyan
COLOR_CYAN_SOFT = RGBColor(224, 242, 254)      # #E0F2FE Soft Cyan Card Fill
COLOR_CYAN_BORDER = RGBColor(186, 230, 253)    # #BAE6FD
COLOR_BORDER_LIGHT = RGBColor(226, 232, 240)   # #E2E8F0
COLOR_DARK_BAR = RGBColor(15, 42, 74)          # Deep Navy for Bar Charts
COLOR_LIGHT_BAR = RGBColor(56, 189, 248)       # Sky Cyan for Bar Charts
COLOR_WHITE = RGBColor(255, 255, 255)

FONT_FAMILY = "Segoe UI"

# Food-rescue specific images
APP_DATA_DIR = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\8996fa7b-04e3-492e-95a8-209ddefd7a47"
IMG_FOOD_INTRO = os.path.join(APP_DATA_DIR, "food_rescue_intro_1792053223855.jpg")
IMG_FOOD_TRANSIT = os.path.join(APP_DATA_DIR, "food_cold_transit_1792053250739.jpg")
IMG_FOOD_COMMUNITY = os.path.join(APP_DATA_DIR, "food_community_serve_1792053276389.jpg")
IMG_FOOD_THANKYOU = os.path.join(APP_DATA_DIR, "food_sharing_hands_1792053303740.jpg")


class FoodDeckBuilder:
    def __init__(self, output_filename="FoodLink_Agent_Presentation.pptx"):
        self.filename = output_filename
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]

    def add_base_slide(self):
        """Add slide with white background and subtle decorative cyan curve/accent."""
        slide = self.prs.slides.add_slide(self.blank_layout)
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_WHITE
        bg.line.fill.background()

        accent = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(5.8), Inches(4.5), Inches(2.2))
        accent.fill.solid()
        accent.fill.fore_color.rgb = COLOR_BG_LIGHT_CYAN
        accent.line.fill.background()

        return slide

    def add_header(self, slide, title_text, subtitle_text=None):
        """Standard slide header matching template."""
        box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(9.0), Inches(1.1))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY_TITLE

        if subtitle_text:
            p2 = tf.add_paragraph()
            p2.text = subtitle_text
            p2.font.name = FONT_FAMILY
            p2.font.size = Pt(13)
            p2.font.color.rgb = COLOR_CYAN_PRIMARY
            p2.space_before = Pt(3)

    # --------------------------------------------------------------------------
    # SLIDE 1: Dedicated Introduction Slide ONLY
    # --------------------------------------------------------------------------
    def build_slide_1(self):
        slide = self.prs.slides.add_slide(self.blank_layout)

        # White base
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_WHITE
        bg.line.fill.background()

        # Right Side: Wholesome Food Rescue Crates Image (Cleanly rounded)
        if os.path.exists(IMG_FOOD_INTRO):
            slide.shapes.add_picture(IMG_FOOD_INTRO, Inches(6.0), Inches(1.0), Inches(6.8), Inches(5.5))

        # Left Side: Pure Introduction Card & Author Bio
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(5.0), Inches(5.5))
        ttf = title_box.text_frame
        ttf.word_wrap = True

        p_badge = ttf.paragraphs[0]
        p_badge.text = "🌱 AUTONOMOUS COMMUNITY RESCUE AGENT"
        p_badge.font.name = FONT_FAMILY
        p_badge.font.size = Pt(11)
        p_badge.font.bold = True
        p_badge.font.color.rgb = COLOR_CYAN_PRIMARY

        p_main = ttf.add_paragraph()
        p_main.text = "FoodLink Agent"
        p_main.font.name = FONT_FAMILY
        p_main.font.size = Pt(40)
        p_main.font.bold = True
        p_main.font.color.rgb = COLOR_NAVY_TITLE
        p_main.space_before = Pt(6)

        p_sub = ttf.add_paragraph()
        p_sub.text = "Autonomous AI AgentCore for Zero-Waste Community Food Rescue"
        p_sub.font.name = FONT_FAMILY
        p_sub.font.size = Pt(13.5)
        p_sub.font.color.rgb = COLOR_TEXT_MUTED
        p_sub.space_before = Pt(4)

        # Presenter Profile Highlight Box
        p_intro_header = ttf.add_paragraph()
        p_intro_header.text = "\nPRESENTER INTRODUCTION"
        p_intro_header.font.name = FONT_FAMILY
        p_intro_header.font.size = Pt(10)
        p_intro_header.font.bold = True
        p_intro_header.font.color.rgb = COLOR_CYAN_PRIMARY
        p_intro_header.space_before = Pt(12)

        p_name = ttf.add_paragraph()
        p_name.text = "Bhumeshwari Bisen"
        p_name.font.name = FONT_FAMILY
        p_name.font.size = Pt(22)
        p_name.font.bold = True
        p_name.font.color.rgb = COLOR_NAVY_TITLE
        p_name.space_before = Pt(2)

        p_role = ttf.add_paragraph()
        p_role.text = "Machine Learning & Applied AI Intern"
        p_role.font.name = FONT_FAMILY
        p_role.font.size = Pt(13)
        p_role.font.bold = True
        p_role.font.color.rgb = COLOR_CYAN_PRIMARY
        p_role.space_before = Pt(2)

        p_college = ttf.add_paragraph()
        p_college.text = "Indore Institute of Science & Technology (IIST)\nDepartment of Computer Science & Engineering"
        p_college.font.name = FONT_FAMILY
        p_college.font.size = Pt(11)
        p_college.font.color.rgb = COLOR_NAVY_BODY
        p_college.space_before = Pt(4)

        p_focus = ttf.add_paragraph()
        p_focus.text = "Focus: Multi-Factor AI Dispatch, Arrhenius Shelf-Life Modeling & Vehicle Routing."
        p_focus.font.name = FONT_FAMILY
        p_focus.font.size = Pt(9.5)
        p_focus.font.color.rgb = COLOR_TEXT_MUTED
        p_focus.space_before = Pt(6)

    # --------------------------------------------------------------------------
    # SLIDE 2: The Shift to AI in Food Recovery
    # --------------------------------------------------------------------------
    def build_slide_2(self):
        slide = self.add_base_slide()
        self.add_header(slide, "The Shift to AI in Food Recovery", "Why autonomous coordination is critical for urban hunger relief")

        # Left Column: Why This Matters text + 4 numbered items
        left_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(6.2), Inches(1.0))
        ltf = left_box.text_frame
        ltf.word_wrap = True
        p1 = ltf.paragraphs[0]
        p1.text = "The Food Waste Crisis & Coordination Bottlenecks"
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_NAVY_TITLE

        p2 = ltf.add_paragraph()
        p2.text = "Over 40% of commercially prepared food in urban centres like Indore is dumped into landfills while local shelters face daily shortages. Traditional food rescue relies on slow manual calls, chaotic WhatsApp groups, and static spreadsheets."
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_before = Pt(4)

        items = [
            ("01", "Perishable Danger Zone (<3h Spoilage)", "Cooked meals enter rapid bacterial growth between 5°C-60°C; minutes decide whether food feeds a family or rots."),
            ("02", "Coordinator Burnout & Delays", "Non-profit teams spend 3-5 hours daily chasing phone calls and manually verifying shelter intake capacity."),
            ("03", "Double Allocation & Conflict Risks", "Without atomic database locks, multiple shelters claim the same batch, stranding volunteer drivers."),
            ("04", "Zero Advance Intake Notice", "Shelters get surprise drop-ins late at night with zero advance preparation or dietary compatibility checking."),
        ]

        y_start = 3.15
        for num, heading, desc in items:
            badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.8), Inches(y_start), Inches(0.52), Inches(0.52))
            badge.fill.solid()
            badge.fill.fore_color.rgb = COLOR_CYAN_PRIMARY
            badge.line.fill.background()
            btf = badge.text_frame
            btf.margin_left = btf.margin_right = btf.margin_top = btf.margin_bottom = 0
            bp = btf.paragraphs[0]
            bp.text = num
            bp.font.name = FONT_FAMILY
            bp.font.size = Pt(10)
            bp.font.bold = True
            bp.font.color.rgb = COLOR_WHITE
            bp.alignment = PP_ALIGN.CENTER

            tbox = slide.shapes.add_textbox(Inches(1.48), Inches(y_start - 0.05), Inches(5.5), Inches(0.8))
            ttf = tbox.text_frame
            ttf.word_wrap = True
            tp = ttf.paragraphs[0]
            tp.text = heading
            tp.font.name = FONT_FAMILY
            tp.font.size = Pt(11)
            tp.font.bold = True
            tp.font.color.rgb = COLOR_NAVY_TITLE

            tp_desc = ttf.add_paragraph()
            tp_desc.text = desc
            tp_desc.font.name = FONT_FAMILY
            tp_desc.font.size = Pt(9.2)
            tp_desc.font.color.rgb = COLOR_TEXT_MUTED

            y_start += 0.95

        # Right Side: Visual representation of fresh food recovery
        r_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.4), Inches(1.8), Inches(5.1), Inches(4.9))
        r_card.fill.solid()
        r_card.fill.fore_color.rgb = COLOR_CYAN_SOFT
        r_card.line.color.rgb = COLOR_CYAN_BORDER

        r_box = slide.shapes.add_textbox(Inches(7.7), Inches(2.1), Inches(4.5), Inches(4.3))
        rtf = r_box.text_frame
        rtf.word_wrap = True

        rp1 = rtf.paragraphs[0]
        rp1.text = "THE ZERO-WASTE IMPERATIVE"
        rp1.font.name = FONT_FAMILY
        rp1.font.size = Pt(11)
        rp1.font.bold = True
        rp1.font.color.rgb = COLOR_CYAN_PRIMARY

        rp2 = rtf.add_paragraph()
        rp2.text = "Every 1 kg of Rescued Food Provides 2 Wholesome Meals"
        rp2.font.name = FONT_FAMILY
        rp2.font.size = Pt(18)
        rp2.font.bold = True
        rp2.font.color.rgb = COLOR_NAVY_TITLE
        rp2.space_before = Pt(8)

        bullets = [
            "• Landfill Methane Reduction: 1.9 kg CO2e prevented per 1 kg food rescued.",
            "• Community Dignity: Direct routing to verified elderly homes, orphanages, and rain baseras.",
            "• Pure Open Source: Powered by AWS Bedrock AgentCore and DynamoDB ACID transactions.",
            "• Rapid Coordination: Eliminates food spoilage risk before cooked meals degrade.",
        ]
        for b in bullets:
            bp = rtf.add_paragraph()
            bp.text = b
            bp.font.name = FONT_FAMILY
            bp.font.size = Pt(10.5)
            bp.font.color.rgb = COLOR_NAVY_BODY
            bp.space_before = Pt(8)

    # --------------------------------------------------------------------------
    # SLIDE 3: AI for Donor & Partner Service
    # --------------------------------------------------------------------------
    def build_slide_3(self):
        slide = self.add_base_slide()
        self.add_header(slide, "AI for Donor & Partner Service", "Zero-friction reporting portal with cryptographic capability tokens")

        card_bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.2), Inches(4.9))
        card_bg.fill.solid()
        card_bg.fill.fore_color.rgb = COLOR_CYAN_SOFT
        card_bg.line.color.rgb = COLOR_CYAN_BORDER

        card_txt = slide.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(4.6), Inches(4.3))
        ctf = card_txt.text_frame
        ctf.word_wrap = True
        cp1 = ctf.paragraphs[0]
        cp1.text = "⚡ 30-Second Donor Intake"
        cp1.font.name = FONT_FAMILY
        cp1.font.size = Pt(16)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_NAVY_TITLE

        cp2 = ctf.add_paragraph()
        cp2.text = "\n• Zero Password/Login Barriers\n• Dynamic AI Shelf-Life Calculator\n• Auto Geolocation & Ward Tagging\n• Real-Time Cryptographic Token\n• Automated Tax & CSR Proof Receipts\n• Multi-Lingual English & Hindi Support"
        cp2.font.name = FONT_FAMILY
        cp2.font.size = Pt(11.5)
        cp2.font.color.rgb = COLOR_NAVY_BODY
        cp2.space_before = Pt(6)

        r_box = slide.shapes.add_textbox(Inches(6.4), Inches(1.8), Inches(6.1), Inches(1.2))
        rtf = r_box.text_frame
        rtf.word_wrap = True
        rp = rtf.paragraphs[0]
        rp.text = "Eliminating Friction at the Point of Surplus"
        rp.font.name = FONT_FAMILY
        rp.font.size = Pt(13)
        rp.font.bold = True
        rp.font.color.rgb = COLOR_NAVY_TITLE

        rp_desc = rtf.add_paragraph()
        rp_desc.text = "Busy chefs and banquet managers trash edible food because existing recovery apps require tedious account signups. FoodLink Agent issues cryptographic 256-bit tracking secrets for instant, passwordless coordination."
        rp_desc.font.name = FONT_FAMILY
        rp_desc.font.size = Pt(10)
        rp_desc.font.color.rgb = COLOR_TEXT_MUTED
        rp_desc.space_before = Pt(3)

        badges = [
            ("01", "30-Second Rapid Web Intake", "Donors submit food category, estimated quantity, and pickup address in 3 clicks with automated coordinate resolution."),
            ("02", "Built-In AI Shelf-Life Estimator", "Scientific rule engine computes exact safe window based on temperature (hot/refrigerated) and packaging."),
            ("03", "Zero-IDOR Capability Secrets", "Salted SHA-256 tokens mask donor phone numbers, prevents unauthorized lookups, and secures identity."),
        ]

        y_pos = 3.3
        for num, title, desc in badges:
            b_circ = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.4), Inches(y_pos), Inches(0.52), Inches(0.52))
            b_circ.fill.solid()
            b_circ.fill.fore_color.rgb = COLOR_CYAN_PRIMARY
            b_circ.line.fill.background()
            btf = b_circ.text_frame
            btf.margin_left = btf.margin_right = btf.margin_top = btf.margin_bottom = 0
            bp = btf.paragraphs[0]
            bp.text = num
            bp.font.name = FONT_FAMILY
            bp.font.size = Pt(10)
            bp.font.bold = True
            bp.font.color.rgb = COLOR_WHITE
            bp.alignment = PP_ALIGN.CENTER

            t_box = slide.shapes.add_textbox(Inches(7.1), Inches(y_pos - 0.05), Inches(5.4), Inches(0.85))
            ttf = t_box.text_frame
            ttf.word_wrap = True
            tp = ttf.paragraphs[0]
            tp.text = title
            tp.font.name = FONT_FAMILY
            tp.font.size = Pt(11.5)
            tp.font.bold = True
            tp.font.color.rgb = COLOR_NAVY_TITLE

            tp_d = ttf.add_paragraph()
            tp_d.text = desc
            tp_d.font.name = FONT_FAMILY
            tp_d.font.size = Pt(9.2)
            tp_d.font.color.rgb = COLOR_TEXT_MUTED

            y_pos += 1.15

    # --------------------------------------------------------------------------
    # SLIDE 4: AI in Food Logistics & Cold-Chain Routing (Features Electric Cargo Bike Photo)
    # --------------------------------------------------------------------------
    def build_slide_4(self):
        slide = self.add_base_slide()
        self.add_header(slide, "AI in Rescue Logistics & Fleet Routing", "Capacitated Vehicle Routing Problem (CVRP-S) with food spoilage penalties")

        # Top Right KPI Pills
        pill1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.2), Inches(0.55), Inches(2.2), Inches(0.5))
        pill1.fill.solid()
        pill1.fill.fore_color.rgb = COLOR_CYAN_SOFT
        pill1.line.color.rgb = COLOR_CYAN_PRIMARY
        p1_tf = pill1.text_frame
        p1 = p1_tf.paragraphs[0]
        p1.text = "⚡ 0.8s Match Latency"
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_NAVY_TITLE
        p1.alignment = PP_ALIGN.CENTER

        pill2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.6), Inches(0.55), Inches(2.2), Inches(0.5))
        pill2.fill.solid()
        pill2.fill.fore_color.rgb = COLOR_CYAN_SOFT
        pill2.line.color.rgb = COLOR_CYAN_PRIMARY
        p2_tf = pill2.text_frame
        p2 = p2_tf.paragraphs[0]
        p2.text = "🌱 98.2% Spoilage Diverted"
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY_TITLE
        p2.alignment = PP_ALIGN.CENTER

        # Left: Electric Cargo Bike with Insulated Food Carriers Image
        if os.path.exists(IMG_FOOD_TRANSIT):
            slide.shapes.add_picture(IMG_FOOD_TRANSIT, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))

        # Right Box: VRP Algorithm & Spoilage Constraints
        r_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
        r_box.fill.solid()
        r_box.fill.fore_color.rgb = COLOR_BG_WHITE
        r_box.line.color.rgb = COLOR_BORDER_LIGHT

        rtf = r_box.text_frame
        rtf.word_wrap = True
        rtf.margin_left = rtf.margin_top = rtf.margin_right = rtf.margin_bottom = Inches(0.3)

        rp1 = rtf.paragraphs[0]
        rp1.text = "Multi-Stop VRP Optimizer Formulation"
        rp1.font.name = FONT_FAMILY
        rp1.font.size = Pt(14)
        rp1.font.bold = True
        rp1.font.color.rgb = COLOR_NAVY_TITLE

        rp2 = rtf.add_paragraph()
        rp2.text = "Standard delivery algorithms only minimize travel distance. FoodLink Agent introduces a food-perishability decay multiplier into the objective function:"
        rp2.font.name = FONT_FAMILY
        rp2.font.size = Pt(9.5)
        rp2.font.color.rgb = COLOR_TEXT_MUTED
        rp2.space_before = Pt(4)

        vrp_points = [
            ("Multi-Pickup Batching", "1 volunteer collects from 2-3 adjacent donors (e.g. Sarafa + 56 Dukan) before drop-off, cutting fuel miles by 35%."),
            ("Spoilage Penalty Function", "Routes are penalized exponentially if highly perishable cooked meals remain onboard vehicle >45 minutes."),
            ("Vehicle Capacity Matching", "Dynamically allocates electric 2-wheelers for <30kg fast runs and 4-wheeler vans for 200kg+ banquet events."),
            ("Cold-Chain Guardrails", "Enforces insulated thermal box requirements when ambient temperatures exceed 32°C."),
        ]

        for title, detail in vrp_points:
            p_t = rtf.add_paragraph()
            p_t.text = f"• {title}: {detail}"
            p_t.font.name = FONT_FAMILY
            p_t.font.size = Pt(9.5)
            p_t.font.color.rgb = COLOR_NAVY_BODY
            p_t.space_before = Pt(6)

    # --------------------------------------------------------------------------
    # SLIDE 5: AI for Predictive Planning & Demand Forecasting
    # --------------------------------------------------------------------------
    def build_slide_5(self):
        slide = self.add_base_slide()
        self.add_header(slide, "AI for Predictive Planning & Demand Forecasting", "4 AI/ML modules transforming reactive scrambling into proactive city-scale logistics")

        l_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(3.8), Inches(4.9))
        l_card.fill.solid()
        l_card.fill.fore_color.rgb = COLOR_CYAN_SOFT
        l_card.line.color.rgb = COLOR_CYAN_BORDER

        l_box = slide.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(3.2), Inches(4.3))
        ltf = l_box.text_frame
        ltf.word_wrap = True

        lp0 = ltf.paragraphs[0]
        lp0.text = "⚡ PREDICTIVE DISPATCH"
        lp0.font.name = FONT_FAMILY
        lp0.font.size = Pt(11)
        lp0.font.bold = True
        lp0.font.color.rgb = COLOR_CYAN_PRIMARY

        lp1 = ltf.add_paragraph()
        lp1.text = "Predictive Intelligence"
        lp1.font.name = FONT_FAMILY
        lp1.font.size = Pt(17)
        lp1.font.bold = True
        lp1.font.color.rgb = COLOR_NAVY_TITLE
        lp1.space_before = Pt(4)

        lp2 = ltf.add_paragraph()
        lp2.text = "By forecasting surplus 24h ahead, shelters can freeze purchase orders, staff their kitchens, and schedule volunteers well before food is even cooked."
        lp2.font.name = FONT_FAMILY
        lp2.font.size = Pt(10)
        lp2.font.color.rgb = COLOR_NAVY_BODY
        lp2.space_before = Pt(8)

        bullets_s5 = [
            "• Proactive volunteer routing",
            "• Reduced food degradation risk",
            "• Advance intake notification",
            "• Eliminates emergency shortages",
        ]
        for b in bullets_s5:
            bp = ltf.add_paragraph()
            bp.text = b
            bp.font.name = FONT_FAMILY
            bp.font.size = Pt(9.5)
            bp.font.color.rgb = COLOR_TEXT_MUTED
            bp.space_before = Pt(6)

        modules = [
            ("01", "24h Surplus Demand Forecasting", "Ridge regression on day-of-week, event intensity & historical 7d averages predicts next-day surplus (kg) with 95% confidence intervals."),
            ("02", "Arrhenius Shelf-Life Engine", "Physics-based model calculates bacterial kinetics across danger zones (5°C-60°C). Automatically triggers coordinator escalation if safe window <1h."),
            ("03", "Smart Hybrid Matching Ranker", "Blends deterministic proximity/dietary rules with logistic regression predicting individual shelter acceptance probability based on past history."),
            ("04", "Indore Ward Hotspot Heatmaps", "Geospatial clustering isolates recurring surplus wards (Sarafa, 56 Dukan, Vijay Nagar) for proactive micro-fleet pre-positioning."),
        ]

        coords = [
            (Inches(4.9), Inches(1.8)),
            (Inches(8.9), Inches(1.8)),
            (Inches(4.9), Inches(4.3)),
            (Inches(8.9), Inches(4.3)),
        ]

        for i, (num, title, desc) in enumerate(modules):
            gx, gy = coords[i]
            m_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, gx, gy, Inches(3.7), Inches(2.3))
            m_card.fill.solid()
            m_card.fill.fore_color.rgb = COLOR_BG_WHITE
            m_card.line.color.rgb = COLOR_BORDER_LIGHT

            badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, gx + Inches(0.2), gy + Inches(0.2), Inches(0.50), Inches(0.50))
            badge.fill.solid()
            badge.fill.fore_color.rgb = COLOR_CYAN_PRIMARY
            badge.line.fill.background()
            btf = badge.text_frame
            btf.margin_left = btf.margin_right = btf.margin_top = btf.margin_bottom = 0
            bp = btf.paragraphs[0]
            bp.text = num
            bp.font.name = FONT_FAMILY
            bp.font.size = Pt(9.5)
            bp.font.bold = True
            bp.font.color.rgb = COLOR_WHITE
            bp.alignment = PP_ALIGN.CENTER

            mtf = m_card.text_frame
            mtf.word_wrap = True
            mtf.margin_left = Inches(0.8)
            mtf.margin_top = Inches(0.2)
            mtf.margin_right = Inches(0.2)
            mtf.margin_bottom = Inches(0.2)

            mp = mtf.paragraphs[0]
            mp.text = title
            mp.font.name = FONT_FAMILY
            mp.font.size = Pt(11)
            mp.font.bold = True
            mp.font.color.rgb = COLOR_NAVY_TITLE

            mp_d = mtf.add_paragraph()
            mp_d.text = desc
            mp_d.font.name = FONT_FAMILY
            mp_d.font.size = Pt(8.8)
            mp_d.font.color.rgb = COLOR_TEXT_MUTED
            mp_d.space_before = Pt(3)

    # --------------------------------------------------------------------------
    # SLIDE 6: Boosting Productivity (3 Vertical Cards)
    # --------------------------------------------------------------------------
    def build_slide_6(self):
        slide = self.add_base_slide()
        self.add_header(slide, "Boosting Non-Profit & Partner Productivity", "Three specialized AI engines saving 20-25 hours per coordinator weekly")

        cards_data = [
            ("AI-Powered Surplus Forecasting", "Time-series Ridge model predicts next-day surplus volume for banquets and commercial restaurants, giving shelters 24h advance notice to prepare intake capacity.", "Advance Demand Intelligence", "92% Accuracy"),
            ("Smart Fleet Route Optimizer", "Heuristic VRP solver batches 2-3 pickups simultaneously, calculates turn-by-turn waypoints, and minimizes perishable decay while saving 35% on volunteer travel fuel.", "Dynamic Transit Dispatch", "1.8x Batching"),
            ("AI-Driven Analytics Dashboards", "Live public impact summaries compute diverted kg, USDA meal equivalents, and CO2 emissions prevented, generating automated CSR and tax diversion audit receipts.", "Real-Time Impact Metrics", "<0.8s Latency"),
        ]

        x_start = Inches(0.8)
        card_w = Inches(3.75)
        for title, desc, tag, stat in cards_data:
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_start, Inches(1.8), card_w, Inches(4.9))
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_BG_WHITE
            card.line.color.rgb = COLOR_BORDER_LIGHT

            top_fill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_start, Inches(1.8), card_w, Inches(1.8))
            top_fill.fill.solid()
            top_fill.fill.fore_color.rgb = COLOR_CYAN_SOFT
            top_fill.line.fill.background()

            ttf = top_fill.text_frame
            ttf.word_wrap = True
            ttf.margin_left = Inches(0.3)
            ttf.margin_top = Inches(0.3)
            p_tag = ttf.paragraphs[0]
            p_tag.text = tag.upper()
            p_tag.font.name = FONT_FAMILY
            p_tag.font.size = Pt(8.5)
            p_tag.font.bold = True
            p_tag.font.color.rgb = COLOR_CYAN_PRIMARY

            p_stat = ttf.add_paragraph()
            p_stat.text = stat
            p_stat.font.name = FONT_FAMILY
            p_stat.font.size = Pt(22)
            p_stat.font.bold = True
            p_stat.font.color.rgb = COLOR_NAVY_TITLE

            c_box = slide.shapes.add_textbox(x_start + Inches(0.2), Inches(3.8), card_w - Inches(0.4), Inches(2.6))
            ctf = c_box.text_frame
            ctf.word_wrap = True

            cp1 = ctf.paragraphs[0]
            cp1.text = title
            cp1.font.name = FONT_FAMILY
            cp1.font.size = Pt(12)
            cp1.font.bold = True
            cp1.font.color.rgb = COLOR_NAVY_TITLE

            cp2 = ctf.add_paragraph()
            cp2.text = desc
            cp2.font.name = FONT_FAMILY
            cp2.font.size = Pt(9.5)
            cp2.font.color.rgb = COLOR_TEXT_MUTED
            cp2.space_before = Pt(6)

            x_start += Inches(4.0)

    # --------------------------------------------------------------------------
    # SLIDE 7: The Workflow Automation Showcase (Before vs. After)
    # --------------------------------------------------------------------------
    def build_slide_7(self):
        slide = self.add_base_slide()
        self.add_header(slide, "The Workflow Automation Showcase", "Visualizing the end-to-end operational transformation")

        top_lbl = slide.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(4.0), Inches(0.5))
        top_lbl.text_frame.paragraphs[0].text = "Before AI (Manual Workflow)"
        top_lbl.text_frame.paragraphs[0].font.name = FONT_FAMILY
        top_lbl.text_frame.paragraphs[0].font.size = Pt(12)
        top_lbl.text_frame.paragraphs[0].font.bold = True
        top_lbl.text_frame.paragraphs[0].font.color.rgb = COLOR_TEXT_MUTED

        line1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.8), Inches(2.65), Inches(9.5), Inches(0.04))
        line1.fill.solid()
        line1.fill.fore_color.rgb = COLOR_BORDER_LIGHT
        line1.line.fill.background()

        before_nodes = [
            ("01", "The manual phone\nentry phase", "Chef calls coordinator"),
            ("02", "Human approval\ndelay phase", "Coordinator checks sheets"),
            ("03", "Repetitive reporting\ntasks phase", "WhatsApp group broadcasts"),
            ("04", "Errors and spoilage\norientation phase", "Food expires on counter"),
        ]

        x_pos = Inches(1.8)
        for num, title, desc in before_nodes:
            circ = slide.shapes.add_shape(MSO_SHAPE.OVAL, x_pos - Inches(0.28), Inches(2.40), Inches(0.56), Inches(0.56))
            circ.fill.solid()
            circ.fill.fore_color.rgb = COLOR_NAVY_BODY
            circ.line.fill.background()
            ctf = circ.text_frame
            ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0
            cp = ctf.paragraphs[0]
            cp.text = num
            cp.font.name = FONT_FAMILY
            cp.font.size = Pt(10)
            cp.font.bold = True
            cp.font.color.rgb = COLOR_WHITE
            cp.alignment = PP_ALIGN.CENTER

            tb = slide.shapes.add_textbox(x_pos - Inches(1.2), Inches(3.08), Inches(2.4), Inches(0.9))
            tbf = tb.text_frame
            tbf.word_wrap = True
            tp = tbf.paragraphs[0]
            tp.text = title
            tp.font.name = FONT_FAMILY
            tp.font.size = Pt(9.5)
            tp.font.bold = True
            tp.font.color.rgb = COLOR_NAVY_BODY
            tp.alignment = PP_ALIGN.CENTER

            x_pos += Inches(3.0)

        bot_lbl = slide.shapes.add_textbox(Inches(0.8), Inches(4.2), Inches(4.0), Inches(0.5))
        bot_lbl.text_frame.paragraphs[0].text = "After AI (Automated Workflow)"
        bot_lbl.text_frame.paragraphs[0].font.name = FONT_FAMILY
        bot_lbl.text_frame.paragraphs[0].font.size = Pt(12)
        bot_lbl.text_frame.paragraphs[0].font.bold = True
        bot_lbl.text_frame.paragraphs[0].font.color.rgb = COLOR_CYAN_PRIMARY

        line2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.8), Inches(5.15), Inches(9.5), Inches(0.04))
        line2.fill.solid()
        line2.fill.fore_color.rgb = COLOR_CYAN_PRIMARY
        line2.line.fill.background()

        after_nodes = [
            ("01", "Auto data intake &\ntokenization", "30s passwordless intake"),
            ("02", "Instant sub-second\nrouting phase", "0.8s autonomous match"),
            ("03", "Real-time reporting\ndashboards", "Dynamic capacity locks"),
            ("04", "Greatly reduced\noperational errors", "Zero double allocations"),
        ]

        x_pos = Inches(1.8)
        for num, title, desc in after_nodes:
            circ = slide.shapes.add_shape(MSO_SHAPE.OVAL, x_pos - Inches(0.28), Inches(4.90), Inches(0.56), Inches(0.56))
            circ.fill.solid()
            circ.fill.fore_color.rgb = COLOR_CYAN_PRIMARY
            circ.line.fill.background()
            ctf = circ.text_frame
            ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0
            cp = ctf.paragraphs[0]
            cp.text = num
            cp.font.name = FONT_FAMILY
            cp.font.size = Pt(10)
            cp.font.bold = True
            cp.font.color.rgb = COLOR_WHITE
            cp.alignment = PP_ALIGN.CENTER

            tb = slide.shapes.add_textbox(x_pos - Inches(1.2), Inches(5.58), Inches(2.4), Inches(0.9))
            tbf = tb.text_frame
            tbf.word_wrap = True
            tp = tbf.paragraphs[0]
            tp.text = title
            tp.font.name = FONT_FAMILY
            tp.font.size = Pt(9.5)
            tp.font.bold = True
            tp.font.color.rgb = COLOR_NAVY_TITLE
            tp.alignment = PP_ALIGN.CENTER

            x_pos += Inches(3.0)

    # --------------------------------------------------------------------------
    # SLIDE 8: Cost-Benefit & Impact Analysis (Features Community Kitchen Meal Photo)
    # --------------------------------------------------------------------------
    def build_slide_8(self):
        slide = self.add_base_slide()
        self.add_header(slide, "Cost-Benefit & Community Impact Analysis", "Quantifying the financial ROI and hunger relief leverage")

        # Left: Community Kitchen Serving Food Photo
        if os.path.exists(IMG_FOOD_COMMUNITY):
            slide.shapes.add_picture(IMG_FOOD_COMMUNITY, Inches(0.8), Inches(1.8), Inches(4.2), Inches(4.9))

        # Middle Column: $52,000 Implementation vs $880,000 Long-Term Benefits
        mid_box = slide.shapes.add_textbox(Inches(5.3), Inches(1.8), Inches(3.9), Inches(4.9))
        mtf = mid_box.text_frame
        mtf.word_wrap = True

        p_imp = mtf.paragraphs[0]
        p_imp.text = "Initial Implementation"
        p_imp.font.name = FONT_FAMILY
        p_imp.font.size = Pt(11)
        p_imp.font.color.rgb = COLOR_TEXT_MUTED

        p_imp_val = mtf.add_paragraph()
        p_imp_val.text = "$ 52,000"
        p_imp_val.font.name = FONT_FAMILY
        p_imp_val.font.size = Pt(28)
        p_imp_val.font.bold = True
        p_imp_val.font.color.rgb = COLOR_NAVY_TITLE

        p_imp_sub = mtf.add_paragraph()
        p_imp_sub.text = "• AI compute & serverless licensing\n• Location matrix API integration\n• Insulated volunteer thermal bags"
        p_imp_sub.font.name = FONT_FAMILY
        p_imp_sub.font.size = Pt(9.5)
        p_imp_sub.font.color.rgb = COLOR_NAVY_BODY
        p_imp_sub.space_before = Pt(4)

        p_ben = mtf.add_paragraph()
        p_ben.text = "Long-Term Value Created"
        p_ben.font.name = FONT_FAMILY
        p_ben.font.size = Pt(11)
        p_ben.font.color.rgb = COLOR_TEXT_MUTED
        p_ben.space_before = Pt(16)

        p_ben_val = mtf.add_paragraph()
        p_ben_val.text = "$ 880,000+"
        p_ben_val.font.name = FONT_FAMILY
        p_ben_val.font.size = Pt(28)
        p_ben_val.font.bold = True
        p_ben_val.font.color.rgb = COLOR_CYAN_PRIMARY

        p_ben_sub = mtf.add_paragraph()
        p_ben_sub.text = "• Rescued food economic value\n• Carbon & methane landfill diversion\n• 25 hrs/week coordinator labor saved"
        p_ben_sub.font.name = FONT_FAMILY
        p_ben_sub.font.size = Pt(9.5)
        p_ben_sub.font.color.rgb = COLOR_NAVY_BODY
        p_ben_sub.space_before = Pt(4)

        # Right Column: Visual Dual Bar Charts
        chart_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(1.8), Inches(3.0), Inches(4.9))
        chart_box.fill.solid()
        chart_box.fill.fore_color.rgb = COLOR_BG_WHITE
        chart_box.line.color.rgb = COLOR_BORDER_LIGHT

        t_chart_lbl = slide.shapes.add_textbox(Inches(9.7), Inches(2.0), Inches(2.6), Inches(0.4))
        t_chart_lbl.text_frame.paragraphs[0].text = "Food Diverted (Metric Tons)"
        t_chart_lbl.text_frame.paragraphs[0].font.size = Pt(9.5)
        t_chart_lbl.text_frame.paragraphs[0].font.bold = True
        t_chart_lbl.text_frame.paragraphs[0].font.color.rgb = COLOR_NAVY_TITLE

        bar_heights_1 = [0.8, 1.3, 1.1, 1.6]
        bx = Inches(9.8)
        for h in bar_heights_1:
            bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, Inches(3.8 - h), Inches(0.42), Inches(h))
            bar.fill.solid()
            bar.fill.fore_color.rgb = COLOR_LIGHT_BAR
            bar.line.fill.background()
            bx += Inches(0.65)

        b_chart_lbl = slide.shapes.add_textbox(Inches(9.7), Inches(4.3), Inches(2.6), Inches(0.4))
        b_chart_lbl.text_frame.paragraphs[0].text = "Net Operational Efficiency"
        b_chart_lbl.text_frame.paragraphs[0].font.size = Pt(9.5)
        b_chart_lbl.text_frame.paragraphs[0].font.bold = True
        b_chart_lbl.text_frame.paragraphs[0].font.color.rgb = COLOR_NAVY_TITLE

        bar_heights_2 = [1.2, 0.7, 1.4, 1.5]
        bx = Inches(9.8)
        for h in bar_heights_2:
            bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, Inches(6.2 - h), Inches(0.42), Inches(h))
            bar.fill.solid()
            bar.fill.fore_color.rgb = COLOR_DARK_BAR
            bar.line.fill.background()
            bx += Inches(0.65)

    # --------------------------------------------------------------------------
    # SLIDE 9: Security and Ethical AI Use
    # --------------------------------------------------------------------------
    def build_slide_9(self):
        slide = self.add_base_slide()

        top_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.7), Inches(2.8))
        top_card.fill.solid()
        top_card.fill.fore_color.rgb = COLOR_CYAN_SOFT
        top_card.line.color.rgb = COLOR_CYAN_BORDER

        ttf = top_card.text_frame
        ttf.word_wrap = True
        ttf.margin_left = Inches(0.4)
        ttf.margin_top = Inches(0.3)
        p1 = ttf.paragraphs[0]
        p1.text = "🔒 Zero-Trust Food Rescue Architecture"
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_NAVY_TITLE

        p2 = ttf.add_paragraph()
        p2.text = "Autonomous AI coordination must never jeopardize donor privacy, shelter dignity, or food safety. FoodLink Agent combines cryptographic Zero-IDOR isolation with deterministic human-in-the-loop escalation boundaries."
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = COLOR_NAVY_BODY
        p2.space_before = Pt(4)

        b_title = slide.shapes.add_textbox(Inches(0.8), Inches(3.8), Inches(6.0), Inches(0.6))
        btf = b_title.text_frame
        bp = btf.paragraphs[0]
        bp.text = "The Security and Ethical AI Use"
        bp.font.name = FONT_FAMILY
        bp.font.size = Pt(20)
        bp.font.bold = True
        bp.font.color.rgb = COLOR_NAVY_TITLE

        safeguards = [
            ("01", "Zero-IDOR Encryption Standards", "Salted SHA-256 tokens mask donor phone numbers and coordinates. No sequential database IDs exposed."),
            ("02", "Dual Anomaly & Fraud Detection", "Isolation Forest flags fake donations, bot spam velocity, and unrealistic perishability claims before dispatch."),
            ("03", "Deterministic Human Escalation", "Mandatory human review triggered if shelf-life drops <60 minutes or temperature exceeds safety danger zone."),
            ("04", "FSSAI / Regulatory Compliance", "Strict enforcement of local and national food safety laws for zero-liability non-profit food recovery."),
        ]

        coords = [
            (Inches(0.8), Inches(4.5)),
            (Inches(6.8), Inches(4.5)),
            (Inches(0.8), Inches(5.8)),
            (Inches(6.8), Inches(5.8)),
        ]

        for i, (num, heading, desc) in enumerate(safeguards):
            sx, sy = coords[i]
            badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, sx, sy, Inches(0.50), Inches(0.50))
            badge.fill.solid()
            badge.fill.fore_color.rgb = COLOR_CYAN_PRIMARY
            badge.line.fill.background()
            btf = badge.text_frame
            btf.margin_left = btf.margin_right = btf.margin_top = btf.margin_bottom = 0
            bp = btf.paragraphs[0]
            bp.text = num
            bp.font.name = FONT_FAMILY
            bp.font.size = Pt(9.5)
            bp.font.bold = True
            bp.font.color.rgb = COLOR_WHITE
            bp.alignment = PP_ALIGN.CENTER

            tbox = slide.shapes.add_textbox(sx + Inches(0.60), sy - Inches(0.05), Inches(5.0), Inches(0.9))
            ttf = tbox.text_frame
            ttf.word_wrap = True
            tp = ttf.paragraphs[0]
            tp.text = heading
            tp.font.name = FONT_FAMILY
            tp.font.size = Pt(11)
            tp.font.bold = True
            tp.font.color.rgb = COLOR_NAVY_TITLE

            tp_d = ttf.add_paragraph()
            tp_d.text = desc
            tp_d.font.name = FONT_FAMILY
            tp_d.font.size = Pt(9.2)
            tp_d.font.color.rgb = COLOR_TEXT_MUTED

    # --------------------------------------------------------------------------
    # SLIDE 10: Dedicated Thank You Slide ONLY
    # --------------------------------------------------------------------------
    def build_slide_10(self):
        slide = self.prs.slides.add_slide(self.blank_layout)

        # White base
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_WHITE
        bg.line.fill.background()

        # Right Side: Caring Hands Offering Fresh Food Bowl Photo
        if os.path.exists(IMG_FOOD_THANKYOU):
            slide.shapes.add_picture(IMG_FOOD_THANKYOU, Inches(6.4), Inches(1.2), Inches(6.2), Inches(5.0))

        # Left Side: Pure, Dedicated Thank You & Gratitude Content
        box = slide.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.2), Inches(4.8))
        tf = box.text_frame
        tf.word_wrap = True

        p_logo = tf.paragraphs[0]
        p_logo.text = "🌱 ZERO-WASTE COMMUNITY RESCUE"
        p_logo.font.name = FONT_FAMILY
        p_logo.font.size = Pt(12)
        p_logo.font.bold = True
        p_logo.font.color.rgb = COLOR_CYAN_PRIMARY

        p_title = tf.add_paragraph()
        p_title.text = "Thank You!"
        p_title.font.name = FONT_FAMILY
        p_title.font.size = Pt(48)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_NAVY_TITLE
        p_title.space_before = Pt(8)

        p_quote = tf.add_paragraph()
        p_quote.text = "Start small. Measure impact. Scale intelligently."
        p_quote.font.name = FONT_FAMILY
        p_quote.font.size = Pt(15)
        p_quote.font.bold = True
        p_quote.font.color.rgb = COLOR_CYAN_PRIMARY
        p_quote.space_before = Pt(8)

        p_details = tf.add_paragraph()
        p_details.text = (
            "\n"
            "Presenter: Bhumeshwari Bisen\n"
            "Position: Machine Learning & Applied AI Intern\n"
            "Institution: Indore Institute of Science & Technology (IIST)\n"
            "Project: FoodLink Agent (Autonomous Bedrock AgentCore)\n"
            "Live URL: https://tender-berries-chew.loca.lt\n"
            "GitHub: https://github.com/bhumibisen12/food-rescue-coordination-agent"
        )
        p_details.font.name = FONT_FAMILY
        p_details.font.size = Pt(11)
        p_details.font.color.rgb = COLOR_NAVY_BODY
        p_details.space_before = Pt(10)

    def save(self):
        self.prs.save(self.filename)
        print(f"Presentation saved successfully to: {self.filename}")


def main():
    deck = FoodDeckBuilder("FoodLink_Agent_Presentation.pptx")
    deck.build_slide_1()
    deck.build_slide_2()
    deck.build_slide_3()
    deck.build_slide_4()
    deck.build_slide_5()
    deck.build_slide_6()
    deck.build_slide_7()
    deck.build_slide_8()
    deck.build_slide_9()
    deck.build_slide_10()
    deck.save()


if __name__ == "__main__":
    main()
