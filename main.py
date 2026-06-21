# main.py

from src.particle_party.config import *
from src.particle_party.engine import run_particle_party
import streamlit as st

st.title("Particle Party! 🎉")
st.write("A Python-based Monte Carlo simulation that sends a single particle on a random path through an unbounded Cartesian grid. The particle continues its party until it becomes trapped by its own path. **Party on!**")

#===============================================================================================

# Run a single party to show sample paths:
st.divider() # Optional: Adds a visual line to separate sections
st.header("One Particle, One Party 🕺")
st.write("In this simulation, a single particle starts at the origin (0,0) and moves in one of four cardinal directions (up, down, left, right) with equal probability. The particle continues to move until it becomes trapped by its own path, at which point the party is over. Each run of the simulation represents one party, and we can analyze the paths taken by the particle across multiple parties.")

if st.button("Start the Party! 🚀"):
    st.write(f"Initializing sample simulation for a single party...")
    
    # Run the core simulation logic
    run_particle_party(1)

#===============================================================================================

# Run simluation for 5 parties to show sample paths
st.divider() # Optional: Adds a visual line to separate sections
st.header("5 Party Simulation 🕺")
st.write("Let's see how the particle's journey unfolds across 5 different parties! Each party represents a new run of the simulation, where the particle starts fresh at the origin and takes a random path until it becomes trapped. This will give us a glimpse into the variety of paths the particle can take and how it interacts with its own path across multiple parties.")
if st.button("Run 5 Parties 🚀"):
    st.write(f"Initializing simulation for 5 parties...")

    run_particle_party(5)

#===============================================================================================

# Run the full simulation when the button is clicked
st.divider() # Optional: Adds a visual line to separate sections
st.header("Full Simulation 🕺")
st.write("Now it's time to get the full picture! You can specify the number of parties (runs) you want to simulate. The more parties you run, the more data we have to analyze the behavior of the particle across different paths. Let's see how the particle's journey unfolds across multiple parties!")

# Full Simulation Logic
num_parties = st.number_input(
    label="Enter the number of parties: ", 
    min_value=1, 
    max_value=max_parties, 
    value=1000, 
    step=1000
)

if st.button("Run Full Simulation 🚀"):
    st.write(f"Initializing simulation for {num_parties} parties...")
    
    # Run the core simulation logic
    run_particle_party(num_parties)

#===============================================================================================

# Math
st.divider() # Optional: Adds a visual line to separate sections
st.header("Mathematical Foundations 🕺")
st.write("The Particle Party simulation is grounded in the mathematical concept of a **self-avoiding random walk**. In this model, a particle moves randomly on a grid but cannot revisit any point it has already occupied. The simulation continues until the particle becomes trapped by its own path, meaning it has no valid moves left. This creates a fascinating interplay between randomness and constraint, leading to complex and often surprising paths as the particle navigates the grid. By analyzing the data from multiple parties, we can gain insights into the behavior of self-avoiding walks and their applications in various fields such as physics, biology, and computer science.")