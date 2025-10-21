# CECS 427: Game Theory

#### Martin Silva (#030854159), Zachary Padilla (#033497475)

## Dependencies
Required Libraries:
- networkx
- pandas
- matplotlib
- scipy

In order to run this project via git:

```
~/: git clone https://github.com/zachfpadilla/CECS-427-Game-Theory
~/: cd CECS-427-Game-Theory/

### Optionally ###
~/CECS-427-Game-Theory/: python3 -m venv .venv
~/CECS-427-Game-Theory/: source .venv/bin/activate
(.venv) ~/CECS-427-Game-Theory/: pip install networkx, pandas, matplotlib, scipy
```

```
~/CECS-427-Game-Theory/: python3 ./traffic_analysis.py -h

usage: traffic_analysis.py [-h] digraph_file n initial final [--plot]

Python application that handles Girvan-Newman graph partitioning, edge removal, homophily/balance verification, and visualization.

positional arguments:
  digraph_file            Path to the input graph file in .gml format
  n                       An integer representing the number of vehicles
  initial                 An integer representing the initial node
  final                   An integer representing the final node

options:
  --plot                  Plots the output of the command
```

## Usage Instructions
* ``--plot`` outputs an image of the plot to a new window.

## Description of Implementation
- All instructions were followed as listed—interpretations were made where needed.

## Examples of Commands and Outputs
``python ./traffic_analysis.py traffic.gml 4 0 3 --plot``
```
```
