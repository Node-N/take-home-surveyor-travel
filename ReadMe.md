# Take Home Problem: Surveyor Travel

## Brief

A mobile surveyor is looking for a system to optimise the order that she
visits the many sites on her job list. She has a list of locations with
their coordinates. It is up to you to create a solution in Python (making
use of appropriate libraries) to take the list and create a new list with
the order of where she should go to minimise the total distance she has to
travel. As she is mobile, she is not worried about a start location, or
time constraints at this point. However, the script needs to complete within
one minute on a normal laptop with a reasonably good solution.

## Solution  
This is the travelling salesman problem without the constraint of returning to the beginning. Using the NetworkX library, we can calculate an approximation of the shortest path using Christofides algorithm. I interpreted "reasonably good solution" as meaning it was okay to use an approximation, which grants us a significant decrease in the computation required. With Christofides algorithm we are guaranteed to be within 3/2 of the optimal solution. 

## Instructions

### Setup
Make sure you are setup with a fairly recent version of Python.

Install the required dependencies : `pip install -r requirements.txt`

### Run unit tests

`pytest`
