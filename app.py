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

def minutes_to_readable(minutes):
    if minutes < 60:
        return f"{minutes} minutes"
    hours = minutes // 60
    mins = minutes % 60
    if mins == 0:
        return f"{hours}h"
    return f"{hours}h {mins}min"

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

    return sorted(scored, key=lambda x: x["score"], reverse=True)

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

def safety_message(injury_status, pain_score):
    if injury_status == "No":
        return None
    if pain_score >= 8:
        return (
            "You reported high pain. Today's session should be replaced by rest, light mobility, "
            "and professional evaluation before returning to normal training."
        )
    if pain_score >= 5:
        return (
            "You reported moderate pain. The session below should be treated as reduced-intensity only. "
            "Avoid explosive work, hard impact, and anything that increases pain."
        )
    return (
        "You reported a minor issue. Keep intensity controlled, reduce volume slightly, "
        "and stop if symptoms increase."
    )

# =========================
# TRAINING GENERATOR FUNCTIONS
# =========================
def generate_running_plan(goal, level, injury_status, pain_score, session_time, running_focus, running_distance):
    minutes = time_to_minutes(session_time)
    category = running_distance_category(running_distance)

    if goal_is_learning(goal):
        return format_plan(
            title="Running Foundation Session",
            focus=f"Learn how to run better for {running_distance}",
            warmup=[
                "5 min brisk walk",
                "5 min easy jog",
                "Dynamic mobility: ankle circles, leg swings, hip openers",
                "2 x 20m marching drills",
            ],
            main_work=[
                "Technique block: 3 x 20m A-march",
                "Technique block: 3 x 20m skipping",
                "4 x 60m relaxed strides at controlled pace",
                "Main set: 12-20 min easy run focused on posture, cadence, and relaxed arms",
            ],
            strength=[
                "2 x 10 split squats each side",
                "2 x 10 calf raises each side",
                "2 x 30 sec front plank",
            ],
            cooldown=[
                "5 min walk",
                "Gentle calf, hip flexor, and hamstring mobility",
            ],
            notes=[
                "Focus on rhythm, posture, and relaxed shoulders.",
                "Do not force speed while learning mechanics.",
            ],
        )

    if category == "short":
        main = [
            "Drill block: 3 x 20m A-skips",
            "Drill block: 3 x 20m fast-feet build-ups",
            "4 x 60m progressive accelerations",
            choose(
                "6 x 100m at strong but controlled speed, 90 sec rest",
                "8 x 60m acceleration runs, walk-back recovery",
                "5 x 150m at 800m rhythm, 2 min rest",
            ),
        ]
        strength = [
            "3 x 5 goblet squats",
            "3 x 6 Romanian deadlifts",
            "3 x 8 calf raises",
            "2 x 20 sec hollow hold",
        ]
        focus = f"Speed / power development for {running_distance}"

    elif category == "medium":
        main = [
            "10 min easy run build-up",
            choose(
                "5 x 3 min at threshold effort, 90 sec easy jog",
                "6 x 800m at controlled pace, 2 min recovery",
                "4 x 5 min steady-hard tempo, 2 min easy jog",
            ),
        ]
        strength = [
            "3 x 8 reverse lunges each side",
            "3 x 8 step-ups each side",
            "2 x 30 sec side plank each side",
        ]
        focus = f"Tempo / aerobic support for {running_distance}"

    elif category == "long":
        long_run_time = max(45, int(minutes * 0.75))
        main = [
            f"Steady run: {minutes_to_readable(long_run_time)} at sustainable pace",
            "Finish with 4 x 20 sec controlled strides if legs still feel good",
        ]
        strength = [
            "2 x 8 split squats each side",
            "2 x 10 glute bridges",
            "2 x 30 sec plank",
        ]
        focus = f"Endurance support for {running_distance}"

    else:
        ultra_time = max(60, int(minutes * 0.80))
        main = [
            f"Main endurance run: {minutes_to_readable(ultra_time)} at very controlled conversational pace",
            "Practice fueling and hydration during the run if relevant",
            "Last 10 min: focus on calm rhythm and efficient form",
        ]
        strength = [
            "2 x 8 single-leg RDL each side",
            "2 x 10 calf raises each side",
            "2 x 30 sec dead bug hold",
        ]
        focus = f"Ultra-endurance support for {running_distance}"

    if beginner_modifier(level):
        main.insert(0, "Reduce pace emphasis and keep all reps controlled.")
    if injury_caution(injury_status):
        main = [item for item in main if "strides" not in item.lower()]

    return format_plan(
        title="Running Session",
        focus=focus,
        warmup=[
            "5-10 min easy jog or brisk walk",
            "Dynamic mobility: hips, ankles, hamstrings",
            "Running drills: march, skip, leg swings",
        ],
        main_work=main,
        strength=strength,
        cooldown=[
            "5-10 min easy walk/jog down",
            "Gentle lower-body mobility",
        ],
        notes=[
            "Keep mechanics clean even when tired.",
            "Stop if pain increases during the session.",
        ],
    )

def generate_gym_plan(goal, level, injury_status, pain_score, session_time, gym_style):
    if goal_is_learning(goal):
        return format_plan(
            title="Gym Fundamentals Session",
            focus="Learn how to train properly in the gym",
            warmup=[
                "5 min bike or treadmill walk",
                "Dynamic mobility for hips, shoulders, and ankles",
                "1 light familiarization set for each major movement",
            ],
            main_work=[
                "3 x 8 goblet squat",
                "3 x 8 dumbbell bench press",
                "3 x 8 seated row",
                "3 x 8 Romanian deadlift with light-moderate load",
            ],
            strength=[
                "2 x 10 split squat each side",
                "2 x 10 dumbbell shoulder press",
                "2 x 30 sec plank",
            ],
            cooldown=[
                "5 min easy walk",
                "Gentle mobility for quads, chest, and hips",
            ],
            notes=[
                "Prioritize correct technique over heavy load.",
                "Leave 2-3 reps in reserve on each set.",
            ],
        )

    if gym_style == "General strength":
        main = [
            "4 x 6 squat or leg press",
            "4 x 6 bench press or dumbbell press",
            "4 x 8 row variation",
            "3 x 6 Romanian deadlift",
        ]
        secondary = [
            "3 x 8 split squat each side",
            "3 x 10 hamstring curl",
            "3 x 12 face pulls",
            "2 x 30 sec plank",
        ]
        focus = "Full-body strength"

    elif gym_style == "Sport-specific strength":
        main = [
            "4 x 5 trap-bar deadlift or squat",
            "4 x 5 push press or landmine press",
            "4 x 6 pull-ups / assisted pull-ups or lat pulldown",
            "3 x 6 rear-foot elevated split squat",
        ]
        secondary = [
            "3 x 8 medicine-ball rotational throws or cable rotations",
            "3 x 10 single-leg RDL each side",
            "3 x 10 Copenhagen plank short lever or side plank",
        ]
        focus = "Athletic strength and transfer"

    else:
        main = [
            "3 x 8 squat pattern",
            "3 x 8 horizontal press",
            "3 x 10 row pattern",
            "3 x 10 hinge pattern",
        ]
        secondary = [
            "2 x 10 calf raises",
            "2 x 10 reverse lunges each side",
            "2 x 20 sec dead bug",
        ]
        focus = "Return to training with controlled load"

    if beginner_modifier(level):
        main = [item.replace("4 x", "3 x") for item in main]
    if injury_caution(injury_status):
        secondary.append("Reduce load 10-20% and avoid painful ranges")

    return format_plan(
        title="Gym Session",
        focus=focus,
        warmup=[
            "5 min easy cardio",
            "Dynamic mobility for main joints involved",
            "2 progressive warm-up sets before first compound lift",
        ],
        main_work=main,
        strength=secondary,
        cooldown=[
            "5 min easy walk",
            "Gentle mobility for worked muscle groups",
        ],
        notes=[
            "Quality reps only.",
            "Rest 60-120 sec on most sets; longer on heavy compounds.",
        ],
    )

def generate_tennis_plan(goal, level, injury_status, pain_score, session_time, tennis_focus):
    if goal_is_learning(goal):
        return format_plan(
            title="Tennis Beginner Session",
            focus="Learn how to play tennis",
            warmup=[
                "5 min light jog and side shuffles",
                "Shoulder circles, trunk rotations, ankle mobility",
                "Mini-tennis for feel and control",
            ],
            main_work=[
                "10 min forehand technique from short court",
                "10 min backhand technique from short court",
                "10 min rallying crosscourt with control target",
                "10 min serve fundamentals: toss, rhythm, and contact point",
            ],
            strength=[
                "2 x 8 split squat each side",
                "2 x 10 band rows",
                "2 x 20 sec side plank each side",
            ],
            cooldown=[
                "Easy walk and shoulder mobility",
                "Light forearm and hip stretching",
            ],
            notes=[
                "Focus on timing, balance, and clean contact.",
                "Consistency matters more than power.",
            ],
        )

    focus_map = {
        "Technique": [
            "15 min rallying with one technical cue only",
            "12 min forehand repetition block",
            "12 min backhand repetition block",
            "10 min serve rhythm work",
        ],
        "Match play": [
            "10 min controlled crosscourt patterns",
            "15 min point construction from neutral ball",
            "20 min live points with first-ball objective",
            "10 min return + first shot patterns",
        ],
        "Movement": [
            "8 x lateral recovery patterns",
            "8 x approach + recovery footwork patterns",
            "12 min live-ball movement emphasis",
            "10 min open-stance to neutral recovery drills",
        ],
        "Serve / return": [
            "15 min serve targets",
            "15 min second-serve repetition",
            "15 min return block against varied placement",
            "10 min serve + first forehand pattern",
        ],
    }

    main = focus_map.get(tennis_focus, focus_map["Technique"])

    if beginner_modifier(level):
        main.insert(0, "Reduce live intensity and prioritize basket-fed repetitions.")

    if injury_caution(injury_status):
        main = [m for m in main if "serve" not in m.lower()]

    return format_plan(
        title="Tennis Session",
        focus=f"Tennis development — {tennis_focus}",
        warmup=[
            "5 min light jog, shuffle, carioca",
            "Dynamic shoulder, hip, and thoracic mobility",
            "Mini-tennis and rhythm hitting",
        ],
        main_work=main,
        strength=[
            "2 x 8 reverse lunges each side",
            "2 x 10 band external rotations",
            "2 x 20 sec anti-rotation hold each side",
        ],
        cooldown=[
            "Walk and breathing reset",
            "Light shoulder, forearm, hip mobility",
        ],
        notes=[
            "Keep feet active before every shot.",
            "Stop if shoulder, elbow, or wrist pain rises during hitting.",
        ],
    )

def generate_baseball_plan(goal, level, injury_status, pain_score, session_time, baseball_focus):
    if goal_is_learning(goal):
        return format_plan(
            title="Baseball Fundamentals Session",
            focus="Learn how to play baseball",
            warmup=[
                "5 min jog and dynamic movement",
                "Shoulder activation and hip mobility",
                "Easy throwing progression",
            ],
            main_work=[
                "10 min throwing mechanics fundamentals",
                "10 min glove-work basics / receiving drills",
                "10 min hitting stance and swing path fundamentals",
                "10 min base running and athletic movement patterns",
            ],
            strength=[
                "2 x 10 split squat each side",
                "2 x 10 band rows",
                "2 x 20 sec plank",
            ],
            cooldown=[
                "Shoulder and forearm mobility",
                "Light lower-body stretching",
            ],
            notes=[
                "Learn rhythm and coordination before adding intensity.",
                "Do not force throwing volume early.",
            ],
        )

    focus_map = {
        "Hitting": [
            "Tee work: 4 x 8 quality swings",
            "Front toss: 4 x 6 swings",
            "Bat path / contact-point drill: 3 rounds",
            "Live timing drill or machine work: 3 rounds",
        ],
        "Throwing": [
            "Progressive throwing build-up",
            "4 x 6 position-specific throws",
            "3 x 5 crow-hop or momentum throws",
            "3 x 6 accuracy-focused throws",
        ],
        "Fielding": [
            "10 min glove presentation work",
            "4 x 6 ground-ball reps",
            "4 x 6 throw-after-field reps",
            "3 x 5 reaction reps",
        ],
        "General skills": [
            "Throwing progression",
            "Fielding fundamentals block",
            "Hitting contact block",
            "Base-running acceleration block",
        ],
    }

    main = focus_map.get(baseball_focus, focus_map["General skills"])

    return format_plan(
        title="Baseball Session",
        focus=f"Baseball development — {baseball_focus}",
        warmup=[
            "Jog, skips, and lateral movement",
            "Shoulder activation with band",
            "Hip and thoracic mobility",
        ],
        main_work=main,
        strength=[
            "3 x 8 split squat each side",
            "3 x 8 rows",
            "2 x 8 med-ball rotations or cable rotations",
        ],
        cooldown=[
            "Forearm, shoulder, and hip mobility",
            "Easy walk",
        ],
        notes=[
            "Protect the arm by keeping total throwing volume reasonable.",
            "Quality mechanics first.",
        ],
    )

def generate_rowing_plan(goal, level, injury_status, pain_score, session_time, rowing_focus):
    if goal_is_learning(goal):
        return format_plan(
            title="Rowing Beginner Session",
            focus="Learn how to row with better rhythm and sequence",
            warmup=[
                "5 min easy erg or bike",
                "Hip, ankle, and thoracic mobility",
                "Arms-only and legs-only sequence drills",
            ],
            main_work=[
                "10 min pick drill progression",
                "3 x 5 min steady rowing at controlled rate",
                "3 x 2 min pause rowing emphasizing body position",
                "5 min easy flush",
            ],
            strength=[
                "2 x 10 goblet squat",
                "2 x 10 seated row",
                "2 x 20 sec side plank each side",
            ],
            cooldown=[
                "Easy erg or walk",
                "Light posterior-chain mobility",
            ],
            notes=[
                "Legs-body-arms on the drive; arms-body-legs on the recovery.",
                "Do not rush the slide.",
            ],
        )

    focus_map = {
        "Technique": [
            "10 min pick drill progression",
            "4 x 4 min steady rowing at low stroke rate with form focus",
            "3 x 2 min pause drills",
        ],
        "Aerobic base": [
            "20-40 min continuous steady rowing",
            "5 x 1 min at slightly higher rate with full control",
        ],
        "Power": [
            "8 x 250m or 45 sec strong strokes, 75 sec easy",
            "4 x 10 power strokes from low rate",
        ],
        "Race prep": [
            "3 x 6 min at projected race rhythm, 3 min easy",
            "4 starts of 10-15 hard strokes",
        ],
    }

    main = focus_map.get(rowing_focus, focus_map["Technique"])

    return format_plan(
        title="Rowing Session",
        focus=f"Rowing development — {rowing_focus}",
        warmup=[
            "5-8 min easy erg",
            "Mobility for hips, ankles, lats, thoracic spine",
            "Progressive build strokes",
        ],
        main_work=main,
        strength=[
            "3 x 8 Romanian deadlift",
            "3 x 10 seated row",
            "2 x 30 sec hollow hold",
        ],
        cooldown=[
            "5 min easy row",
            "Hamstring, glute, and lat mobility",
        ],
        notes=[
            "Sequence and rhythm matter more than muscling each stroke.",
            "Keep the catch controlled and connected.",
        ],
    )

def generate_weightlifting_plan(goal, level, injury_status, pain_score, session_time, wl_focus):
    if goal_is_learning(goal):
        return format_plan(
            title="Weightlifting Fundamentals Session",
            focus="Learn Olympic lifting basics",
            warmup=[
                "5 min easy cardio",
                "Ankle, hip, thoracic, and wrist mobility",
                "PVC/bar-only movement prep",
            ],
            main_work=[
                "3 x 5 front squat with light load",
                "4 x 3 hang power clean with technique emphasis",
                "4 x 3 muscle snatch or overhead drill with PVC/bar",
                "3 x 5 strict press or push press technique work",
            ],
            strength=[
                "2 x 8 Romanian deadlift",
                "2 x 8 split squat each side",
                "2 x 20 sec front-rack hold or plank",
            ],
            cooldown=[
                "Easy walk",
                "Wrist, hip, and thoracic mobility",
            ],
            notes=[
                "Technique before load always.",
                "Catch positions must be stable and pain-free.",
            ],
        )

    focus_map = {
        "Snatch": [
            "5 x 2 hang snatch",
            "5 x 2 snatch pull",
            "4 x 2 overhead squat or snatch balance variation",
        ],
        "Clean & jerk": [
            "5 x 2 clean",
            "5 x 1 jerk from rack",
            "4 x 3 clean pull",
        ],
        "General Olympic lifting": [
            "4 x 2 power snatch",
            "4 x 2 power clean + jerk",
            "4 x 3 front squat",
        ],
        "Strength support": [
            "5 x 3 front squat",
            "4 x 4 push press",
            "4 x 4 pull variation",
        ],
    }

    main = focus_map.get(wl_focus, focus_map["General Olympic lifting"])

    return format_plan(
        title="Weightlifting Session",
        focus=f"Weightlifting development — {wl_focus}",
        warmup=[
            "5-8 min easy cardio",
            "Joint prep: wrists, ankles, hips, thoracic spine",
            "Bar-only technical sets",
        ],
        main_work=main,
        strength=[
            "3 x 5 Romanian deadlift or pull variation",
            "3 x 6 split squat each side",
            "2 x 30 sec overhead stability or core hold",
        ],
        cooldown=[
            "Easy walk",
            "Mobility for wrists, hips, shoulders",
        ],
        notes=[
            "Fast elbows, stable receiving positions, controlled bar path.",
            "Do not chase load if positions break down.",
        ],
    )

def generate_water_polo_plan(goal, level, injury_status, pain_score, session_time, wp_focus):
    if goal_is_learning(goal):
        return format_plan(
            title="Water Polo Beginner Session",
            focus="Learn how to play water polo",
            warmup=[
                "200m easy swim",
                "Shoulder circles and trunk rotation on deck",
                "Eggbeater basics and body-position prep",
            ],
            main_work=[
                "4 x 25m head-up swim technique",
                "4 x 30 sec eggbeater holds",
                "10 min passing mechanics and catching",
                "10 min shooting fundamentals with controlled form",
            ],
            strength=[
                "2 x 10 band external rotations",
                "2 x 10 split squat each side",
                "2 x 20 sec side plank each side",
            ],
            cooldown=[
                "100-200m easy swim",
                "Shoulder and hip mobility",
            ],
            notes=[
                "Stay tall in the water.",
                "Build shoulder volume gradually.",
            ],
        )

    focus_map = {
        "Swimming conditioning": [
            "6 x 50m moderate head-up swim, 20 sec rest",
            "6 x 25m fast swim, 30 sec rest",
            "4 x 30 sec eggbeater holds",
        ],
        "Shooting": [
            "10 min passing progression",
            "5 x 5 controlled shooting reps",
            "4 x 20 sec leg-drive + shot setup",
        ],
        "Match skills": [
            "Passing under pressure block",
            "Drive-and-recover repetitions",
            "2v2 or 3v3 tactical sequence work",
        ],
        "General development": [
            "Swimming conditioning block",
            "Eggbeater block",
            "Passing + shooting block",
            "Short tactical sequence block",
        ],
    }

    main = focus_map.get(wp_focus, focus_map["General development"])

    return format_plan(
        title="Water Polo Session",
        focus=f"Water polo development — {wp_focus}",
        warmup=[
            "200-300m easy swim",
            "Dynamic shoulder prep",
            "Ball-handling and eggbeater activation",
        ],
        main_work=main,
        strength=[
            "3 x 10 band external rotation",
            "3 x 8 push-up variation",
            "2 x 30 sec hollow hold",
        ],
        cooldown=[
            "100-200m easy swim",
            "Shoulder, chest, and hip mobility",
        ],
        notes=[
            "Shoulder health and leg drive are priorities.",
            "Stop hard throwing if shoulder pain rises.",
        ],
    )

def generate_plan(
    sport,
    goal,
    level,
    injury_status,
    pain_score,
    session_time,
    sport_inputs,
):
    if sport == "Running":
        return generate_running_plan(
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            running_focus=sport_inputs["running_focus"],
            running_distance=sport_inputs["running_distance"],
        )

    if sport == "Gym":
        return generate_gym_plan(
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            gym_style=sport_inputs["gym_style"],
        )

    if sport == "Tennis":
        return generate_tennis_plan(
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            tennis_focus=sport_inputs["tennis_focus"],
        )

    if sport == "Baseball":
        return generate_baseball_plan(
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            baseball_focus=sport_inputs["baseball_focus"],
        )

    if sport == "Rowing":
        return generate_rowing_plan(
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            rowing_focus=sport_inputs["rowing_focus"],
        )

    if sport == "Weightlifting":
        return generate_weightlifting_plan(
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            wl_focus=sport_inputs["wl_focus"],
        )

    if sport == "Water Polo":
        return generate_water_polo_plan(
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            wp_focus=sport_inputs["wp_focus"],
        )

    return "Sport not supported yet."

# =========================
# TOP NAVIGATION
# =========================
st.session_state.active_section = st.radio(
    "Choose section",
    SECTION_OPTIONS,
    index=SECTION_OPTIONS.index(st.session_state.active_section),
    horizontal=True,
)

# =========================
# SECTION 1 — TRAINING GENERATOR
# =========================
if st.session_state.active_section == "Training Generator":
    st.header("Training Generator")

    c1, c2 = st.columns(2)

    with c1:
        sport = st.selectbox("What sport do you want to train?", SPORTS)
        goal = st.selectbox("What is your goal with this sport?", COMMON_GOALS)
        level = st.selectbox("What is your level?", SKILL_LEVELS)
        training_days = st.slider("How many days do you train per week?", 1, 7, 4)

    with c2:
        injury_status = st.selectbox("Any injury or limitation?", INJURY_OPTIONS)
        pain_score = 0
        if injury_status != "No":
            pain_score = st.slider("Pain scale from 1 to 10", 1, 10, 3)

        session_time = st.selectbox(
            "How much time do you have for this session?",
            TIME_OPTIONS_ENDURANCE if sport in ["Running", "Rowing"] else TIME_OPTIONS_GENERAL,
        )

    sport_inputs = {}

    st.markdown("### Sport-specific questions")

    if sport == "Running":
        rc1, rc2 = st.columns(2)
        with rc1:
            running_focus = st.selectbox("What's the focus?", RUNNING_FOCUS_OPTIONS)
        with rc2:
            running_distance = st.selectbox(
                "Choose the event / distance",
                RUNNING_DISTANCE_MAP[running_focus]
            )
        sport_inputs["running_focus"] = running_focus
        sport_inputs["running_distance"] = running_distance

    elif sport == "Gym":
        sport_inputs["gym_style"] = st.selectbox(
            "What type of gym session do you want?",
            ["General strength", "Sport-specific strength", "Return to training"]
        )

    elif sport == "Tennis":
        sport_inputs["tennis_focus"] = st.selectbox(
            "What is the main tennis focus today?",
            ["Technique", "Match play", "Movement", "Serve / return"]
        )

    elif sport == "Baseball":
        sport_inputs["baseball_focus"] = st.selectbox(
            "What is the main baseball focus today?",
            ["General skills", "Hitting", "Throwing", "Fielding"]
        )

    elif sport == "Rowing":
        sport_inputs["rowing_focus"] = st.selectbox(
            "What is the main rowing focus today?",
            ["Technique", "Aerobic base", "Power", "Race prep"]
        )

    elif sport == "Weightlifting":
        sport_inputs["wl_focus"] = st.selectbox(
            "What is the main weightlifting focus today?",
            ["General Olympic lifting", "Snatch", "Clean & jerk", "Strength support"]
        )

    elif sport == "Water Polo":
        sport_inputs["wp_focus"] = st.selectbox(
            "What is the main water polo focus today?",
            ["General development", "Swimming conditioning", "Shooting", "Match skills"]
        )

    if st.button("Generate training session", use_container_width=True):
        safety = safety_message(injury_status, pain_score)
        if safety:
            st.warning(safety)

        plan = generate_plan(
            sport=sport,
            goal=goal,
            level=level,
            injury_status=injury_status,
            pain_score=pain_score,
            session_time=session_time,
            sport_inputs=sport_inputs,
        )

        st.subheader("Your training plan")
        st.markdown(plan)

        st.caption(
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
    else:
        st.info("Upload a file to use this review shell.")

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

    if st.button("Generate tournament advice", use_container_width=True):
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
            st.warning("An unranked player should usually prioritize ITF-level opportunities and local/regional events first.")
        elif player_ranking <= 120:
            st.success("This ranking profile is already more naturally aligned with ATP 250 qualifying/direct-entry logic or strong Challenger scheduling.")
        elif player_ranking <= 300:
            st.success("This profile fits Challenger scheduling best, with ATP 250 qualifying as a selective option and ITF mainly when points/confidence are needed.")
        elif player_ranking <= 900:
            st.info("This profile is usually best served by stronger ITF scheduling and selective Challenger attempts when surface/location align.")
        else:
            st.info("This profile should usually prioritize ITF entries and match volume before aggressively chasing Challenger events.")

        if main_goal == "Get into the draw":
            st.write("Priority rule: choose the highest event where entry is still realistic, not the biggest-name event.")
        elif main_goal == "Get matches and confidence":
            st.write("Priority rule: choose the tier where the player can likely win rounds, not just get in.")
        elif main_goal == "Prepare for a higher tier soon":
            st.write("Priority rule: one level below the stretch target is often the smartest scheduling choice.")

        if travel_style == "Stay close / reduce travel":
            st.write("Travel logic note: regional proximity should break ties between similar-fit events.")
        elif travel_style == "Surface matters most":
            st.write("Travel logic note: staying on the preferred surface should carry extra weight when two events are similarly realistic.")

        st.info(
            "This counselling engine is intentionally conservative. Exact cutoffs move week to week, "
            "so this version uses tour-level fit bands and official current tournament windows."
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

    if st.button("Generate physio guidance", use_container_width=True):
        result = physio_guidance(body_area, physio_pain, symptoms)

        st.subheader("Initial guidance")
        st.markdown(
            f"""
- **Pain area:** {body_area}
- **Pain level:** {physio_pain}/10
- **Pain duration:** {pain_duration}
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
            )
