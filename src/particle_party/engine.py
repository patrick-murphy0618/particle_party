# engine.py

# imports
from src.particle_party.config import*
import random
import pandas as pd
from src.particle_party.analysis import get_data
import sys
#import time
#import numpy as np
import streamlit as st

# conductor function (calls parties, then calls get_data to perform analysis on the data created by parties))
def run_particle_party(num_parties):

    dict_user_input = {}

    #num_parties = int(input('How many parties? ')) #prompt user for number of parties (runs)
    if num_parties > max_parties:
        print(f"Too many parties! Max of {max_parties}")
        sys.exit()

    dict_user_input['num_parties'] = num_parties

    # run parties to create data
    print(f"\nThe particles have arrived at the parties!")
    
    df_parties = parties(dict_user_input)
    print(f"\nDone!")

    # analysis gets dataframe
    get_data(data=df_parties, num_parties=num_parties)


# main function that creates data (calls particle_path for each party, creates dataframe of all parties and their moves))
def parties(user_input):
    
    # extract user inputs
    parties = user_input['num_parties']

    dict_parties = {} # ALL data

    # 1. BEFORE your loop starts, initialize the progress bar
    progress_bar = st.progress(0)

    # Run each party (calls particle_path, creates dataframe)
    for party in range(1, parties+1):

        per = int(round((party/parties)*100,0))
        print(f"Tracking path data: Progress...{per}%", end="\r", flush=True)
        
        # 2. Calculate a float between 0.0 and 1.0 for Streamlit's progress bar
        progress_float = (party) / parties
        
        # 3. Update the bar in real time
        progress_bar.progress(progress_float)
        
        # Set initial conditions (starting position)
        x0, y0 = 0, 0 # starting position

        # main loop
        list_visited_nodes = particle_path(visited_nodes=[(x0, y0)]) # returns a list of tuples
        dict_parties[party] = list_visited_nodes
        
    # Create a dictionary of Series, then concat
    df_parties = pd.concat({party: pd.Series(moves, name="Node") for party, moves in dict_parties.items()}, axis=0)

    # Name the index levels for clarity
    df_parties.index.names = ['Party', 'Move']

    # Convert Series to DataFrame if you prefer the look
    df_parties = df_parties.to_frame()
    
    return df_parties
    
    
# particle path (returns dict_path, a dictionary of all of the particles moves during the party)
def particle_path(visited_nodes):
    
    if len(visited_nodes) == 1:
        move = 0
    
    current_node = visited_nodes[move]


    while True:

        current_x, current_y = current_node[0], current_node[1]

        node_neg_x = (current_x-1, current_y) # Check if particle has already been to the node in the -x direction
        node_pos_x = (current_x+1, current_y) # Check if particle has already been to the node in the +x direction
        node_neg_y = (current_x, current_y-1) # Check if particle has already been to the node in the -y direction
        node_pos_y = (current_x, current_y+1) # Check if particle has already been to the node in the +y direction

        surrounding_nodes = [node_neg_x, node_neg_y, node_pos_x, node_pos_y]

        set_visited_nodes = set(visited_nodes)

        # Rebuild B, keeping only items NOT in A
        available_nodes = [item for item in surrounding_nodes if tuple(item) not in set_visited_nodes]

        # is the party over?
        num_options = int(len(available_nodes)) # How many positions can the particle move to?
        if num_options == 0: # No place to move!
            break
            
        else: # The particle has option(s) to move

            new_node = random.choice(available_nodes) # Pick a random direction from the possible options
            visited_nodes.append(new_node)

        current_node = new_node
        move = move+1

    # returns all moves the particle made during the party (this is the particles path)
    return visited_nodes # This is a list of tuples
        

