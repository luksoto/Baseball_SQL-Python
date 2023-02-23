
# %%
import pandas as pd 
import altair as alt
import numpy as np
import sqlite3

# %%
sqlite_file = 'lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)
# %%
# See the tables in the database
table = pd.read_sql_query(
    "SELECT * FROM sqlite_master WHERE type='table'",
    con)
print(table.filter(['name']))
print('\n\n')
# 8 is collegeplaying
#print(table.sql[8])
#%%

fullpull=pd.read_sql_query(
'''
SELECT bp.yearid, sum(ab) as ab, sum(h) as h,
    sum(g) as games, count(DISTINCT bp.playerid) as num_players, 
    asf.gp, asf.gameid
FROM BattingPost as bp
JOIN AllstarFull as asf
    ON  bp.playerid = asf.playerid AND
        bp.yearid = asf.yearid
WHERE bp.yearid > 1999
    AND gp == 0
GROUP BY bp.yearid
ORDER BY bp.yearid
''',
con)
#%%

bp = pd.read_sql_query(
'''
SELECT *
FROM battingpost
WHERE yearid IN (2006,2017)
''', con)

alst = pd.read_sql_query(
'''
SELECT *
FROM allstarfull
WHERE yearid IN ( 2006,2007)
''', con)
# %%
bp_noals = (bp.merge(
        alst.filter(['playerID', 'yearID', "GP"]), 
        on = ['playerID', 'yearID'])
    .query('GP == 0'))
#%%

##Using .groupby(), agg(), and .reset_index() lets recreate the year 2017 line. We can use 'sum' and 'nunique' in our .agg() method.

bp_noals.groupby('yearID').agg(
    count_games=("AB", "size"),
    ab=("AB","sum"),
    h=("H","sum"),
    players=("playerID","nunique")).reset_index()
# %%
fullpull