# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:42:58 2022

@author: Jake JR
"""

# Imports the required
# modules into the file

import pandas as pd
from matplotlib import pyplot as plt

# Reads the csv file and convets it into 
# a dataframe.

estate_data = pd.read_csv("EstateAgents.csv")

def get_graph_axis(return_as_frame=False):
    # Creates the graph_data variable that
    # orgainises the amount of times
    # a value is uses within a column.
    #
    # This then orders them in decending
    # order.
    
    graph_data = estate_data["County"].value_counts()
    if return_as_frame:
        frame = pd.DataFrame({
            "County": [], "Visits": []})
    x_axis, y_axis = [], []
    
    for i in graph_data:
        y_axis.append(i)
        if return_as_frame:
            frame.loc[len(frame), "Visits"] = i
            
    county_id = 0
    for i in graph_data.index:
        x_axis.append(i)
        if return_as_frame:
            frame.loc[county_id, "County"] = i
            county_id += 1
    
    if return_as_frame:
        return frame    
    else:
        return x_axis, y_axis

while True:
    try:
        # Creates the menu options which
        # will allow the user to be able
        # to navigate through the program.
        
        menu_option = "\nMain Menu:\n"
        menu_option = menu_option + "\nOption 1: Display Popularity of county"
        menu_option = menu_option + "\nOption 2: Display Graph"
        menu_option = menu_option + "\nOption 3: Exit Program"
        
        # Displays the options to the user.
        
        print(menu_option)
        
        # Gets an input from the user
        # to find out where the user
        # would like to go.
        
        user_choice = int(input("\nUser Choice: "))
        
        # Checks if the user has typed
        # in a valid option.
        
        if user_choice == 1:

            frame = get_graph_axis(True)
            
            # Displays information about what the
            # program is about to display.

            print("\nDestinations in order of popularity:\n")

            # Displays the count variable 
            # which will show the popularity
            # of each county.
            
            print(frame)
            
        elif user_choice == 2:
            while True:
                try:
                    # Creates a graph
                    # choice menu which
                    # will be displayed to the
                    # user so they can navigate
                    # the menu.
                    
                    graph_choice = "\nGraph Options:\n"
                    graph_choice = graph_choice + "\nOption 1: Bar Chart"
                    graph_choice = graph_choice + "\nOption 2: Scatter Graph"
                    graph_choice = graph_choice + "\nOption 3: Pie Chart"
                    graph_choice = graph_choice + "\nOption 4: Exit Menu" 
                    
                    graph_title = "Destination Popularity of Counties by Visits"
                    
                    
                    print(graph_choice)
                    graph_user_choice = int(input("\nUser Choice: "))
                    
                    if graph_user_choice == 1:
                        # Uses the get axis function
                        # which will return a sorted
                        # data frame which will be used
                        # to create the graph.
                        
                        x_axis, y_axis = get_graph_axis()
                        
                        # Creates the bar chart with red lines.
                        
                        plt.bar(x_axis, y_axis, color="r")
                        
                        # Sets the graph title.
                        
                        plt.title(graph_title)
                        
                        # Sets the angle of the
                        # x axis labels.
                        
                        plt.xticks(rotation=45)
                        
                        # Sets the x axis label
                        
                        plt.xlabel("County")
                        
                        # Sets the y axis label
                        
                        plt.ylabel("Visits")
                        
                        # Displays the graph to the
                        # user.
                        
                        plt.show()
                    elif graph_user_choice == 2:
                        # Uses the get axis function
                        # which will return a sorted
                        # data frame which will be used
                        # to create the graph.
                        
                        x_axis, y_axis = get_graph_axis()
                        
                        # Creates the scatter graph with red lines.
                        
                        plt.scatter(x_axis, y_axis, color="r")
                        
                        # Sets the graph title.
                        
                        plt.title(graph_title)
                        
                        # Sets the angle of the
                        # x axis labels.
                        
                        plt.xticks(rotation=45)
                        
                        # Sets the x axis label
                        
                        plt.xlabel("County")
                        
                        # Sets the y axis label
                        
                        plt.ylabel("Visits")
                        
                        # Displays the graph to the
                        # user.
                        
                        plt.show()
                    elif graph_user_choice == 3:
                        # Uses the get axis function
                        # which will return a sorted
                        # data frame which will be used
                        # to create the graph.
                        
                        x_axis, y_axis = get_graph_axis()
                            
                        # Creates a pie chart.
                        
                        plt.pie(labels=x_axis, x=y_axis, autopct="%1.0f%%")
                        
                        # Sets the graph title.
                        
                        plt.title(graph_title)
                        
                        # Sets the angle of the
                        # x axis labels.
                        
                        plt.xticks(rotation=45)
                        
                        # Displays the graph to the
                        # user.
                        
                        plt.show()
                    elif graph_user_choice == 4:
                        break
                except:
                    pass
            
        elif user_choice == 3:
            # Exits the function
            break
        
    except:
        pass
    