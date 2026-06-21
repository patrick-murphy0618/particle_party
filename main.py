# main.py

from src.particle_party.config import *
from src.particle_party.engine import run_particle_party
import streamlit as st

st.title("Particle Party! 🎉")
st.write("A Python-based Monte Carlo simulation that sends a single particle on a random path. The particle continues its party until it becomes trapped by its own path. **Party on!**")

# Mechanics and Sample Parties:
if st.button("Run Sample Parties 🚀"):
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