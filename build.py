import os

NAME = "Muhammad Asad"
INITIALS = "MA"
ROLE = "FULL-STACK WEB DEVELOPER"
SUB = "React · Next.js · Node.js · Python · Databases"
USER = "Muhammadasad43"
EMAIL = "khanking2778@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/muhammad-asad-53462043b"
FACEBOOK = "https://www.facebook.com/mkbaloch1538"
WHATSAPP = "https://wa.me/923048648492"
ABOUT = ("I'm a full-stack web developer who builds fast, clean web apps "
         "from database to UI. I like turning ideas into products people actually use.")

# Edit these to match what you really use
CARD = [("FRONTEND", "React · Next.js"), ("BACKEND", "Node.js · Express"),
        ("DATABASE", "PostgreSQL · Prisma"), ("DEPLOY", "Render · Vercel")]
SKILLS = ["HTML", "CSS", "JavaScript", "TypeScript", "React", "Next.js",
          "Node.js", "Python", "Prisma", "Git"]

os.makedirs("assets", exist_ok=True)
BG, PANEL, GREEN, WHITE, GREY = "#0b1020", "#0f1a1a", "#2ee59d", "#ffffff", "#9aa4b2"

def save(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

# ---------- banner ----------
banner = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300">
<defs><pattern id="g" width="30" height="30" patternUnits="userSpaceOnUse">
<path d="M30 0H0V30" fill="none" stroke="#1c2b26" stroke-width="1"/></pattern></defs>
<rect width="1200" height="300" rx="16" fill="{BG}"/>
<rect width="1200" height="300" rx="16" fill="url(#g)"/>
<text x="50" y="80" font-family="monospace" font-size="16" letter-spacing="5" fill="{GREEN}">{ROLE}</text>
<text x="50" y="150" font-family="sans-serif" font-weight="700" font-size="58" fill="{WHITE}">{NAME}</text>
<text x="50" y="190" font-family="sans-serif" font-size="22" fill="{GREY}">{SUB}</text>
<path d="M0 255H330L350 215H470L490 255H640L660 215H780L800 255H950L970 215H1090L1110 255H1200"
 fill="none" stroke="{GREEN}" stroke-width="3" stroke-dasharray="1400" stroke-dashoffset="1400">
<animate attributeName="stroke-dashoffset" from="1400" to="0" dur="4s" repeatCount="indefinite"/></path>
<text x="1150" y="45" text-anchor="end" font-family="monospace" font-size="13" fill="{GREEN}" opacity=".7">&lt;/&gt; github.com/{USER}</text>
</svg>'''
save("assets/banner.svg", banner)

# ---------- stats card ----------
pos = [(330, 150), (700, 150), (330, 250), (700, 250)]
items = ""
for (label, val), (x, y) in zip(CARD, pos):
    items += (f'<text x="{x}" y="{y}" font-family="sans-serif" font-weight="700" font-size="34" fill="{GREEN}">{val}</text>'
              f'<text x="{x}" y="{y+26}" font-family="monospace" font-size="14" letter-spacing="2" fill="{GREY}">{label}</text>\n')
card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="340" viewBox="0 0 1200 340">
<rect width="1200" height="340" rx="16" fill="{BG}"/>
<rect x="30" y="30" width="1140" height="280" rx="12" fill="{PANEL}" stroke="#1c3b30"/>
<rect x="30" y="30" width="1140" height="42" rx="12" fill="#12332a"/>
<text x="55" y="57" font-family="monospace" font-size="15" letter-spacing="3" fill="{GREEN}">{NAME.upper()} · {ROLE}</text>
<circle cx="150" cy="170" r="52" fill="#0f2b24" stroke="{GREEN}" stroke-width="3"/>
<text x="150" y="184" text-anchor="middle" font-family="sans-serif" font-weight="700" font-size="40" fill="{WHITE}">{INITIALS}</text>
<text x="55" y="270" font-family="sans-serif" font-weight="700" font-size="20" fill="{WHITE}">{NAME}</text>
<text x="55" y="292" font-family="monospace" font-size="13" fill="{GREY}">Web Developer</text>
{items}</svg>'''
save("assets/card.svg", card)

# ---------- skills strip ----------
x, chips = 0, ""
for s in SKILLS:
    w = len(s) * 10 + 34
    chips += (f'<rect x="{x}" y="10" width="{w}" height="40" rx="20" fill="#12332a" stroke="{GREEN}"/>'
              f'<text x="{x + w/2}" y="36" text-anchor="middle" font-family="monospace" font-size="15" fill="{GREEN}">{s}</text>\n')
    x += w + 12
skills = f'<svg xmlns="http://www.w3.org/2000/svg" width="{x}" height="60" viewBox="0 0 {x} 60">\n{chips}</svg>'
save("assets/skills.svg", skills)

# ---------- README ----------
def badge(label, color, logo, url):
    return (f'<a href="{url}"><img src="https://img.shields.io/badge/{label}-{color}'
            f'?style=for-the-badge&logo={logo}&logoColor=white"></a>')

readme = f'''<p align="center"><img src="./assets/banner.svg" width="100%" alt="{NAME}"></p>

<p align="center">
{badge("LINKEDIN", "0A66C2", "linkedin", LINKEDIN)}
{badge("EMAIL", "D14836", "gmail", "mailto:" + EMAIL)}
{badge("FACEBOOK", "1877F2", "facebook", FACEBOOK)}
{badge("WHATSAPP", "25D366", "whatsapp", WHATSAPP)}
</p>

### About
{ABOUT}

<p align="center"><img src="./assets/card.svg" width="100%" alt="Stack"></p>

### Skills
<p align="center"><img src="./assets/skills.svg" alt="Skills"></p>
'''
save("README.md", readme)
print("Built: README.md + assets/banner.svg, card.svg, skills.svg")
