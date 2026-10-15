"""Render one banner per skill, in English and Spanish, into .github/assets/.

    python3 .github/banner/skills.py      # needs Playwright (pip install playwright && playwright install chromium)

Same look as the main banner (banner.html): Build to Lead palette on cream, navy footer.
"""
import base64
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ASSETS = HERE.parent / "assets"
LOGO = base64.b64encode((ROOT / "tech-to-business-faq-one-pager/assets/build-to-lead-logo.png").read_bytes()).decode()

CSS = """
:root { --navy:#171A30; --teal:#204B4C; --terra:#A97F6A; --gray:#4E4F52; --cream:#F6F1EC; --sand:#EADFD5;
        --green:#3F8A5C; --orange:#D3893B; --red:#B4503E; }
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1280px; height:440px; background:transparent; font-family:Inter, sans-serif; color:var(--navy); }
.card { position:relative; width:1280px; height:440px; background:var(--cream); border-radius:28px; overflow:hidden; }
.label { position:absolute; top:36px; font-weight:700; font-size:14px; letter-spacing:.22em; color:var(--terra); }
.footer { position:absolute; left:0; right:0; bottom:0; height:64px; background:var(--navy); display:flex;
          align-items:center; padding:0 40px; color:var(--cream); font-size:19px; }
.footer strong { font-weight:800; margin-right:16px; }
.footer span { opacity:.78; }
.footer .by { margin-left:auto; opacity:.6; font-size:15px; letter-spacing:.04em; }
.arrow { position:absolute; left:0; top:0; }
.mono { font-family:"DejaVu Sans Mono", monospace; }
.serif { font-family:Lora, serif; }
"""

ARROW = """<svg class="arrow" width="1280" height="440"><defs><marker id="ah" viewBox="0 0 10 10" refX="5" refY="5"
markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#A97F6A"/></marker></defs>
<path d="M{x1},{y} C{c1},{yc} {c2},{yc} {x2},{y}" stroke="#A97F6A" stroke-width="4" fill="none" stroke-linecap="round" marker-end="url(#ah)"/></svg>"""


def arrow(x1, x2, y):
    return ARROW.format(x1=x1, x2=x2, y=y, c1=x1 + 40, c2=x2 - 40, yc=y - 46)


def page(body, footer_title, footer_text, by):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">
{body}
<div class="footer"><strong>{footer_title}</strong><span>{footer_text}</span><span class="by">{by}</span></div>
</div></body></html>"""


# ---------------------------------------------------------------- Skill 1: short report
def report(t):
    rows = ""
    for i, (color, label, title, line) in enumerate(t["rows"]):
        rows += f"""<div style="position:absolute; left:640px; top:{86 + i * 92}px; width:600px; height:78px; background:#fff;
          border-radius:12px; box-shadow:0 2px 0 rgba(23,26,48,.07); border-left:8px solid var(--{color}); padding:12px 18px;">
          <div style="font-size:19px"><b style="color:var(--{color}); letter-spacing:.02em">{label}</b>
          <b style="margin-left:8px">{title}</b></div>
          <div style="font-size:15px; color:var(--gray); margin-top:6px">{line}</div></div>"""
    notes = "".join(f'<div style="margin-bottom:9px">{n}</div>' for n in t["notes"])
    body = f"""
<div class="label" style="left:56px">{t['left']}</div>
<div class="label" style="left:640px">{t['right']}</div>
<div class="mono" style="position:absolute; left:52px; top:82px; width:420px; height:236px; background:#fff;
     border-radius:12px; padding:20px 22px; font-size:16px; color:var(--teal); transform:rotate(-1.5deg);
     box-shadow:0 2px 0 rgba(23,26,48,.07); background-image:repeating-linear-gradient(#fff 0 33px, #EADFD5 33px 34px);
     line-height:24px">{notes}</div>
{arrow(492, 616, 220)}
{rows}"""
    return page(body, t["ft"], t["fx"], t["by"])


REPORT = {
    "en": dict(left="YOUR NOTES", right="WHAT LEADERSHIP READS",
               notes=["- db 32→24 vCPU oct 11, ~1.2k/mo", "- 2h maint window, all good",
                      "- checkout down 25m oct 7", "  ~1,100 failed pmts, rolled back",
                      "- BF nov 27, only tested 2x", "  (last yr peak 3x) 😬"],
               rows=[("orange", "🟠 RISK – HIGH", "Black Friday readiness", "Checkout may fail on our biggest day · ASK: what you need, by when"),
                     ("red", "🔴 LOWLIGHT", "Service interruption", "Customers couldn't pay for 25 min · ~1,100 failed payments"),
                     ("green", "🟢 HIGHLIGHT", "Infrastructure optimization", "USD 1,200/month saved (≈ USD 14,400/year) · Owner: SRE team")],
               ft="Skill 1 · Short report", fx="One topic → one 3–4 line update · traffic light · number · owner", by="BUILD TO LEAD"),
    "es": dict(left="TUS NOTAS", right="LO QUE LEE EL LIDERAZGO",
               notes=["- bd 32→24 vCPU 11 oct, ~1,2k/mes", "- ventana 2h, todo ok",
                      "- checkout caído 25m 7 oct", "  ~1.100 pagos fallidos, rollback",
                      "- BF 27 nov, solo probado 2x", "  (peak año pasado 3x) 😬"],
               rows=[("orange", "🟠 RISK – HIGH", "Preparación para Black Friday", "El checkout puede caer el día de más ventas · ASK: qué y para cuándo"),
                     ("red", "🔴 LOWLIGHT", "Interrupción del servicio", "Clientes sin poder pagar 25 min · ~1.100 pagos fallidos"),
                     ("green", "🟢 HIGHLIGHT", "Optimización de infraestructura", "USD 1.200/mes de ahorro (≈ USD 14.400/año) · Responsable: SRE")],
               ft="Skill 1 · Reporte corto", fx="Un tema → una actualización de 3–4 líneas · semáforo · número · responsable", by="BUILD TO LEAD"),
}


# ---------------------------------------------------------------- Skill 2: SMART objectives
def smart(t):
    steps = ""
    for i, (icon, name, date) in enumerate(t["steps"]):
        x = 664 + i * 186
        steps += f"""<div style="position:absolute; left:{x}px; top:200px; width:168px; height:58px; background:var(--cream);
            border-radius:10px; padding:8px 12px"><div style="font-size:15px; font-weight:700">{icon} {name}</div>
            <div style="font-size:14px; color:var(--gray); margin-top:3px">{date}</div></div>"""
        if i < 2:
            steps += f'<div style="position:absolute; left:{x + 170}px; top:216px; color:var(--terra); font-size:18px">→</div>'
    badges = "".join(
        f"""<div style="position:absolute; left:{664 + i * 46}px; top:282px; width:38px; height:38px; border-radius:50%;
        background:var(--teal); color:var(--cream); font-weight:800; font-size:17px; display:flex; align-items:center;
        justify-content:center">{c}</div>""" for i, c in enumerate("SMART"))
    body = f"""
<div class="label" style="left:56px">{t['left']}</div>
<div class="label" style="left:648px">{t['right']}</div>
<div class="serif" style="position:absolute; left:56px; top:120px; font-size:52px; font-style:italic; font-weight:700;
     color:var(--gray); white-space:nowrap">{t['vague']}</div>
<div style="position:absolute; left:48px; top:156px; width:{t['strike']}px; height:6px; background:var(--terra);
     border-radius:3px; transform:rotate(-3deg)"></div>
<div style="position:absolute; left:58px; top:212px; width:400px; font-size:18px; line-height:32px; color:var(--gray)">{t['missing']}</div>
{arrow(500, 624, 262)}
<div style="position:absolute; left:648px; top:74px; width:596px; height:258px; background:#fff; border-radius:14px;
     box-shadow:0 2px 0 rgba(23,26,48,.07); padding:18px 20px">
  <div style="font-size:21px; font-weight:800">{t['title']}</div>
  <div style="font-size:16px; color:var(--gray); margin-top:8px; line-height:23px">{t['goal']}</div>
</div>
{steps}{badges}
<div style="position:absolute; left:906px; top:290px; font-size:15px; color:var(--gray)">{t['owner']}</div>"""
    return page(body, t["ft"], t["fx"], t["by"])


SMART = {
    "en": dict(left="WHAT MOST OBJECTIVES LOOK LIKE", right="WHAT LEADERSHIP CAN APPROVE",
               vague="Improve monitoring.", strike=500,
               missing="✕ no number<br>✕ no date<br>✕ no owner<br>✕ no business reason",
               title="🎯 Early problem detection · Q3",
               goal="<b style='color:var(--navy)'>Plan and implement</b> on-call paging for our 40 services, cutting customer-reported incidents from <b style='color:var(--navy)'>60% to under 20%</b> by Sep 25.",
               steps=[("🗺️", "Planning", "Jul 17"), ("🛠️", "Execution", "Aug 28"), ("✅", "Validation", "Sep 25")],
               owner="Owner: SRE team",
               ft="Skill 2 · SMART objectives", fx="One initiative → one quarterly objective · plan first · numbers · dates · owner", by="BUILD TO LEAD"),
    "es": dict(left="CÓMO SE VEN LA MAYORÍA", right="LO QUE EL LIDERAZGO PUEDE APROBAR",
               vague="Mejorar el monitoreo.", strike=540,
               missing="✕ sin número<br>✕ sin fecha<br>✕ sin responsable<br>✕ sin motivo de negocio",
               title="🎯 Detección temprana de problemas · Q3",
               goal="<b style='color:var(--navy)'>Planear e implementar</b> alertas de guardia para nuestros 40 servicios, bajando los incidentes reportados por clientes del <b style='color:var(--navy)'>60% a menos del 20%</b> antes del 25 de sept.",
               steps=[("🗺️", "Planificación", "17 jul"), ("🛠️", "Ejecución", "28 ago"), ("✅", "Validación", "25 sept")],
               owner="Responsable: Equipo SRE",
               ft="Skill 2 · Objetivos SMART", fx="Una iniciativa → un objetivo trimestral · primero el plan · números · fechas · responsable", by="BUILD TO LEAD"),
}


# ---------------------------------------------------------------- Skill 3: FAQ one-pager
def faq(t):
    bubbles = ""
    for (x, y, r, txt, dim) in t["bubbles"]:
        bubbles += f"""<div style="position:absolute; left:{x}px; top:{y}px; transform:rotate({r}deg); background:#fff;
          border:1.5px solid rgba(32,75,76,.3); border-radius:18px 18px 18px 4px; padding:9px 15px; font-size:17px;
          color:var(--teal); white-space:nowrap; opacity:{.45 if dim else 1}">{txt}</div>"""
    glance = "".join(f"""<div style="flex:1; background:var(--cream); border-radius:6px; padding:5px 7px">
        <div style="font-size:8px; font-weight:800; color:var(--terra); letter-spacing:.06em">{k}</div>
        <div style="font-size:10px; font-weight:600">{v}</div></div>""" for k, v in t["glance"])
    qa = "".join(f"""<div style="margin-top:8px"><div style="font-size:11px; font-weight:800; color:var(--teal)">{q}</div>
        <div style="height:5px; width:{w}%; background:var(--sand); border-radius:3px; margin-top:4px"></div>
        <div style="height:5px; width:{w - 18}%; background:var(--sand); border-radius:3px; margin-top:3px"></div></div>"""
                 for q, w in t["qa"])
    body = f"""
<div class="label" style="left:56px">{t['left']}</div>
<div class="label" style="left:700px">{t['right']}</div>
{bubbles}
{arrow(540, 676, 220)}
<div style="position:absolute; left:740px; top:70px; width:250px; height:300px; background:#fff; border-radius:6px;
     box-shadow:0 10px 30px rgba(23,26,48,.14); transform:rotate(-2deg); padding:16px 16px; overflow:hidden">
  <img src="data:image/png;base64,{LOGO}" style="position:absolute; right:12px; top:10px; width:34px">
  <div style="font-size:15px; font-weight:800; width:170px; line-height:18px">{t['doc']}</div>
  <div style="display:flex; gap:5px; margin-top:10px">{glance}</div>
  {qa}
  <div style="position:absolute; left:0; right:0; bottom:0; height:22px; background:var(--navy); color:var(--cream);
       font-size:8px; display:flex; align-items:center; justify-content:center">{t['made']}</div>
</div>
<div style="position:absolute; left:1024px; top:110px; font-size:17px; line-height:40px; color:var(--gray)">{t['feats']}</div>
<div style="position:absolute; left:1028px; top:290px; background:var(--terra); color:#fff; font-weight:800; font-size:16px;
     padding:7px 14px; border-radius:8px">.docx · {t['page']}</div>"""
    return page(body, t["ft"], t["fx"], t["by"])


FAQ = {
    "en": dict(left="WHAT PEOPLE KEEP ASKING YOU", right="ONE PAGE THAT ANSWERS IT",
               bubbles=[(56, 86, -2, "Since when does it work?", 0), (300, 96, 3, "Can I use it?", 0),
                        (70, 146, 1, "What can't I do with it?", 0), (330, 160, -3, "Where is it?", 1),
                        (48, 208, -1, "Who do I call if it breaks?", 0), (150, 264, 2, "Is there a limit?", 0),
                        (360, 268, -2, "Since when…?", 1), (60, 316, -3, "Can I use it…?", 1), (260, 320, 1, "Who do I call…?", 1)],
               doc="Self-service data portal · FAQ",
               glance=[("FROM", "Nov 3"), ("FOR", "Business"), ("WHERE", "data.co"), ("HELP", "#data")],
               qa=[("What is it?", 92), ("Who can use it?", 86), ("What can't I do?", 90), ("Who do I call?", 80)],
               made="Made with ♥ by @build2lead.club and @maisfloro.tech",
               feats="❓ The 6 questions<br>🎮 Rules of the game<br>🆘 Who helps, and how<br>🖍️ Gaps highlighted",
               page="1 page",
               ft="Skill 3 · FAQ one-pager", fx="Something new you built → one friendly page of FAQs, as Word", by="BUILD TO LEAD"),
    "es": dict(left="LO QUE TODOS TE PREGUNTAN", right="UNA PÁGINA QUE LO RESPONDE",
               bubbles=[(56, 86, -2, "¿Desde cuándo funciona?", 0), (316, 96, 3, "¿Lo puedo usar?", 0),
                        (70, 146, 1, "¿Qué no puedo hacer?", 0), (310, 160, -3, "¿Dónde está?", 1),
                        (48, 208, -1, "¿A quién llamo si falla?", 0), (150, 264, 2, "¿Hay algún límite?", 0),
                        (370, 268, -2, "¿Desde cuándo…?", 1), (60, 316, -3, "¿Lo puedo usar…?", 1), (270, 320, 1, "¿A quién llamo…?", 1)],
               doc="Portal de datos de autoservicio · FAQ",
               glance=[("DESDE", "3 nov"), ("PARA", "Negocio"), ("DÓNDE", "datos.co"), ("AYUDA", "#datos")],
               qa=[("¿Qué es?", 92), ("¿Quién lo puede usar?", 86), ("¿Qué no puedo hacer?", 90), ("¿A quién llamo?", 80)],
               made="Hecho con ♥ por @build2lead.club y @maisfloro.tech",
               feats="❓ Las 6 preguntas<br>🎮 Las reglas del juego<br>🆘 Quién ayuda y cómo<br>🖍️ Vacíos resaltados",
               page="1 página",
               ft="Skill 3 · FAQ de una página", fx="Algo nuevo que construiste → una página amigable de FAQ, en Word", by="BUILD TO LEAD"),
}

# ---------------------------------------------------------------- Skill 4: interviews
def interviews(t):
    trivia = ""
    for (x, y, r, txt) in t["trivia"]:
        trivia += f"""<div style="position:absolute; left:{x}px; top:{y}px; transform:rotate({r}deg); background:#fff;
          border:1.5px solid rgba(78,79,82,.25); border-radius:18px 18px 18px 4px; padding:9px 15px; font-size:17px;
          color:var(--gray); white-space:nowrap; opacity:.8"><span style="text-decoration:line-through;
          text-decoration-color:var(--terra); text-decoration-thickness:3px">{txt}</span></div>"""
    star = "".join(f"""<div style="display:inline-flex; align-items:center; margin-right:12px; font-weight:800; font-size:15px;
        color:var(--teal)"><span style="width:18px; height:18px; border:2px solid var(--teal); border-radius:4px;
        display:inline-flex; align-items:center; justify-content:center; margin-right:5px; font-size:13px">{'✓' if on else ''}</span>{l}</div>"""
                   for l, on in zip("STAR", (1, 1, 1, 0)))
    score = "".join(f"""<span style="display:inline-block; width:16px; height:16px; border:2px solid var(--terra); border-radius:50%;
        margin:0 3px -3px 8px; background:{'var(--terra)' if v == '3' else 'transparent'}"></span><b style="color:var(--terra)">{v}</b>"""
                    for v in "1234")
    body = f"""
<div class="label" style="left:56px">{t['left']}</div>
<div class="label" style="left:640px">{t['right']}</div>
{trivia}
{arrow(500, 618, 230)}
<div style="position:absolute; left:640px; top:84px; width:604px; height:264px; background:#fff; border-radius:14px;
     box-shadow:0 2px 0 rgba(23,26,48,.07); padding:18px 22px">
  <div style="display:flex; align-items:center; gap:10px">
    <div style="width:30px; height:30px; border-radius:50%; background:var(--terra); color:#fff; font-weight:800;
         display:flex; align-items:center; justify-content:center; font-size:15px">9</div>
    <div style="font-size:13px; font-weight:800; letter-spacing:.12em; color:var(--teal)">{t['block']}</div>
  </div>
  <div style="font-size:19px; font-weight:800; margin-top:12px; line-height:25px">{t['q']}</div>
  <div style="font-size:15px; color:var(--gray); margin-top:10px"><b style="color:var(--terra)">{t['dig']}</b> {t['deep']}</div>
  <div style="font-size:15px; color:var(--gray); margin-top:6px; font-style:italic"><b style="color:var(--teal); font-style:normal">{t['strong']}</b> {t['expect']}</div>
  <div style="margin-top:16px; font-size:15px; display:flex; align-items:center">{star}<span style="margin-left:14px; font-weight:800; color:var(--gray)">{t['score']}</span>{score}</div>
</div>
<div style="position:absolute; right:36px; top:32px; background:var(--terra); color:#fff; font-weight:800; font-size:14px;
     padding:5px 12px; border-radius:7px">{t['badge']}</div>"""
    return page(body, t["ft"], t["fx"], t["by"])


INTERVIEWS = {
    "en": dict(left="WHAT MOST INTERVIEWS ASK", right="WHAT YOU'LL FIND OUT",
               trivia=[(56, 92, -2, "What is Kubernetes?"), (250, 150, 3, "Explain the CAP theorem"),
                       (60, 210, 1, "Which tools do you know?"), (230, 270, -3, "Reverse a linked list"),
                       (70, 320, 2, "Years of experience?")],
               block="EXECUTION AND INCIDENTS",
               q="Tell me about the worst incident you handled. What did it cost the business, and what did you do in the first 15 minutes?",
               dig="Dig deeper:", deep="What did you tell leadership, and when?",
               strong="Strong answer:", expect="own actions, impact in numbers, communicates early",
               score="Score", badge="20 questions · STAR · fillable PDF",
               ft="Skill 4 · Interviews", fx="One role → 20 technical questions that reveal business thinking", by="BUILD TO LEAD"),
    "es": dict(left="LO QUE PREGUNTAN LA MAYORÍA", right="LO QUE VAS A DESCUBRIR",
               trivia=[(56, 92, -2, "¿Qué es Kubernetes?"), (250, 150, 3, "Explica el teorema CAP"),
                       (60, 210, 1, "¿Qué herramientas manejas?"), (230, 270, -3, "Invierte una lista enlazada"),
                       (70, 320, 2, "¿Años de experiencia?")],
               block="EJECUCIÓN E INCIDENTES",
               q="Cuéntame del peor incidente que manejaste. ¿Cuánto le costó al negocio y qué hiciste en los primeros 15 minutos?",
               dig="Profundiza:", deep="¿Qué le dijiste a la gerencia, y cuándo?",
               strong="Respuesta fuerte:", expect="acciones propias, impacto en números, comunica temprano",
               score="Puntaje", badge="20 preguntas · STAR · PDF editable",
               ft="Skill 4 · Entrevistas", fx="Un rol → 20 preguntas técnicas que revelan si piensa en negocio", by="BUILD TO LEAD"),
}

# ---------------------------------------------------------------- Skill 5: tech interviews
def tech_interviews(t):
    chips = ""
    for (x, y, r, txt, strong) in t["chips"]:
        chips += f"""<div class="mono" style="position:absolute; left:{x}px; top:{y}px; transform:rotate({r}deg); background:#fff;
          border:1.5px solid rgba(32,75,76,{.45 if strong else .2}); border-radius:8px; padding:7px 12px; font-size:16px;
          color:var(--teal); white-space:nowrap; opacity:{1 if strong else .55}">{txt}</div>"""
    box = lambda x, y, w, label, color: f"""<div style="position:absolute; left:{x}px; top:{y}px; width:{w}px; height:34px;
        border:2px solid var(--{color}); border-radius:7px; background:#fff; font-size:13px; font-weight:700;
        color:var(--{color}); display:flex; align-items:center; justify-content:center">{label}</div>"""
    checks = "".join(f"""<div style="display:inline-flex; align-items:center; margin-right:12px; font-weight:800; font-size:15px;
        color:var(--teal)"><span style="width:18px; height:18px; border:2px solid var(--teal); border-radius:4px;
        display:inline-flex; align-items:center; justify-content:center; margin-right:5px; font-size:13px">{'✓' if on else ''}</span>{l}</div>"""
                     for l, on in zip(t["letters"], (1, 1, 1, 0)))
    body = f"""
<div class="label" style="left:56px">{t['left']}</div>
<div class="label" style="left:640px">{t['right']}</div>
{chips}
{arrow(500, 618, 230)}
<div style="position:absolute; left:640px; top:84px; width:604px; height:264px; background:#fff; border-radius:14px;
     box-shadow:0 2px 0 rgba(23,26,48,.07)"></div>
<div style="position:absolute; left:662px; top:100px; display:flex; align-items:center; gap:10px">
  <div style="width:30px; height:30px; border-radius:50%; background:var(--terra); color:#fff; font-weight:800;
       display:flex; align-items:center; justify-content:center; font-size:15px">9</div>
  <div style="font-size:13px; font-weight:800; letter-spacing:.12em; color:var(--teal)">{t['block']}</div>
</div>
<div style="position:absolute; left:662px; top:142px; width:560px; font-size:18px; font-weight:800; line-height:24px">{t['q']}</div>
<svg width="1280" height="440" style="position:absolute; left:0; top:0">
  <g stroke="#A97F6A" stroke-width="2" fill="none">
    <line x1="752" y1="235" x2="782" y2="235"/><line x1="872" y1="235" x2="902" y2="235"/>
    <line x1="992" y1="235" x2="1022" y2="235"/><line x1="947" y1="252" x2="947" y2="268"/>
  </g>
</svg>
{box(662, 218, 90, t['b1'], 'gray')}{box(782, 218, 90, 'API', 'teal')}{box(902, 218, 90, t['b3'], 'teal')}
{box(1022, 218, 90, 'DB', 'teal')}{box(892, 268, 110, t['b5'], 'terra')}
<div style="position:absolute; left:662px; top:318px; font-size:15px; display:flex; align-items:center">{checks}
  <span style="margin-left:10px; color:var(--gray); font-size:14px">{t['legend']}</span></div>
<div style="position:absolute; right:36px; top:32px; background:var(--terra); color:#fff; font-weight:800; font-size:14px;
     padding:5px 12px; border-radius:7px">{t['badge']}</div>"""
    return page(body, t["ft"], t["fx"], t["by"])


TECH_INTERVIEWS = {
    "en": dict(left="WHAT THE ROLE MUST MASTER", right="WHAT YOU'LL TEST",
               chips=[(56, 92, -2, "API design", 1), (230, 86, 2, "Indexes", 0), (360, 100, -1, "Caching", 1),
                      (70, 146, 1, "Transactions", 0), (250, 150, -3, "Queues", 1), (380, 158, 2, "Auth", 0),
                      (50, 204, -1, "Kubernetes", 1), (220, 212, 2, "CI/CD", 0), (330, 214, -2, "Observability", 1),
                      (80, 266, 2, "Idempotency", 1), (280, 272, -1, "Scaling", 0), (140, 322, -2, "Security", 1),
                      (310, 322, 1, "Trade-offs", 0)],
               block="ARCHITECTURE AND DESIGN",
               q="Design the order flow for 2,000 orders a minute, so a retry never creates a duplicate charge.",
               b1="App", b3="Queue", b5="Payments", letters="CREH",
               legend="correct · reasoning · edge cases · hands-on",
               badge="80% technical · 20% business",
               ft="Skill 5 · Tech interviews", fx="One role → 20 questions from its roadmap · design exercise · fillable PDF", by="BUILD TO LEAD"),
    "es": dict(left="LO QUE EL ROL DEBE DOMINAR", right="LO QUE VAS A PROBAR",
               chips=[(56, 92, -2, "Diseño de APIs", 1), (250, 86, 2, "Índices", 0), (370, 100, -1, "Caché", 1),
                      (70, 146, 1, "Transacciones", 0), (270, 150, -3, "Colas", 1), (390, 158, 2, "Auth", 0),
                      (50, 204, -1, "Kubernetes", 1), (220, 212, 2, "CI/CD", 0), (330, 214, -2, "Observabilidad", 1),
                      (80, 266, 2, "Idempotencia", 1), (290, 272, -1, "Escalar", 0), (140, 322, -2, "Seguridad", 1),
                      (310, 322, 1, "Trade-offs", 0)],
               block="ARQUITECTURA Y DISEÑO",
               q="Diseña el flujo de pedidos para 2.000 por minuto, sin que un reintento cobre dos veces.",
               b1="App", b3="Cola", b5="Pagos", letters="CRBP",
               legend="correcto · razonamiento · bordes · práctica",
               badge="80% técnico · 20% negocio",
               ft="Skill 5 · Entrevistas técnicas", fx="Un rol → 20 preguntas de su roadmap · ejercicio de diseño · PDF editable", by="BUILD TO LEAD"),
}

JOBS = [("skill-1", report, REPORT), ("skill-2", smart, SMART), ("skill-3", faq, FAQ),
        ("skill-4", interviews, INTERVIEWS), ("skill-5", tech_interviews, TECH_INTERVIEWS)]

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page(viewport={"width": 1280, "height": 440}, device_scale_factor=2)
        for name, fn, texts in JOBS:
            for lang, t in texts.items():
                pg.set_content(fn(t))
                pg.wait_for_timeout(250)
                out = ASSETS / f"{name}-{lang}.png"
                pg.screenshot(path=str(out), omit_background=True)
                print(f"wrote {out.relative_to(ROOT)}")
        browser.close()
