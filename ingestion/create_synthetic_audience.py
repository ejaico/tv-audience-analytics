from pathlib import Path
import numpy as np
import pandas as pd


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "imdb_tv_programs.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "synthetic"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# Configuration
# --------------------------------------------------

RANDOM_SEED = 42

NUM_HOUSEHOLDS = 1000
NUM_SESSIONS = 25000

rng = np.random.default_rng(RANDOM_SEED)


# --------------------------------------------------
# Load IMDb programs
# --------------------------------------------------

print("Reading IMDb TV programs...")

titles = pd.read_csv(INPUT_FILE)

titles = titles[
    [
        "tconst",
        "primaryTitle",
        "genres",
        "startYear",
        "runtimeMinutes",
        "averageRating",
    ]
].copy()


# --------------------------------------------------
# Prepare title information
# --------------------------------------------------

titles["genres"] = titles["genres"].fillna("Unknown")

titles["primary_genre"] = (
    titles["genres"]
    .str.split(",")
    .str[0]
    .fillna("Unknown")
)


# --------------------------------------------------
# Create households
# --------------------------------------------------

print("Creating synthetic households...")

household_ids = [
    f"HH{number:05d}"
    for number in range(1, NUM_HOUSEHOLDS + 1)
]

age_bands = [
    "18-24",
    "25-34",
    "35-44",
    "45-54",
    "55+",
]

genders = [
    "Female",
    "Male",
]

income_bands = [
    "Under $50K",
    "$50K-$99K",
    "$100K-$149K",
    "$150K+",
]

markets = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Dallas",
    "Atlanta",
]

audience = pd.DataFrame(
    {
        "household_id": household_ids,
        "age_band": rng.choice(
            age_bands,
            size=NUM_HOUSEHOLDS,
        ),
        "gender": rng.choice(
            genders,
            size=NUM_HOUSEHOLDS,
        ),
        "income_band": rng.choice(
            income_bands,
            size=NUM_HOUSEHOLDS,
        ),
        "market": rng.choice(
            markets,
            size=NUM_HOUSEHOLDS,
        ),
    }
)


# --------------------------------------------------
# Generate viewing sessions
# --------------------------------------------------

print("Generating synthetic viewing sessions...")

# Assign each viewing event to a household.
# Sampling with replacement allows households to have
# multiple viewing events.

selected_households = rng.choice(
    household_ids,
    size=NUM_SESSIONS,
)

selected_titles = rng.choice(
    titles["tconst"],
    size=NUM_SESSIONS,
)


session_dates = pd.date_range(
    start="2026-01-01",
    end="2026-08-31",
    freq="D",
)

selected_dates = rng.choice(
    session_dates,
    size=NUM_SESSIONS,
)

selected_times = rng.integers(
    low=0,
    high=24 * 60,
    size=NUM_SESSIONS,
)

platforms = rng.choice(
    ["Linear", "Streaming"],
    size=NUM_SESSIONS,
    p=[0.40, 0.60],
)

devices = rng.choice(
    [
        "Smart TV",
        "Connected TV",
        "Mobile",
        "Tablet",
        "Desktop",
    ],
    size=NUM_SESSIONS,
    p=[0.40, 0.30, 0.10, 0.08, 0.12],
)


viewing_minutes = rng.integers(
    low=5,
    high=121,
    size=NUM_SESSIONS,
)


sessions = pd.DataFrame(
    {
        "household_id": selected_households,
        "viewing_date": (
            pd.to_datetime(selected_dates)
            + pd.to_timedelta(selected_times, unit="m")
        ),
        "tconst": selected_titles,
        "platform_type": platforms,
        "viewing_minutes": viewing_minutes,
        "device_type": devices,
    }
)

# --------------------------------------------------
# Create viewing sequence
# --------------------------------------------------

sessions = sessions.sort_values(
    ["household_id", "viewing_date"]
).reset_index(drop=True)

sessions["viewing_sequence"] = (
    sessions.groupby("household_id").cumcount() + 1
)

# --------------------------------------------------
# Add title information
# --------------------------------------------------

sessions = sessions.merge(
    titles,
    on="tconst",
    how="left",
)


# --------------------------------------------------
# Add household attributes
# --------------------------------------------------

sessions = sessions.merge(
    audience,
    on="household_id",
    how="left",
)


# --------------------------------------------------
# Add network
# --------------------------------------------------

streaming_providers = [
    "Netflix",
    "Prime Video",
    "Disney+",
    "HBO Max",
    "Paramount+",
]

linear_networks = [
    "NBC",
    "CBS",
    "ABC",
    "FOX",
    "ESPN",
]

sessions["network"] = np.where(
    sessions["platform_type"] == "Streaming",
    rng.choice(
        streaming_providers,
        size=NUM_SESSIONS,
    ),
    rng.choice(
        linear_networks,
        size=NUM_SESSIONS,
    ),
)


# --------------------------------------------------
# Create session IDs
# --------------------------------------------------

sessions["session_id"] = [
    f"S{number:07d}"
    for number in range(1, len(sessions) + 1)
]


# --------------------------------------------------
# Simulate advertising exposure
# --------------------------------------------------

sessions["ad_exposed"] = rng.choice(
    [0, 1],
    size=NUM_SESSIONS,
    p=[0.65, 0.35],
)


campaign_ids = [
    "CMP001",
    "CMP002",
    "CMP003",
]

sessions["campaign_id"] = np.where(
    sessions["ad_exposed"] == 1,
    rng.choice(
        campaign_ids,
        size=NUM_SESSIONS,
    ),
    None,
)


# --------------------------------------------------
# Select final columns
# --------------------------------------------------

sessions = sessions[
    [
        "session_id",
        "household_id",
        "viewing_date",
        "viewing_sequence",
        "tconst",
        "primaryTitle",
        "genres",
        "primary_genre",
        "platform_type",
        "network",
        "market",
        "age_band",
        "gender",
        "income_band",
        "viewing_minutes",
        "device_type",
        "ad_exposed",
        "campaign_id",
    ]
]


# --------------------------------------------------
# Save
# --------------------------------------------------

output_file = (
    OUTPUT_DIR
    / "synthetic_audience_viewing.csv"
)

sessions.to_csv(
    output_file,
    index=False,
)


# --------------------------------------------------
# Results
# --------------------------------------------------

print()
print("Synthetic audience dataset created.")
print(f"Saved to: {output_file}")
print(f"Rows: {len(sessions):,}")
print(f"Columns: {len(sessions.columns):,}")
print()
print(sessions.head())