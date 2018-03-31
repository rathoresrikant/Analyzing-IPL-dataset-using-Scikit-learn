#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 17:08:37 2018

@author: srikant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

deliveries = pd.read_csv('deliveries.csv')
matches = pd.read_csv('matches.csv')

print(deliveries.head(2))
print(matches.head(2))
print(len(deliveries['match_id'].unique()))  #Total number of matches

# Printing the seasons of IPL in ascending order
season = matches['season'].unique()
season.sort()
print(season)

matches.iloc[:5,:5]

# Runs scored by Shikhar Dhawan
sum(deliveries[deliveries['batsman'] == 'S Dhawan']['batsman_runs'])

# Highest run scorers in IPL
top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending = False)
top_scorers = pd.DataFrame({'batsman' : top_scorers.index, 'runs' : top_scorers.values})
top_scorers.head()

# All the teams in IPL
print(deliveries['batting_team'].unique())

# Which team has won how many matches
num_wins = matches.groupby('winner')['winner'].count().sort_values(ascending = False)
num_wins = pd.DataFrame({'winner':num_wins.index, 'wins':num_wins.values})
print(num_wins)

#Most number of deliveries bowled by a bowler in IPL
num_balls = deliveries.groupby('bowler')['bowler'].count().sort_values(ascending=False)
num_balls = pd.DataFrame({'bowler':num_balls.index, 'num_balls':num_balls.values})
print(num_balls.head())

#Top 10 wicket takers in IPL
delv_nro = deliveries[deliveries['dismissal_kind'] != 'run out']
wickets = delv_nro[delv_nro['dismissal_kind'].notnull()].groupby('bowler')['bowler'].count()
top_wicket_takers = wickets.sort_values(ascending=False)
top_wicket_takers = pd.DataFrame({'bowler' :top_wicket_takers.index, 'wickets' : top_wicket_takers.values})
print(top_wicket_takers.head(10))

#Most number of catches in IPL including wicketkeepers
catches = deliveries[deliveries['dismissal_kind'] == 'caught'].groupby('fielder')['fielder'].count()
highest_catches = catches.sort_values(ascending=False)
highest_catches = pd.DataFrame({'fielder':highest_catches.index, 'catches':highest_catches.values})
print(highest_catches.head())

#Most run outs in ipl
run_outs = deliveries[deliveries['dismissal_kind']=='run out'].groupby('fielder')['fielder'].count()
run_outs = run_outs.sort_values(ascending=False)
run_outs = pd.DataFrame({'player' : run_outs.index, 'run_outs' : run_outs.values})
print(run_outs.head())

#Most sixes in IPL
no_sixes = deliveries[deliveries['batsman_runs']==6].groupby('batsman')['batsman'].count().sort_values(ascending=False)
no_sixes = pd.DataFrame({'batsman' : no_sixes.index, 'sixes':no_sixes.values})
print(no_sixes.head(10))

#Most fours by batsman
no_fours = deliveries[deliveries['batsman_runs']==4].groupby('batsman')['batsman'].count().sort_values(ascending=False)
no_fours = pd.DataFrame({'batsman' : no_fours.index, 'fours':no_fours.values})
print(no_fours.head())

#Most doubles in IPL
no_doubles = deliveries[deliveries['batsman_runs']==2].groupby('batsman')['batsman'].count().sort_values(ascending=False)
no_doubles = pd.DataFrame({'batsman' : no_doubles.index, 'doubles':no_doubles.values})
print(no_doubles.head())

#Most three runs in IPL
most_threes = deliveries[deliveries['batsman_runs']==3].groupby('batsman')['batsman'].count().sort_values(ascending=False)
most_threes = pd.DataFrame({'batsman' : most_threes.index, 'threes':most_threes.values})
print(most_threes.head())

# Types of result in IPl
print(matches['result'].unique())

#No of no result matches in IPL
noresult = len(matches[matches['result'] == 'no result'])
print(" Number of matches having no result is",format(noresult))

#No. of tie matches in IPL.
tie = len(matches[matches['result']=='tie'])
print("In {} matches, both the team had the same score".format(tie))

#Seasonwise number of matches in IPL
swmatches = matches.groupby('season')['season'].count()
swmatches = pd.DataFrame({'season' : swmatches.index, 'matches' : swmatches.values})
print(swmatches)

#Team winning most number of tosses in IPL
tosses = matches.groupby('toss_winner')['toss_winner'].count().sort_values(ascending= False)
tosses = pd.DataFrame({'team' : tosses.index, 'tosses':tosses.values})
print(tosses.head())