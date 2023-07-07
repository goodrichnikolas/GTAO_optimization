'''
EDA on NFL stats for Fantasy Football
'''
import pandas as pd
import nfl_data_py as nfl
import random

def main():
    
    df_players = nfl.import_rosters([2022])
    df_quarterbacks = df_players[df_players['position'] == 'QB']
    df_wide_receivers = df_players[df_players['position'] == 'WR']
    df_running_backs = df_players[df_players['position'] == 'RB']
    df_tight_ends = df_players[df_players['position'] == 'TE']
    df_special = df_players[df_players['position'] == 'SPEC']

    #Print all unique positions
    print(df_players['position'].unique())

    #Print the count
    print(f'Quarterbacks: {len(df_quarterbacks)}')
    print(f'Wide Receivers: {len(df_wide_receivers)}')
    print(f'Running Backs: {len(df_running_backs)}')
    print(f'Tight Ends: {len(df_tight_ends)}')
    print(f'Special Teams: {len(df_special)}')

    #Create a new df with the last name, position, and completion percentage
    df_2022 = nfl.import_pbp_data([2022])
    df_players = nfl.import_rosters([2022])
    df_teams = nfl.import_team_desc()

    #Pass attempts only
    df_pass = df_2022[df_2022['play_type'] == 'pass']

    #Merge player names with pass attempts
    df_pass = pd.merge(df_pass, df_players, how='left', left_on='passer_player_id', right_on='player_id')

    #Print all player names

    for name in df_pass['name'].unique():
        print(name)
    


    print('Done')
if __name__ == '__main__':
    main()