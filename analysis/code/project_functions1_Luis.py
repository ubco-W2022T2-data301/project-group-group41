import pandas as pd
import numpy as np

# Method chain 1

def load_and_process_matches(url_or_path_to_csv_file):
    df1 = ( pd.read_csv(url_or_path_to_csv_file).dropna(axis=0).rename(columns         {'team1':'home_team1','team2':'away_team2'}).loc[48:63]
        )
    
    team1_offense = [2.54424,2.5762,2.80437,2.65733,2.04074,3.17048,1.80298,2.89158,2.17124,2.52711,1.79236,2.71564,2.69895,2.89548,2.20264,2.8361]
team2_offense = [1.95077, 1.62507, 1.84609, 1.95825, 2.16748, 1.95504, 2.59723, 2.18629, 3.122, 2.58007, 2.78069, 2.86212, 2.20264, 1.74313, 1.74313, 2.96765]
match_winner = ['team1', 'team1', 'team1', 'team1', 'team2', 'team1', 'team1', 'team1', 'team1', 'team2', 'team1', 'team2', 'team1', 'team1', 'team1', 'team1']
offensive_difference = [0.59347, 0.95113, 0.95828, 0.69908, -0.12674, 1.21544, -0.79425, 0.70529, -0.95076, -0.05296, -0.98833, -0.14648, 0.49631, 1.15235, 0.45951, -0.13155]
stage = ['Round of 16','Round of 16','Round of 16','Round of 16','Round of 16','Round of 16','Round of 16','Round of 16','Quarter-final','Quarter-final','Quarter-final','Quarter-final','Semi-final','Semi-final','Third place decider','Final']

    
    df2 = ( df1.assign(home_offense=team1_offense, away_offense=team2_offense, winner=match_winner,offensive_diff=offensive_difference,stage=stage).drop(axis=1, columns=['date', 'league_id', 'league', 'prob1', 'prob2', 'probtie', 'proj_score1', 'proj_score2'])
          )
    
    return df2