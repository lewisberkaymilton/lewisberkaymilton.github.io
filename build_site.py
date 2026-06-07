#!/usr/bin/env python3
"""Generate Grid & Glory F1 site pages (2026 season)."""
from pathlib import Path

ROOT = Path(__file__).parent

CIRCUITS = [
    ("circuit-monaco.html", "Monaco", "Circuit de Monaco"),
    ("circuit-silverstone.html", "Silverstone", "Silverstone Circuit"),
    ("circuit-spa.html", "Spa", "Spa-Francorchamps"),
    ("circuit-suzuka.html", "Suzuka", "Suzuka International Racing Course"),
    ("circuit-monza.html", "Monza", "Autodromo Nazionale Monza"),
    ("circuit-abu-dhabi.html", "Abu Dhabi", "Yas Marina Circuit"),
]

DRIVERS = [
    ("driver-verstappen.html", "Max Verstappen"),
    ("driver-hamilton.html", "Lewis Hamilton"),
    ("driver-leclerc.html", "Charles Leclerc"),
    ("driver-norris.html", "Lando Norris"),
    ("driver-russell.html", "George Russell"),
]

TEAMS_2026 = [
    ("McLaren", "Lando Norris", "Oscar Piastri", "Mercedes", "img-team-mclaren.jpg", "McLaren MCL39 Formula 1 car"),
    ("Mercedes", "George Russell", "Kimi Antonelli", "Mercedes", "img-team-mercedes.jpg", "Mercedes-AMG W16 Formula 1 car"),
    ("Red Bull Racing", "Max Verstappen", "Isack Hadjar", "Red Bull Ford", "img-team-redbull.jpg", "Oracle Red Bull Racing RB21"),
    ("Ferrari", "Charles Leclerc", "Lewis Hamilton", "Ferrari", "img-team-ferrari.jpg", "Scuderia Ferrari SF-25"),
    ("Williams", "Carlos Sainz", "Alex Albon", "Mercedes", "img-team-williams.jpg", "Williams FW47"),
    ("Racing Bulls", "Liam Lawson", "Arvid Lindblad", "Red Bull Ford", "img-team-racingbulls.jpg", "Visa Cash App Racing Bulls car"),
    ("Aston Martin", "Fernando Alonso", "Lance Stroll", "Honda", "img-team-astonmartin.jpg", "Aston Martin AMR26"),
    ("Haas", "Esteban Ocon", "Oliver Bearman", "Ferrari", "img-team-haas.jpg", "MoneyGram Haas VF-26"),
    ("Audi", "Nico Hülkenberg", "Gabriel Bortoleto", "Audi", "img-team-audi.jpg", "Audi Revolut Formula 1 car"),
    ("Alpine", "Pierre Gasly", "Franco Colapinto", "Mercedes", "img-team-alpine.jpg", "BWT Alpine A526"),
    ("Cadillac", "Sergio Pérez", "Valtteri Bottas", "Ferrari", "img-team-cadillac.jpg", "Cadillac Formula 1 Team car"),
]

CIRCUIT_DATA = {
    "circuit-monaco.html": {
        "name": "Circuit de Monaco",
        "country": "Monaco",
        "meta": "Street circuit · Lap length: 3.337 km · Race laps: 78",
        "img": "img-circuit-monaco.jpg",
        "alt": "Monaco Grand Prix through the streets of Monte Carlo",
        "stats": [("78", "Race laps"), ("260", "km distance"), ("Street", "Circuit type"), ("1929", "First held")],
        "about": "Monaco is the slowest and tightest track on the calendar. Overtaking is extremely difficult, so qualifying position is critical. Walls are close on every side — one mistake ends the session.",
        "corners": "Casino Square, the Tunnel exit, and the Swimming Pool section are the most famous parts of this harbour-side layout.",
        "prev": ("circuit-abu-dhabi.html", "Abu Dhabi"),
        "next": ("circuit-silverstone.html", "Silverstone"),
    },
    "circuit-silverstone.html": {
        "name": "Silverstone Circuit",
        "country": "United Kingdom",
        "meta": "Home of British GP · Lap length: 5.891 km · Race laps: 52",
        "img": "img-circuit-silverstone.jpg",
        "alt": "Silverstone Circuit during the British Grand Prix",
        "stats": [("52", "Race laps"), ("306", "km distance"), ("Permanent", "Circuit type"), ("1950", "First F1 GP")],
        "about": "Silverstone hosted the first world championship race in 1950. High-speed corners like Maggotts, Becketts, and Chapel make it a favourite for drivers and fans.",
        "corners": "Copse, Maggotts-Becketts, and Stowe are key overtaking and tyre-management zones on the modern layout.",
        "prev": ("circuit-monaco.html", "Monaco"),
        "next": ("circuit-spa.html", "Spa"),
    },
    "circuit-spa.html": {
        "name": "Circuit de Spa-Francorchamps",
        "country": "Belgium",
        "meta": "Ardennes forest · Lap length: 7.004 km · Race laps: 44",
        "img": "img-circuit-spa.jpg",
        "alt": "Spa-Francorchamps circuit in the Ardennes",
        "stats": [("44", "Race laps"), ("308", "km distance"), ("Permanent", "Circuit type"), ("1950", "First F1 GP")],
        "about": "Spa is one of the longest and fastest tracks in Formula 1. Weather can change lap by lap, and Eau Rouge-Raidillon remains the circuit's most famous sequence.",
        "corners": "La Source, Eau Rouge-Raidillon, Pouhon, and Blanchimont define this classic European venue.",
        "prev": ("circuit-silverstone.html", "Silverstone"),
        "next": ("circuit-suzuka.html", "Suzuka"),
    },
    "circuit-suzuka.html": {
        "name": "Suzuka International Racing Course",
        "country": "Japan",
        "meta": "Figure-eight layout · Lap length: 5.807 km · Race laps: 53",
        "img": "img-circuit-suzuka.jpg",
        "alt": "Suzuka circuit during the Japanese Grand Prix",
        "stats": [("53", "Race laps"), ("308", "km distance"), ("Permanent", "Circuit type"), ("1987", "First F1 GP")],
        "about": "Suzuka's figure-eight layout and fast Esses make it one of the most demanding driver circuits. Japanese fans create one of the loudest atmospheres on the calendar.",
        "corners": "The Esses, Spoon Curve, and 130R are legendary sections that reward precision and commitment.",
        "prev": ("circuit-spa.html", "Spa"),
        "next": ("circuit-monza.html", "Monza"),
    },
    "circuit-monza.html": {
        "name": "Autodromo Nazionale Monza",
        "country": "Italy",
        "meta": "Temple of Speed · Lap length: 5.793 km · Race laps: 53",
        "img": "img-circuit-monza.jpg",
        "alt": "Monza circuit with the Italian Grand Prix crowd",
        "stats": [("53", "Race laps"), ("307", "km distance"), ("Permanent", "Circuit type"), ("1950", "First F1 GP")],
        "about": "Monza is the spiritual home of Ferrari and one of the fastest tracks in the sport. Long straights and heavy braking zones produce classic slipstream battles.",
        "corners": "The Rettifilo chicanes, Lesmo corners, and Parabolica define Monza's unique low-downforce challenge.",
        "prev": ("circuit-suzuka.html", "Suzuka"),
        "next": ("circuit-abu-dhabi.html", "Abu Dhabi"),
    },
    "circuit-abu-dhabi.html": {
        "name": "Yas Marina Circuit",
        "country": "United Arab Emirates",
        "meta": "Season finale · Lap length: 5.281 km · Race laps: 58",
        "img": "img-circuit-abudhabi.jpg",
        "alt": "Yas Marina Circuit under floodlights at the Abu Dhabi Grand Prix",
        "stats": [("58", "Race laps"), ("306", "km distance"), ("Permanent", "Circuit type"), ("2009", "First F1 GP")],
        "about": "Yas Marina often hosts the final round of the championship. The layout was updated in 2021 to improve overtaking. The race starts in daylight and finishes under floodlights.",
        "corners": "Turns 5–7 through the hotel section and the long back straight into Turn 9 are key battle zones.",
        "prev": ("circuit-monza.html", "Monza"),
        "next": ("circuit-monaco.html", "Monaco"),
    },
}

DRIVER_DATA = {
    "driver-verstappen.html": {
        "name": "Max Verstappen",
        "meta": "Netherlands · Red Bull Racing · Car #3",
        "img": "img-verstappen.jpg",
        "alt": "Max Verstappen in Red Bull Racing overalls",
        "stats": [("4+", "World Titles"), ("65+", "Race Wins"), ("2015", "F1 Debut"), ("3", "Car Number")],
        "career": [
            "Verstappen became the youngest Formula 1 race winner in 2016 and later dominated the ground-effect era with Red Bull, winning multiple world championships.",
            "In 2026 he leads Red Bull's new Red Bull Ford power unit project with rookie team mate Isack Hadjar. Laurent Mekies is team principal.",
        ],
        "legacy": "Known for aggressive racecraft and consistent qualifying speed, Verstappen remains the benchmark driver of the 2020s generation.",
        "prev": ("driver-russell.html", "George Russell"),
        "next": ("driver-hamilton.html", "Lewis Hamilton"),
    },
    "driver-hamilton.html": {
        "name": "Lewis Hamilton",
        "meta": "United Kingdom · Ferrari · Car #44",
        "img": "img-hamilton.jpg",
        "alt": "Lewis Hamilton driving for Scuderia Ferrari",
        "stats": [("7", "World Titles"), ("105+", "Race Wins"), ("2007", "F1 Debut"), ("44", "Car Number")],
        "career": [
            "Hamilton debuted with McLaren in 2007 and won his first title in 2008. He moved to Mercedes in 2013 and dominated the hybrid era with seven world championships.",
            "He joined Ferrari in 2025 and continues with the team in 2026 alongside Charles Leclerc, chasing Ferrari's first drivers' title since 2007.",
        ],
        "legacy": "He holds records for race wins and pole positions, and remains one of the most influential figures in modern Formula 1.",
        "prev": ("driver-verstappen.html", "Max Verstappen"),
        "next": ("driver-leclerc.html", "Charles Leclerc"),
    },
    "driver-leclerc.html": {
        "name": "Charles Leclerc",
        "meta": "Monaco · Ferrari · Car #16",
        "img": "img-leclerc.jpg",
        "alt": "Charles Leclerc in Ferrari racing gear",
        "stats": [("7", "Race Wins"), ("24+", "Pole Positions"), ("2018", "F1 Debut"), ("16", "Car Number")],
        "career": [
            "Leclerc joined Ferrari in 2019 after winning races with Sauber. His qualifying speed quickly made him the team's lead driver.",
            "In 2026 he partners Lewis Hamilton at Ferrari under Fred Vasseur, with the SF-25 successor targeting both championships in the new power unit era.",
        ],
        "legacy": "A home-race winner at Monaco and a fan favourite, Leclerc combines raw one-lap pace with deep Ferrari commitment.",
        "prev": ("driver-hamilton.html", "Lewis Hamilton"),
        "next": ("driver-norris.html", "Lando Norris"),
    },
    "driver-norris.html": {
        "name": "Lando Norris",
        "meta": "United Kingdom · McLaren · Car #1",
        "img": "img-norris.jpg",
        "alt": "Lando Norris celebrating a McLaren Grand Prix victory",
        "stats": [("1", "World Title"), ("8+", "Race Wins"), ("2019", "F1 Debut"), ("1", "Car Number")],
        "career": [
            "Norris joined McLaren in 2019 and developed into a race-winning front-runner alongside Oscar Piastri.",
            "Entering 2026 as reigning world champion, Norris leads McLaren's title defence with the papaya team targeting a repeat in the new regulations.",
        ],
        "legacy": "Combining strong race pace with popular appeal, Norris has become the face of McLaren's modern revival.",
        "prev": ("driver-leclerc.html", "Charles Leclerc"),
        "next": ("driver-russell.html", "George Russell"),
    },
    "driver-russell.html": {
        "name": "George Russell",
        "meta": "United Kingdom · Mercedes · Car #63",
        "img": "img-russell.jpg",
        "alt": "George Russell in Mercedes-AMG Petronas Formula One team kit",
        "stats": [("4+", "Race Wins"), ("30+", "Pole Positions"), ("2019", "F1 Debut"), ("63", "Car Number")],
        "career": [
            "Russell made his breakthrough with Williams before joining Mercedes as a race winner and regular front-row qualifier.",
            "In 2026 he leads the Mercedes factory team with rookie Kimi Antonelli as team mate, targeting wins under the new 2026 aerodynamic and power unit rules.",
        ],
        "legacy": "Russell is known for strong wet-weather performances and precise qualifying laps, making him a key figure in Mercedes' next era.",
        "prev": ("driver-norris.html", "Lando Norris"),
        "next": ("driver-verstappen.html", "Max Verstappen"),
    },
}


def circuit_strip(active=None):
    links = []
    for href, label, _ in CIRCUITS:
        cls = ' class="active"' if href == active else ""
        links.append(f'            <a href="{href}"{cls}>{label}</a>')
    return f"""        <nav class="circuit-strip" aria-label="2026 featured circuits">
            <span class="circuit-strip-label">Featured Circuits →</span>
{chr(10).join(links)}
        </nav>"""


def main_nav(active_page=None, active_section=None):
    def nav_link(href, label):
        cls = ' class="active"' if href == active_page else ""
        return f'        <a href="{href}"{cls}>{label}</a>'

    driver_links = []
    for href, name in DRIVERS:
        driver_links.append(f'                <a href="{href}">{name}</a>')
    circuit_links = []
    for href, label, full in CIRCUITS:
        circuit_links.append(f'                <a href="{href}">{full if len(full) < 20 else label}</a>')

    drivers_active = ' active' if active_section == "drivers" else ""
    circuits_active = ' active' if active_section == "circuits" else ""

    return f"""    <nav class="main-nav">
{nav_link("f1-home.html", "Overview")}
{nav_link("history.html", "History")}
        <div class="nav-dropdown">
            <span class="nav-trigger{drivers_active}">Drivers</span>
            <div class="nav-dropdown-menu">
                <div class="nav-dropdown-label">2026 Drivers</div>
{chr(10).join(driver_links)}
                <a class="nav-dropdown-footer" href="drivers.html">View all drivers →</a>
            </div>
        </div>
        <div class="nav-dropdown">
            <span class="nav-trigger{circuits_active}">Circuits</span>
            <div class="nav-dropdown-menu">
                <div class="nav-dropdown-label">Featured Circuits</div>
{chr(10).join(circuit_links)}
                <a class="nav-dropdown-footer" href="circuits.html">View all circuits →</a>
            </div>
        </div>
{nav_link("teams.html", "Teams")}
{nav_link("contact.html", "Contact")}
    </nav>"""


def page_shell(title, body, active_page=None, active_section=None, circuit_active=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="site-header">
        <div class="brand">
            <h1>Grid & Glory</h1>
            <p>Final Project · Berkay Gündoğdu · 2026 F1 Season</p>
        </div>
{circuit_strip(circuit_active)}
    </header>
{main_nav(active_page, active_section)}
{body}
    <footer class="site-footer">Final Project · Near East University · 2026</footer>
    <script src="script.js"></script>
</body>
</html>
"""


def write(name, content):
    (ROOT / name).write_text(content, encoding="utf-8")
    print("wrote", name)


def build_home():
    cards = """
        <article class="panel hero-panel">
            <h1>2026 Formula 1 Season</h1>
            <p>The 2026 championship brings new power units, Cadillac on the grid, and 11 teams fighting across 24 rounds. This site covers six iconic circuits, five star drivers, and the full 2026 entry list.</p>
            <img src="images/img-hero-2026.jpg" alt="Modern Formula 1 cars on track">
        </article>
        <article class="panel">
            <h2>How To Use This Site</h2>
            <p>Use the <strong>Featured Circuits</strong> bar in the header to jump to Monaco, Monza, Spa, and other legendary tracks. Open the <strong>Drivers</strong> and <strong>Teams</strong> menus for profiles and car photos from the current season.</p>
        </article>
        <article class="panel">
            <h2>Also On This Site</h2>
            <div class="card-grid">
                <div class="profile-card">
                    <img src="images/img-hamilton.jpg" alt="Lewis Hamilton at Ferrari">
                    <div class="card-body">
                        <h3>Drivers</h3>
                        <p>Verstappen, Hamilton, Leclerc, Norris, Russell.</p>
                        <a href="drivers.html">Browse drivers →</a>
                    </div>
                </div>
                <div class="profile-card">
                    <img src="images/img-circuit-monza.jpg" alt="Autodromo Nazionale Monza">
                    <div class="card-body">
                        <h3>Circuits</h3>
                        <p>Six of the most famous venues in Formula 1.</p>
                        <a href="circuits.html">Browse circuits →</a>
                    </div>
                </div>
                <div class="profile-card">
                    <img src="images/img-team-ferrari.jpg" alt="Ferrari Formula 1 car">
                    <div class="card-body">
                        <h3>Teams</h3>
                        <p>All 11 teams and 22 drivers on the 2026 grid.</p>
                        <a href="teams.html">View the grid →</a>
                    </div>
                </div>
            </div>
        </article>"""
    write("f1-home.html", page_shell("Grid & Glory | 2026 Formula 1", f"    <main class=\"page-wrap\">\n{cards}\n    </main>", "f1-home.html"))


def build_drivers_index():
    cards = []
    driver_cards = [
        ("driver-verstappen.html", "img-verstappen.jpg", "Max Verstappen", "Netherlands · Red Bull · 4× World Champion"),
        ("driver-hamilton.html", "img-hamilton.jpg", "Lewis Hamilton", "UK · Ferrari · 7× World Champion"),
        ("driver-leclerc.html", "img-leclerc.jpg", "Charles Leclerc", "Monaco · Ferrari · Race winner"),
        ("driver-norris.html", "img-norris.jpg", "Lando Norris", "UK · McLaren · Reigning World Champion"),
        ("driver-russell.html", "img-russell.jpg", "George Russell", "UK · Mercedes · Grand Prix winner"),
    ]
    for href, img, name, sub in driver_cards:
        cards.append(f"""            <div class="profile-card">
                <img src="images/{img}" alt="{name}" class="card-photo">
                <div class="card-body"><h3>{name}</h3><p>{sub}</p><a href="{href}">Read profile →</a></div>
            </div>""")
    body = f"""    <main class="page-wrap">
        <article class="panel hero-panel">
            <h1>2026 Formula 1 Drivers</h1>
            <p>Five of the biggest names on the current grid. Each profile includes team details, career stats, and a portrait photo.</p>
        </article>
        <div class="card-grid">
{chr(10).join(cards)}
        </div>
    </main>"""
    write("drivers.html", page_shell("Grid & Glory | 2026 Drivers", body, active_section="drivers"))


def build_circuits_index():
    cards = []
    circuit_cards = [
        ("circuit-monaco.html", "img-circuit-monaco.jpg", "Monaco", "Monte Carlo · Street circuit · 3.337 km"),
        ("circuit-silverstone.html", "img-circuit-silverstone.jpg", "Silverstone", "UK · British GP · 5.891 km"),
        ("circuit-spa.html", "img-circuit-spa.jpg", "Spa-Francorchamps", "Belgium · Eau Rouge · 7.004 km"),
        ("circuit-suzuka.html", "img-circuit-suzuka.jpg", "Suzuka", "Japan · Figure-eight · 5.807 km"),
        ("circuit-monza.html", "img-circuit-monza.jpg", "Monza", "Italy · Temple of Speed · 5.793 km"),
        ("circuit-abu-dhabi.html", "img-circuit-abudhabi.jpg", "Abu Dhabi", "Yas Marina · Season finale · 5.281 km"),
    ]
    for href, img, name, sub in circuit_cards:
        cards.append(f"""            <div class="profile-card">
                <img src="images/{img}" alt="{name} Grand Prix circuit">
                <div class="card-body"><h3>{name}</h3><p>{sub}</p><a href="{href}">Read profile →</a></div>
            </div>""")
    body = f"""    <main class="page-wrap">
        <article class="panel hero-panel">
            <h1>Iconic Formula 1 Circuits</h1>
            <p>Six of the most famous tracks in the sport — from Monaco's streets to Monza's straights. Each page includes lap data, history, and a circuit photo.</p>
        </article>
        <div class="card-grid">
{chr(10).join(cards)}
        </div>
    </main>"""
    write("circuits.html", page_shell("Grid & Glory | Circuits", body, active_section="circuits"))


def build_teams():
    cards = []
    rows = []
    for team, d1, d2, pu, img, alt in TEAMS_2026:
        cards.append(f"""            <div class="profile-card">
                <img src="images/{img}" alt="{alt}">
                <div class="card-body">
                    <h3>{team}</h3>
                    <p>{d1} · {d2}</p>
                    <p class="muted">Power unit: {pu}</p>
                </div>
            </div>""")
        rows.append(f"                <tr><td>{team}</td><td>{d1}</td><td>{d2}</td><td>{pu}</td></tr>")
    body = f"""    <main class="page-wrap">
        <article class="panel hero-panel">
            <h1>2026 Formula 1 Grid</h1>
            <p>Eleven teams and twenty-two drivers enter the new power unit era. Cadillac joins as the first new American constructor in decades, while Audi replaces Sauber as a factory entry.</p>
            <img src="images/img-team-redbull.jpg" alt="Red Bull Racing Formula 1 car">
        </article>
        <article class="panel">
            <h2>Team Cars</h2>
            <p>Each constructor runs two cars. Below are the 2026 challengers — from McLaren's papaya machine to Cadillac's debut livery.</p>
            <div class="card-grid">
{chr(10).join(cards)}
            </div>
        </article>
        <article class="panel">
            <h2>Full Entry List</h2>
            <table>
                <tr><th>Team</th><th>Driver 1</th><th>Driver 2</th><th>Power Unit</th></tr>
{chr(10).join(rows)}
            </table>
            <h2>What's New in 2026</h2>
            <p>New 1.6-litre hybrid power units with increased electrical power, active aerodynamics, and a larger grid with Cadillac. Engine suppliers are Mercedes, Ferrari, Red Bull Ford, Honda (Aston Martin), and Audi.</p>
        </article>
    </main>"""
    write("teams.html", page_shell("Grid & Glory | 2026 Teams", body, "teams.html"))


def build_history():
    body = """    <main class="page-wrap">
        <article class="panel hero-panel">
            <h1>History of Formula 1</h1>
            <p>The FIA Formula One World Championship began in 1950 at Silverstone, UK. In 2026 the sport enters a new rules cycle — but the story below spans more than seven decades of racing.</p>
            <img src="images/img-hero-2026.jpg" alt="Modern McLaren Formula 1 car">
        </article>
        <article class="panel" id="era-1950">
            <h2>1950s — The Championship Begins</h2>
            <p>Giuseppe Farina won the first title in 1950 driving for Alfa Romeo. Juan Manuel Fangio dominated the decade with five championships. Cars had front engines, narrow tyres, and almost no safety equipment by modern standards.</p>
        </article>
        <article class="panel" id="era-1980">
            <h2>1980s — Turbo Era</h2>
            <p>Turbocharged engines produced extreme power. Ayrton Senna and Alain Prost fought legendary battles at McLaren. Ground-effect aerodynamics made cars faster but more dangerous until rules changed.</p>
        </article>
        <article class="panel" id="era-2000">
            <h2>2000s — Schumacher & Ferrari</h2>
            <p>Michael Schumacher won five consecutive titles with Ferrari (2000–2004). The era also saw improved TV coverage, more Asian races, and the rise of teams like Renault and McLaren as title contenders.</p>
        </article>
        <article class="panel" id="era-2010">
            <h2>2010s — Hybrid Revolution</h2>
            <p>1.6-litre V6 turbo hybrid power units replaced V8 engines in 2014. Mercedes won eight consecutive constructors' titles. Lewis Hamilton matched Schumacher's seven championships.</p>
        </article>
        <article class="panel" id="era-2020">
            <h2>2020s — Verstappen, Norris & New Rules</h2>
            <p>Ground-effect cars returned in 2022. Max Verstappen dominated early in the decade before McLaren's rise. A cost cap limits spending, and 2026 introduces new power units, active aero, and an 11-team grid including Cadillac.</p>
            <img src="images/img-team-mclaren.jpg" alt="McLaren Formula 1 car from the 2020s era">
        </article>
    </main>"""
    write("history.html", page_shell("Grid & Glory | F1 History", body, "history.html"))


def build_contact():
    body = """    <main class="page-wrap">
        <article class="panel">
            <h1>Contact</h1>
            <p>Questions about this 2026 F1 homework project? Use the form below. (JavaScript demo — no data is sent to a server.)</p>
            <form id="contactForm">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" rows="5" required></textarea>
                </div>
                <button type="submit">Send Message</button>
            </form>
        </article>
    </main>"""
    write("contact.html", page_shell("Grid & Glory | Contact", body, "contact.html"))


def build_circuit_page(filename, data):
    stats = "".join(f'                <div class="stat-box"><strong>{a}</strong><span>{b}</span></div>\n' for a, b in data["stats"])
    prev_h, prev_l = data["prev"]
    next_h, next_l = data["next"]
    body = f"""    <main class="page-wrap">
        <article class="panel">
            <h1>{data["name"]}</h1>
            <p><strong>Country:</strong> {data["country"]} &nbsp;|&nbsp; {data["meta"]}</p>
            <img class="profile-img circuit-photo" src="images/{data["img"]}" alt="{data["alt"]}">
            <div class="stats-grid">
{stats}            </div>
            <h2>About This Track</h2>
            <p>{data["about"]}</p>
            <h2>Famous Sections</h2>
            <p>{data["corners"]}</p>
            <div class="page-nav">
                <a href="{prev_h}">← {prev_l}</a>
                <a href="{next_h}">Next: {next_l} →</a>
            </div>
        </article>
    </main>"""
    write(filename, page_shell(f'{data["name"]} | Grid & Glory', body, active_section="circuits", circuit_active=filename))


def build_driver_page(filename, data):
    stats = "".join(f'                <div class="stat-box"><strong>{a}</strong><span>{b}</span></div>\n' for a, b in data["stats"])
    paras = "".join(f"            <p>{p}</p>\n" for p in data["career"])
    prev_h, prev_l = data["prev"]
    next_h, next_l = data["next"]
    body = f"""    <main class="page-wrap">
        <article class="panel">
            <h1>{data["name"]}</h1>
            <p><strong>{data["meta"]}</strong></p>
            <img class="profile-img driver-photo" src="images/{data["img"]}" alt="{data["alt"]}">
            <div class="stats-grid">
{stats}            </div>
            <h2>Career</h2>
{paras}            <h2>2026 Season</h2>
            <p>{data["legacy"]}</p>
            <div class="page-nav">
                <a href="{prev_h}">← {prev_l}</a>
                <a href="{next_h}">Next: {next_l} →</a>
            </div>
        </article>
    </main>"""
    write(filename, page_shell(f'{data["name"]} | Grid & Glory', body, active_section="drivers"))


def remove_legacy():
    legacy = [
        "driver-senna.html", "driver-schumacher.html", "driver-alonso.html",
        "circuit-bahrain.html", "circuit-singapore.html", "circuit-interlagos.html",
    ]
    for name in legacy:
        path = ROOT / name
        if path.exists():
            path.unlink()
            print("removed", name)


def main():
    build_home()
    build_drivers_index()
    build_circuits_index()
    build_teams()
    build_history()
    build_contact()
    for fn, data in CIRCUIT_DATA.items():
        build_circuit_page(fn, data)
    for fn, data in DRIVER_DATA.items():
        build_driver_page(fn, data)
    remove_legacy()
    print("Done.")


if __name__ == "__main__":
    main()
