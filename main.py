# main.py

from src.particle_party.config import *
from src.particle_party.engine import run_particle_party
import streamlit as st

st.title("Particle Party! 🎉")
st.write("A Python-based Monte Carlo simulation that sends a single particle on a random path through an unbounded Cartesian grid. The particle continues its party until it becomes trapped by its own path. **Party on!**")
st.divider() # Optional: Adds a visual line to separate sections

# Mechanics and Sample Parties:
st.header("One Particle, One Party 🕺")
st.write("In this simulation, a single particle starts at the origin (0,0) and moves in one of four cardinal directions (up, down, left, right) with equal probability. The particle continues to move until it becomes trapped by its own path, at which point the party is over. Each run of the simulation represents one party, and we can analyze the paths taken by the particle across multiple parties.")

if st.button("Start the Party! 🚀"):
    st.write(f"Initializing sample simulation for {sample_parties} parties...")
    
    # Run the core simulation logic
    run_particle_party(sample_parties)



# Full Simulation Logic
num_parties = st.number_input(
    label="Enter the number of parties: ", 
    min_value=1, 
    max_value=max_parties, 
    value=1000, 
    step=1000
)

if st.button("Start Full Simulation 🚀"):
    st.write(f"Initializing simulation for {num_parties} parties...")
    
    # Run the core simulation logic
    run_particle_party(num_parties)