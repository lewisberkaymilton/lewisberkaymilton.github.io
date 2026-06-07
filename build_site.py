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
        "about": [
            "Monaco is the slowest and tightest track on the Formula 1 calendar. Average lap speeds are far lower than at permanent circuits like Monza or Silverstone, and the margin for error is almost zero.",
            "The circuit runs through the streets of Monte Carlo and La Condamine, passing the harbour, the casino, and the tunnel. Barriers line every inch of the track — there is no run-off area and nowhere to hide a mistake.",
            "Overtaking is extremely difficult because the track is narrow and corners are slow. Qualifying position is critical: pole sitters win a large share of races here. Strategy calls on tyre life, pit timing, and safety-car restarts often decide the winner more than raw pace.",
            "Teams use maximum downforce wings to maximise grip in the slow corners. Even with DRS or active aero in 2026, passing another car on track remains one of the hardest tasks in the sport.",
            "The glamour of the harbour, the yachts, and the casino square make this the most famous race on the calendar — even when the racing itself is processional, the event itself is unmatched.",
        ],
        "history": [
            "The Monaco Grand Prix was first held in 1929, organised by Anthony Noghès before the world championship even existed. It joined the inaugural F1 calendar in 1950 and has been a permanent fixture since 1955, with only a few exceptions.",
            "Graham Hill earned the nickname \"Mr Monaco\" with five wins in the 1960s. Ayrton Senna later matched and surpassed that legend with six victories between 1987 and 1993 — a record that still stands.",
            "The circuit layout has changed gradually over the decades. The Swimming Pool section was redesigned in 2003, and the Nouvelle Chicane replaced the old chicane near the harbour to improve safety.",
            "Modern winners include Lewis Hamilton, Max Verstappen, and Charles Leclerc — though Leclerc, born in Monaco, has yet to win his home race despite taking pole position multiple times.",
            "Monaco remains the race every driver wants to win. The combination of history, prestige, and the challenge of threading a car through the streets at the limit makes it unique in world sport.",
        ],
        "corners": "Casino Square, the Tunnel exit, and the Swimming Pool section are the most famous parts of this harbour-side layout. Tabac and the Nouvelle Chicane are key overtaking attempts — though they rarely succeed.",
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
        "about": [
            "Silverstone hosted the first world championship race in 1950 and remains the home of the British Grand Prix. The circuit sits on a former RAF bomber station in Northamptonshire, and the old runways still shape parts of the layout.",
            "High-speed corners like Copse, Maggotts, Becketts, and Chapel make it a favourite for drivers who enjoy commitment and precision. The layout rewards aerodynamic efficiency through long flat-out sections linked by quick direction changes.",
            "British fans pack the grandstands every July, creating one of the loudest atmospheres in the sport. When a home driver leads — especially Lewis Hamilton in his Mercedes or Ferrari years — the crowd noise is deafening.",
            "Weather is unpredictable in the English summer. Rain can transform the race entirely, as seen in the dramatic 2021 race where Hamilton and Verstappen collided while battling for the lead after a restart.",
            "The 2026 cars with active aerodynamics will behave differently through the high-speed sections, but Silverstone's core challenge — trusting the car through Becketts at full throttle — remains unchanged.",
        ],
        "history": [
            "Originally a wartime airfield, Silverstone hosted the very first F1 world championship race on 13 May 1950. Giuseppe Farina won for Alfa Romeo, and the circuit became the permanent home of the British GP from 1987 onward.",
            "The track has been redesigned several times — the Bridge section was removed, and the Arena loop was added in 2010 — but it always kept its high-speed, flowing character that drivers love.",
            "Lewis Hamilton has won the British GP a record nine times, turning Silverstone into a personal fortress during his Mercedes dominance. Nigel Mansell's 1992 crowd invasion and the 2021 Hamilton-Verstappen collision are among its most famous moments.",
            "Other legendary winners include Jim Clark, Jackie Stewart, Alain Prost, and Max Verstappen. The British GP is one of the oldest and most prestigious races on the calendar.",
            "Silverstone also hosts MotoGP and many other events, but Formula 1 at the British GP remains the circuit's defining weekend every summer.",
        ],
        "corners": "Copse, Maggotts-Becketts, and Stowe are key overtaking and tyre-management zones. The Wellington Straight and Hangar Straight produce slipstream battles into Brooklands and Stowe.",
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
        "about": [
            "Spa-Francorchamps is one of the longest and fastest tracks in Formula 1 at 7.004 km per lap. Set in the Ardennes forest in eastern Belgium, it combines long straights with blind crests and dramatic elevation changes.",
            "Weather can change lap by lap — sunshine at La Source and heavy rain at Stavelot is common. Teams must gamble on tyre strategy more here than at almost any other circuit, and rain specialists often shine.",
            "Eau Rouge-Raidillon remains the circuit's most famous sequence: a flat-out uphill left-right-left through a compression at over 300 km/h in modern F1 cars. Every driver remembers their first lap through it.",
            "The Kemmel Straight leads into Les Combes, one of the best overtaking zones on the calendar. DRS and active aero in 2026 make slipstream battles into Les Combes and the Bus Stop Chicane especially important.",
            "Spa rewards brave drivers and punishes mistakes. Gravel traps and barriers sit close to the edge of the track, and a spin at Pouhon or Blanchimont can end a race instantly.",
        ],
        "history": [
            "Spa first hosted Formula 1 in 1950 on a fearsome 14 km layout through public roads. The old circuit was shortened repeatedly for safety, but the modern 7 km track keeps the sport's most dramatic corners.",
            "The Belgian GP was a regular calendar fixture but dropped out during periods when the old layout was deemed too dangerous. The current circuit returned in the 1980s and has been a permanent home since.",
            "Ayrton Senna described Eau Rouge in the rain as a test of courage. Michael Schumacher won six times at Spa; Lewis Hamilton and Max Verstappen have added multiple modern victories.",
            "The 1998 race started in torrential rain and produced one of the biggest first-lap pile-ups in history. Spa's unpredictability is part of its identity — the best car does not always win here.",
            "Fans travel from across Europe for the Belgian GP weekend. The forest setting, unpredictable weather, and legendary corners make it one of the most beloved venues in motorsport.",
        ],
        "corners": "La Source, Eau Rouge-Raidillon, Pouhon, and Blanchimont define this classic European venue. Bus Stop Chicane is the main overtaking zone after the Kemmel Straight.",
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
        "about": [
            "Suzuka's unique figure-eight layout crosses over itself via a bridge between the exit of the Degner curve and the back straight, making it one of only a handful of tracks in the world with that design.",
            "The fast Esses in Sector 1 reward rhythm and confidence — a slight mistake in the opening sequence costs time through the entire lap. Drivers who find a flow through the Esses often qualify at the front.",
            "Spoon Curve and 130R test car balance at high speed before the tight Casio Triangle chicane at the end of the lap. 130R taken flat in qualifying is one of the most impressive sights in Formula 1.",
            "Japanese fans are among the most passionate and knowledgeable in the sport. The grandstands fill early, and the atmosphere when a Honda-powered car or a Japanese driver performs well is extraordinary.",
            "Suzuka often hosts championship-deciding races. The combination of high-speed corners, technical slow sections, and variable weather makes it a complete test of car and driver.",
        ],
        "history": [
            "Built by Honda as a test track in 1962, Suzuka was designed by Dutch engineer John Hugenholtz. It hosted its first Japanese Grand Prix in 1987 and replaced Fuji as Japan's primary F1 venue.",
            "The circuit became the stage for two of the most famous championship showdowns in history: Senna and Prost collided here in 1989 and 1990, deciding the title both times in controversial fashion.",
            "Michael Schumacher won six Japanese GPs. Lewis Hamilton clinched multiple titles at Suzuka, and Max Verstappen has dominated recent editions with Red Bull and Honda power.",
            "The track was modified over the years — the 130R corner was eased slightly for safety, and the chicane before the pit straight was added — but the core figure-eight challenge remained.",
            "After COVID-related absences, the Japanese GP returned to a full calendar slot and remains one of the most anticipated weekends of the season for drivers and fans alike.",
        ],
        "corners": "The Esses, Spoon Curve, and 130R are legendary sections that reward precision and commitment. Degner and the Casio Triangle are key braking zones for overtakes.",
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
        "about": [
            "Monza is the spiritual home of Ferrari and one of the fastest tracks in the sport. The Autodromo Nazionale sits in the Royal Park of Monza, north of Milan, and teams run low-downforce wings to maximise straight-line speed.",
            "The long Lombardy straights — including the main straight and the back straight through the Curva Grande — produce the highest top speeds of the season, often exceeding 350 km/h with DRS or active aero open.",
            "Slipstream battles into the Rettifilo and Parabolica chicanes create classic wheel-to-wheel racing. A driver in the slipstream can pass on the straight, but braking late into the chicane requires precision — mistakes end races instantly.",
            "The tifosi — Ferrari's passionate Italian fan base — turn the park into a sea of red every September. Winning here means more to Ferrari drivers than almost any other race on the calendar.",
            "Monza is one of the few circuits where teams accept being slow in corners in exchange for straight-line speed. Setup compromise is extreme: high straight speed, lower cornering grip.",
        ],
        "history": [
            "Monza opened in 1922, making it one of the oldest permanent circuits in the world. It has hosted the Italian Grand Prix since the championship began in 1950 — only the Indianapolis 500 shared the inaugural calendar.",
            "The old banked oval layout was used alongside the road course until the 1960s. The banking still exists in the forest but is no longer used for F1 — the current layout uses the classic road course only.",
            "Ferrari has won more Italian GPs than any other team. Tifosi celebrations when a Ferrari driver wins at Monza — especially Charles Leclerc in 2019 or Carlos Sainz in recent years — are among the loudest in sport.",
            "Legendary winners include Juan Manuel Fangio, Stirling Moss, Nelson Piquet, Ayrton Senna, and Lewis Hamilton. The circuit's combination of speed and history makes it non-negotiable on any F1 calendar.",
            "Monza also hosts endurance racing and other categories, but the Italian Grand Prix weekend in early September remains the circuit's defining event every year.",
        ],
        "corners": "The Rettifilo chicanes, Lesmo corners, and Parabolica define Monza's unique low-downforce challenge. Ascari and the Curva Grande set up the main straight battles.",
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
        "about": [
            "Yas Marina Circuit on Yas Island in Abu Dhabi often hosts the final round of the Formula 1 world championship. The modern pit building, marina, and five-star hotel create a unique end-of-season atmosphere.",
            "The layout was redesigned in 2021 to improve overtaking. The old slow hairpin behind the hotel was removed and replaced with a faster Turns 5–9 sequence that flows more naturally and encourages side-by-side racing.",
            "The race starts in daylight and finishes under floodlights as the sun sets over the Persian Gulf, making it one of the most visually striking events on the calendar. The twilight timing affects track temperature and tyre behaviour.",
            "The long back straight into Turn 9 is a primary DRS overtaking zone. Turn 1 after the main straight is another key passing place, especially when drivers lock up under braking from high speed.",
            "Abu Dhabi is a popular destination for teams and fans at season's end. Championship trophies are often decided here, adding extra tension to every position on track.",
        ],
        "history": [
            "The Abu Dhabi Grand Prix joined the calendar in 2009 as Formula 1 expanded into the Middle East. Hermann Tilke designed the circuit on Yas Island, combining a permanent track with a marina and entertainment district.",
            "Sebastian Vettel won the inaugural race for Red Bull. Lewis Hamilton, Max Verstappen, and other champions have since added Abu Dhabi victories to their records.",
            "The 2021 season finale here was one of the most controversial in history. Hamilton led the title-deciding race late on before a safety-car restart allowed Verstappen to pass on the final lap and win the championship.",
            "The 2021 layout change was a direct response to criticism that the old circuit produced processional racing. Early reviews of the new section were positive, with more overtaking through the hotel complex.",
            "Abu Dhabi has become the traditional season closer. Teams often use the weekend to evaluate development directions for the following year, especially when new regulations — like the 2026 reset — are approaching.",
        ],
        "corners": "Turns 5–7 through the hotel section and the long back straight into Turn 9 are key battle zones. Turn 1 after the main straight is the primary overtaking spot.",
        "prev": ("circuit-monza.html", "Monza"),
        "next": ("circuit-monaco.html", "Monaco"),
    },
}

DRIVER_DATA = {
    "driver-verstappen.html": {
        "name": "Max Verstappen",
        "meta": "Netherlands · Red Bull Racing · Car #3 · Team mate: Isack Hadjar",
        "img": "img-verstappen.jpg",
        "alt": "Max Verstappen in Red Bull Racing overalls",
        "stats": [("4+", "World Titles"), ("65+", "Race Wins"), ("2015", "F1 Debut"), ("3", "Car Number")],
        "early": [
            "Born in Hasselt, Belgium, Verstappen grew up in a racing family — his father Jos raced in Formula 1 and his mother Sophie competed in karting.",
            "He dominated karting across Europe before stepping straight into single-seaters. Red Bull's junior programme signed him early, betting on raw speed over experience.",
        ],
        "career": [
            "Verstappen made his F1 debut with Toro Rosso in 2015 aged 17, becoming the youngest driver in history. He moved to Red Bull mid-2016 and won on his first appearance for the team in Spain.",
            "From 2021 onwards he fought Lewis Hamilton for titles, breaking Mercedes' hybrid-era dominance. He won four consecutive championships from 2021 to 2024 with aggressive racecraft and relentless qualifying pace.",
            "He holds records for most wins in a single season and has led hundreds of laps across the ground-effect regulation era.",
        ],
        "season_2026": [
            "In 2026 Verstappen leads Oracle Red Bull Racing into the new power unit era with Red Bull Ford. Rookie Isack Hadjar joins as team mate after impressing at Racing Bulls.",
            "Laurent Mekies took over as team principal, and the team must adapt to active aerodynamics and higher electrical deployment. Verstappen remains the benchmark every rival is measured against.",
        ],
        "legacy": "Verstappen combines late-braking aggression with tyre management that improved dramatically after 2020. He rarely makes unforced errors under pressure and is widely regarded as the complete package of the current generation.",
        "prev": ("driver-russell.html", "George Russell"),
        "next": ("driver-hamilton.html", "Lewis Hamilton"),
    },
    "driver-hamilton.html": {
        "name": "Lewis Hamilton",
        "meta": "United Kingdom · Ferrari · Car #44 · Team mate: Charles Leclerc",
        "img": "img-hamilton.jpg",
        "alt": "Lewis Hamilton driving the Ferrari SF-25 at the Japanese Grand Prix",
        "stats": [("7", "World Titles"), ("105+", "Race Wins"), ("2007", "F1 Debut"), ("44", "Car Number")],
        "early": [
            "Hamilton grew up in Stevenage, Hertfordshire, UK. His father Anthony worked multiple jobs to fund his karting career after Lewis began racing aged eight.",
            "McLaren team principal Ron Dennis signed him to the young driver programme in 1998 when Hamilton was 13 — famously telling him, \"Phone me in nine years if you've won something and we'll sort something out.\"",
            "He won every category he entered on the way up: British karting titles, Formula Renault, Formula Three, and the GP2 championship in 2006 with five wins from 21 races.",
            "McLaren promoted him directly to Formula 1 for 2007 alongside double world champion Fernando Alonso — one of the most hyped debuts the sport had ever seen.",
        ],
        "career": [
            "Hamilton's rookie season in 2007 was sensational. He led the championship for much of the year, took four wins, and finished third at his home race at Silverstone. He lost the title to Kimi Räikkönen by a single point after a gearbox issue in the final race at Interlagos.",
            "He became the youngest world champion at the time in 2008, winning the title in dramatic fashion — passing Timo Glock in the rain on the last corner of the last lap in Brazil to steal the crown from Felipe Massa.",
            "Four more seasons at McLaren brought wins at Monaco, Silverstone, and Hungary, but the team could not match Red Bull and Brawn GP. Hamilton grew frustrated with unreliable machinery and made the shock move to Mercedes for 2013.",
            "Mercedes had not won a race since returning to F1 in 2010, but Hamilton bet on the team's long-term hybrid engine project. It proved the best decision of his career. He won the 2014 and 2015 titles, beating Nico Rosberg both years in a tense intra-team rivalry.",
            "Rosberg took the 2016 championship and retired immediately afterward. Hamilton responded with four consecutive titles from 2017 to 2020, equalling Michael Schumacher's record of seven world championships at the 2020 Turkish Grand Prix.",
            "He broke Schumacher's record for most race wins at the 2020 Portuguese GP and continued adding poles and podiums. His wet-weather drives — Brazil 2016, Silverstone 2008, Turkey 2020 — are studied as masterclasses in car control.",
            "The 2021 season brought a fierce title fight with Max Verstappen. Hamilton won a record-breaking eighth title on track at Abu Dhabi, but a controversial safety-car restart allowed Verstappen to pass on the final lap and take the championship.",
            "He stayed at Mercedes through 2024, taking his final Mercedes win at the 2024 British Grand Prix — a record ninth home victory — before announcing his move to Ferrari, the team he had dreamed of driving for since childhood.",
            "In 2025 he joined Scuderia Ferrari alongside Charles Leclerc. The switch ended a twelve-year Mercedes partnership that delivered six drivers' titles and transformed him into the most successful driver in Formula 1 history by race wins and poles.",
        ],
        "season_2026": [
            "Hamilton enters 2026 in Ferrari red with car number 44 — the same number he has used throughout his F1 career. Fred Vasseur leads the team with pressure to deliver Ferrari's first drivers' title since Kimi Räikkönen in 2007.",
            "The new 2026 power unit regulations reset the competitive order. Hamilton's experience developing cars through regulation changes — he did it in 2014, 2017, and 2022 — is a major asset for Ferrari's engineering team.",
            "His relationship with Leclerc is one of the most watched in the paddock. Leclerc brings raw qualifying speed; Hamilton brings racecraft honed over 20 seasons. Ferrari needs both to beat McLaren and Red Bull.",
            "Monza and Monaco are the emotional peaks of his calendar. A Ferrari win at either circuit — especially Monza in front of the tifosi — would rank among the greatest moments in the sport's history.",
            "Beyond results, Hamilton continues to push for diversity through his Mission 44 foundation and remains one of the most globally recognised athletes in any sport.",
        ],
        "legacy": "Hamilton combines wet-weather genius with tyre management that allows him to extend stints when rivals cannot. He reads races better than almost anyone on the grid and rarely makes unforced errors when fighting for championships. His move to Ferrari in 2025 added a new chapter to a career that already redefined what is possible in Formula 1.",
        "prev": ("driver-verstappen.html", "Max Verstappen"),
        "next": ("driver-leclerc.html", "Charles Leclerc"),
    },
    "driver-leclerc.html": {
        "name": "Charles Leclerc",
        "meta": "Monaco · Ferrari · Car #16 · Team mate: Lewis Hamilton",
        "img": "img-leclerc.jpg",
        "alt": "Charles Leclerc in Ferrari racing gear",
        "stats": [("7", "Race Wins"), ("24+", "Pole Positions"), ("2018", "F1 Debut"), ("16", "Car Number")],
        "early": [
            "Leclerc was born and raised in Monaco and started karting aged four. He won multiple junior titles despite the tragedy of losing his close friend and mentor Jules Bianchi.",
            "Ferrari's driver academy signed him after he dominated Formula 2 in 2017. Sauber gave him his F1 debut in 2018, where he outscored team mate Marcus Ericsson in his rookie season.",
        ],
        "career": [
            "Ferrari promoted him for 2019, and he won at Spa and Monza in only his second year with the team — Monza sent the tifosi into delirium with a first Ferrari home victory since 2010.",
            "He has taken pole positions at circuits where Ferrari struggled in race trim, earning a reputation as one of the fastest qualifiers on the grid.",
            "Despite car limitations in some seasons, Leclerc remained loyal to Ferrari and developed into a team leader before Hamilton's arrival.",
        ],
        "season_2026": [
            "Leclerc enters 2026 as Ferrari's home-grown star alongside seven-time champion Hamilton. The pairing is one of the strongest line-ups on the grid on paper.",
            "Winning at Monaco remains an unfulfilled dream — he has pole there multiple times but never stood on the top step at home. The 2026 car and new regulations offer another chance.",
            "Fred Vasseur leads the team with pressure to deliver Ferrari's first title in nearly two decades. Leclerc's qualifying speed and Hamilton's racecraft could be the combination Ferrari needs.",
        ],
        "legacy": "Leclerc combines raw one-lap pace with deep emotional connection to Ferrari and its fans. His aggressive qualifying style and improved race management make him a genuine title contender when the car allows.",
        "prev": ("driver-hamilton.html", "Lewis Hamilton"),
        "next": ("driver-norris.html", "Lando Norris"),
    },
    "driver-norris.html": {
        "name": "Lando Norris",
        "meta": "United Kingdom · McLaren · Car #1 · Team mate: Oscar Piastri",
        "img": "img-norris.jpg",
        "alt": "Lando Norris celebrating a McLaren Grand Prix victory",
        "stats": [("1", "World Title"), ("8+", "Race Wins"), ("2019", "F1 Debut"), ("1", "Car Number")],
        "early": [
            "Norris grew up in Bristol and began karting aged seven. He won the FIA Formula 3 European Championship and finished second in Formula 2 before McLaren promoted him straight to F1.",
            "McLaren's young driver programme backed him through the junior categories. His personality and sim-racing background made him popular with fans long before his first podium.",
        ],
        "career": [
            "He joined McLaren in 2019 alongside Carlos Sainz. Early seasons were difficult as the car lacked pace, but Norris steadily improved and took his first podium at Imola in 2020.",
            "The team's revival under Andrea Stella brought regular podiums and his first win in 2021 at Russia. By 2024–2025 McLaren had the fastest car, and Norris fought Verstappen for the title.",
            "He became world champion entering 2026, carrying the #1 plate as McLaren's first title winner since Lewis Hamilton in 2008.",
        ],
        "season_2026": [
            "Norris leads McLaren's title defence with Oscar Piastri as team mate — a pairing that pushes each other hard while McLaren targets the constructors' crown again.",
            "The 2026 regulation reset could compress the field, but McLaren's aerodynamic understanding under Stella gives them a strong foundation.",
            "Norris must balance aggression with consistency — the mistakes that cost him points in 2024 were largely eliminated in his championship-winning campaign.",
        ],
        "legacy": "Norris blends strong race pace with popular appeal across social media and streaming. He is the face of McLaren's modern revival and one of the sport's biggest global stars.",
        "prev": ("driver-leclerc.html", "Charles Leclerc"),
        "next": ("driver-russell.html", "George Russell"),
    },
    "driver-russell.html": {
        "name": "George Russell",
        "meta": "United Kingdom · Mercedes · Car #63 · Team mate: Kimi Antonelli",
        "img": "img-russell.jpg",
        "alt": "George Russell in Mercedes-AMG Petronas Formula One team kit",
        "stats": [("4+", "Race Wins"), ("30+", "Pole Positions"), ("2019", "F1 Debut"), ("63", "Car Number")],
        "early": [
            "Russell grew up in King's Lynn, Norfolk, and followed his karter brother Ben into motorsport. He won the GP3 title and the FIA Formula 2 championship on his way to F1.",
            "Mercedes' junior programme signed him, but his F1 debut came with Williams in 2019 — a backmarker team where he still impressed with qualifying performances beyond the car's natural pace.",
        ],
        "career": [
            "At Williams he scored the team's only points in difficult seasons and memorably led a wet Belgian GP in 2020 before crashing behind the safety car.",
            "Mercedes promoted him in 2022 when Lewis Hamilton was absent with COVID. Russell nearly won on debut for the team in Sakhir and became a full-time driver in 2022.",
            "He has won multiple grands prix and taken pole positions, establishing himself as a lead driver rather than a future prospect.",
        ],
        "season_2026": [
            "Russell leads Mercedes into the 2026 regulation era with 18-year-old Kimi Antonelli as team mate — Toto Wolff's bold bet on youth alongside experience.",
            "New power units and active aerodynamics offer Mercedes a chance to return to the front after struggling post-2021. Russell's development work in simulators is central to the programme.",
            "He must mentor Antonelli while fighting for wins himself — a dual role that could define his legacy at Mercedes beyond raw results.",
        ],
        "legacy": "Russell is known for exceptional wet-weather driving and precise qualifying laps. His analytical approach and physical size make car setup feedback especially valuable to engineers.",
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


def paras_html(items):
    return "".join(f"            <p>{p}</p>\n" for p in items)


def build_home():
    cards = """
        <article class="panel hero-panel">
            <h1>2026 Formula 1 Season</h1>
            <p>Welcome to <strong>Grid &amp; Glory</strong> — a guide to the world's fastest motorsport. Whether you already follow every race or you are completely new to F1, this page explains the basics before you explore drivers, tracks, and teams.</p>
            <img src="images/img-team-ferrari.jpg" alt="Scuderia Ferrari Formula 1 car">
        </article>

        <article class="panel">
            <h2>What Is Formula 1?</h2>
            <p>Formula 1 — often called <strong>F1</strong> — is the highest level of single-seater racing in the world. "Formula" means the cars must follow strict rules (a formula). "One" means it is the top category — faster and more advanced than Formula 2, Formula 3, or any other series.</p>
            <p>Think of it like the Champions League of car racing. The best drivers, the best engineers, and the biggest manufacturers compete on famous tracks across the globe — from Monaco's city streets to Monza's long straights in Italy.</p>
            <p>Each car is built for speed: open wheels (tyres outside the body), a single seat, wings front and rear for downforce, and a hybrid engine that combines petrol power with electric motors. In 2026, cars can reach over 300 km/h on the straights.</p>
        </article>

        <article class="panel">
            <h2>How Does a Race Weekend Work?</h2>
            <p>A Formula 1 event is called a <strong>Grand Prix</strong> (French for "big prize"). Most weekends follow the same pattern:</p>
            <ul>
                <li><strong>Practice (Friday &amp; Saturday)</strong> — Drivers learn the track and teams test setup changes. Nothing counts for points.</li>
                <li><strong>Qualifying (Saturday)</strong> — Drivers push for the fastest lap time. The quickest driver starts from <strong>pole position</strong> (first on the grid). Slower drivers start further back.</li>
                <li><strong>Race (Sunday)</strong> — All drivers start together in a grid formation. The first to complete the set number of laps wins. Points are awarded to the top finishers.</li>
            </ul>
            <p>Some weekends also include a <strong>Sprint</strong> — a shorter race on Saturday that awards extra points, before the main race on Sunday.</p>
        </article>

        <article class="panel">
            <h2>How Does the Championship Work?</h2>
            <p>There are two titles fought over every season:</p>
            <ul>
                <li><strong>Drivers' Championship</strong> — Points from every race are added up for each driver. The driver with the most points at the end of the season becomes <strong>World Champion</strong>. In 2026, Lando Norris defends the title he won in 2025.</li>
                <li><strong>Constructors' Championship</strong> — Each team runs two cars. Both drivers' points count toward the team total. The team with the most combined points wins. McLaren, Ferrari, and Red Bull usually fight for this.</li>
            </ul>
            <p>Points are given to the top ten finishers in each race — from 25 points for first place down to 1 point for tenth. This means consistency matters: you do not have to win every race to win the title, but you cannot afford many bad weekends either.</p>
        </article>

        <article class="panel">
            <h2>Key Words Explained</h2>
            <ul>
                <li><strong>Pit stop</strong> — The car stops in the pit lane to change tyres or repair damage. A fast pit stop takes under three seconds.</li>
                <li><strong>DRS / Active aero</strong> — Systems that reduce drag on straights to help overtaking. In 2026, active aerodynamics replace much of the old DRS system.</li>
                <li><strong>Safety Car</strong> — A pace car that leads the field at reduced speed after a crash, so marshals can clear the track safely.</li>
                <li><strong>Team / Constructor</strong> — The company that builds the car — Ferrari, McLaren, Mercedes, Red Bull, and so on. Each team enters two drivers.</li>
                <li><strong>Power unit</strong> — The engine plus hybrid electric systems. In 2026, suppliers include Mercedes, Ferrari, Red Bull Ford, Honda, and Audi.</li>
            </ul>
        </article>

        <article class="panel">
            <h2>What's New in 2026</h2>
            <p>The 2026 season brings the biggest rule change in years. New hybrid engines split power roughly 50/50 between petrol and electric. Active front and rear wings adjust automatically in corners and on straights.</p>
            <p>Cadillac joins as the first new American team in decades. Audi replaces Sauber as a factory entry. The grid grows to <strong>11 teams and 22 drivers</strong>, racing across <strong>24 rounds</strong> on six continents.</p>
        </article>

        <article class="panel">
            <h2>How To Use This Site</h2>
            <p>Use the <strong>Featured Circuits</strong> bar at the top to explore Monaco, Monza, Spa, and other legendary tracks. Open the <strong>Drivers</strong> menu for full biographies of Verstappen, Hamilton, Leclerc, Norris, and Russell.</p>
            <p>The <strong>Teams</strong> page shows every constructor with car photos and the full 2026 entry list. The <strong>History</strong> page covers more than 75 years of the sport, from the 1950 championship to today.</p>
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
            <p>Five of the biggest names on the current grid — all race winners and title contenders. Each profile includes early career, highlights, 2026 season outlook, and a portrait photo.</p>
            <p>Click any card below or use the Drivers menu in the navigation bar to open a full biography.</p>
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
            <p>Six of the most famous tracks in the sport — from Monaco's harbour streets to Monza's Temple of Speed. Each page includes lap data, track history, famous corners, and an aerial or race-weekend photo.</p>
            <p>These venues have hosted championship-deciding races, legendary battles, and some of the most memorable moments in F1 history.</p>
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
            <p>Eleven teams and twenty-two drivers enter the new power unit era. Cadillac joins as the first new American constructor in decades, while Audi replaces Sauber as a factory entry with its own power unit.</p>
            <p>Mercedes supplies four teams, Ferrari powers three, and Red Bull Ford supplies Red Bull and Racing Bulls. Aston Martin runs Honda, and Alpine switches to Mercedes engines for 2026.</p>
            <img src="images/img-team-redbull.jpg" alt="Red Bull Racing Formula 1 car">
        </article>
        <article class="panel">
            <h2>Team Cars</h2>
            <p>Each constructor runs two cars, and combined points decide the constructors' championship — which brings prize money and prestige. A team with one superstar and one slow second driver rarely wins the title.</p>
            <p>Below are the 2026 challengers — from McLaren's papaya machine to Cadillac's debut livery on the grid.</p>
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
            <p>New 1.6-litre hybrid power units with increased electrical power and simplified fuel rules. Active aerodynamics replace DRS on many straights. Cars are slightly shorter and lighter than the previous generation.</p>
            <p>Engine suppliers are Mercedes (McLaren, Williams, Aston Martin, Alpine), Ferrari (Ferrari, Haas, Cadillac), Red Bull Ford (Red Bull, Racing Bulls), Honda (Aston Martin works deal), and Audi (factory).</p>
            <h2>Championship Format</h2>
            <p>24 grands prix make up the season. Sprint races continue at selected rounds. Points are awarded to the top ten finishers, with bonus points for pole and fastest lap at some events.</p>
        </article>
    </main>"""
    write("teams.html", page_shell("Grid & Glory | 2026 Teams", body, "teams.html"))


def build_history():
    body = """    <main class="page-wrap">
        <article class="panel hero-panel">
            <h1>History of Formula 1</h1>
            <p>The FIA Formula One World Championship began in 1950 at Silverstone, UK. Seventy-six years later, the sport reaches 2026 with new technology, a wider grid, and global audiences in the hundreds of millions.</p>
            <p>The timeline below covers the major eras — from front-engined pioneers to hybrid champions and the regulation reset of today.</p>
            <img src="images/img-circuit-silverstone.jpg" alt="Silverstone Circuit — venue of the first F1 world championship race in 1950">
        </article>
        <article class="panel" id="era-1950">
            <h2>1950s — The Championship Begins</h2>
            <p>Giuseppe Farina won the first title in 1950 driving for Alfa Romeo. Juan Manuel Fangio dominated the decade with five championships across Alfa Romeo, Ferrari, Mercedes, and Maserati.</p>
            <p>Cars had front engines, narrow tyres, and almost no safety equipment by modern standards. Drivers raced in shirt sleeves with little more than a leather cap for protection.</p>
        </article>
        <article class="panel" id="era-1980">
            <h2>1980s — Turbo Era</h2>
            <p>Turbocharged engines produced over 1,000 horsepower in qualifying trim. Ayrton Senna and Alain Prost fought legendary battles at McLaren while ground-effect aerodynamics made cars faster but more dangerous.</p>
            <p>Tragedies including Imola 1994 eventually forced slower, safer cars. The turbo era ended in 1988, but its legends — Senna, Prost, Piquet, Mansell — defined the sport for a generation.</p>
        </article>
        <article class="panel" id="era-2000">
            <h2>2000s — Schumacher & Ferrari</h2>
            <p>Michael Schumacher won five consecutive titles with Ferrari (2000–2004), breaking records that stood for years. Ferrari's dominance transformed the team into the most successful constructor in history.</p>
            <p>The era also saw improved TV coverage, more Asian races, and the rise of teams like Renault and McLaren as title contenders. Schumacher retired in 2006, returned with Mercedes in 2010, and retired for good in 2012.</p>
        </article>
        <article class="panel" id="era-2010">
            <h2>2010s — Hybrid Revolution</h2>
            <p>1.6-litre V6 turbo hybrid power units replaced V8 engines in 2014. Mercedes won eight consecutive constructors' titles from 2014 to 2021. Lewis Hamilton matched Schumacher's seven championships.</p>
            <p>The hybrid era rewarded engine manufacturers as much as aerodynamicists. Red Bull and Honda eventually broke Mercedes' hold, setting up the Verstappen dominance of the early 2020s.</p>
        </article>
        <article class="panel" id="era-2020">
            <h2>2020s — Verstappen, Norris & New Rules</h2>
            <p>Ground-effect cars returned in 2022, producing closer racing. Max Verstappen dominated early in the decade before McLaren's rise brought Lando Norris a world title. A cost cap now limits team spending.</p>
            <p>2026 introduces new power units, active aero, and an 11-team grid including Cadillac. Hamilton drives for Ferrari, Audi replaces Sauber, and the sport enters its next chapter.</p>
            <img src="images/img-team-audi.jpg" alt="Audi Formula 1 car — new factory team for the 2026 regulation era">
        </article>
    </main>"""
    write("history.html", page_shell("Grid & Glory | F1 History", body, "history.html"))


def build_contact():
    body = """    <main class="page-wrap">
        <article class="panel">
            <h1>Contact</h1>
            <p>Questions about this 2026 F1 homework project? Use the form below to send a message.</p>
            <p>Project by Berkay Gündoğdu · Near East University · Grid & Glory Formula 1 website.</p>
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
    about = paras_html(data["about"])
    history = paras_html(data["history"])
    body = f"""    <main class="page-wrap">
        <article class="panel">
            <h1>{data["name"]}</h1>
            <p><strong>Country:</strong> {data["country"]} &nbsp;|&nbsp; {data["meta"]}</p>
            <img class="profile-img circuit-photo" src="images/{data["img"]}" alt="{data["alt"]}">
            <div class="stats-grid">
{stats}            </div>
            <h2>About This Track</h2>
{about}            <h2>History</h2>
{history}            <h2>Famous Sections</h2>
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
    early = paras_html(data["early"])
    career = paras_html(data["career"])
    season = paras_html(data["season_2026"])
    prev_h, prev_l = data["prev"]
    next_h, next_l = data["next"]
    body = f"""    <main class="page-wrap">
        <article class="panel">
            <h1>{data["name"]}</h1>
            <p><strong>{data["meta"]}</strong></p>
            <img class="profile-img driver-photo" src="images/{data["img"]}" alt="{data["alt"]}">
            <div class="stats-grid">
{stats}            </div>
            <h2>Early Career</h2>
{early}            <h2>Career Highlights</h2>
{career}            <h2>2026 Season</h2>
{season}            <h2>Driving Style & Legacy</h2>
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
