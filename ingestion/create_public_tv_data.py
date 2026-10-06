from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "public_tv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# Nielsen public data
#
# Source:
# https://www.nielsen.com/data-center/top-ten/
#
# The records below represent a small, documented
# sample of Nielsen's publicly available Top 10
# streaming and linear TV data.
#
# Streaming and linear measurements are kept in
# separate metric columns because they are different
# audience measures.
# --------------------------------------------------

records = [

    # ------------------------------------------------
    # Streaming TV
    # Reporting period: Aug. 31 - Sep. 6, 2026
    # ------------------------------------------------

    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Reacher",
        "rank": 1,
        "platform_type": "Streaming",
        "network_or_provider": "Prime Video",
        "viewers_000s": None,
        "minutes_viewed_millions": 1246,
        "household_rating": None,
        "number_of_episodes": 30,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "The Big Bang Theory",
        "rank": 2,
        "platform_type": "Streaming",
        "network_or_provider": "HBO Max",
        "viewers_000s": None,
        "minutes_viewed_millions": 1071,
        "household_rating": None,
        "number_of_episodes": 281,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Beauty in Black",
        "rank": 3,
        "platform_type": "Streaming",
        "network_or_provider": "Netflix",
        "viewers_000s": None,
        "minutes_viewed_millions": 1058,
        "household_rating": None,
        "number_of_episodes": 40,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Ted Lasso",
        "rank": 4,
        "platform_type": "Streaming",
        "network_or_provider": "Apple TV",
        "viewers_000s": None,
        "minutes_viewed_millions": 899,
        "household_rating": None,
        "number_of_episodes": 39,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "The Whisper Man",
        "rank": 5,
        "platform_type": "Streaming",
        "network_or_provider": "Netflix",
        "viewers_000s": None,
        "minutes_viewed_millions": 863,
        "household_rating": None,
        "number_of_episodes": 1,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Lioness",
        "rank": 6,
        "platform_type": "Streaming",
        "network_or_provider": "Paramount+",
        "viewers_000s": None,
        "minutes_viewed_millions": 805,
        "household_rating": None,
        "number_of_episodes": 22,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Death of the Pastor's Wife",
        "rank": 7,
        "platform_type": "Streaming",
        "network_or_provider": "Netflix",
        "viewers_000s": None,
        "minutes_viewed_millions": 796,
        "household_rating": None,
        "number_of_episodes": 3,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Outer Banks",
        "rank": 8,
        "platform_type": "Streaming",
        "network_or_provider": "Netflix",
        "viewers_000s": None,
        "minutes_viewed_millions": 762,
        "household_rating": None,
        "number_of_episodes": 50,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Bluey",
        "rank": 9,
        "platform_type": "Streaming",
        "network_or_provider": "Disney+",
        "viewers_000s": None,
        "minutes_viewed_millions": 760,
        "household_rating": None,
        "number_of_episodes": 154,
    },
    {
        "viewing_period": "2026-08-31 to 2026-09-06",
        "program_name": "Star Wars: The Mandalorian and Grogu",
        "rank": 10,
        "platform_type": "Streaming",
        "network_or_provider": "Disney+",
        "viewers_000s": None,
        "minutes_viewed_millions": 727,
        "household_rating": None,
        "number_of_episodes": 1,
    },

    # ------------------------------------------------
    # Linear TV
    # Reporting period: Sep. 7 - Sep. 13, 2026
    # ------------------------------------------------

    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "NBC SUNDAY NIGHT FOOTBALL – COWBOYS VS. GIANTS",
        "rank": 1,
        "platform_type": "Linear",
        "network_or_provider": "NBC",
        "viewers_000s": 25661,
        "minutes_viewed_millions": None,
        "household_rating": 12.2,
        "number_of_episodes": None,
    },
    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "NBC NFL WED SPECIAL – SEAHAWKS VS. PATRIOTS",
        "rank": 2,
        "platform_type": "Linear",
        "network_or_provider": "NBC",
        "viewers_000s": 25094,
        "minutes_viewed_millions": None,
        "household_rating": 11.8,
        "number_of_episodes": None,
    },
    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "FOX NFL SUNDAY – NATIONAL (4:47PM)",
        "rank": 3,
        "platform_type": "Linear",
        "network_or_provider": "FOX",
        "viewers_000s": 20346,
        "minutes_viewed_millions": None,
        "household_rating": 8.7,
        "number_of_episodes": None,
    },
    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "SUNDAY NIGHT NFL PRE-KICK",
        "rank": 4,
        "platform_type": "Linear",
        "network_or_provider": "NBC",
        "viewers_000s": 19379,
        "minutes_viewed_millions": None,
        "household_rating": 8.8,
        "number_of_episodes": None,
    },
    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "CBS NFL NATIONAL (4:25PM)",
        "rank": 5,
        "platform_type": "Linear",
        "network_or_provider": "CBS",
        "viewers_000s": 18598,
        "minutes_viewed_millions": None,
        "household_rating": 8.0,
        "number_of_episodes": None,
    },
    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "NFL MELBOURNE GAME – 49ERS VS. RAMS",
        "rank": 6,
        "platform_type": "Linear",
        "network_or_provider": "NETFLIX",
        "viewers_000s": 18519,
        "minutes_viewed_millions": None,
        "household_rating": 7.9,
        "number_of_episodes": None,
    },
    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "NBC NFL WED PRE-KICK",
        "rank": 7,
        "platform_type": "Linear",
        "network_or_provider": "NBC",
        "viewers_000s": 16458,
        "minutes_viewed_millions": None,
        "household_rating": 8.0,
        "number_of_episodes": None,
    },
    {
        "viewing_period": "2026-09-07 to 2026-09-13",
        "program_name": "CBS NFL – REGIONAL (1:05PM)",
        "rank": 8,
        "platform_type": "Linear",
        "network_or_provider": "CBS",
        "viewers_000s": 14096,
        "minutes_viewed_millions": None,
        "household_rating": 6.2,
        "number_of_episodes": None,
    },
]


# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

df = pd.DataFrame(records)


# --------------------------------------------------
# Add source information
# --------------------------------------------------

df["source_name"] = "Nielsen"

df["source_url"] = (
    "https://www.nielsen.com/data-center/top-ten/"
)


# --------------------------------------------------
# Reorder columns
# --------------------------------------------------

df = df[
    [
        "viewing_period",
        "program_name",
        "rank",
        "platform_type",
        "network_or_provider",
        "viewers_000s",
        "minutes_viewed_millions",
        "household_rating",
        "number_of_episodes",
        "source_name",
        "source_url",
    ]
]


# --------------------------------------------------
# Save CSV
# --------------------------------------------------

output_file = OUTPUT_DIR / "public_tv_viewing.csv"

df.to_csv(output_file, index=False)


# --------------------------------------------------
# Display results
# --------------------------------------------------

print()
print("Public TV dataset created successfully.")
print(f"Saved to: {output_file}")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")
print()
print(df.to_string(index=False))