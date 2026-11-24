# Shared content for the Sony Europe case study: used by app.py (Streamlit) and build_preview.py (static preview)
RED, YEL, BLUE, GREEN, DARK, PALE = "#000000", "#5B9BFF", "#1F4FA8", "#6E6E6E", "#000000", "#F3F4F6"
TABCOL = [RED, YEL, BLUE, GREEN]

CSS = f"""
.cs {{ font-family: 'Helvetica Neue', Arial, sans-serif; color:#1F1F24; max-width:1150px; margin:0 auto; }}
.cs p, .cs li {{ line-height:1.6; color:#1F1F24; }}
.cs .banner {{ background:{RED}; border-radius:14px 14px 0 0; padding:1.8rem 2.2rem 1.5rem; position:relative; overflow:hidden; }}
.cs .stripe {{ height:8px; background:{YEL}; border-radius:0 0 14px 14px; margin-bottom:1.2rem; }}
.cs .tag {{ display:inline-block; background:{YEL}; color:#FFFFFF !important; font-weight:800; font-size:1.05rem; letter-spacing:0.06em; text-transform:uppercase; padding:0.45rem 1.1rem; border-radius:999px; }}
.cs .co {{ color:{YEL} !important; }}
.cs .btitle {{ color:#FFFFFF !important; font-size:2.1rem; font-weight:800; margin:0.7rem 0 0.4rem; line-height:1.2; max-width:640px; }}
.cs .bsub {{ color:#D9D9D9 !important; font-size:1.05rem; max-width:640px; }}
.cs .by {{ color:#FFFFFF !important; margin-top:1rem; font-size:0.95rem; }}
.cs .by a {{ color:{YEL} !important; text-decoration:none; font-weight:700; }}
.cs .bricks {{ position:absolute; right:26px; top:22px; width:300px; height:150px; }}
.cs .brick {{ position:absolute; border-radius:5px; }}
.cs .stud {{ position:absolute; top:-9px; width:17px; height:9px; border-radius:4px 4px 0 0; }}
.cs .kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:0.9rem; margin:0 0 1.2rem; }}
.cs .kpi {{ background:{PALE}; border-top:6px solid {RED}; border-radius:8px; padding:0.9rem 1rem; }}
.cs .kpi .v {{ font-size:1.7rem; font-weight:800; color:#111111 !important; }}
.cs .kpi .l {{ font-size:0.85rem; color:#555555 !important; }}
.cs .nav {{ display:flex; flex-wrap:wrap; gap:0.45rem; margin:0 0 1.4rem; }}
.cs .nav a {{ text-decoration:none; font-weight:700; font-size:0.86rem; padding:0.5rem 0.85rem; border-radius:8px; }}
.cs .block {{ border:1px solid #E2E4E8; border-radius:12px; overflow:hidden; margin:0 0 1.6rem; background:#FFFFFF; scroll-margin-top:70px; }}
.cs .bh, .cs .bh *, .cs .bh small, .cs .nav a, .cs .nav a * {{ color:#FFFFFF !important; opacity:1 !important; }}
.cs .nav a, .cs div.nav a:link, .cs div.nav a:visited {{ color:#FFFFFF !important; }}
.cs .bh {{ padding:0.7rem 1.1rem; font-weight:800; font-size:1.05rem; }}
.cs .bh small {{ display:block; font-weight:700; font-size:0.72rem; letter-spacing:0.12em; color:#FFFFFF !important; opacity:1; }}
.cs .bb {{ padding:1rem 1.2rem 1.1rem; }}
.cs .cards {{ display:grid; grid-template-columns:repeat(3,1fr); gap:0.8rem; margin:0.4rem 0 0.9rem; }}
.cs .cards.two {{ grid-template-columns:repeat(2,1fr); }}
.cs .cards.four {{ grid-template-columns:repeat(4,1fr); }}
.cs .card {{ background:#FFFFFF; border:1px solid #ECECEC; border-top:5px solid {BLUE}; border-radius:8px; padding:0.8rem 0.9rem; }}
.cs .card h4 {{ margin:0 0 0.35rem; font-size:0.98rem; color:#14213D !important; }}
.cs .card div, .cs .card li {{ font-size:0.9rem; color:#3A4250 !important; }}
.cs .card ul {{ margin:0; padding-left:1.1rem; }}
.cs table.t {{ width:100%; border-collapse:collapse; margin:0.3rem 0 0.9rem; font-size:0.92rem; }}
.cs table.t th {{ background:{DARK}; color:#FFFFFF !important; text-align:left; padding:0.55rem 0.7rem; }}
.cs table.t td {{ border-bottom:1px solid #EEE; padding:0.55rem 0.7rem; vertical-align:top; color:#1F1F24 !important; }}
.cs table.t tr:nth-child(even) td {{ background:{PALE}; }}
.cs .note {{ background:{PALE}; border-left:5px solid {YEL}; padding:0.75rem 1rem; border-radius:6px; margin:0.5rem 0 0; color:#1F1F24 !important; }}
.cs .code {{ background:#F6F6F6; border:1px solid #E5E5E5; border-radius:6px; padding:0.6rem 0.8rem; font-family:Menlo,Consolas,monospace; font-size:0.82rem; color:#1A1A1A !important; margin:0.3rem 0 0.7rem; white-space:pre-wrap; }}
.cs .footer {{ background:{DARK}; color:#D9D9D9 !important; text-align:center; font-size:0.85rem; padding:0.8rem; border-radius:10px; margin-top:0.6rem; }}
@media (max-width:1050px) {{ .cs .bricks {{ display:none; }} }}
@media (max-width:800px) {{ .cs .kpis, .cs .cards, .cs .cards.four {{ grid-template-columns:repeat(2,1fr); }} .cs .btitle {{ font-size:1.6rem; }} }}
"""

def dot(x, y, d, col, ring=False):
    st = f"border:5px solid {col};background:transparent;" if ring else f"background:{col};"
    return f'<div class="brick" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;border-radius:50%;{st}"></div>'

def bar(x, y, w, h, col):
    return f'<div class="brick" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{h//2}px;background:{col};"></div>'

BRICKS = '<div class="bricks">' + "".join([
    bar(10, 70, 120, 14, BLUE), bar(60, 100, 150, 14, "#FFFFFF"), bar(150, 40, 120, 14, GREEN),
    dot(0, 20, 44, YEL), dot(120, 84, 46, "#FFFFFF", True), dot(222, 92, 56, YEL, True),
    dot(250, 0, 34, "#FFFFFF"), dot(96, 16, 26, GREEN),
]) + '</div>'

def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>" for row in rows)
    return f'<table class="t"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'

def cards(items, cls=""):
    out = []
    for i, (t, b) in enumerate(items):
        col = TABCOL[(i + 2) % 4]
        out.append(f'<div class="card" style="border-top-color:{col};"><h4>{t}</h4><div>{b}</div></div>')
    return f'<div class="cards {cls}">' + "".join(out) + "</div>"

def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def note(t):
    return f'<div class="note">{t}</div>'

def p(t):
    return f"<p>{t}</p>"


BANNER = (
    '<div class="banner">' + BRICKS +
    '<span class="tag">Prepared for Sony Europe · Talent Acquisition</span>'
    '<div class="btitle"><span class="co">Sony Europe</span>: full-cycle recruitment across Europe, with candidates and managers first</div>'
    '<div class="bsub">A Recruitment Specialist plan for Sales, Marketing, Finance, Operations and business support: quality at speed, data-driven and inclusive</div>'
    '<div class="by"><b>Adam Baig</b> · Recruitment Specialist · Weybridge · '
    '<a href="https://www.linkedin.com/in/adambaiguk">LinkedIn</a> · '
    '<a href="https://peachbox-demo.streamlit.app">PeachBox. demo</a></div>'
    '</div><div class="stripe"></div>'
)

KPIS = '<div class="kpis">' + "".join(
    f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in [
        ("28", "European countries with Sony Europe offices"), ("48h", "First shortlist to the hiring manager"),
        ("100%", "Candidates updated at every stage"), ("90%+", "Target offer-accept rate")]
) + "</div>"

S = []

S.append(("Partnering with the Talent Acquisition Manager", p(
    "<b>The scenario.</b> Sony Europe's HR function is growing, and the Recruitment Specialist works alongside the Talent Acquisition Manager to deliver full-cycle recruitment across Sales, Marketing, Finance, Operations and business support. "
    "This plan shows how I would deliver quality at speed while putting candidate and manager experience first. It is a hypothetical plan built on public information; no real candidates are named.")
 + table(["Sample search", "Market", "Why it is hard"], [
    ["Area Business Manager – Headphones", "Sales · UK retail", "Small pool with audio and retail account experience; competitors such as Bose, Sennheiser and Apple hold the best people"],
    ["Analog LSI Sales Manager", "Sales · Semiconductor, EU customers", "Rare technical sales profile; candidates spread across the UK, DACH and the Netherlands; regular EU travel"],
    ["Supply Chain Solutions Specialist", "Operations · Weybridge", "Fast-moving market; candidates often hold multiple offers"],
 ]) + note("These sample searches are based on the types of roles Sony Europe has recently advertised in Weybridge, such as an Area Business Manager for headphones, a Business Planning Manager, a Product Manager for Digital Imaging and an Analog LSI Sales Manager.") + cards([
    ("Weekly with the TA Manager", ul(["Priorities across all live vacancies", "Pipeline health and blockers", "Agency use and spend", "Ideas to improve the process"])),
    ("Owning my vacancies", ul(["Intake to offer on every role", "Clear updates to hiring managers", "Escalate risks early", "Hand over cleanly to People Services"])),
    ("Working across HR", ul(["HR Business Partners on org plans", "Reward on offers and benchmarking", "L&D on manager training", "People Services on contracts and onboarding"])),
 ])))

S.append(("Sony Europe at a glance: who I would hire for", table(["Business area", "Typical hires in my remit", "What attracts candidates to Sony"], [
    ["Consumer electronics (TV, audio, imaging)", "Key Account Managers, Channel Sales, Product and Trade Marketing", "Iconic products, brand pride, retail and e-commerce scope"],
    ["Professional solutions (broadcast, cinema, display)", "B2B Sales, Solutions Sales, Product Marketing", "Technical products, big-name customers, European scope"],
    ["Imaging &amp; sensing, semiconductor, R&amp;D, AI", "Business Development, Marketing, Programme and Operations roles", "Innovation, technology leadership, global projects"],
    ["Healthcare and biotech", "Commercial and Operations roles", "Purpose-led work and growth markets"],
    ["Business support across 28 countries", "Finance (e.g. FP&amp;A), Business Planning, Supply Chain, Customer Service, HR and Mobility", "Stability, hybrid working, career mobility across Europe"],
    ["Early careers", "European Graduate programme and placement-year interns", "Learning, rotation and a big-brand start"],
 ]) + note("Sony's strongest selling points: a purpose to fill the world with emotion through creativity and technology, hybrid working, the Weybridge campus, and the chance to move roles across 28 countries. I would build these into every approach.")))

S.append(("Intake: understanding the hire", cards([
    ("Agree the outcome", "What the hire must deliver in the first 6 and 12 months, and which skills are essential versus trainable"),
    ("Agree the process", "Interview stages, interviewers, assessment method and the decision owner, in writing before sourcing starts"),
    ("Calibrate early", "Share 3–5 profiles within 48 hours, agree yes, maybe or no, and adjust the search the same day"),
]) + note("A strong intake is the fastest way to quality at speed: fewer wasted interviews and fewer surprises at offer.")))

S.append(("Sourcing, screening & shortlisting", p("Data-driven sourcing across every channel, with a direct approach to passive candidates.")
 + table(["Channel", "How I would use it"], [
    ["LinkedIn Recruiter", "Targeted Boolean searches, InMail and saved talent pools by market and function"],
    ["Boolean and X-ray search", "Find passive candidates on LinkedIn, GitHub and company sites"],
    ["Talent pools and silver medallists", "Re-engage strong past finalists first"],
    ["Employee referrals", "Sony Europe's own network across 28 countries"],
    ["External recruitment partners", "Used selectively for hard-to-fill or niche roles, with clear briefs and SLAs"],
    ["PeachBox. (built by me)", "Turns a brief into a ranked, evidence-based shortlist with recruiter-approved outreach"],
 ]) + '<div class="code">("Area Business Manager" OR "Key Account Manager" OR "National Account Manager") AND (headphones OR audio OR "consumer electronics") AND (Currys OR Argos OR Amazon OR retail) AND (UK OR "United Kingdom")</div>'
   + '<div class="code">("Sales Manager" OR "Account Manager" OR "Business Development Manager" OR "Vertriebsleiter") AND (semiconductor OR "analog IC" OR LSI OR "mixed-signal") AND (UK OR Germany OR Deutschland OR Netherlands OR Nederland)</div>'
   + '<div class="note" style="border-left:5px solid #1F4FA8;"><b>Sample outreach (Area Business Manager – Headphones):</b><br>'
     'Hi Anna, your work growing the audio category with Currys and Argos stood out. Sony Europe is hiring an Area Business Manager for headphones, owning key UK retail partners for one of the best-known audio ranges in the world, with hybrid working from Weybridge. '
     'Open to a 15-minute call this week? Happy to share the full brief first.</div>'
   + table(["Scorecard criterion (Area Business Manager)", "Weight", "Evidence I look for"], [
    ["Retail account management in consumer electronics", "30%", "Named accounts, revenue owned, growth delivered"],
    ["Negotiation and commercial planning", "25%", "Annual deals, joint business plans, margin"],
    ["Audio or category knowledge", "20%", "Understands the headphone market and competitor ranges"],
    ["Stakeholder management", "15%", "Works across marketing, supply chain and finance"],
    ["Motivation and fit with Sony values", "10%", "Curiosity, integrity, drive"],
 ])
   + table(["Screening stage", "What I assess"], [
    ["Phone screen", "Motivation, must-have skills, notice period, salary expectations, right to work"],
    ["Structured shortlist", "Scorecard against agreed criteria, with a short summary for each candidate"],
 ])))

S.append(("Navigating European markets", table(["Market", "Language", "Typical notice", "What to plan for"], [
    ["UK", "English", "1–3 months", "Right-to-work checks; counter-offers common"],
    ["Germany (DACH)", "German", "Often 3 months, sometimes to quarter end", "Works councils; German-language outreach and interviews"],
    ["France", "French", "1–3 months", "CDI contracts and local employment law; French-language approach"],
    ["Netherlands", "Dutch / English", "1–2 months", "English widely used; expat tax rules matter for international hires"],
    ["Southern Europe", "Spanish / Italian", "15 days – 2 months", "Collective agreements shape pay and terms"],
 ]) + cards([
    ("Employment law", "Partner with HR and legal on contract type, probation and local terms before offer"),
    ("Visa and immigration", "Check right to work and sponsorship needs at screen, so there are no surprises at offer; plan relocation early"),
    ("Cultural nuance", "Adapt outreach, interview style and feedback to each market"),
]) + note("I have hired across the UK and Ireland, DACH, France, the Netherlands, Southern Europe and worldwide, managing right-to-work, relocation and local terms.")))

S.append(("Offers & closing", cards([
    ("No surprises", "Test salary, notice and motivation at every stage, so the offer matches what the candidate expects"),
    ("Benchmarked offers", "Partner with Reward using established benchmarking for a fair, competitive offer"),
    ("Counter-offer plan", "Talk about counter-offers early and keep in close contact during notice periods"),
]) + note("Result in my career: around a 90% offer-accept rate.")))

S.append(("Working with external partners", cards([
    ("When to use agencies", "Only for hard-to-fill, niche or urgent roles, after direct sourcing has been tested"),
    ("How I manage them", "Clear briefs, agreed fees, SLAs and a single point of contact; no duplicate submissions"),
    ("Why I am well placed", "15 years agency-side means I know how agencies work, what good looks like and how to get the best from them"),
])))

S.append(("Candidate & manager experience", table(["Touchpoint", "What I do"], [
    ["Application and outreach", "Personal, clear messages that reflect Sony's brand"],
    ["Every stage", "Updates within 48 hours, so no candidate is left waiting"],
    ["Interview preparation", "Clear guidance on format, interviewers and what to expect"],
    ["Feedback", "Timely, specific feedback for every interviewed candidate"],
    ["Hiring managers", "Weekly updates, consultative advice and shortlists they can trust"],
    ["Surveys", "Short surveys after each stage; act on the results"],
 ]) + cards([
    ("Inclusive hiring", "Inclusive job adverts, diverse shortlists and structured, scored interviews"),
    ("Unconscious bias", "Brief interviewers on bias and use consistent questions and scorecards"),
    ("Employer brand", "Every interaction protects and builds Sony's reputation as an employer"),
])))

S.append(("Recruitment technology & data", table(["Metric", "Why it matters", "Target"], [
    ["Time to hire", "Speed without losing quality", "Under 6 weeks"],
    ["Pipeline conversion by stage", "Shows where a process is breaking down", "Reviewed weekly"],
    ["Offer-accept rate", "Quality of offers and candidate experience", "90%+"],
    ["Source of hire", "Direct vs agency; cost and quality", "Direct-led"],
    ["Candidate and manager satisfaction", "Experience first", "Survey score 4.5/5"],
 ]) + '<div class="note" style="border-left:5px solid #5B9BFF;"><b>Built by me: PeachBox.</b>, an AI sourcing and headhunting platform. '
   'It turns a plain-English hiring brief into a ranked shortlist with a "why this match" panel, weighted scoring on skills, experience and location, '
   'recruiter-approved outreach, a six-stage pipeline with conversion analytics, and GDPR consent records with an audit log. '
   'I did not wait to be given better tools; I built one myself. It shows how I approach new recruitment technology: try it, test it, and keep a human in the loop. '
   '<a href="https://peachbox-demo.streamlit.app"><b>Watch the demo: peachbox-demo.streamlit.app</b></a></div>'
   + note("I would bring the same approach to evaluating and implementing tools at Sony: clear goals, a small test, data on the results, then roll out.")))

S.append(("Improving the process & training managers", cards([
    ("Streamlining", "Map each step from intake to start date, remove delays and agree timings with hiring managers"),
    ("Using feedback", "Act on candidate and manager feedback every month"),
    ("Scaling", "Templates for intake, scorecards and offers so the process grows with the business"),
]) + table(["Hiring manager training module", "Content"], [
    ["Writing a strong brief", "Outcomes, must-haves and what good looks like"],
    ["Structured interviewing", "Consistent questions, scorecards and independent scoring"],
    ["Inclusive hiring", "Unconscious bias and fair assessment"],
    ["Candidate experience", "Fast feedback and selling the role"],
])))

S.append(("Quality, compliance & reporting", cards([
    ("GDPR", "Lawful basis, consent records, retention periods and accurate data in the ATS"),
    ("Anti-discrimination", "Fair, consistent processes and inclusive adverts in every market"),
    ("Regular reporting", "Weekly pipeline report and a monthly summary of activity and key metrics for the TA Manager"),
])))

S.append(("Living Sony's values", table(["Sony value", "How it shows up in my recruiting"], [
    ["Dreams & Curiosity", "Try new ideas and tools, like building PeachBox., to find better ways to hire"],
    ["Diversity", "Diverse shortlists and inclusive hiring across 28 countries"],
    ["Integrity & Sincerity", "Honest, timely communication with every candidate and hiring manager"],
    ["Sustainability", "Build talent pools and processes that keep working as the business grows"],
 ]) + note("Sony's purpose is to fill the world with emotion, through the power of creativity and technology. Recruitment is where that starts: hiring the people who make it happen.")))

S.append(("Why Adam for Sony Europe", table(["What the role needs", "What I bring"], [
    ["Full-cycle recruitment, quality at speed", "15 years end to end, 120+ hires, typical time-to-fill of 1–2 weeks"],
    ["Sales, Marketing and Operations hiring", "Account Executives, Account Managers, Sales Directors, Product Marketing, Operations and commercial roles"],
    ["Diverse European markets", "UK and Ireland, DACH, France, the Netherlands, Southern Europe, plus worldwide hiring"],
    ["Visa, right-to-work and employment law", "Managed right-to-work, relocation and local terms across many countries"],
    ["External recruitment partners", "15 years agency-side: I know how to brief agencies, hold them to SLAs and when not to use them"],
    ["Offers and closing", "Around a 90% offer-accept rate, with counter-offers handled early"],
    ["Recruitment technology and data", "Built PeachBox., my own AI sourcing platform; Greenhouse, Ashby, Bullhorn, LinkedIn Recruiter"],
    ["Training and developing others", "Trained every new recruiter as two businesses grew, and coached hiring managers on assessment"],
    ["A growing HR team that wants people who stretch", "Curious and hands-on: I build my own tools and take on new challenges"],
 ]) + note("<b>Every one of my 120+ hires was someone I found myself. That's what I'd bring to Sony Europe from day one.</b>")))

S.append(("First 90 days", table(["Days", "Focus", "Output"], [
    ["1–30", "Learn the business, HR team, ATS and live vacancies; intake with every hiring manager", "Clear plan for each vacancy"],
    ["31–60", "Full sourcing and shortlisting; weekly reporting; review agency use", "First offers and accepted hires"],
    ["61–90", "Improve the process using data and feedback; first hiring manager training session", "Faster, smoother process"],
 ]) + cards([
    ("End-to-end experience", "15 years of full-cycle recruitment and 120+ hires"),
    ("Across Europe and worldwide", "UK, DACH, France, the Netherlands, Southern Europe"),
    ("Track record", "1–2 week typical time-to-fill, ~90% offer-accept, 75% fill rate"),
    ("Technology", "Built PeachBox.; LinkedIn Recruiter, Greenhouse, Bullhorn, Ashby"),
 ], "four")))

def nav():
    out = []
    for i, (t, _) in enumerate(S):
        col = TABCOL[i % 4]
        out.append(f'<a href="#s{i+1}" style="background:{col};color:#FFFFFF;">{i+1:02d} {t}</a>')
    return '<div class="nav">' + "".join(out) + "</div>"

def block(i):
    t, body = S[i]
    col = TABCOL[i % 4]
    return (f'<div class="block" id="s{i+1}"><div class="bh" style="background:{col};color:#FFFFFF;">'
            f'<small>SECTION {i+1:02d}</small>{t}</div><div class="bb">{body}</div></div>')

FOOTER = '<div class="footer">Prepared by Adam Baig · London, UK · A hypothetical plan built on public information.</div>'

def full_html():
    return BANNER + KPIS + nav() + "".join(block(i) for i in range(len(S))) + FOOTER
