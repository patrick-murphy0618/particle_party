# analysis.py

# imports
import math
#import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from src.particle_party.renderer import *


sns.set_theme(style="ticks")

# get data from run_particle_party
def get_data(data, num_parties):

    df_parties = data

    print('----------------------------------------------------------------------------')
    print('Getting Data for Analysis (Preview below)')
    print(df_parties.head())
    print('----------------------------------------------------------------------------')
    
    # perform analysis
    analysis_manager(df_parties, num_parties)
    

'''

    

    # Basic Statistics:
    dict_basic_analysis = basic_analysis(data=pvt_moves_per_party)


    # Advanced Analysis & Calculations:
    df_data_with_distance, move_average_distance = distance_from_origin(df_parties)
    #print(df_data_with_distance)
    df_area_density = area_density(df_parties)


    # Visualizations (called from renderer.py):
    #scatter_plot(data=pvt_moves_per_party)
    histogram(data=pvt_moves_per_party)
    #linear_distance_from_origin(data=df_data_with_distance)

    dict_data = {'pvt_moves_per_party': pvt_moves_per_party,
                 'df_data_with_distance': df_data_with_distance,
                 'move_average_distance': move_average_distance
                 }
    
    combined(dict_data)

    
- Consists of Calculation functions (e.g. distance_from_origin) and Visualization functions (e.g. histogram).
    The calculation functions perform specific data manipulations or calculations, while the visualization
    functions create plots based on the data.
'''
def analysis_manager(df_parties, num_parties):


    # Pivot Tables:
    pvt_moves_per_party = moves_per_party(data=df_parties)

    path_slot = create_path_canvas()
    for i in range(1, len(df_parties) + 1):
        # Slice the dataframe to grab history up to the current point
        current_history = df_parties.iloc[:i]
        
        # Update the exact same layout slot with the new figure
        update_live_path(path_slot, current_history)
        
        # Pause for 0.2 seconds before the next point
        time.sleep(0.2)


    
    #update_live_path(path_slot=path_slot, data=df_parties)

    # Visualizations (called from renderer.py)
    histogram(data=pvt_moves_per_party, num_parties=num_parties)

    #df_data_with_distance = distance_from_origin(data=df_parties)
    #linear_distance_from_origin(data=df_data_with_distance)
    

    '''

    

    # Basic Statistics:
    dict_basic_analysis = basic_analysis(data=pvt_moves_per_party)


    # Advanced Analysis & Calculations:
    df_data_with_distance, move_average_distance = distance_from_origin(df_parties)
    #print(df_data_with_distance)
    df_area_density = area_density(df_parties)


    # Visualizations (called from renderer.py):
    #scatter_plot(data=pvt_moves_per_party)
    histogram(data=pvt_moves_per_party)
    #linear_distance_from_origin(data=df_data_with_distance)

    dict_data = {'pvt_moves_per_party': pvt_moves_per_party,
                 'df_data_with_distance': df_data_with_distance,
                 'move_average_distance': move_average_distance
                 }
    
    combined(dict_data)

    
    '''


# create pivot table that counts the number of moves the particle made at each party, returns pivot table
def moves_per_party(data):

    # Reset index to turn Party and Move into columns
    pvt_moves_per_party = data.reset_index().pivot_table(index='Party', values='Move', aggfunc='max')
    return pvt_moves_per_party
    
    
# Simple statistics, returns dictionary
def basic_analysis(data):

    min = int(data['Move'].min())
    mean = int(data['Move'].mean())
    median = int(data['Move'].median())
    max = int(data['Move'].max())

    dict_basic_analysis = {'min': min, 'mean': mean, 'median': median, 'max': max}

    return dict_basic_analysis


# calculates linear distance the particle is from the origin for each move (pythagorean theorem)
def distance_from_origin(data):

    print('')

    # Assuming 'data' is a pandas DataFrame or a dict of columns
    # 1. Convert the 'Node' column directly into a 2D numpy array
    coords = np.array(data['Node'].tolist())  # Shape will be (N, 2)

    # 2. Extract x and y columns efficiently as views/arrays
    x2 = coords[:, 0]
    y2 = coords[:, 1]

    # 3. Calculate distance from the origin (0,0)
    # You don't need np.subtract(x2, 0) since subtracting 0 doesn't change the value!
    data['distance'] = np.hypot(x2, y2)

    df_data_with_distance = data

    print("Data with Distance from Origin:")
    print(df_data_with_distance.head())
    print("")

    # Gets the average distance for each move across all Party's
    move_average_distance = data.groupby('Move')['distance'].mean()
    print("Move Average Distance from Origin:")
    print(move_average_distance.head())
    

    return df_data_with_distance, move_average_distance

'''
# Calculate the area and density
def area_density(data):

    print("")
    print("AREA:")

    import numpy as np

    # 1. Unzip the tuples into x and y coordinate lists
    x, y = zip(*data['new node'])

    # 2. Calculate the total span of the coordinates
    L = np.max(x) - np.min(x)
    H = np.max(y) - np.min(y)

    # 3. Calculate area (simply multiply the scalars)
    total_area = L * H

    # 4. Assign it to the dataframe
    data['area'] = total_area

    print(data)

    '''