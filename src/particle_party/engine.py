
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import time
import pandas as pd
import math
import numpy as np


list_data = []

def party(particle):

    #list_dir = ['Up', 'Down', 'Left', 'Right']
    x0, y0 = 0, 0 # starting position
    #node_0 = tuple((x0, y0))
    #arr_nodes = [node_0]
    arr_nodes = np.array([x0, y0])
    dict_party = {}
    

    plt.ioff()  # Turn on interactive mode

    fig, ax = plt.subplots()

    x_data, y_data = [], []
    line, = ax.plot(x_data, y_data, 'r-')
    ax.set_facecolor('black')
    fig.canvas.manager.set_window_title(f'Particle Party! Particle {particle}')

    node_current = (x0, y0)
    node_num = 0
    while True:

        if node_num == 0:
            plt.plot(x0, y0, marker='H', markersize=8, color='dodgerblue')
        
        list_options = []
        node_left = tuple((node_current[0]-1, node_current[1]))
        if node_left not in arr_nodes:
            dir = 'Left'
            list_options.append(node_left)

        node_right = tuple((node_current[0]+1, node_current[1]))
        if node_right not in arr_nodes:
            dir = 'Right'
            list_options.append(node_right)

        node_up = tuple((node_current[0], node_current[1]+1))
        if node_up not in arr_nodes:
            dir = 'Up'
            list_options.append(node_up)

        node_down = tuple((node_current[0], node_current[1]-1))
        if node_down not in arr_nodes:
            dir = 'Down'
            list_options.append(node_down)


        num_options = int(len(list_options))
        if num_options == 0:

            #List_NumNodes.append(node_num)
            plt.plot(node_current[0], node_current[1], marker='X', markersize=8, color='red')
            fig.canvas.draw()
            fig.canvas.flush_events() # Process GUI events
            
            #print(f'Partys Over! Moves: {node_num}')
            time.sleep(1)
            plt.close()
            break
            
        else:

            new_node = tuple(random.choice(list_options))
            arr_nodes.append(new_node)

            new_node_x = new_node[0]
            new_node_y = new_node[1]
            if new_node_x > 0 and new_node_y > 0:
                quad = 1
            elif new_node_x < 0 and new_node_y > 0:
                quad = 2
            elif new_node_x < 0 and new_node_y < 0:
                quad = 3
            elif new_node_x > 0 and new_node_y < 0:
                quad = 4
            else:
                quad = 0
            
           

            current_x, current_y = node_current[0], node_current[1]
            new_x, new_y = new_node[0], new_node[1]

            dist_from_origin = math.sqrt(new_y**2+new_x**2)

            dict_party[node_num] = {'current node': node_current, 'options': num_options, 'direction': dir, 'new node': new_node, 'quadrant': quad, 'distance': dist_from_origin}
            list_data.append(dict_party)

            plt.plot(new_x, new_y, marker='o', markersize=4, color='white')
            plt.plot([current_x, new_x], [current_y, new_y], color='lime', linestyle='-', linewidth=2)
            

            # Update the plot line
            line.set_xdata(x_data)
            line.set_ydata(y_data)

            # Rescale axes if needed (optional)
            ax.relim()
            ax.autoscale_view()

            # Redraw the canvas
            fig.canvas.draw()
            fig.canvas.flush_events() # Process GUI events

            plt.pause(.0001) # Pause for a short duration to see the update

        node_current = new_node
        node_num = node_num+1

    plt.ioff() # Turn off interactive mode
    plt.show() # Display the final plot (optional)


def statistics(list_numnodes):

    num_parties = len(list_numnodes)
    max_moves = max(list_numnodes)
    min_moves = min(list_numnodes)
    avg_moves = int(sum(list_numnodes)/num_parties)

    print(f'Parties: {num_parties}\nMin: {min_moves}\nAvg: {avg_moves}\nMax: {max_moves}')

df_data = pd.DataFrame(list_data)
df_data = df_data.T



# Entry Point
def initialize():
    parties = int(input('How many parties? '))
    for particle in range(1, parties+1):
        party(particle=particle)

# main.py
if __name__ == "__main__":
    # This allows you to still run this file directly if you want
    initialize()