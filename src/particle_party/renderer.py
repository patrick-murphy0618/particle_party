# renderer.py

# imports
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import time
import pandas as pd
import math
import numpy as np
import streamlit as st


list_data = []


# src/particle_party/renderer.py
import streamlit as st
import matplotlib.pyplot as plt

def histogram(data):
    """
    Creates a matplotlib histogram and renders it on the Streamlit web page.
    """
    # 1. Your exact plotting logic remains the same
    fig, ax = plt.subplots()

    # Note: Ensure your calculation function adds the 'Move' column before this is called!
    n, bins, patches = ax.hist(data['Move'], bins=50, density=True, color='steelblue')

    ax.set_title('Probability Distribution')
    ax.set_xlabel('Moves')
    ax.set_ylabel('Probability')

    # 2. Swap out plt.show() for Streamlit's canvas renderer
    st.pyplot(fig)


def render_visuals(enriched_df):
    """
    The main layout hub that engine.py calls to build the web page.
    """
    st.title("Particle Party Tracker 🎉")
    st.write("Live visualization dashboard for particle coordinate analysis.")

    # Display the table view of your dataframe
    st.subheader("Current Particle Metrics")
    st.dataframe(enriched_df) 

    # Display your custom histogram
    st.subheader("Move Probability Density")
    histogram(enriched_df)

'''
# x-axis = bins, y-axis = probability density
def histogram(data):

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(data['Move'], bins=50, density=True, color='steelblue')

    ax.set_title('Probability Distribution')
    ax.set_xlabel('Moves')
    ax.set_ylabel('Probability')

    plt.show()

'''

# x-axis = Move #, y-axis = Linear Distance from Origin
def linear_distance_from_origin(data):
    
    fig, ax = plt.subplots()

    print(data.head())
    exit()

    distance = data['distance'].groupby(level=0).last()
    #print(distance = data['distance'])
    #exit()

    
    #print(distance)
    
    n, bins, patches = ax.hist(distance, bins=50, color='steelblue')
    #ax.plot(distance.index, distance, color='blue', linestyle='-')
    
    ax.set_title("Linear Distance from Origin")
    ax.set_xlabel("Distance")
    ax.set_ylabel("Party's")

    plt.show()


# x-axis = Party #, y-axis = Moves
def scatter_plot(data):
    
    fig, ax = plt.subplots()

    ax.scatter(data.index, data['Move'])
    
    ax.set_title("Moves per Party")
    ax.set_xlabel("Party")
    ax.set_ylabel("Moves")

    plt.show()


# x-axis = bins, y-axis = probability density
def combined(dict_data):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Histogram (Moves Per Party)
    data = dict_data['pvt_moves_per_party']
    n, bins, patches = ax1.hist(data['Move'], bins=50, density=True, color='steelblue')

    ax1.set_title('Probability Distribution')
    ax1.set_xlabel('Move')
    ax1.set_ylabel('Probability')


    # Histogram (Linear Distance from Origin)
    #data = dict_data['df_data_with_distance']
    data = dict_data['move_average_distance']
    
    #n, bins, patches = ax2.hist(distance, bins=50, color='steelblue')

    ax2.plot(data)
    
    ax2.set_title("Average Linear Distance from Origin")
    ax2.set_xlabel("Move")
    ax2.set_ylabel("Distance")

    plt.tight_layout() # Adjusts layout to prevent overlapping
    plt.show()