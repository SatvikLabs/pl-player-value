import duckdb

con = duckdb.connect("data/transfermarkt-datasets.duckdb")

# # prem players:
# df = con.execute("""
#     SELECT player_id,
#     date, 
#     market_value_in_eur,
#     current_club_name,
#     player_club_domestic_competition_id,
#     FROM player_valuations
#     WHERE player_club_domestic_competition_id = 'GB1'
#     ORDER BY date DESC
#     LIMIT 20
# """).df()

# print(df)
# print("\nColumns:")
# print(df.columns.tolist())


# # appearances:
# df = con.execute("""
#     SELECT *
#     FROM appearances
#     LIMIT 10
# """).df()

# print(df)
# print("\nColumns:")
# print(df.columns.tolist())


# # appearances by competition:
# df = con.execute("""
#     SELECT
#         competition_id,
#         MIN(date) AS first_date,
#         MAX(date) AS last_date,
#         COUNT(*) AS appearances
#     FROM appearances
#     GROUP BY competition_id
#     ORDER BY appearances DESC
# """).df()

# print(df)

# # no of seasons/years we have data for:

# df = con.execute("""
#     SELECT
#         EXTRACT(YEAR FROM date) AS year,
#         COUNT(*) AS appearances
#     FROM appearances
#     WHERE competition_id = 'GB1'
#     GROUP BY year
#     ORDER BY year
# """).df()

# print(df)

# # creating a column "season":

# df = con.execute("""
#     SELECT
#         *,
#         CASE
#             WHEN EXTRACT(MONTH FROM date) >= 8
#              THEN CONCAT(EXTRACT(YEAR FROM date), '/', EXTRACT(YEAR FROM date) + 1)
#             ELSE CONCAT(EXTRACT(YEAR FROM date) - 1, '/', EXTRACT(YEAR FROM date))
#         END AS season
#     FROM appearances
#     WHERE competition_id = 'GB1'
# """).df()

# print(df)

# turning match rows -> one row per player per season;

df = con.execute("""
    SELECT
        player_id,
        player_name,

        CASE
            WHEN EXTRACT(MONTH FROM date) >= 8
                THEN CONCAT(EXTRACT(YEAR FROM date), '/', EXTRACT(YEAR FROM date) + 1)
            ELSE CONCAT(EXTRACT(YEAR FROM date) - 1, '/', EXTRACT(YEAR FROM date))
        END AS season,

        COUNT(*) AS appearances,
        SUM(minutes_played) AS minutes,
        SUM(goals) AS goals,
        SUM(assists) AS assists,
        SUM(yellow_cards) AS yellow_cards,
        SUM(red_cards) AS red_cards

    FROM appearances
    WHERE competition_id = 'GB1'

    GROUP BY
        player_id,
        player_name,
        season

    ORDER BY season, player_name
""").df()

print(df.head(20))
print(df.shape)

df.to_csv("data/pl_player_season_stats.csv", index=False)

df = con.execute("""
    SELECT
        player_id,
        date,
        market_value_in_eur,
        current_club_name
    FROM player_valuations
    WHERE player_id = 14221
    ORDER BY date
""").df()

print(df)

df = con.execute("""
    SELECT
        EXTRACT(YEAR FROM date) AS year,
        COUNT(*) AS valuations
    FROM player_valuations
    WHERE player_club_domestic_competition_id = 'GB1'
    GROUP BY year
    ORDER BY year
""").df()

print(df)

df = con.execute("""
    SELECT
        date,
        market_value_in_eur,
        player_id,
        current_club_name
    FROM player_valuations
    WHERE player_club_domestic_competition_id = 'GB1'
    ORDER BY date
    LIMIT 30
""").df()

print(df)

df = con.execute("""
    SELECT
        date,
        market_value_in_eur,
        player_id,
        current_club_name
    FROM player_valuations
    WHERE player_club_domestic_competition_id = 'GB1'
      AND date >= '2012-01-01'
    ORDER BY date
    LIMIT 30
""").df()

print(df)