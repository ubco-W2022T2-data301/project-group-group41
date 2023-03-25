import pandas as pd

def load_and_process_wc_data(match_url, forecast_url):
    # Load match data and select columns of interest
    match_df = pd.read_csv(match_url)[['team1', 'team2', 'spi1', 'spi2', 'score1', 'score2', 'xg1', 'xg2', 'nsxg1', 'nsxg2', 'adj_score1', 'adj_score2']]

    # Load forecast data and select columns of interest
    forecast_df = pd.read_csv(forecast_url)[['team', 'spi', 'global_o', 'global_d', 'sim_wins', 'sim_ties', 'sim_losses', 'sim_goal_diff', 'goals_scored', 'goals_against', 'group_1', 'group_2', 'group_3', 'group_4', 'make_round_of_16', 'make_quarters', 'make_semis', 'make_final', 'win_league']]

    # Merge match and forecast data on team names
    merged_df = pd.merge(match_df, forecast_df, left_on='team1', right_on='team').merge(forecast_df, left_on='team2', right_on='team', suffixes=('_home', '_away'))

    # Create columns for the difference in SPI, scores, and expected goals
    merged_df['spi_diff'] = merged_df['spi1'] - merged_df['spi2']
    merged_df['score_diff'] = merged_df['score1'] - merged_df['score2']
    merged_df['xg_diff'] = merged_df['xg1'] - merged_df['xg2']
    merged_df['nsxg_diff'] = merged_df['nsxg1'] - merged_df['nsxg2']
    merged_df['adj_score_diff'] = merged_df['adj_score1'] - merged_df['adj_score2']

    # Create column for the goal difference
    merged_df['goal_diff'] = merged_df['goals_scored_home'] - merged_df['goals_scored_away']

    # Select final columns of interest
    final_df = merged_df[['team1', 'team2', 'spi_diff', 'score_diff', 'xg_diff', 'nsxg_diff', 'adj_score_diff', 'goal_diff', 'sim_wins_home', 'sim_ties_home', 'sim_losses_home', 'sim_wins_away', 'sim_ties_away', 'sim_losses_away', 'sim_goal_diff_home', 'sim_goal_diff_away']]

    return final_df

final_df