"""Regenerate the bold variant of the presentation template.

    pip install python-pptx
    python scripts/make_deck_template_gradient.py

The alternative to make_deck_template.py. That one follows the group's existing
white deck; this one leads with the KRICT CI ramp - gradient title and closing
slides, gradient rules on the content slides. Use it where a deck should look
like the website rather than like a report. The institute mark is joined to the
lab's own on every slide that carries a mark, so the deck reads as a group
inside KRICT rather than as a lab standing on its own.

Writes assets/templates/MS3L_presentation_template_gradient.pptx.
"""
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.makedirs("assets/templates", exist_ok=True)

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

FONT = "Arial"
NAVY = RGBColor(0x0B, 0x2F, 0x5B)
BLUE = RGBColor(0x00, 0x75, 0xC2)
TEAL = RGBColor(0x00, 0xAD, 0xA9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x5B, 0x6F, 0x84)
LIGHT = RGBColor(0xF4, 0xF8, 0xFD)
LINE = RGBColor(0xD6, 0xE2, 0xEE)
PALE = RGBColor(0xDC, 0xF1, 0xF6)
PALE2 = RGBColor(0xB6, 0xE5, 0xE3)

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
W, H = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]
L = "assets/images/logo"
LOCKW = f"{L}/ms3l-lockup-horizontal-white.png"
MARK = f"{L}/ms3l-avatar-circle.png"
KRICT = "assets/images/logos/krict-logo.png"
KRICTW = "assets/images/logos/krict-logo-white.png"
KRICT_AR = 1200 / 379              # the wordmark as supplied, width over height
M = Inches(0.85)


def grad(sh, angle=0.0):
    sh.fill.gradient(); st = sh.fill.gradient_stops
    st[0].color.rgb, st[0].position = BLUE, 0.0
    st[1].color.rgb, st[1].position = TEAL, 1.0
    sh.fill.gradient_angle = angle; sh.line.fill.background()


def rect(s, x, y, w, h):
    return s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)


def solid(sh, c, line=None):
    sh.fill.solid(); sh.fill.fore_color.rgb = c
    if line is not None:
        sh.line.color.rgb = line; sh.line.width = Pt(0.75)
    else:
        sh.line.fill.background()


def text(s, x, y, w, h, t, size, color, bold=False, align=PP_ALIGN.LEFT, space=1.0):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = align; p.line_spacing = space
    r = p.add_run(); r.text = t
    r.font.size, r.font.bold, r.font.name = Pt(size), bold, FONT
    r.font.color.rgb = color
    return tb


def endorse(s, right, cy, mh, kh, krict=KRICT, rule=LINE):
    """The lab ring, a hairline, then the institute wordmark - one lockup ending
    at `right` and centred on `cy`. Joined rather than parked in opposite
    corners, which is what makes MS3L read as a group within KRICT."""
    kw = int(kh * KRICT_AR)
    kx = right - kw
    s.shapes.add_picture(krict, kx, cy - kh // 2, height=kh)
    rx = kx - Inches(0.18)
    solid(rect(s, rx, cy - mh // 2 + Inches(0.03), Inches(0.014), mh - Inches(0.06)), rule)
    s.shapes.add_picture(MARK, rx - Inches(0.18) - mh, cy - mh // 2, height=mh)


def chrome(s, n, title):
    grad(rect(s, 0, 0, W, Inches(0.10)))
    text(s, M, Inches(0.52), Inches(9.4), Inches(0.7), title, 28, NAVY, True)
    grad(rect(s, M, Inches(1.16), Inches(1.5), Inches(0.05)))
    endorse(s, W - M, Inches(0.73), Inches(0.42), Inches(0.26))
    text(s, W - Inches(1.55), H - Inches(0.52), Inches(0.7), Inches(0.3),
         str(n), 12, GREY, align=PP_ALIGN.RIGHT)


# 1 title -------------------------------------------------------------------
s = prs.slides.add_slide(BLANK); grad(rect(s, 0, 0, W, H), 315.0)
s.shapes.add_picture(LOCKW, M, Inches(1.95), width=Inches(7.9))
solid(rect(s, M + Inches(8.32), Inches(2.03), Inches(0.016), Inches(1.20)), PALE2)
_kh = Inches(0.74)
s.shapes.add_picture(KRICTW, M + Inches(8.80), Inches(2.63) - _kh // 2, height=_kh)
text(s, M, Inches(4.05), Inches(10.6), Inches(0.9), "Title", 38, WHITE, True)
text(s, M, Inches(4.92), Inches(10.6), Inches(0.6), "Sub-title", 20, PALE)
text(s, M, Inches(5.72), Inches(10.6), Inches(0.5), "Name", 15, WHITE, True)
text(s, M, Inches(6.10), Inches(11.4), Inches(0.5),
     "Membrane-based Sustainable Separation Solutions Laboratory"
     "  ·  Korea Research Institute of Chemical Technology", 13, PALE2)
text(s, M, Inches(6.46), Inches(10.6), Inches(0.4), "2026.00.00.", 12, PALE2)

# 2 section divider ---------------------------------------------------------
s = prs.slides.add_slide(BLANK); solid(rect(s, 0, 0, W, H), WHITE)
grad(rect(s, 0, 0, Inches(0.40), H), 270.0)
text(s, Inches(1.5), Inches(3.05), Inches(9), Inches(0.5), "01", 16, TEAL, True)
text(s, Inches(1.5), Inches(3.48), Inches(10), Inches(1.0), "Section title", 40, NAVY, True)
grad(rect(s, Inches(1.5), Inches(4.62), Inches(2.0), Inches(0.07)))
endorse(s, W - M, H - Inches(1.28), Inches(0.95), Inches(0.34))

# 3 content -----------------------------------------------------------------
s = prs.slides.add_slide(BLANK); solid(rect(s, 0, 0, W, H), WHITE); chrome(s, 3, "Content #1")
text(s, M, Inches(1.52), Inches(11.4), Inches(0.4), "Lead line for the slide.", 15, BLUE, True)
for i, (hd, bd) in enumerate([("Point one", "Supporting detail for the first point."),
                              ("Point two", "Supporting detail for the second point."),
                              ("Point three", "Supporting detail for the third point.")]):
    y = Inches(2.20 + i * 0.98)
    solid(s.shapes.add_shape(MSO_SHAPE.OVAL, M, y + Inches(0.07), Inches(0.15), Inches(0.15)), TEAL)
    text(s, M + Inches(0.38), y, Inches(11.0), Inches(0.4), hd, 17, NAVY, True)
    text(s, M + Inches(0.38), y + Inches(0.34), Inches(11.0), Inches(0.4), bd, 14, GREY)

# 4 two column --------------------------------------------------------------
s = prs.slides.add_slide(BLANK); solid(rect(s, 0, 0, W, H), WHITE); chrome(s, 4, "Content #2")
for i, side in enumerate(["Left column", "Right column"]):
    x = M + Inches(i * 5.92)
    solid(rect(s, x, Inches(1.62), Inches(5.62), Inches(4.85)), LIGHT, LINE)
    grad(rect(s, x, Inches(1.62), Inches(0.06), Inches(4.85)), 270.0)
    text(s, x + Inches(0.36), Inches(1.94), Inches(5.0), Inches(0.4), side, 17, NAVY, True)
    text(s, x + Inches(0.36), Inches(2.42), Inches(5.0), Inches(3.6),
         "Body text. Replace with a figure, a table or bullets.", 14, GREY, space=1.35)

# 5 figure ------------------------------------------------------------------
s = prs.slides.add_slide(BLANK); solid(rect(s, 0, 0, W, H), WHITE); chrome(s, 5, "Content #3")
ph = rect(s, M, Inches(1.55), W - 2 * M, Inches(4.8)); solid(ph, LIGHT, LINE)
text(s, M, Inches(3.80), W - 2 * M, Inches(0.5), "Place figure here", 15,
     RGBColor(0x9A, 0xAE, 0xC2), align=PP_ALIGN.CENTER)
text(s, M, Inches(6.48), W - 2 * M, Inches(0.4), "Figure 1. Caption.", 12, GREY)

# 6 closing -----------------------------------------------------------------
s = prs.slides.add_slide(BLANK); grad(rect(s, 0, 0, W, H), 315.0)
s.shapes.add_picture(MARK, Inches(6.07), Inches(1.90), width=Inches(1.5))
text(s, M, Inches(3.85), W - 2 * M, Inches(0.8), "Thank you", 36, WHITE, True, PP_ALIGN.CENTER)
text(s, M, Inches(4.80), W - 2 * M, Inches(0.4), "jh.kim@krict.re.kr", 15, PALE, align=PP_ALIGN.CENTER)
text(s, M, Inches(5.20), W - 2 * M, Inches(0.4), "https://ms3l.org", 14, PALE2, align=PP_ALIGN.CENTER)
solid(rect(s, (W - Inches(1.1)) // 2, Inches(5.82), Inches(1.1), Inches(0.014)), PALE2)
_kh = Inches(0.46)
s.shapes.add_picture(KRICTW, (W - int(_kh * KRICT_AR)) // 2, Inches(6.08), height=_kh)
text(s, M, Inches(6.72), W - 2 * M, Inches(0.35),
     "Korea Research Institute of Chemical Technology", 11, PALE2, align=PP_ALIGN.CENTER)

prs.save("assets/templates/MS3L_presentation_template_gradient.pptx")
print("gradient deck built")
