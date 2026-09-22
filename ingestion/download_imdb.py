import requests
from pathlib import Path

BASE_URL = "https://datasets.imdbws.com/"

FILES = [
    "title.basics.tsv.gz",
    "title.ratings.tsv.gz"
]

OUTPUT_DIR = Path("data/raw/imdb")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for filename in FILES:
    url = BASE_URL + filename
    output_file = OUTPUT_DIR / filename

    print(f"Downloading {filename}...")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)

    print(f"Saved: {output_file}")

print("IMDb download complete.")