"""Regenerate the group poster template.

    pip install python-pptx
    python scripts/make_poster_template.py

36 x 48 in portrait, the size most conference boards take. White ground with the
title in KRICT blue over a thin CI rule, matching the group's existing deck.
make_poster_template_gradient.py is the bold alternative.

Body copy is 26 pt, which stays readable from about 1.5 m. If you rescale the
board, scale the type with it.

Writes assets/templates/MS3L_poster_template.pptx.
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
NAVY = RGBColor(0x0B, 0x2F, 0x5B); BLUE = RGBColor(0x00, 0x75, 0xC2)
TEAL = RGBColor(0x00, 0xAD, 0xA9); WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x5B, 0x6F, 0x84); LIGHT = RGBColor(0xF4, 0xF8, 0xFD)
LINE = RGBColor(0xD6, 0xE2, 0xEE)

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(36), Inches(48)
W, H = prs.slide_width, prs.slide_height
s = prs.slides.add_slide(prs.slide_layouts[6])
L = "assets/images/logo"


def grad(sh, a=0.0):
    sh.fill.gradient(); st = sh.fill.gradient_stops
    st[0].color.rgb, st[0].position = BLUE, 0.0
    st[1].color.rgb, st[1].position = TEAL, 1.0
    sh.fill.gradient_angle = a; sh.line.fill.background()


def rect(x, y, w, h): return s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)


def solid(sh, c, line=None):
    sh.fill.solid(); sh.fill.fore_color.rgb = c
    if line is not None:
        sh.line.color.rgb = line; sh.line.width = Pt(1)
    else:
        sh.line.fill.background()


def text(x, y, w, h, t, size, color, bold=False, align=PP_ALIGN.LEFT, space=1.0):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = align; p.line_spacing = space
    r = p.add_run(); r.text = t
    r.font.size, r.font.bold, r.font.name = Pt(size), bold, FONT
    r.font.color.rgb = color
    return tb


solid(rect(0, 0, W, H), WHITE)

# ---- header ----------------------------------------------------------------
BAND = Inches(6.4)
M = Inches(1.6)
s.shapes.add_picture(f"{L}/ms3l-lockup-horizontal.png", M, Inches(0.72), width=Inches(10.2))
s.shapes.add_picture("assets/images/logos/krict-logo.png", Inches(30.0), Inches(1.05), width=Inches(4.2))
text(M, Inches(2.62), Inches(33), Inches(2.1),
     "Poster title goes here, one or two lines at most", 60, NAVY, True, space=1.06)
text(M, Inches(4.58), Inches(33), Inches(0.8),
     "Jihoon Kim¹²*, Coauthor One¹, Coauthor Two²", 28, BLUE, True)
text(M, Inches(5.32), Inches(33), Inches(1.2),
     "¹ Chemical Process Technology Division, Korea Research Institute of Chemical Technology (KRICT), Daejeon, Republic of Korea\n"
     "² Advanced Materials and Chemical Engineering, University of Science and Technology (UST)    •    * jh.kim@krict.re.kr",
     20, GREY, space=1.32)
grad(rect(0, BAND, W, Inches(0.12)))

# ---- columns ---------------------------------------------------------------
GAP = Inches(1.1)
COLW = int((W - 2 * M - 2 * GAP) / 3)
TOP = BAND + Inches(1.3)
BOTBAR = Inches(2.6)
COLH = H - TOP - BOTBAR - Inches(1.2)

BODY = ("Replace with your text. Body copy at this size stays readable from about 1.5 m, "
        "which is where people stand at a poster board.\n\n"
        "Keep each section to a few short paragraphs and let the figures carry the argument.")


def panel(cx, y, h, title):
    x = M + cx * (COLW + GAP)
    solid(rect(x, y, COLW, h), WHITE, LINE)
    grad(rect(x, y, COLW, Inches(0.14)))
    text(x + Inches(0.8), y + Inches(0.62), COLW - Inches(1.6), Inches(1.0), title, 40, NAVY, True)
    grad(rect(x + Inches(0.8), y + Inches(1.72), Inches(3.4), Inches(0.11)))
    return x


def card(cx, y, h, title, body=BODY):
    x = panel(cx, y, h, title)
    text(x + Inches(0.8), y + Inches(2.26), COLW - Inches(1.6), h - Inches(3.0), body, 26, GREY, space=1.45)


def figure(cx, y, h, cap):
    x = M + cx * (COLW + GAP)
    solid(rect(x, y, COLW, h), WHITE, LINE)
    grad(rect(x, y, COLW, Inches(0.14)))
    solid(rect(x + Inches(0.8), y + Inches(0.85), COLW - Inches(1.6), h - Inches(2.85)), LIGHT, LINE)
    text(x + Inches(0.8), y + h / 2 - Inches(0.5), COLW - Inches(1.6), Inches(0.9),
         "Place figure here", 30, RGBColor(0x9A, 0xAE, 0xC2), align=PP_ALIGN.CENTER)
    text(x + Inches(0.8), y + h - Inches(1.6), COLW - Inches(1.6), Inches(1.1), cap, 24, GREY, space=1.35)


card(0, TOP, Inches(11.5), "1. Introduction")
card(0, TOP + Inches(12.3), Inches(11.5), "2. Materials and methods")
card(0, TOP + Inches(24.6), COLH - Inches(24.6), "3. Experimental setup")
figure(1, TOP, Inches(17.0), "Figure 1. Caption describing what the reader should take from this panel.")
figure(1, TOP + Inches(17.8), COLH - Inches(17.8), "Figure 2. Caption.")
card(2, TOP, Inches(17.0), "4. Results")
x = panel(2, TOP + Inches(17.8), COLH - Inches(17.8), "5. Conclusions")
for i, b in enumerate(["First conclusion in one line.", "Second conclusion.", "Third conclusion."]):
    yy = TOP + Inches(20.1 + i * 1.6)
    solid(s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.8), yy + Inches(0.18), Inches(0.3), Inches(0.3)), TEAL)
    text(x + Inches(1.45), yy, COLW - Inches(2.3), Inches(1.3), b, 27, NAVY, space=1.3)
text(x + Inches(0.8), TOP + Inches(25.9), COLW - Inches(1.6), Inches(2.4),
     "Acknowledgements. Funding source and grant number.", 23, GREY, space=1.4)

# ---- footer ----------------------------------------------------------------
grad(rect(0, H - BOTBAR, W, Inches(0.12)))
text(M, H - BOTBAR + Inches(0.72), Inches(22), Inches(1.2),
     "Membrane-based Sustainable Separation Solutions Laboratory  •  KRICT", 30, NAVY, True)
text(M, H - BOTBAR + Inches(1.56), Inches(22), Inches(0.9),
     "jh.kim@krict.re.kr    •    +82-42-860-7506", 24, GREY)
text(Inches(21.5), H - BOTBAR + Inches(1.05), Inches(12.9), Inches(1.0),
     "https://ms3l.org", 26, BLUE, align=PP_ALIGN.RIGHT)

prs.save("assets/templates/MS3L_poster_template.pptx")
print("light poster built")
