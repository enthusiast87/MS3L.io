from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
FONT="Noto Sans KR"
NAVY=RGBColor(0x0B,0x2F,0x5B); BLUE=RGBColor(0x00,0x75,0xC2)
TEAL=RGBColor(0x00,0xAD,0xA9); WHITE=RGBColor(0xFF,0xFF,0xFF)
GREY=RGBColor(0x5B,0x6F,0x84); LIGHT=RGBColor(0xF4,0xF8,0xFD)
prs=Presentation(); prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
W,H=prs.slide_width,prs.slide_height; blank=prs.slide_layouts[6]
def grad(sh,a=45.0):
    sh.fill.gradient(); st=sh.fill.gradient_stops
    st[0].color.rgb,st[0].position=BLUE,0.0
    st[1].color.rgb,st[1].position=TEAL,1.0
    sh.fill.gradient_angle=a; sh.line.fill.background()
def rect(s,x,y,w,h): return s.shapes.add_shape(MSO_SHAPE.RECTANGLE,x,y,w,h)
def solid(sh,c): sh.fill.solid(); sh.fill.fore_color.rgb=c; sh.line.fill.background()
def text(s,x,y,w,h,t,size,color,bold=False,align=PP_ALIGN.LEFT):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True
    tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=0
    p=tf.paragraphs[0]; p.alignment=align; r=p.add_run(); r.text=t
    r.font.size,r.font.bold,r.font.name=Pt(size),bold,FONT; r.font.color.rgb=color
L="assets/images/logo"; CIRC=f"{L}/ms3l-avatar-circle.png"; LOCKW=f"{L}/ms3l-lockup-horizontal-white.png"
s=prs.slides.add_slide(blank); grad(rect(s,0,0,W,H),315.0)
s.shapes.add_picture(LOCKW,Inches(1.0),Inches(2.15),width=Inches(8.8))
text(s,Inches(1.05),Inches(4.35),Inches(10),Inches(0.6),"Presentation title goes here",30,WHITE,True)
text(s,Inches(1.05),Inches(5.05),Inches(10),Inches(0.5),"Jihoon Kim  |  Korea Research Institute of Chemical Technology",15,RGBColor(0xD8,0xEF,0xF6))
text(s,Inches(1.05),Inches(5.5),Inches(10),Inches(0.4),"Conference / Date",13,RGBColor(0xB2,0xE2,0xE0))
s=prs.slides.add_slide(blank); solid(rect(s,0,0,W,H),WHITE); grad(rect(s,0,0,Inches(0.42),H),270.0)
text(s,Inches(1.3),Inches(3.0),Inches(9),Inches(0.5),"01",18,TEAL,True)
text(s,Inches(1.3),Inches(3.45),Inches(10),Inches(1.0),"Section title",44,NAVY,True)
grad(rect(s,Inches(1.3),Inches(4.65),Inches(2.2),Inches(0.09)),0.0)
s.shapes.add_picture(CIRC,Inches(11.5),Inches(5.85),width=Inches(0.95))
for title,kind in (("Slide title","bul"),("Two-column layout","col"),("Figure","fig")):
    s=prs.slides.add_slide(blank); solid(rect(s,0,0,W,H),WHITE); grad(rect(s,0,0,W,Inches(0.11)),0.0)
    text(s,Inches(0.9),Inches(0.62),Inches(11),Inches(0.7),title,30,NAVY,True)
    grad(rect(s,Inches(0.9),Inches(1.32),Inches(1.5),Inches(0.06)),0.0)
    if kind=="bul":
        text(s,Inches(0.9),Inches(1.75),Inches(11.5),Inches(0.5),"Lead line for the slide, one sentence.",17,BLUE)
        for i,(hd,bd) in enumerate([("Point one","Supporting detail for the first point."),("Point two","Supporting detail for the second point."),("Point three","Supporting detail for the third point.")]):
            y=Inches(2.55+i*1.15)
            solid(s.shapes.add_shape(MSO_SHAPE.OVAL,Inches(0.9),y+Inches(0.07),Inches(0.16),Inches(0.16)),TEAL)
            text(s,Inches(1.3),y,Inches(10.5),Inches(0.4),hd,18,NAVY,True)
            text(s,Inches(1.3),y+Inches(0.42),Inches(10.5),Inches(0.5),bd,15,GREY)
    elif kind=="col":
        for i,side in enumerate(["Left column","Right column"]):
            x=Inches(0.9+i*6.1)
            solid(rect(s,x,Inches(1.95),Inches(5.65),Inches(4.4)),LIGHT)
            grad(rect(s,x,Inches(1.95),Inches(0.07),Inches(4.4)),270.0)
            text(s,x+Inches(0.42),Inches(2.3),Inches(4.9),Inches(0.5),side,20,NAVY,True)
            text(s,x+Inches(0.42),Inches(2.95),Inches(4.9),Inches(3.0),"Body text. Replace with figure, table or bullets.",15,GREY)
    else:
        ph=rect(s,Inches(0.9),Inches(1.95),Inches(11.5),Inches(4.35)); solid(ph,LIGHT)
        ph.line.color.rgb=RGBColor(0xD6,0xE2,0xEE); ph.line.width=Pt(1)
        text(s,Inches(0.9),Inches(3.95),Inches(11.5),Inches(0.5),"Place figure here",16,RGBColor(0x9A,0xAE,0xC2),align=PP_ALIGN.CENTER)
        text(s,Inches(0.9),Inches(6.45),Inches(11.5),Inches(0.4),"Figure 1. Caption.",13,GREY)
    if kind!="fig": s.shapes.add_picture(CIRC,Inches(12.42),Inches(6.62),width=Inches(0.48))
s=prs.slides.add_slide(blank); grad(rect(s,0,0,W,H),315.0)
s.shapes.add_picture(CIRC,Inches(6.06),Inches(1.75),width=Inches(1.6))
text(s,Inches(1.0),Inches(3.85),Inches(11.3),Inches(0.8),"Thank you",40,WHITE,True,PP_ALIGN.CENTER)
text(s,Inches(1.0),Inches(4.82),Inches(11.3),Inches(0.4),"jh.kim@krict.re.kr",16,RGBColor(0xD8,0xEF,0xF6),align=PP_ALIGN.CENTER)
text(s,Inches(1.0),Inches(5.25),Inches(11.3),Inches(0.4),"https://ms3l.org",15,RGBColor(0xB2,0xE2,0xE0),align=PP_ALIGN.CENTER)
prs.save("assets/templates/MS3L_presentation_template.pptx")
print("deck rebuilt")
