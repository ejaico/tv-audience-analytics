# TV Audience & Campaign Analytics Platform

I created a personal analytics project to demonstrate how a modern data workflow can transform public and synthetic viewing data into business-facing analytical insights and a Power BI dashboard.  The project combines hands-on exposure to **Python, DuckDB, dbt Core, SQL, Parquet, and Power BI** to move from data ingestion and transformation through analytical modeling and visualization.  I used public datasets from IMDb and Nielsen to provide source data for TV ratings and viewing data, and created a synthetic viewing dataset of hypothetical 1,000 random households.

The primary focus is not the technology itself, but how the resulting data can be used to answer business questions about **viewing behavior, audience affinity, viewer journeys, and campaign reach**.

> **Portfolio focus:** Modern analytics workflow + analytical modeling + business-facing BI + data storytelling

---

## Power BI Analytical Story

I organized the dashboard as a four-page analytical journey, moving from broad viewing patterns toward increasingly specific audience and campaign questions.

### 1. Audience Overview — What is happening?

A high-level view of viewing activity across time, programs, genres, platforms, and audience characteristics.  Key elements include:

- Viewing Hours over time
- Top Programs by viewing hours
- Viewing by Genre
- Viewing by Platform type
- Viewing by Age band

### 2. Viewer Journey — How are viewers behaving?

Examines genre-to-genre transitions to understand how viewing behavior changes as audiences move from one type of content to another.  Key elements include:

- Overall genre viewing
- Genre transition counts
- Top genre transitions
- Genre-to-genre transition matrix

### 3. Audience Affinity — Who is watching what?

Analyzes genre preferences and audience composition across demographic and audience segments.  Key elements include:

- Audience affinity by segment and genre
- Genre composition by audience segment
- Audience composition by age and gender
- Viewing hours by audience segment

### 4. Campaign Reach & Measurement — How could audience insights be applied?

Uses simulated campaign exposure data to show how audience analytics could be extended into campaign reach and cross-platform measurement.  Key elements include:

- Total campaign reach
- Linear and streaming reach
- Cross-platform reach
- Reach by audience segment
- Campaign exposure frequency

The four pages are designed to tell a connected story: **What is happening → How are viewers behaving → Who is watching what → How could those insights be applied?**

> **Important:** Campaign reach and exposure metrics are simulated and illustrative. They are not causal estimates of advertising effectiveness and do not represent proprietary IMDb, Nielsen, or client data.

---

## Data & Workflow

The project follows a simplified modern analytics workflow:

**Public Data + Synthetic Data → Python Ingestion → DuckDB → dbt Transformations → Analytical Data Models → Curated Parquet Outputs → Power BI Dashboard**

### Data Sources

**IMDb**

Public IMDb datasets provide television program metadata and ratings used to enrich the viewing data.

**Nielsen**

A small sample of publicly available Nielsen Top 10 television viewing data is included to provide real-world television viewing context.  The public Nielsen data are documented separately in:

`docs/public_tv_data_source.md`

**Synthetic Audience Data**

Household-level viewing and audience data are generated specifically for this project. The synthetic data allow the project to demonstrate audience segmentation, sequential viewing behavior, platform usage, and campaign exposure concepts without using proprietary audience-level data.

---

## Analytical Model

The dbt project organizes the data into staging models and reporting-oriented fact and dimension models.

### Staging Models

Staging models prepare source data for downstream analysis:

- `stg_imdb_tv_programs`
- `stg_public_tv_viewing`
- `stg_synthetic_viewing`

### Reporting Models

Dimension tables include:

- `dim_audience`
- `dim_campaign`
- `dim_date`
- `dim_market`
- `dim_platform`
- `dim_title`

Fact and analytical tables include:

- `fact_viewing_session`
- `fact_public_viewing`
- `fct_genre_transitions`

This structure provides reporting-ready analytical datasets for the Power BI layer.

---

## Analytical Concepts

The project demonstrates several analytical techniques commonly used in BI and audience analytics:

- Audience segmentation
- Genre affinity analysis
- Viewing behavior analysis
- Sequential viewing and genre transitions
- Cross-platform reach
- Campaign exposure frequency
- KPI development
- Interactive filtering and segmentation
- Analytical data modeling
- Data validation and consistency checks

The campaign section is intentionally presented as an illustrative measurement framework, rather than as a claim of advertising effectiveness.

---

## Technology Stack

The project represents **hands-on exposure to a modern analytics workflow**, rather than production-level data engineering experience.

| Technology | Role |
|---|---|
| **Python** | Data ingestion and synthetic data generation |
| **DuckDB** | Local analytical database |
| **SQL** | Data transformation and analysis |
| **dbt Core** | Analytical modeling and transformation workflow |
| **Parquet** | Curated analytical data outputs |
| **Power BI** | Business-facing analysis, visualization, and storytelling |
| **Git / GitHub** | Version control and project documentation |

---

## Repository Structure

- `data/`
  - `exports/parquet/` — Curated analytical datasets used for reporting
  - `processed/` — Processed source data
  - `raw/` — Raw source data, excluded from the repository

- `dbt_tv_analytics/`
  - `tv_audience_analytics/`
    - `models/staging/` — Source preparation models
    - `models/marts/` — Reporting-oriented analytical models
    - `scripts/` — dbt-related utility scripts

- `docs/`
  - `public_tv_data_source.md` — Documentation for the public Nielsen data

- `ingestion/`
  - `download_imdb.py` — Downloads public IMDb source files
  - `create_imdb_tv_data.py` — Creates the processed TV program dataset
  - `create_public_tv_data.py` — Creates the public TV viewing dataset
  - `create_synthetic_audience.py` — Generates synthetic audience and viewing data

- `scripts/`
  - `load_data_to_duckdb.py` — Loads prepared data into DuckDB

- `export_genre_transitions.py` — Exports the genre transition analytical dataset

- `requirements.txt` — Python dependencies

- `README.md` — Project documentation

Large raw source files, local databases, logs, and generated dbt artifacts are excluded from the repository.

---

## Data Limitations

This project is designed as a portfolio demonstration, with the following limitations:

- Household-level audience data are synthetic.
- Campaign exposure data are synthetic.
- Campaign metrics are illustrative and are not causal effectiveness estimates.
- The public Nielsen data represent a small sample rather than a complete dataset.
- Public Nielsen streaming and linear metrics are not treated as directly interchangeable.
- The project does not use proprietary Nielsen or client audience data.
- The workflow is intended to demonstrate analytics and BI concepts rather than production-scale data engineering.

---

## Project Focus

This project was built to strengthen familiarity with how modern analytics workflows connect to established BI practices.  The goal was to move beyond creating individual reports and gain hands-on exposure to the broader process of:

**ingesting data → transforming data → modeling analytical datasets → validating results → building business-facing dashboards → communicating insights**

The resulting dashboard brings those pieces together into a single analytical story focused on television audiences, viewing behavior, and campaign measurement.