# Client Report - [Baseball Data SQL/Python
__Lucas Soto__

## Elevator pitch
####The data that I analyzed this time is compund by all the information recorded for many years about the  Major baseball League. The data is divided in different tables adn in this case I used three of these tables to make my analysis.  
### GRAND QUESTION 1
#### Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

|    | playerid   |   yearid | schoolid   | teamid   |   salary |
|---:|:-----------|---------:|:-----------|:---------|---------:|
|  0 | lindsma01  |     2014 | idbyuid    | CHA      |  4000000 |
|  1 | lindsma01  |     2012 | idbyuid    | BAL      |  3600000 |
|  2 | lindsma01  |     2011 | idbyuid    | COL      |  2800000 |
|  3 | lindsma01  |     2013 | idbyuid    | CHA      |  2300000 |
|  4 | lindsma01  |     2010 | idbyuid    | HOU      |  1625000 |
|  5 | stephga01  |     2001 | idbyuid    | SLN      |  1025000 |
|  6 | stephga01  |     2002 | idbyuid    | SLN      |   900000 |
|  7 | stephga01  |     2003 | idbyuid    | SLN      |   800000 |
|  8 | stephga01  |     2000 | idbyuid    | SLN      |   550000 |
|  9 | lindsma01  |     2009 | idbyuid    | FLO      |   410000 |



### GRAND QUESTION 2 A
#### Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.


##### TECHNICAL DETAILS

|    | playerid   |   yearid |   Hits |   Batting |   average_bat |
|---:|:-----------|---------:|-------:|----------:|--------------:|
|  0 | snowch01   |     1874 |      1 |         1 |             1 |
|  1 | baldwki01  |     1884 |      1 |         1 |             1 |
|  2 | oconnfr01  |     1893 |      2 |         2 |             1 |
|  3 | gumbebi01  |     1893 |      1 |         1 |             1 |
|  4 | mccafsp01  |     1889 |      1 |         1 |             1 |




### GRAND QUESTION 2 B
#### Use the same query as above, but only include players with more than 10 “at bats” that year. Print the top 5 results.

|    | playerid   |   yearid |   Hits |   Batting |   average_bat |
|---:|:-----------|---------:|-------:|----------:|--------------:|
|  0 | nymanny01  |     1974 |      9 |        14 |      0.642857 |
|  1 | carsoma01  |     2013 |      7 |        11 |      0.636364 |
|  2 | altizda01  |     1910 |      6 |        10 |      0.6      |
|  3 | johnsde01  |     1975 |      6 |        10 |      0.6      |
|  4 | silvech01  |     1948 |      8 |        14 |      0.571429 |







### GRAND QUESTION 2 C
#### Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.


|    | playerid   |   Hits |   Batting |   average_bat |
|---:|:-----------|-------:|----------:|--------------:|
|  0 | cobbty01   |   4189 |     11436 |      0.366299 |
|  1 | barnero01  |    860 |      2391 |      0.359682 |
|  2 | hornsro01  |   2930 |      8173 |      0.358497 |
|  3 | jacksjo01  |   1772 |      4981 |      0.355752 |
|  4 | meyerle01  |    513 |      1443 |      0.355509 |






### GRAND QUESTION 3
#### Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to visualize the comparison. Provide the visualization and its description.
 
####Answer: 
##### It is interesting to obvserve in the chart that the New york Yankees have won more games in the long of the history when it is not an older team as  the Chicago Sox. It is clear that the Yankees have been always a better team winning more than 80 wames each year while the Chicago Sox are below the 80 games in repetly occations. 

##### Chart

![](chart3.png)

### CODE APENDIX
```python 
import pandas as pd
import numpy as np
import altair as alt
#%%
import sys
!{sys.executable} -m pip install datadotworld

#%%
import datadotworld as dw


#%%

# %%
#  
question1 = '''
SELECT s.yearid, c.schoolid, s.teamid,
    c.playerid, s.salary  
FROM salaries as s, collegeplaying as c
    #JOIN collegeplaying as c ON s.playerid = c.playerid
Where c.schoolid= "byu"
GROUP by s.salary
ORDER BY s.salary DESC
LIMIT 10
'''

q1=dw.query('byuidss/cse-250-baseball-database', question1).dataframe

print(q1.to_markdown())


# %%
## What means with at least one atbat? 
# Why I am getting just one row? 
question2a = '''
SELECT
    playerid, yearid,h as Hits, ab as Batting,
    (h /ab) as average_bat
FROM batting 
WHERE ab >= 1
ORDER BY average_bat DESC
LIMIT 5

'''

q2=dw.query('byuidss/cse-250-baseball-database', question2a).dataframe

print(q2.to_markdown())
# %%

question2b = '''
SELECT
    playerid, yearid,h as Hits, ab as Batting,
    (h  /ab ) as average_bat
FROM batting 
WHERE ab >= 10
ORDER BY average_bat DESC
LIMIT 5

'''

q2b=dw.query('byuidss/cse-250-baseball-database', question2b).dataframe

print(q2b.to_markdown())

# %%

question2c = '''
SELECT
    playerid, yearid, h as Hits, ab as Batting,
    avg(h/ab) as average_bat
FROM batting as b
WHERE b.ab >= 100
GROUP BY  playerid
ORDER BY average_bat DESC
LIMIT 5

'''

q2c=dw.query('byuidss/cse-250-baseball-database', question2c).dataframe

print(q2c.to_markdown())

# %%

question3 = '''
SELECT
    yearid, teamid, name, w as Wins_Games, divwin as Divition_Win, l as Lost_Games
FROM teams 
WHERE teamid = "NYA"
    OR teamid = "CHA"
'''

q3=dw.query('byuidss/cse-250-baseball-database', question3).dataframe
print(q3.to_markdown())
#%%

chart=alt.Chart(q3).mark_line().encode(
    alt.X('yearid',axis=alt.Axis(format= 'd',title= "Years")),
    alt.Y('Wins_Games', axis=alt.Axis(title="Games Won in History")),
    color='teamid'
).properties(title= "The Yankes Won More Games in History than the White Sox")
yrule = (
    alt.Chart().mark_rule(strokeDash=[12, 6], size=2).encode(y=alt.datum(80)))

final=chart + yrule
final
# %%

```