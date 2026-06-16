# main.py

from src.particle_party.config import *
from src.particle_party.engine import run_particle_party
import streamlit as st

st.title("Particle Party! 🎉")
st.write("Configure your simulation parameters below and launch the party!")

num_parties = st.number_input(
    label="Enter the number of parties: ", 
    min_value=1, 
    max_value=max_parties, 
    value=1000, 
    step=1000
)

if st.button("Start Particle Party 🚀"):
    st.write(f"Initializing simulation for {num_parties} parties...")
    
    # Run the core simulation logic
    run_particle_party(num_parties)