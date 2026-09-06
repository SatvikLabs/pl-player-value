# Premier League Player Market Value Predictor ⚽📊

A data science project exploring whether a player's performance and characteristics in one Premier League season can help predict their **market value in the following season**.

## Why I'm Building This

I love football, and I want to learn data science by working on problems I actually care about.

Instead of building another generic ML project, I'm using Premier League player data to investigate how performance, age, previous market value, and other factors relate to how the football market values players.

The goal isn't just to build a model that gives a number.

I want to understand **why the model makes its predictions, how reliable those predictions are, and whether the patterns we find actually hold up when tested on future seasons.**

## Core Question

> **Can information from a player's Year N Premier League season help us predict their market value in Year N+1?**

A secondary question:

> **Does having more historical Premier League data improve our ability to predict future player values?**

## Current Approach

The basic prediction structure is:

**Year N performance & characteristics → Year N+1 market value**

For example:

**2023/24 performance → 2024/25 market value**

The project uses chronological evaluation rather than randomly mixing seasons, so the model is tested on future data it has not seen during training.

## Dataset

The main dataset comes from the `transfermarkt-datasets` project and contains historical football data sourced from Transfermarkt.

The data is stored locally in **DuckDB** and queried using SQL before being brought into Python for analysis and machine learning.

### Current data being used

* Premier League appearances
* Minutes played
* Goals
* Assists
* Yellow cards
* Red cards
* Player market valuations

More features may be added later if they improve the quality of the analysis.

## Data Structure

The raw appearance data contains individual player-match records.

For modeling, these are aggregated into:

> **One player + one Premier League season = one observation**

Example:

| Player         | Season  | Appearances | Minutes | Goals | Assists |
| -------------- | ------- | ----------: | ------: | ----: | ------: |
| Example Player | 2023/24 |          35 |   2,900 |    16 |       9 |

This gives us a consistent Year N observation that can be connected to the player's Year N+1 market value.

## Initial Dataset Boundary

For the main prediction model, we plan to include players who have played in the Premier League for **at least two seasons**.

Players with only one Premier League season may be analyzed separately if the data supports it.

## Methodological Principles

A few rules are being established early in the project:

* Use **player IDs**, rather than player names, when joining datasets.
* Use actual Premier League appearances to establish whether a player participated in a Premier League season.
* Do not assume a `GB1` label in the valuation table automatically means the player was playing in the Premier League at that point.
* Use **Year N information only** when predicting Year N+1 value.
* Avoid data leakage.
* Evaluate models chronologically to better simulate real-world prediction.
* Investigate missing data before deciding whether it should be removed or recovered.

## Project Status

**V0.1 — Data Foundation & Methodology**

Currently working on:

* Understanding the Transfermarkt dataset
* Building the Premier League player-season dataset
* Defining the prediction target
* Establishing data-quality rules
* Preparing the data for machine learning

Modeling and evaluation will be added after the dataset and methodology are properly established.
