Name: Notebook to Streamlit

Description: Convert the code from this repository's notebook into a Streamlit web app. Use this skill to create the Streamlit app (app.py) that replicates the functionality of the notebook.

# Notebook to Streamlit

## Goal
Build a Streamlit app ('app.py') that replicates the functionality of the notebook in this repository so Rosa can choose the best promised delivery time for a zone and time block.

## Steps to Build the Streamlit App
1. Read the notebook and find the constraints (ZONES, TIME_BLOCKS, COSTS) and the functions the app needs: delivery_times, cost_per_late_order, net_profit, best_profit.
2. Copy these into the app exactly as written. Do not change the calculations or logic, so the app gives the same results as the notebook.
3. Build the interface:
a. a dropdown for the zone, using the ZONES variable.
b. a dropdown for the time block, using the TIME_BLOCKS variable.
c. call best_promise with the selected zone, time block, promises 5 to 50 in steps of 5, COSTS, and seed = 1.
d. show the best promise and the corresponding profit. 

## Rules
a. Keep the code simple and readable, with short comments.
b. Use the same variable names as in the notebook.
c. Do not invent data or change cost values.  