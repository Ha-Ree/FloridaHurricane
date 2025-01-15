# FloridaHurricane
A Python project to simulate the economic loss caused by hurricanes. 
This project was created specifically for Florida and the Gulf States, but it can be used to model any location.

## Installation 
Simply clone the directory using 

`git clone https://github.com/yourusername/FloridaHurricane.git`.

## Usage
Run the simulation using the command

`python gethurricaneloss.py [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev`

### Arguments
```
florida_landfall_rate: float
    The rate at which hurricanes hit Florida per year. Must be positive.
florida_mean: float
    The mean of the economic loss in Florida when modelled as log-normal, in billions of dollars.
florida_stddev: float
    The standard deviation of the economic loss in Florida when modelled as log-normal, in billions of dollars. Must be non-negative.
gulf_landfall_rate: float
    The rate at which hurricanes hit Gulf States per year. Must be positive.
gulf_mean: float 
    The mean of the economic loss in Gulf States when modelled as log-normal, in billions of dollars.
gulf_stddev: float 
    The standard deviation of the economic loss in Gulf States when modelled as log-normal, in billions of dollars. Must be non-negative.
Options:
-n, --num_monte_carlo_samples
    Number of samples (i.e., simulation years) to run. Default is 1000.
--use_CLT
    Use the Central Limit Theorem (CLT) to speed up the simulation. Use for large numbers (>10^6 years). Leave out to disable the CLT.
```
    
### Example Commands
Simulating a large number of years using CLT:

`python gethurricaneloss.py 1.2 2.0 0.5 1.5 1.8 0.4 -n 100000000 --use_CLT`

Simulating smaller case without CLT:

`python gethurricaneloss.py 1.2 2.0 0.5 1.5 1.8 0.4 -n 100000`

## Logging
This program includes logging to track the progress of the simulation and other relevant information. The logs are output to the terminal or can be configured to be written to a file.
Example Output:
```
python gethurricaneloss.py -n 1000 --use_CLT 1.2 2.0 0.5 1.5 1.8 0.4
2025-01-15 17:48:43,140 - __main__ - INFO - Received arguments: Namespace(florida_landfall_rate=1.2, florida_mean=2.0, florida_stddev=0.5, gulf_landfall_rate=1.5, gulf_mean=1.8, gulf_stddev=0.4, num_monte_carlo_samples=1000, use_CLT=True)
2025-01-15 17:48:43,140 - HurricaneSimulator - INFO - HurricaneSimulation initialized with rate=1.2, mean=2.0, stddev=0.5.
2025-01-15 17:48:43,142 - HurricaneSimulator - INFO - HurricaneSimulation initialized with rate=1.5, mean=1.8, stddev=0.4.
2025-01-15 17:48:43,142 - Simulation - INFO - Simulation initialised.
2025-01-15 17:48:43,142 - Simulation - INFO - Starting simulation for 1000 years.
2025-01-15 17:48:43,144 - HurricaneSimulator - INFO - Simulating 1166 hurricanes.
2025-01-15 17:48:43,144 - HurricaneSimulator - INFO - Simulating using CLT.
2025-01-15 17:48:43,145 - HurricaneSimulator - INFO - Finished simulating. Total loss: 9993.538654057857.
2025-01-15 17:48:43,146 - Simulation - INFO - Florida simulation completed. Florida loss: 9993.54 billion.
2025-01-15 17:48:43,146 - HurricaneSimulator - INFO - Simulating 1528 hurricanes.
2025-01-15 17:48:43,147 - HurricaneSimulator - INFO - Simulating using CLT.
2025-01-15 17:48:43,148 - HurricaneSimulator - INFO - Finished simulating. Total loss: 9939.138658707823.
2025-01-15 17:48:43,148 - Simulation - INFO - Gulf simulation completed. Gulf loss: 9939.14 billion.
2025-01-15 17:48:43,148 - Simulation - INFO - Simulation completed. Average loss: 19.93 billion.
2025-01-15 17:48:43,148 - __main__ - INFO - Average annual hurricane loss: $19.93 Billion
```

Thanks for reading!
