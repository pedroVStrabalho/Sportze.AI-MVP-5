import streamlit as st
import random
from datetime import date, datetime

# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="Sportze.AI", layout="wide")

st.title("Sportze.AI")
st.write("Generate smarter, more professional sport-specific training sessions.")

TODAY = date(2026, 3, 17)

# =========================
# SESSION STATE
# =========================
if "active_section" not in st.session_state:
    st.session_state.active_section = "Training Generator"

# =========================
# CONSTANTS / OPTIONS
# =========================
SPORTS = [
    "Gym",
    "Running",
    "Tennis",
    "Baseball",
    "Rowing",
    "Weightlifting",
    "Water Polo",
]

COMMON_GOALS = [
    "Improve performance",
    "Build fitness",
    "Return after a break",
    "Learn how to play",
    "Have fun / stay active",
]

RUNNING_FOCUS_OPTIONS = [
    "Short distance",
    "Medium distance",
    "Long distance",
    "Ultra long distance",
]

RUNNING_DISTANCE_MAP = {
    "Short distance": ["100m", "200m", "400m", "800m"],
    "Medium distance": ["1.2k", "1.5k", "3k", "5k", "10k"],
    "Long distance": ["15k", "Half marathon", "32k", "Marathon"],
    "Ultra long distance": ["50k", "160k"],
}

SKILL_LEVELS = ["Beginner", "Intermediate", "Advanced"]
INJURY_OPTIONS = ["No", "Yes - minor limitation", "Yes - recent injury"]

TIME_OPTIONS_GENERAL = [
    "30 minutes",
    "45 minutes",
    "60 minutes",
    "75 minutes",
    "90 minutes",
    "120 minutes",
]

TIME_OPTIONS_ENDURANCE = [
    "30 minutes",
    "45 minutes",
    "60 minutes",
    "75 minutes",
    "90 minutes",
    "120 minutes",
    "150 minutes",
    "180 minutes",
    "210 minutes",
    "240 minutes",
]

PHYSIO_BODY_AREAS = [
    "Knee",
    "Ankle / foot",
    "Hamstring",
    "Quad",
    "Hip / groin",
    "Lower back",
    "Shoulder",
    "Elbow / forearm",
    "Wrist / hand",
    "Neck",
    "Other",
]

SECTION_OPTIONS = [
    "Training Generator",
    "Video Review",
    "Counselling",
    "Physio",
]

# =========================
# TENNIS COUNSELLING DATA
# =========================
# Research-backed current window around 17 Mar 2026.
# This is a "fit engine" for now, not a live acceptance-list engine.

UPCOMING_TOURNAMENTS = [
    {
        "name": "Fayez Sarofim & Co. U.S. Men's Clay Court Championship",
        "tour": "ATP Tour",
        "level": "ATP 250",
        "city": "Houston",
        "country": "USA",
        "region": "North America",
        "surface": "Clay",
        "start_date": date(2026, 3, 29),
        "estimated_direct_acceptance_best_fit": (1, 120),
        "estimated_qualifying_fit": (100, 220),
        "notes": "High-level option; better for established ATP players who already travel on ATP schedule.",
    },
    {
        "name": "Tiriac Open",
        "tour": "ATP Tour",
        "level": "ATP 250",
        "city": "Bucharest",
        "country": "Romania",
        "region": "Europe",
        "surface": "Clay",
        "start_date": date(2026, 3, 29),
        "estimated_direct_acceptance_best_fit": (1, 120),
        "estimated_qualifying_fit": (100, 220),
        "notes": "Clay ATP 250. Good if player level is already close to ATP Tour / upper Challenger level.",
    },
    {
        "name": "Grand Prix Hassan II",
        "tour": "ATP Tour",
        "level": "ATP 250",
        "city": "Marrakech",
        "country": "Morocco",
        "region": "Africa / Europe travel corridor",
        "surface": "Clay",
        "start_date": date(2026, 3, 29),
        "estimated_direct_acceptance_best_fit": (1, 120),
        "estimated_qualifying_fit": (100, 220),
        "notes": "Clay ATP 250. Usually better for stronger clay-court profiles.",
    },
    {
        "name": "Sao Paulo Challenger",
        "tour": "ATP Challenger Tour",
        "level": "Challenger",
        "city": "Sao Paulo",
        "country": "Brazil",
        "region": "South America",
        "surface": "Clay",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (80, 260),
        "estimated_qualifying_fit": (220, 420),
        "notes": "Very logical option for Brazilian or South American clay-court players.",
    },
    {
        "name": "Morelia Open",
        "tour": "ATP Challenger Tour",
        "level": "Challenger",
        "city": "Morelia",
        "country": "Mexico",
        "region": "North America",
        "surface": "Hard",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (90, 260),
        "estimated_qualifying_fit": (220, 420),
        "notes": "Better for hard-court players already above typical ITF range.",
    },
    {
        "name": "Split Open",
        "tour": "ATP Challenger Tour",
        "level": "Challenger",
        "city": "Split",
        "country": "Croatia",
        "region": "Europe",
        "surface": "Clay",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (90, 260),
        "estimated_qualifying_fit": (220, 420),
        "notes": "European clay option, best for players already at strong Challenger standard.",
    },
    {
        "name": "III Challenger Montemar ENE Construccion",
        "tour": "ATP Challenger Tour",
        "level": "Challenger",
        "city": "Alicante",
        "country": "Spain",
        "region": "Europe",
        "surface": "Clay",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (90, 260),
        "estimated_qualifying_fit": (220, 420),
        "notes": "Spanish clay option, good for clay specialists with Challenger level.",
    },
    {
        "name": "Bucaramanga Challenger",
        "tour": "ATP Challenger Tour",
        "level": "Challenger",
        "city": "Bucaramanga",
        "country": "Colombia",
        "region": "South America",
        "surface": "Clay",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (90, 260),
        "estimated_qualifying_fit": (220, 420),
        "notes": "South American clay route. Strong fit for players already established above ITF level.",
    },
    {
        "name": "Yokkaichi Challenger",
        "tour": "ATP Challenger Tour",
        "level": "Challenger",
        "city": "Yokkaichi",
        "country": "Japan",
        "region": "Asia",
        "surface": "Hard",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (90, 260),
        "estimated_qualifying_fit": (220, 420),
        "notes": "Hard-court Challenger option. Better only if the player is strong enough and travel makes sense.",
    },
    {
        "name": "M15 Punta del Este",
        "tour": "ITF Men's World Tennis Tour",
        "level": "M15",
        "city": "Punta del Este",
        "country": "Uruguay",
        "region": "South America",
        "surface": "Clay",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (250, 900),
        "estimated_qualifying_fit": (700, 1800),
        "notes": "Entry-level pro event. Good for lower-ranked players building points on clay.",
        "entry_deadline": "Thu 5 Mar 2026, 14:00 GMT",
        "withdrawal_deadline": "Tue 10 Mar 2026, 14:00 GMT",
    },
    {
        "name": "M15 Altamura",
        "tour": "ITF Men's World Tennis Tour",
        "level": "M15",
        "city": "Altamura",
        "country": "Italy",
        "region": "Europe",
        "surface": "Hard",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (250, 900),
        "estimated_qualifying_fit": (700, 1800),
        "notes": "Entry-level pro event on indoor hard. Better for developing hard-court players.",
        "entry_deadline": "Thu 5 Mar 2026, 14:00 GMT",
        "withdrawal_deadline": "Tue 10 Mar 2026, 14:00 GMT",
    },
    {
        "name": "M15 Antalya",
        "tour": "ITF Men's World Tennis Tour",
        "level": "M15",
        "city": "Antalya",
        "country": "Turkiye",
        "region": "Europe / Asia",
        "surface": "Clay",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (250, 900),
        "estimated_qualifying_fit": (700, 1800),
        "notes": "Common entry-level route on clay. Good for players trying to manage costs and get matches.",
        "entry_deadline": "Thu 5 Mar 2026, 14:00 GMT",
        "withdrawal_deadline": "Tue 10 Mar 2026, 14:00 GMT",
    },
    {
        "name": "M15 Opatija",
        "tour": "ITF Men's World Tennis Tour",
        "level": "M15",
        "city": "Opatija",
        "country": "Croatia",
        "region": "Europe",
        "surface": "Clay",
        "start_date": date(2026, 3, 23),
        "estimated_direct_acceptance_best_fit": (250, 900),
        "estimated_qualifying_fit": (700, 1800),
        "notes": "Solid European clay ITF route for players still building ranking.",
        "entry_deadline": "Thu 5 Mar 2026, 14:00 GMT",
        "withdrawal_deadline": "Tue 10 Mar 2026, 14:00 GMT",
    },
]

# =========================
# HELPER FUNCTIONS
# =========================
def choose(*options):
    return random.choice(options)

def bullet_list(items):
    return "\n".join([f"- {item}" for item in items])

def format_plan(title, focus, warmup, main_work, strength=None, cooldown=None, notes=None):
    text = f"## {title}\n"
    text += f"**Focus:** {focus}\n\n"

    text += f"### Warm-up\n{bullet_list(warmup)}\n\n"
    text += f"### Main part\n{bullet_list(main_work)}\n\n"

    if strength:
        text += f"### Secondary block\n{bullet_list(strength)}\n\n"

    if cooldown:
        text += f"### Cooldown\n{bullet_list(cooldown)}\n\n"

    if notes:
        text += f"### Coaching notes\n{bullet_list(notes)}\n\n"

    return text

def beginner_modifier(level):
    return level == "Beginner"

def injury_caution(injury_status):
    return injury_status != "No"

def goal_is_learning(goal):
    return goal == "Learn how to play"

def time_to_minutes(time_str):
    digits = "".join([c for c in time_str if c.isdigit()])
    return int(digits) if digits else 60

def running_distance_category(distance):
    sprint = ["100m", "200m", "400m", "800m"]
    medium = ["1.2k", "1.5k", "3k", "5k", "10k"]
    long = ["15k", "Half marathon", "32k", "Marathon"]
    ultra = ["50k", "160k"]

    if distance in sprint:
        return "short"
    if distance in medium:
        return "medium"
    if distance in long:
        return "long"
    if distance in ultra:
        return "ultra"
    return "medium"

def pain_requires_physio(pain_score):
    return pain_score >= 6

def parse_date(d):
    if isinstance(d, date):
        return d
    return datetime.strptime(d, "%Y-%m-%d").date()

def format_date(d):
    return parse_date(d).strftime("%d %b %Y")

def region_match_score(player_region, tournament_region):
    player_region = player_region.lower()
    tournament_region = tournament_region.lower()

    if player_region in tournament_region:
        return 20
    if player_region == "south america" and "north america" in tournament_region:
        return 8
    if player_region == "north america" and "south america" in tournament_region:
        return 8
    if player_region == "europe" and ("africa" in tournament_region or "europe" in tournament_region):
        return 12
    return 0

def surface_match_score(preferred_surface, tournament_surface):
    if preferred_surface == "No preference":
        return 8
    if preferred_surface == tournament_surface:
        return 20
    return 0

def ranking_fit_score(player_ranking, event):
    direct_low, direct_high = event["estimated_direct_acceptance_best_fit"]
    qual_low, qual_high = event["estimated_qualifying_fit"]

    if player_ranking <= 0:
        return 0, "No ranking entered"
    if direct_low <= player_ranking <= direct_high:
        return 35, "Strong direct-acceptance fit"
    if qual_low <= player_ranking <= qual_high:
        return 24, "More realistic qualifying/alternate fit"
    if player_ranking < direct_low:
        return 18, "Strong enough level-wise, but event may be below best schedule level"
    return 6, "Probably too low for comfortable entry"

def level_preference_score(target_level, event_level):
    if target_level == "Best fit":
        return 0
    if target_level == event_level:
        return 18
    if target_level == "ITF" and event_level in ["M15", "M25"]:
        return 18
    if target_level == "Challenger" and event_level == "Challenger":
        return 18
    if target_level == "ATP Tour" and event_level.startswith("ATP"):
        return 18
    return -8

def entry_status_label(event):
    if "entry_deadline" in event:
        return f"Entry deadline listed: {event['entry_deadline']}"
    return "Use official acceptance list / fact sheet for live deadline confirmation"

def recommend_tournaments(player_ranking, player_region, preferred_surface, target_level):
    scored = []

    for event in UPCOMING_TOURNAMENTS:
        score = 0

        rank_score, rank_note = ranking_fit_score(player_ranking, event)
        score += rank_score
        score += region_match_score(player_region, event["region"])
        score += surface_match_score(preferred_surface, event["surface"])
        score += level_preference_score(target_level, event["level"])

        scored.append({
            **event,
            "score": score,
            "ranking_note": rank_note,
        })

    scored = sorted(scored, key=lambda x: x["score"], reverse=True)
    return scored

def physio_guidance(area, pain_score, symptoms):
    base = {
        "Knee": {
            "stretch": "gentle quad + calf stretch",
            "mobility": "controlled knee extension/flexion and ankle mobility",
            "support": "ice 15-20 minutes after activity, reduce jumping and deep knee bend if painful",
            "watch": "swelling, instability, locking, or pain that gets sharper with weight-bearing",
        },
        "Ankle / foot": {
            "stretch": "calf stretch and gentle ankle circles",
            "mobility": "alphabet ankle mobility and slow calf raises if tolerated",
            "support": "ice 15-20 minutes, compress if swollen, avoid hard cutting or sprinting",
            "watch": "major swelling, inability to hop, inability to bear weight, visible deformity",
        },
        "Hamstring": {
            "stretch": "very gentle hamstring mobility only, not aggressive stretching",
            "mobility": "heel digs and easy bridge holds if comfortable",
            "support": "reduce sprinting/explosive work, use ice after training if irritated",
            "watch": "sudden sharp pain, bruising, or pain with normal walking",
        },
        "Quad": {
            "stretch": "gentle standing quad stretch",
            "mobility": "easy leg swings and controlled bodyweight sit-to-stand",
            "support": "reduce explosive work, ice after activity if sore",
            "watch": "bruising, major tightness after a pop sensation, or pain climbing stairs",
        },
        "Hip / groin": {
            "stretch": "adductor rock-back and light hip flexor stretch",
            "mobility": "90/90 transitions and controlled adductor movement",
            "support": "avoid lateral explosions and change-of-direction if symptoms increase",
            "watch": "pain with walking, sharp groin pain, or reduced range strongly affecting movement",
        },
        "Lower back": {
            "stretch": "gentle child's pose or knees-to-chest only if it feels relieving",
            "mobility": "cat-cow and controlled pelvic tilts",
            "support": "avoid heavy axial loading and high-impact rotation until calmer",
            "watch": "pain shooting down the leg, numbness, weakness, or bowel/bladder issues",
        },
        "Shoulder": {
            "stretch": "cross-body posterior shoulder stretch and pec mobility",
            "mobility": "wall slides and light band external rotation",
            "support": "reduce overhead hitting/serving/pressing for now, ice after loading if irritated",
            "watch": "night pain, weakness, instability, or pain raising the arm overhead",
        },
        "Elbow / forearm": {
            "stretch": "wrist flexor/extensor stretch",
            "mobility": "light forearm rotation and grip opening/closing",
            "support": "reduce repetitive hitting/throwing volume, ice after activity if sore",
            "watch": "pain that keeps worsening with gripping, swelling, or notable loss of strength",
        },
        "Wrist / hand": {
            "stretch": "gentle wrist flexion/extension mobility",
            "mobility": "tendon glides and easy wrist circles",
            "support": "reduce impact loading and repetitive contact, ice after activity if needed",
            "watch": "sharp pain on grip, visible swelling, or pain after a fall",
        },
        "Neck": {
            "stretch": "gentle upper-trap and levator scap stretch",
            "mobility": "slow neck rotations and chin tucks",
            "support": "avoid heavy shrugging/contact and monitor headache or radiating symptoms",
            "watch": "tingling, dizziness, radiating arm symptoms, or severe restricted movement",
        },
        "Other": {
            "stretch": "gentle mobility only",
            "mobility": "controlled pain-free range of motion",
            "support": "reduce load and monitor how symptoms change over 24-48h",
            "watch": "worsening pain, swelling, bruising, or normal movement becoming difficult",
        },
    }

    plan = base.get(area, base["Other"])

    severity_line = "Low pain profile."
    if pain_score >= 8:
        severity_line = "High pain profile. Do not train through this."
    elif pain_score >= 6:
        severity_line = "Moderate-to-high pain profile. Sport work should be paused or reduced substantially."
    elif pain_score >= 4:
        severity_line = "Moderate pain profile. Keep activity submaximal and avoid aggravating actions."

    red_flags = [
        "heard a pop",
        "cannot bear weight",
        "can’t bear weight",
        "numbness",
        "tingling",
        "severe swelling",
        "locking",
        "giving way",
        "fever",
    ]
    red_flag_found = any(flag in symptoms.lower() for flag in red_flags)

    return {
        "severity": severity_line,
        "stretch": plan["stretch"],
        "mobility": plan["mobility"],
        "support": plan["support"],
        "watch": plan["watch"],
        "red_flag_found": red_flag_found,
    }

# =========================
# YOUR EXISTING TRAINING FUNCTIONS STAY HERE
# KEEP ALL YOUR CURRENT:
# - safety_message()
# - generate_running_plan()
# - generate_gym_plan()
# - generate_tennis_plan()
# - generate_baseball_plan()
# - generate_rowing_plan()
# - generate_weightlifting_plan()
# - generate_water_polo_plan()
# - generate_plan()
# EXACTLY AS YOU ALREADY HAVE THEM
# =========================

def safety_message():
    if injury_status == "No":
        return None

    if pain_score >= 8:
        return (
            "You reported high pain. Today's session should be replaced by rest, light mobility, "
            "and professional evaluation before returning to normal training."
        )
    elif pain_score >= 5:
        return (
            "You reported moderate pain. The session below should be treated as reduced-intensity only. "
            "Avoid explosive work, hard impact, and anything that increases pain."
        )
    else:
        return (
            "You reported a minor issue. Keep intensity controlled, reduce volume slightly, "
            "and stop if symptoms increase."
        )

# =========================
# PASTE ALL YOUR EXISTING SPORT GENERATOR FUNCTIONS BELOW THIS LINE
# =========================
# generate_running_plan()
# generate_gym_plan()
# generate_tennis_plan()
# generate_baseball_plan()
# generate_rowing_plan()
# generate_weightlifting_plan()
# generate_water_polo_plan()
 )import streamlit as st
import random

# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="Sportze.AI", layout="wide")

st.title("Sportze.AI")
st.write("Generate smarter, more professional sport-specific training sessions.")

# =========================
# CONSTANTS / OPTIONS
# =========================
SPORTS = [
    "Gym",
    "Running",
    "Tennis",
    "Baseball",
    "Rowing",
    "Weightlifting",
    "Water Polo",
]

COMMON_GOALS = [
    "Improve performance",
    "Build fitness",
    "Return after a break",
    "Learn how to play",
    "Have fun / stay active",
]

RUNNING_FOCUS_OPTIONS = [
    "Short distance",
    "Medium distance",
    "Long distance",
    "Ultra long distance",
]

RUNNING_DISTANCE_MAP = {
    "Short distance": ["100m", "200m", "400m", "800m"],
    "Medium distance": ["1.2k", "1.5k", "3k", "5k", "10k"],
    "Long distance": ["15k", "Half marathon", "32k", "Marathon"],
    "Ultra long distance": ["50k", "160k"],
}

SKILL_LEVELS = ["Beginner", "Intermediate", "Advanced"]
INJURY_OPTIONS = ["No", "Yes - minor limitation", "Yes - recent injury"]

TIME_OPTIONS_GENERAL = [
    "30 minutes",
    "45 minutes",
    "60 minutes",
    "75 minutes",
    "90 minutes",
    "120 minutes",
]

TIME_OPTIONS_ENDURANCE = [
    "30 minutes",
    "45 minutes",
    "60 minutes",
    "75 minutes",
    "90 minutes",
    "120 minutes",
    "150 minutes",
    "180 minutes",
    "210 minutes",
    "240 minutes",
]

# =========================
# HELPER FUNCTIONS
# =========================
def choose(*options):
    return random.choice(options)

def bullet_list(items):
    return "\n".join([f"- {item}" for item in items])

def format_plan(title, focus, warmup, main_work, strength=None, cooldown=None, notes=None):
    text = f"## {title}\n"
    text += f"**Focus:** {focus}\n\n"

    text += f"### Warm-up\n{bullet_list(warmup)}\n\n"
    text += f"### Main part\n{bullet_list(main_work)}\n\n"

    if strength:
        text += f"### Secondary block\n{bullet_list(strength)}\n\n"

    if cooldown:
        text += f"### Cooldown\n{bullet_list(cooldown)}\n\n"

    if notes:
        text += f"### Coaching notes\n{bullet_list(notes)}\n\n"

    return text

def beginner_modifier(level):
    if level == "Beginner":
        return True
    return False

def injury_caution(injury_status):
    return injury_status != "No"

def goal_is_learning(goal):
    return goal == "Learn how to play"

def time_to_minutes(time_str):
    digits = "".join([c for c in time_str if c.isdigit()])
    return int(digits) if digits else 60

def running_distance_category(distance):
    sprint = ["100m", "200m", "400m", "800m"]
    medium = ["1.2k", "1.5k", "3k", "5k", "10k"]
    long = ["15k", "Half marathon", "32k", "Marathon"]
    ultra = ["50k", "160k"]

    if distance in sprint:
        return "short"
    if distance in medium:
        return "medium"
    if distance in long:
        return "long"
    if distance in ultra:
        return "ultra"
    return "medium"

# =========================
# QUESTION UI
# =========================
sport = st.selectbox("What sport do you want to train?", SPORTS)
goal = st.selectbox("What is your goal with this sport?", COMMON_GOALS)
level = st.selectbox("What is your level?", SKILL_LEVELS)
days_per_week = st.slider("How many days do you train per week?", 1, 7, 3)
injury_status = st.selectbox("Do you have any injury or limitation?", INJURY_OPTIONS)

if injury_status != "No":
    pain_score = st.slider("Current pain level from 1 to 10", 1, 10, 3)
else:
    pain_score = 0

if sport in ["Running", "Rowing", "Water Polo"]:
    session_time = st.selectbox("How much time do you have for this session?", TIME_OPTIONS_ENDURANCE, index=2)
else:
    session_time = st.selectbox("How much time do you have for this session?", TIME_OPTIONS_GENERAL, index=2)

# =========================
# SPORT-SPECIFIC QUESTIONS
# =========================
running_focus = None
running_event = None

if sport == "Running":
    running_focus = st.selectbox("What's the focus?", RUNNING_FOCUS_OPTIONS)
    running_event = st.selectbox(
        f"Which {running_focus.lower()} event do you want to prepare for?",
        RUNNING_DISTANCE_MAP[running_focus]
    )

    running_priority = st.selectbox(
        "What needs the most improvement?",
        ["Speed", "Endurance", "Pacing", "Technique", "Race preparation"]
    )

if sport == "Gym":
    gym_type = st.selectbox(
        "What kind of gym session do you want?",
        ["General fitness", "Strength", "Hypertrophy", "Sport-specific support", "Fat loss / conditioning"]
    )
    gym_split = st.selectbox(
        "What area do you want to train most today?",
        ["Full body", "Upper body", "Lower body", "Push", "Pull", "Core + conditioning"]
    )

if sport == "Tennis":
    tennis_focus = st.selectbox(
        "What is today's tennis focus?",
        ["Consistency", "Footwork", "Serve", "Forehand / backhand", "Match play", "Learn fundamentals"]
    )
    dominant_hand = st.selectbox("Dominant hand", ["Right-handed", "Left-handed"])

if sport == "Baseball":
    baseball_focus = st.selectbox(
        "What is today's baseball focus?",
        ["Learn fundamentals", "Hitting", "Throwing", "Fielding", "Base running", "General athletic baseball session"]
    )
    baseball_position = st.selectbox(
        "Which role best matches you?",
        ["Not sure yet", "Infield", "Outfield", "Pitcher", "Catcher", "General player"]
    )

if sport == "Rowing":
    rowing_environment = st.selectbox(
        "Where is this session mainly happening?",
        ["Erg / indoor", "On water", "Mixed"]
    )
    rowing_focus = st.selectbox(
        "What is the focus?",
        ["Technique", "Aerobic endurance", "Power", "Race prep", "Beginner learning"]
    )

if sport == "Weightlifting":
    wl_focus = st.selectbox(
        "What is the focus?",
        ["Learn technique", "Snatch emphasis", "Clean & jerk emphasis", "Strength base", "Power / speed"]
    )
    wl_experience = st.selectbox(
        "How comfortable are you with the Olympic lifts?",
        ["Very new", "Some experience", "Comfortable"]
    )

if sport == "Water Polo":
    wp_focus = st.selectbox(
        "What is the focus?",
        ["Learn fundamentals", "Swimming conditioning", "Passing and shooting", "Game fitness", "Position skills"]
    )
    wp_role = st.selectbox(
        "What role best describes you?",
        ["Field player", "Goalkeeper", "Not sure / beginner"]
    )

# =========================
# SAFETY LAYER
# =========================
def safety_message():
    if injury_status == "No":
        return None

    if pain_score >= 8:
        return (
            "You reported high pain. Today's session should be replaced by rest, light mobility, "
            "and professional evaluation before returning to normal training."
        )
    elif pain_score >= 5:
        return (
            "You reported moderate pain. The session below should be treated as reduced-intensity only. "
            "Avoid explosive work, hard impact, and anything that increases pain."
        )
    else:
        return (
            "You reported a minor issue. Keep intensity controlled, reduce volume slightly, "
            "and stop if symptoms increase."
        )

# =========================
# SESSION GENERATORS
# =========================
def generate_running_plan():
    total_minutes = time_to_minutes(session_time)
    category = running_distance_category(running_event)
    learn = goal_is_learning(goal)
    beginner = beginner_modifier(level)

    warmup = [
        "5-10 min easy jog or brisk walk",
        "Dynamic mobility: ankles, hips, hamstrings",
        "2-4 progressive run-throughs"
    ]
    cooldown = [
        "5-10 min easy jog or walk",
        "Light calf, hip flexor, and hamstring mobility"
    ]

    if category == "short":
        plans = [
            format_plan(
                "Running Session - Sprint Acceleration",
                f"{running_event} development with first-step speed and mechanics",
                warmup,
                [
                    "4 x 30m acceleration runs, full walk-back recovery",
                    "4 x 60m at fast but controlled speed, focus on posture and relaxation",
                    "3 x 80m build-up runs at about 85-90% effort",
                ],
                strength=[
                    "3 rounds: 8 split squats each leg",
                    "3 rounds: 10 glute bridges",
                    "3 rounds: 20 seconds plank"
                ],
                cooldown=cooldown,
                notes=[
                    "Think tall posture, active arms, and smooth turnover",
                    "Quality is more important than fatigue"
                ]
            ),
            format_plan(
                "Running Session - Speed Endurance",
                f"{running_event} work for holding form under fatigue",
                warmup,
                [
                    "3 x 150m controlled fast runs with full recovery",
                    "4 x 80m relaxed-fast strides",
                    "2 x 200m at target rhythm if preparing for 200m or 400m"
                ],
                strength=[
                    "2 rounds: 8 bodyweight reverse lunges each leg",
                    "2 rounds: 8 calf raises each leg"
                ],
                cooldown=cooldown,
                notes=[
                    "Do not sprint the first rep too hard",
                    "Maintain mechanics instead of forcing pace"
                ]
            ),
            format_plan(
                "Running Session - Sprint Technique",
                f"{running_event} technique session for mechanics and rhythm",
                warmup,
                [
                    "A-skips, B-skips, straight-leg bounds, high knees: 2 sets each",
                    "6 x 40m technical strides",
                    "4 x 60m starts from standing or 2-point position"
                ],
                strength=[
                    "Med ball throws or explosive squat jumps: 3 x 5",
                    "Dead bug: 3 x 8 each side"
                ],
                cooldown=cooldown,
                notes=[
                    "Best for beginners or technical reset days",
                    "Keep reps crisp and stop before form breaks"
                ]
            ),
            format_plan(
                "Running Session - 800m Blend",
                "Useful when training 800m with both speed and aerobic support",
                warmup,
                [
                    "4 x 200m at controlled 800m rhythm, 90 sec rest",
                    "4 x 100m relaxed-fast with good mechanics",
                    "5 min easy jog reset"
                ],
                strength=[
                    "3 x 8 step-ups each leg",
                    "3 x 20 sec side plank each side"
                ],
                cooldown=cooldown,
                notes=[
                    "Good blend for athletes between sprint and middle-distance demands"
                ]
            ),
        ]
        return choose(*plans)

    if category == "medium":
        plans = [
            format_plan(
                "Running Session - Threshold Builder",
                f"{running_event} support with sustained aerobic work",
                warmup,
                [
                    "15-25 min steady run at controlled hard effort",
                    "4 x 30 sec quicker surges with 60 sec easy jog",
                    "Finish with 5 min relaxed running"
                ],
                strength=[
                    "2 rounds: 10 single-leg RDL each side",
                    "2 rounds: 12 calf raises",
                    "2 rounds: 20 sec hollow hold"
                ],
                cooldown=cooldown,
                notes=[
                    "You should feel in control, not all-out",
                    "Great for 3k, 5k and 10k development"
                ]
            ),
            format_plan(
                "Running Session - Intervals",
                f"{running_event} pace control and aerobic power",
                warmup,
                [
                    "6 x 400m at controlled target pace with 90 sec recovery",
                    "or 5 x 800m if preparing for 5k or 10k",
                    "2 x 100m relaxed strides"
                ],
                strength=[
                    "2 rounds: 8 walking lunges each leg",
                    "2 rounds: 10 push-ups",
                    "2 rounds: 25 sec plank"
                ],
                cooldown=cooldown,
                notes=[
                    "Stay even from first rep to last rep",
                    "Best when pace discipline is the priority"
                ]
            ),
            format_plan(
                "Running Session - Technique + Aerobic Base",
                f"{running_event} session for beginners or return-to-training phases",
                warmup,
                [
                    "20-40 min easy run",
                    "6 x 20 sec stride-outs with full easy recovery",
                    "Short running drill block before or after"
                ],
                strength=[
                    "Glute bridge: 3 x 12",
                    "Side plank: 2 x 20 sec each side"
                ],
                cooldown=cooldown,
                notes=[
                    "Ideal when learning pacing and form without overcooking the session"
                ]
            ),
            format_plan(
                "Running Session - Race Rhythm Session",
                f"{running_event} race-specific rhythm work",
                warmup,
                [
                    "3 x 1k at controlled race rhythm for 5k/10k athletes",
                    "or 5 x 600m for 1.5k/3k athletes",
                    "3 x 100m relaxed strides"
                ],
                strength=[
                    "2 rounds: 8 split squats each leg",
                    "2 rounds: 10 band pull-aparts or scap squeezes"
                ],
                cooldown=cooldown,
                notes=[
                    "Teach the body what target rhythm feels like"
                ]
            ),
        ]
        return choose(*plans)

    if category == "long":
        plans = [
            format_plan(
                "Running Session - Long Run",
                f"{running_event} endurance development",
                warmup,
                [
                    f"Run continuously for {max(45, min(total_minutes - 15, total_minutes - 10))} minutes at easy to moderate effort",
                    "Finish with last 10-15 min slightly stronger only if feeling good"
                ],
                strength=[
                    "2 rounds: 8 step-ups each leg",
                    "2 rounds: 10 calf raises",
                    "2 rounds: 20 sec plank"
                ],
                cooldown=cooldown,
                notes=[
                    "Conversation pace for most of the run",
                    "For half marathon and marathon athletes, consistency matters more than speed today"
                ]
            ),
            format_plan(
                "Running Session - Marathon Tempo Blend",
                f"{running_event} pacing and economy session",
                warmup,
                [
                    "15 min easy run",
                    "20-40 min at steady controlled marathon/half-marathon rhythm",
                    "10 min easy finish"
                ],
                strength=[
                    "2 rounds: 10 glute bridges",
                    "2 rounds: 8 single-leg balance reaches each side"
                ],
                cooldown=cooldown,
                notes=[
                    "Stay smooth and fuel properly for longer sessions"
                ]
            ),
            format_plan(
                "Running Session - Aerobic Intervals",
                f"{running_event} controlled interval session without overreaching",
                warmup,
                [
                    "4 x 2k at controlled steady-hard pace with easy jog recovery",
                    "or 3 x 10 min tempo with 3 min easy jog"
                ],
                strength=[
                    "2 rounds: 8 reverse lunges each leg",
                    "2 rounds: 20 sec side plank each side"
                ],
                cooldown=cooldown,
                notes=[
                    "Use this when you want quality but not a maximal session"
                ]
            ),
            format_plan(
                "Running Session - Form Under Fatigue",
                f"{running_event} support session for late-race posture and control",
                warmup,
                [
                    "35-50 min easy aerobic running",
                    "6 x 20 sec short pickups near the end with full easy recovery"
                ],
                strength=[
                    "3 x 10 calf raises",
                    "2 x 10 bird dogs each side"
                ],
                cooldown=cooldown,
                notes=[
                    "A very useful secondary day for half marathon and marathon prep"
                ]
            ),
        ]
        return choose(*plans)

    # ultra
    plans = [
        format_plan(
            "Running Session - Ultra Aerobic Base",
            f"{running_event} endurance base session",
            warmup,
            [
                f"{max(60, min(total_minutes - 10, total_minutes - 5))} minutes easy aerobic running or run-walk format",
                "Practice fueling and hydration during the session if it is long enough"
            ],
            strength=[
                "2 rounds: 8 step-downs each leg",
                "2 rounds: 10 glute bridges",
                "2 rounds: 20 sec plank"
            ],
            cooldown=cooldown,
            notes=[
                "For ultra distances, durability and fueling are major priorities"
            ]
        ),
        format_plan(
            "Running Session - Climbs / Strength Endurance",
            f"{running_event} hill or resisted endurance session",
            warmup,
            [
                "8 x 60-90 sec uphill efforts at controlled hard effort",
                "Easy jog back recovery",
                "10-15 min easy running to finish"
            ],
            strength=[
                "2 rounds: 8 split squats each leg",
                "2 rounds: 8 single-leg RDL each leg"
            ],
            cooldown=cooldown,
            notes=[
                "Helps build strong durable legs for long trail or ultra efforts"
            ]
        ),
        format_plan(
            "Running Session - Back-to-Back Style Support",
            f"{running_event} low-to-moderate stress session for ultra preparation",
            warmup,
            [
                "40-70 min easy run",
                "Add 6 x 20 sec controlled uphill strides if feeling fresh"
            ],
            strength=[
                "Mobility circuit: ankles, hips, thoracic spine",
                "Core: 2 x 25 sec side plank each side"
            ],
            cooldown=cooldown,
            notes=[
                "Works well as a secondary day in bigger ultra blocks"
            ]
        ),
    ]
    return choose(*plans)

def generate_gym_plan():
    if goal_is_learning(goal):
        return format_plan(
            "Gym Session - Beginner Learn the Basics",
            "Learning movement patterns and building confidence in the gym",
            [
                "5 min bike, treadmill walk, or rowing machine",
                "Dynamic mobility for hips, shoulders, and ankles"
            ],
            [
                "Goblet squat - 3 x 8",
                "Dumbbell bench press - 3 x 8",
                "Lat pulldown - 3 x 10",
                "Romanian deadlift with dumbbells - 3 x 8",
                "Seated cable row - 3 x 10"
            ],
            strength=[
                "Plank - 3 x 20 sec",
                "Farmer carry - 3 x 20-30 m"
            ],
            cooldown=[
                "Walk 3 min",
                "Easy stretching for chest, quads, hamstrings"
            ],
            notes=[
                "Focus on good form, not heavy weight",
                "Leave 2-3 reps in reserve on each set"
            ]
        )

    plans = [
        format_plan(
            "Gym Session - Full Body Strength",
            f"{gym_type} with {gym_split.lower()} emphasis",
            [
                "5 min easy cardio",
                "Mobility for ankles, hips, shoulders",
                "2 light prep sets before first main lift"
            ],
            [
                "Back squat or goblet squat - 4 x 6",
                "Bench press or dumbbell bench - 4 x 6",
                "Romanian deadlift - 3 x 8",
                "Seated cable row - 3 x 10",
                "Walking lunges - 2 x 10 each leg"
            ],
            strength=[
                "Plank - 3 x 30 sec",
                "Dead bug - 2 x 8 each side"
            ],
            cooldown=[
                "Easy bike 3-5 min",
                "Lower-body stretching"
            ],
            notes=[
                "Best for overall progress and athletic base"
            ]
        ),
        format_plan(
            "Gym Session - Lower Body Power + Support",
            "Useful for field/court athletes or general performance",
            [
                "5 min cardio",
                "Glute activation and hip mobility"
            ],
            [
                "Trap bar deadlift or RDL - 4 x 5",
                "Split squat - 3 x 8 each leg",
                "Box step-up - 3 x 8 each leg",
                "Hamstring curl - 3 x 10",
                "Calf raises - 3 x 12"
            ],
            strength=[
                "Med ball slam or kettlebell swing - 3 x 6-8",
                "Pallof press - 3 x 10 each side"
            ],
            cooldown=[
                "Walk 3 min",
                "Stretch glutes, hamstrings, calves"
            ],
            notes=[
                "A strong option for running, tennis, baseball, rowing support"
            ]
        ),
        format_plan(
            "Gym Session - Upper Body Push/Pull",
            "Strength and posture support",
            [
                "5 min rower or bike",
                "Shoulder circles, band pull-aparts, scap prep"
            ],
            [
                "Incline dumbbell press - 4 x 8",
                "Chest-supported row - 4 x 8",
                "Overhead press - 3 x 8",
                "Lat pulldown or pull-ups - 3 x 8-10",
                "Face pulls - 3 x 12"
            ],
            strength=[
                "Biceps curl - 2 x 12",
                "Triceps rope pressdown - 2 x 12"
            ],
            cooldown=[
                "Chest and lat stretch",
                "Breathing down-regulation 2 min"
            ],
            notes=[
                "Great if lower body is tired from sport practice"
            ]
        ),
        format_plan(
            "Gym Session - Athletic Conditioning Circuit",
            "General fitness with movement quality and conditioning",
            [
                "5 min easy cardio",
                "Dynamic full-body mobility"
            ],
            [
                "3-4 rounds:",
                "8 goblet squats",
                "10 push-ups",
                "10 cable rows or ring rows",
                "8 reverse lunges each leg",
                "30 sec bike, rower, or ski erg hard but controlled"
            ],
            strength=[
                "Side plank - 2 x 20 sec each side",
                "Farmer carry - 3 x 20 m"
            ],
            cooldown=[
                "Light walk",
                "Stretch quads, chest, calves"
            ],
            notes=[
                "Good when the user wants a tougher but not overly technical gym day"
            ]
        ),
    ]
    return choose(*plans)

def generate_tennis_plan():
    if goal_is_learning(goal) or tennis_focus == "Learn fundamentals":
        return format_plan(
            "Tennis Session - Learn to Play",
            "Beginner fundamentals: movement, rally basics, contact point",
            [
                "5 min light jog or skips",
                "Dynamic mobility",
                "Shadow swings forehand/backhand"
            ],
            [
                "Mini tennis - 10 min",
                "Forehand cross-court rally drill - 5 x 2 min",
                "Backhand controlled rally drill - 5 x 2 min",
                "Simple movement drill: split step + recover - 6 reps each side",
                "Serve toss practice + easy serves - 20 total"
            ],
            strength=[
                "Lateral shuffle - 4 x 20 sec",
                "Band external rotation - 2 x 12 each arm"
            ],
            cooldown=[
                "Walk 3 min",
                "Shoulder and calf mobility"
            ],
            notes=[
                "Goal is clean contact and footwork rhythm, not power"
            ]
        )

    plans = [
        format_plan(
            "Tennis Session - Baseline Consistency",
            "Longer rallies, margin, and movement control",
            [
                "Jog + mobility",
                "Mini tennis",
                "Progressive groundstrokes"
            ],
            [
                "Cross-court forehand rally target: 6 rounds x 2 min",
                "Cross-court backhand rally target: 6 rounds x 2 min",
                "Down-the-line change drill: 4 rounds each side",
                "10-point consistency game"
            ],
            strength=[
                "Lateral bounds - 3 x 6 each side",
                "Split-step reaction drill - 3 x 20 sec"
            ],
            cooldown=[
                "Walk and breathing reset",
                "Hip and shoulder mobility"
            ],
            notes=[
                "Useful for match players who miss too early in rallies"
            ]
        ),
        format_plan(
            "Tennis Session - Serve + First Ball",
            "Serve quality and the shot after serve",
            [
                "Shoulder mobility",
                "Shadow serves",
                "Light serving build-up"
            ],
            [
                "20 serves to deuce side targets",
                "20 serves to ad side targets",
                "Serve + first forehand pattern: 12 reps each side",
                "Second-serve spin practice: 15-20 reps"
            ],
            strength=[
                "Band shoulder external rotation - 2 x 12",
                "Rotational med-ball throw - 3 x 5 each side"
            ],
            cooldown=[
                "Forearm, shoulder, thoracic mobility"
            ],
            notes=[
                "Prioritize toss consistency and balance through contact"
            ]
        ),
        format_plan(
            "Tennis Session - Footwork and Defense",
            "Recovering, changing direction, and defending balls",
            [
                "Movement warm-up with shuffles, crossover steps, split step",
                "Mini tennis"
            ],
            [
                "Wide-ball recovery drill - 8 reps each side",
                "Short ball in / recover back drill - 8 reps each side",
                "Defense-to-neutral rally drill - 6 x 90 sec",
                "Conditioning finisher: 6 x 20 sec on / 40 sec off movement pattern"
            ],
            strength=[
                "Split squat - 2 x 8 each leg",
                "Side plank - 2 x 20 sec each side"
            ],
            cooldown=[
                "Walk",
                "Stretch calves, glutes, groin"
            ],
            notes=[
                "Excellent support session for competitive tennis"
            ]
        ),
        format_plan(
            "Tennis Session - Match Pattern Builder",
            "Decision-making and point construction",
            [
                "Dynamic warm-up",
                "Mini tennis",
                "Progressive rallying"
            ],
            [
                "Cross-court rally then attack down the line - 10 reps each wing",
                "Approach + volley + overhead sequence - 8 reps",
                "Serve + 3-ball live point pattern - 12 points",
                "Tie-break style point play"
            ],
            strength=[
                "Jump rope - 3 x 45 sec",
                "Pallof press - 2 x 10 each side"
            ],
            cooldown=[
                "Shoulder and hip mobility"
            ],
            notes=[
                "Better for intermediates and advanced players"
            ]
        ),
    ]
    return choose(*plans)

def generate_baseball_plan():
    if goal_is_learning(goal) or baseball_focus == "Learn fundamentals":
        return format_plan(
            "Baseball Session - Learn How to Play",
            "Beginner baseball fundamentals",
            [
                "5 min light jog",
                "Dynamic shoulders, hips, and ankles",
                "Easy catch progression"
            ],
            [
                "Grip and throwing basics - 10 min",
                "Partner catch, short distance to moderate distance - 5 rounds",
                "Ground ball fielding basics - 12 reps",
                "Batting stance and dry swings - 15 reps",
                "Tee work or soft toss - 20 swings",
                "Base running basics: first-step and touching the bag - 6 reps"
            ],
            strength=[
                "Med-ball rotational throws - 3 x 5 each side",
                "Band shoulder routine - 2 x 12"
            ],
            cooldown=[
                "Walk",
                "Shoulder, forearm, hip mobility"
            ],
            notes=[
                "This should feel instructional, not exhausting",
                "Great first session for beginners"
            ]
        )

    plans = [
        format_plan(
            "Baseball Session - Hitting Focus",
            "Bat path, timing, and contact quality",
            [
                "Dynamic warm-up",
                "Band shoulders",
                "Dry swing progression"
            ],
            [
                "Tee work - 4 rounds of 8 swings",
                "Front toss or soft toss - 4 rounds of 6 swings",
                "Opposite-field contact drill - 10 reps",
                "Pull-side power line-drive drill - 10 reps"
            ],
            strength=[
                "Rotational med-ball throw - 3 x 5 each side",
                "Split squat - 2 x 8 each leg"
            ],
            cooldown=[
                "Forearm and thoracic mobility"
            ],
            notes=[
                "Keep the barrel through the zone cleanly"
            ]
        ),
        format_plan(
            "Baseball Session - Throwing + Fielding",
            "Arm care, throwing mechanics, and glove work",
            [
                "Dynamic shoulder prep",
                "Easy catch progression"
            ],
            [
                "Progressive throwing - 15-20 total throws",
                "Ground balls left/right/at body - 15 reps",
                "Quick transfer drill - 10 reps",
                "Short reaction fielding drill - 8 reps"
            ],
            strength=[
                "Band external rotation - 2 x 12",
                "Scap push-up - 2 x 10",
                "Farmer carry - 3 x 20 m"
            ],
            cooldown=[
                "Shoulder and forearm recovery"
            ],
            notes=[
                "Prioritize smooth arm action over max effort throwing"
            ]
        ),
        format_plan(
            "Baseball Session - Athletic Baseball Conditioning",
            "Speed, change of direction, and baseball movement",
            [
                "Jog and mobility",
                "Dynamic sprint prep"
            ],
            [
                "6 x 10-20 m acceleration runs",
                "Shuffle to sprint drill - 6 reps each side",
                "Base steal first-step drill - 8 reps",
                "Reaction cone drill - 6 rounds"
            ],
            strength=[
                "Reverse lunge - 3 x 8 each leg",
                "Push-up - 3 x 10",
                "Plank - 3 x 25 sec"
            ],
            cooldown=[
                "Walk and stretch calves, hips, shoulders"
            ],
            notes=[
                "Useful when you want a baseball-specific athletic day"
            ]
        ),
        format_plan(
            "Baseball Session - Position Blend",
            f"Position-support session for {baseball_position}",
            [
                "Dynamic warm-up",
                "Easy catch work"
            ],
            [
                "Footwork into throw - 8 reps each side",
                "Reaction catch drill - 10 reps",
                "Tee or soft toss contact block - 15-20 swings",
                "Short sprint change-of-direction block - 6 reps"
            ],
            strength=[
                "Med-ball scoop toss - 3 x 5 each side",
                "Band arm care - 2 rounds"
            ],
            cooldown=[
                "Arm recovery and hip mobility"
            ],
            notes=[
                "Balanced session when the athlete is not specializing too much yet"
            ]
        ),
    ]
    return choose(*plans)

def generate_rowing_plan():
    if goal_is_learning(goal) or rowing_focus == "Beginner learning":
        return format_plan(
            "Rowing Session - Learn the Basics",
            "Beginner rowing technique, rhythm, and stroke understanding",
            [
                "5-8 min easy erg or light movement",
                "Hip, ankle, and thoracic mobility",
                "Arms-only then arms+body then half-slide drill"
            ],
            [
                "3 x 5 min very easy rowing focusing on sequence",
                "Pause drill at body-over position - 3 rounds",
                "10 short technical starts focusing on leg drive and posture"
            ],
            strength=[
                "Glute bridge - 2 x 12",
                "Bird dog - 2 x 8 each side"
            ],
            cooldown=[
                "Easy paddle or easy erg 5 min",
                "Hamstring and low-back mobility"
            ],
            notes=[
                "Sequence: legs, body, arms on the drive; arms, body, legs on the recovery",
                "Stay long, tall, and controlled"
            ]
        )

    plans = [
        format_plan(
            "Rowing Session - Aerobic Endurance",
            "Technique under steady aerobic work",
            [
                "8 min easy build-up on erg or water",
                "Technique drill block"
            ],
            [
                "3 x 12 min steady rowing with 2 min easy between blocks",
                "Stroke rate controlled and smooth",
                "Focus on connection at the catch and relaxed recovery"
            ],
            strength=[
                "Bodyweight reverse lunge - 2 x 8 each leg",
                "Plank - 2 x 30 sec"
            ],
            cooldown=[
                "5 min easy paddle / erg",
                "Mobility for hamstrings, hips, thoracic spine"
            ],
            notes=[
                "Classic base session for rowers"
            ]
        ),
        format_plan(
            "Rowing Session - Power and Rate Control",
            "More pressure per stroke without losing shape",
            [
                "Easy warm-up",
                "Drills: pause drill and pick drill"
            ],
            [
                "8 x 1 min hard / 1.5 min easy",
                "Then 6 short starts of 10 strokes each",
                "Stay strong through the legs and tall through the finish"
            ],
            strength=[
                "Goblet squat - 3 x 8",
                "Single-arm row - 3 x 10 each side"
            ],
            cooldown=[
                "Easy row 5-8 min",
                "Stretch lats, glutes, hamstrings"
            ],
            notes=[
                "Useful for improving pressure application and boat speed feel"
            ]
        ),
        format_plan(
            "Rowing Session - Race Preparation",
            "Specific rowing rhythm and efficiency",
            [
                "10 min easy build-up",
                "Technical starts"
            ],
            [
                "4 x 500m controlled hard with full technical focus",
                "3 x 10 high-quality start strokes",
                "Easy paddling between efforts"
            ],
            strength=[
                "Romanian deadlift - 3 x 8",
                "Pallof press - 2 x 10 each side"
            ],
            cooldown=[
                "Easy row 5 min",
                "Mobility reset"
            ],
            notes=[
                "Do not sacrifice technical quality for raw effort"
            ]
        ),
        format_plan(
            "Rowing Session - Technique Reset",
            "A lower-stress technical day",
            [
                "Easy erg or paddle",
                "Mobility"
            ],
            [
                "Pick drill progression",
                "Pause at quarter-slide and body-over positions",
                "20-30 min easy rowing focusing on stroke length and rhythm"
            ],
            strength=[
                "Side plank - 2 x 20 sec each side",
                "Scap row / band pull-aparts - 2 x 12"
            ],
            cooldown=[
                "Easy breathing and stretching"
            ],
            notes=[
                "Very good after harder days or for developing rowers"
            ]
        ),
    ]
    return choose(*plans)

def generate_weightlifting_plan():
    if goal_is_learning(goal) or wl_focus == "Learn technique" or wl_experience == "Very new":
        return format_plan(
            "Weightlifting Session - Learn Olympic Lifting Basics",
            "Intro to positions, bar path, and confidence",
            [
                "5 min bike or row",
                "Ankle, hip, thoracic, shoulder mobility",
                "PVC / empty bar positions"
            ],
            [
                "Tall muscle snatch - 3 x 5",
                "Front squat - 4 x 5",
                "Hang power clean - 4 x 3",
                "Push press - 3 x 5",
                "Clean pull - 3 x 4"
            ],
            strength=[
                "RDL - 3 x 6",
                "Hollow hold - 3 x 20 sec"
            ],
            cooldown=[
                "Wrist, lat, hip mobility"
            ],
            notes=[
                "Prioritize positions and timing over load",
                "Olympic lifting is technical; stop sets when form drops"
            ]
        )

    plans = [
        format_plan(
            "Weightlifting Session - Snatch Emphasis",
            "Technique and speed in the snatch pattern",
            [
                "General warm-up",
                "Mobility",
                "Empty bar snatch progression"
            ],
            [
                "Snatch pull - 4 x 3",
                "Hang power snatch - 4 x 2",
                "Full snatch or power snatch - 5 x 1-2",
                "Overhead squat - 3 x 3"
            ],
            strength=[
                "Back squat - 4 x 4",
                "Romanian deadlift - 3 x 6"
            ],
            cooldown=[
                "Shoulder and ankle mobility"
            ],
            notes=[
                "Fast elbows, active turnover, stable overhead position"
            ]
        ),
        format_plan(
            "Weightlifting Session - Clean & Jerk Emphasis",
            "Leg drive, clean timing, and jerk mechanics",
            [
                "General warm-up",
                "Front rack and ankle mobility",
                "Empty bar clean + jerk prep"
            ],
            [
                "Clean pull - 4 x 3",
                "Hang clean - 4 x 2",
                "Clean & jerk - 5 x 1-2",
                "Jerk from rack - 3 x 2"
            ],
            strength=[
                "Front squat - 4 x 3-4",
                "Split squat - 3 x 6 each leg"
            ],
            cooldown=[
                "Hip flexor, quad, wrist mobility"
            ],
            notes=[
                "Strong front rack and aggressive leg drive"
            ]
        ),
        format_plan(
            "Weightlifting Session - Strength Base",
            "Build the force base behind the lifts",
            [
                "5-8 min cardio",
                "Lower-body and front rack mobility"
            ],
            [
                "Back squat - 5 x 5",
                "Push press - 4 x 5",
                "RDL - 4 x 6",
                "Barbell row - 3 x 8"
            ],
            strength=[
                "Farmer carry - 3 x 20 m",
                "Plank - 3 x 25 sec"
            ],
            cooldown=[
                "Breathing reset and mobility"
            ],
            notes=[
                "A great support day when technical lifts are not the priority"
            ]
        ),
        format_plan(
            "Weightlifting Session - Power / Speed Day",
            "Explosive quality without excessive fatigue",
            [
                "Movement prep",
                "Empty bar speed work"
            ],
            [
                "Power snatch - 5 x 2",
                "Power clean + push jerk - 5 x 2",
                "Jump squat or med-ball throw - 4 x 4"
            ],
            strength=[
                "Front squat - 3 x 3",
                "Back extension - 3 x 10"
            ],
            cooldown=[
                "Mobility for wrists, ankles, hips"
            ],
            notes=[
                "Best done fresh, not after a brutal conditioning day"
            ]
        ),
    ]
    return choose(*plans)

def generate_water_polo_plan():
    if goal_is_learning(goal) or wp_focus == "Learn fundamentals":
        return format_plan(
            "Water Polo Session - Learn the Basics",
            "Swimming, treading, ball familiarity, and simple game skills",
            [
                "200-400m easy swim",
                "Shoulder mobility",
                "Easy eggbeater practice"
            ],
            [
                "Eggbeater sets: 6 x 20 sec work / 20 sec easy",
                "Partner passing: 4 rounds of 10 passes each side",
                "Catch and lift drill: receive, lift, and control ball - 12 reps",
                "Easy shooting technique from short distance - 10-15 reps",
                "Short swim repeats: 6 x 25m controlled"
            ],
            strength=[
                "Push-up - 2 x 10",
                "Band shoulder external rotation - 2 x 12"
            ],
            cooldown=[
                "Easy swim 100-200m",
                "Shoulder and hip mobility"
            ],
            notes=[
                "For beginners, control and body position come before power"
            ]
        )

    plans = [
        format_plan(
            "Water Polo Session - Swimming Conditioning",
            "Swim fitness with polo-specific movement demands",
            [
                "300m easy swim",
                "Mobility and shoulder activation"
            ],
            [
                "8 x 50m swim at controlled hard effort",
                "6 x 25m sprint swims with good technique",
                "4 x 20 sec eggbeater holds",
                "4 x 20 sec vertical reach / blocking actions"
            ],
            strength=[
                "Pull-ups or lat pulldown - 3 x 6-8",
                "Push-up - 3 x 10",
                "Hollow hold - 3 x 20 sec"
            ],
            cooldown=[
                "Easy swim down",
                "Stretch lats, pecs, shoulders"
            ],
            notes=[
                "Great for game fitness and repeated effort ability"
            ]
        ),
        format_plan(
            "Water Polo Session - Passing and Shooting",
            "Ball control, release quality, and upper-body timing",
            [
                "200m easy swim",
                "Shoulder prep",
                "Eggbeater warm-up"
            ],
            [
                "Stationary passing - 3 rounds of 12 passes",
                "Move-and-pass drill - 10 reps each side",
                "Catch, lift, shoot drill - 12 reps",
                "Shooting from 3 spots - 5 shots each",
                "Quick-release passing game - 3 rounds"
            ],
            strength=[
                "Band shoulder work - 2 rounds",
                "Rotational med-ball throw - 3 x 5 each side"
            ],
            cooldown=[
                "Easy swim",
                "Shoulder mobility"
            ],
            notes=[
                "Stay high in the water using consistent eggbeater support"
            ]
        ),
        format_plan(
            "Water Polo Session - Game Fitness + Decision Work",
            "Conditioning with tactical pressure",
            [
                "Swim warm-up",
                "Mobility",
                "Ball warm-up"
            ],
            [
                "6 x 25m sprint + 20 sec tread combo",
                "3 rounds of passing under pressure",
                "Drive and recover drill - 8 reps each side",
                "Small-sided live play or tactical sequence block"
            ],
            strength=[
                "Split squat - 2 x 8 each leg",
                "Side plank - 2 x 20 sec each side"
            ],
            cooldown=[
                "Easy swim down",
                "Breathing and shoulder reset"
            ],
            notes=[
                "Excellent field-player option"
            ]
        ),
        format_plan(
            "Water Polo Session - Goalkeeper Skills",
            "Explosiveness, reaction, and set position",
            [
                "Easy swim",
                "Eggbeater prep",
                "Shoulder warm-up"
            ],
            [
                "6 x 20 sec strong eggbeater",
                "Lateral movement across goal - 8 reps",
                "Reaction saves / high-hand drill - 10 reps",
                "Explosive block and reset drill - 8 reps"
            ],
            strength=[
                "Push press - 3 x 5",
                "Med-ball chest pass - 3 x 5",
                "Band shoulder care - 2 rounds"
            ],
            cooldown=[
                "Easy swim",
                "Shoulder recovery"
            ],
            notes=[
                "Best when wp_role is goalkeeper"
            ]
        ),
    ]

    if wp_role == "Goalkeeper":
        return plans[-1]
    return choose(*plans[:-1])

# =========================
# MASTER PLAN SELECTOR
# =========================
def generate_plan():
    if sport == "Running":
        return generate_running_plan()
    if sport == "Gym":
        return generate_gym_plan()
    if sport == "Tennis":
        return generate_tennis_plan()
    if sport == "Baseball":
        return generate_baseball_plan()
    if sport == "Rowing":
        return generate_rowing_plan()
    if sport == "Weightlifting":
        return generate_weightlifting_plan()
    if sport == "Water Polo":
        return generate_water_polo_plan()
    return "Sport not configured yet."

# =========================
# GENERATE BUTTON
# =========================
if st.button("Generate training plan"):
    st.subheader("Your training plan")

    warning = safety_message()
    if warning:
        st.warning(warning)

    plan = generate_plan()
    st.markdown(plan)

    st.info(
        "This planner gives general training guidance and is not medical advice. "
        "If pain is sharp, worsening, or affecting normal movement, stop and seek qualified help."
    )

# =========================
# SECTION 2 — VIDEO REVIEW
# =========================
elif st.session_state.active_section == "Video Review":
    st.header("Video Review")

    st.write("Upload a sports video for a basic form review.")

    review_sport = st.selectbox(
        "Which sport is this video for?",
        ["Tennis", "Running", "Gym / strength", "Baseball", "Rowing", "Weightlifting", "Water Polo"]
    )

    review_focus = st.selectbox(
        "What do you want reviewed?",
        [
            "General technique",
            "Serve / shot mechanics",
            "Running mechanics",
            "Lifting form",
            "Movement efficiency",
            "Injury-risk cues",
        ]
    )

    uploaded_video = st.file_uploader(
        "Upload video (.mp4, .mov, .avi)",
        type=["mp4", "mov", "avi"]
    )

    if uploaded_video:
        st.success("Video uploaded.")
        st.markdown(
            f"""
### Preliminary review structure
- **Sport:** {review_sport}
- **Review focus:** {review_focus}
- **Next version recommendation:** add MediaPipe/OpenCV pipeline for pose extraction, joint angles, frame-by-frame checkpoints, and annotated feedback.
- **Current version behavior:** keep this as a review shell so the app architecture is ready without breaking your current app.
"""
        )

        st.info(
            "For now this section is structured professionally but does not yet run automated biomechanics. "
            "The architecture is here so you can plug your CV pipeline in later."
        )

# =========================
# SECTION 3 — COUNSELLING
# =========================
elif st.session_state.active_section == "Counselling":
    st.header("Tennis Counselling")
    st.write("Current first counselling function: helping a tennis player choose the most logical tournament to play.")

    c1, c2 = st.columns(2)

    with c1:
        player_ranking = st.number_input(
            "What ATP ranking does the player have? (Use 0 if unranked)",
            min_value=0,
            max_value=5000,
            value=450,
            step=1
        )
        player_region = st.selectbox(
            "Where is the player today?",
            ["South America", "North America", "Europe", "Asia", "Africa", "Oceania"]
        )
        preferred_surface = st.selectbox(
            "Preferred surface",
            ["Clay", "Hard", "Grass", "No preference"]
        )

    with c2:
        target_level = st.selectbox(
            "What tournament level is the player realistically targeting?",
            ["Best fit", "ITF", "Challenger", "ATP Tour"]
        )
        main_goal = st.selectbox(
            "Main tournament objective",
            [
                "Get into the draw",
                "Get matches and confidence",
                "Chase points",
                "Prepare for a higher tier soon",
                "Stay on preferred surface",
            ]
        )
        travel_style = st.selectbox(
            "Travel logic",
            [
                "Stay close / reduce travel",
                "Best competitive fit matters most",
                "Surface matters most",
            ]
        )

    if st.button("Generate tournament advice"):
        ranked_events = recommend_tournaments(
            player_ranking=player_ranking,
            player_region=player_region,
            preferred_surface=preferred_surface,
            target_level=target_level,
        )

        st.subheader("Best tournament fits right now")

        for event in ranked_events[:5]:
            st.markdown(
                f"""
### {event['name']}
- **Tour / level:** {event['tour']} — {event['level']}
- **City:** {event['city']}, {event['country']}
- **Surface:** {event['surface']}
- **Week starts:** {format_date(event['start_date'])}
- **Why it fits:** {event['ranking_note']}
- **Estimated direct-acceptance band:** {event['estimated_direct_acceptance_best_fit'][0]}–{event['estimated_direct_acceptance_best_fit'][1]}
- **Estimated qualifying/alternate band:** {event['estimated_qualifying_fit'][0]}–{event['estimated_qualifying_fit'][1]}
- **Travel / route note:** {event['notes']}
- **Entry note:** {entry_status_label(event)}
"""
            )
            if "withdrawal_deadline" in event:
                st.caption(f"Withdrawal deadline listed: {event['withdrawal_deadline']}")

        st.markdown("### Recommendation summary")

        if player_ranking == 0:
            st.warning(
                "An unranked player should usually prioritize ITF-level opportunities and local/regional events first."
            )
        elif player_ranking <= 120:
            st.success(
                "This ranking profile is already more naturally aligned with ATP 250 qualifying/direct-entry logic or strong Challenger scheduling."
            )
        elif player_ranking <= 300:
            st.success(
                "This profile fits Challenger scheduling best, with ATP 250 qualifying as a selective option and ITF mainly when points/confidence are needed."
            )
        elif player_ranking <= 900:
            st.info(
                "This profile is usually best served by stronger ITF scheduling and selective Challenger attempts when surface/location align."
            )
        else:
            st.info(
                "This profile should usually prioritize ITF entries and match volume before aggressively chasing Challenger events."
            )

        if main_goal == "Get into the draw":
            st.write(
                "Priority rule: choose the highest event where entry is still realistic, not the biggest-name event."
            )
        elif main_goal == "Get matches and confidence":
            st.write(
                "Priority rule: choose the tier where the player can likely win rounds, not just get in."
            )
        elif main_goal == "Prepare for a higher tier soon":
            st.write(
                "Priority rule: one level below the stretch target is often the smartest scheduling choice."
            )

        st.info(
            "This counselling engine is intentionally conservative. Exact cutoffs move week to week, so this version uses tour-level fit bands and official current tournament windows."
        )

# =========================
# SECTION 4 — PHYSIO
# =========================
elif st.session_state.active_section == "Physio":
    st.header("Physio")
    st.write("This section gives first-line conservative recovery guidance. It is not a diagnosis.")

    p1, p2 = st.columns(2)

    with p1:
        body_area = st.selectbox("Where is it hurting?", PHYSIO_BODY_AREAS)
        physio_pain = st.slider("Pain scale from 1 to 10", 1, 10, 4)
        pain_duration = st.selectbox(
            "How long has it been hurting?",
            ["Today only", "A few days", "1-2 weeks", "More than 2 weeks"]
        )

    with p2:
        symptoms = st.text_area(
            "Describe the symptoms briefly",
            placeholder="For example: sharp pain on the outside of the knee when bending, no swelling, worse after running..."
        )
        injury_mechanism = st.selectbox(
            "How did it start?",
            ["Gradually / overload", "During training", "After a match/game", "After a fall / awkward movement", "Not sure"]
        )
        uploaded_photo = st.file_uploader(
            "Upload a photo of the painful area (optional, can be implemented more deeply later)",
            type=["jpg", "jpeg", "png"]
        )

    if st.button("Generate physio guidance"):
        result = physio_guidance(body_area, physio_pain, symptoms)

        st.subheader("Initial guidance")
        st.markdown(
            f"""
- **Pain area:** {body_area}
- **Pain level:** {physio_pain}/10
- **Severity note:** {result['severity']}
- **Suggested stretch:** {result['stretch']}
- **Suggested mobility:** {result['mobility']}
- **Support advice:** {result['support']}
- **Watch closely for:** {result['watch']}
"""
        )

        if physio_pain >= 6:
            st.warning(
                "Because pain is 6 or more, training should be reduced, modified heavily, or paused until symptoms calm down."
            )

        if result["red_flag_found"] or physio_pain >= 8 or injury_mechanism == "After a fall / awkward movement":
            st.error(
                "This symptom profile has warning signs. A qualified sports physio or doctor should assess it before normal training continues."
            )
        else:
            st.info(
                "This is conservative first-aid style guidance only. If pain is worsening, sharp, or changing normal movement, stop sport and seek qualified help."
            )

        if uploaded_photo:
            st.success(
                "Photo received. In a later version, this section can use image analysis for location marking and more specific guidance."
           
