# FloridaHurricane
A Python project to simulate the economic loss caused by hurricanes. 
This project was created specifically for Florida and the Gulf States, but it can be used to model any location.

## Installation 
Simply clone the directory using 

`git clone https://github.com/Ha-Ree/FloridaHurricane.git`.

## Usage
Run the simulation using the command

`python gethurricaneloss.py [options] florida_landfall_rate florida_mean florida_stddev gulf_landfall_rate gulf_mean gulf_stddev`

### Arguments
```
florida_landfall_rate: float
    The rate at which hurricanes hit Florida per year. Must be positive.
florida_mean: float
    The mean of the economic loss in Florida when modeled as log-normal, in billions of dollars.
florida_stddev: float
    The standard deviation of the economic loss in Florida when modeled as log-normal, in billions of dollars. Must be non-negative.
gulf_landfall_rate: float
    The rate at which hurricanes hit Gulf States per year. Must be positive.
gulf_mean: float 
    The mean of the economic loss in Gulf States when modeled as log-normal, in billions of dollars.
gulf_stddev: float 
    The standard deviation of the economic loss in Gulf States when modeled as log-normal, in billions of dollars. Must be non-negative.
Options:
-n, --num_monte_carlo_samples
    Number of samples (years) to run. Default is 1000.
--fast
    Speeds up the process by using the Poisson additive property and the Central Limit Theorem (CLT). 

    This option should be used for any simulation with a high number of years and can handle cases beyond 10,000,000,000,000,000,000,000,000 (10^25) with no difficulties.
```
    
### Example Commands
Simulating a large number of years using fast mode:

`python gethurricaneloss.py -n 10000000000000000000000000 --fast 1.2 2.0 0.5 1.5 1.8 0.4`

Simulating smaller case:

`python gethurricaneloss.py -n 100000 1.2 2.0 0.5 1.5 1.8 0.4`

## Logging
This program includes logging to track the progress of the simulation and other relevant information. The logs are output to the terminal or can be configured to be written to a file.

For debug logging, simply change `level=logging.INFO` to `level=logging.DEBUG` in `gethurricaneloss.py`.

Example fast output:
```
python gethurricaneloss.py 1.2 2.0 0.5 1.5 1.8 0.4 -n 10000000000000000000000000 --fast
2025-01-16 11:13:38,873 - __main__ - INFO - Received arguments: Namespace(florida_landfall_rate=1.2, florida_mean=2.0, florida_stddev=0.5, gulf_landfall_rate=1.5, gulf_mean=1.8, gulf_stddev=0.4, num_monte_carlo_samples=10000000000000000000000000, fast=True)
2025-01-16 11:13:38,873 - __main__ - INFO - Starting simulation for 10000000000000000000000000 years.
2025-01-16 11:13:38,873 - HurricaneSimulator - INFO - HurricaneSimulation initialised with rate=1.2, mean=2.0, stddev=0.5.
2025-01-16 11:13:38,873 - HurricaneSimulator - INFO - HurricaneSimulation initialised with rate=1.5, mean=1.8, stddev=0.4.
2025-01-16 11:13:38,873 - Simulation - INFO - Simulation initialised.
2025-01-16 11:13:38,873 - HurricaneSimulator - INFO - Simulating 1.1999999999997466e+25 hurricanes.
2025-01-16 11:13:38,873 - HurricaneSimulator - INFO - Finished simulating. Total loss: 1.0047476985752347e+26.
2025-01-16 11:13:38,873 - Simulation - INFO - Florida simulation completed. Florida loss: 100474769857523468329811968.00 billion.
2025-01-16 11:13:38,873 - HurricaneSimulator - INFO - Simulating 1.4999999999995798e+25 hurricanes.
2025-01-16 11:13:38,873 - HurricaneSimulator - INFO - Finished simulating. Total loss: 9.830257293284754e+25.
2025-01-16 11:13:38,880 - Simulation - INFO - Gulf simulation completed. Gulf loss: 98302572932847542391013376.00 billion.
2025-01-16 11:13:38,881 - Simulation - INFO - Simulation completed. Average loss: 19.88 billion.
2025-01-16 11:13:38,881 - __main__ - INFO - Average annual hurricane loss: 19.8777342790371 Billion
```
Example non-fast output:
```
python gethurricaneloss.py 1.2 2.0 0.5 1.5 1.8 0.4 -n 100000
2025-01-16 11:17:44,665 - __main__ - INFO - Received arguments: Namespace(florida_landfall_rate=1.2, florida_mean=2.0, florida_stddev=0.5, gulf_landfall_rate=1.5, gulf_mean=1.8, gulf_stddev=0.4, num_monte_carlo_samples=100000, fast=False)
2025-01-16 11:17:44,665 - __main__ - INFO - Starting simulation for 100000 years.
2025-01-16 11:17:44,673 - HurricaneSimulator - INFO - HurricaneSimulation initialised with rate=1.2, mean=2.0, stddev=0.5.
2025-01-16 11:17:44,674 - HurricaneSimulator - INFO - HurricaneSimulation initialised with rate=1.5, mean=1.8, stddev=0.4.
2025-01-16 11:17:44,675 - Simulation - INFO - Simulation initialised.
2025-01-16 11:17:46,768 - __main__ - INFO - Average annual hurricane loss: 19.90647341204799 Billion
```
Example debugging output:
```
python gethurricaneloss.py 1.2 2.0 0.5 1.5 1.8 0.4 -n 1000 
2025-01-16 11:20:12,749 - __main__ - INFO - Received arguments: Namespace(florida_landfall_rate=1.2, florida_mean=2.0, florida_stddev=0.5, gulf_landfall_rate=1.5, gulf_mean=1.8, gulf_stddev=0.4, num_monte_carlo_samples=1000, fast=False)
2025-01-16 11:20:12,749 - __main__ - INFO - Starting simulation for 1000 years.
2025-01-16 11:20:12,751 - HurricaneSimulator - INFO - HurricaneSimulation initialised with rate=1.2, mean=2.0, stddev=0.5.
2025-01-16 11:20:12,751 - HurricaneSimulator - INFO - HurricaneSimulation initialised with rate=1.5, mean=1.8, stddev=0.4.
2025-01-16 11:20:12,751 - Simulation - INFO - Simulation initialised.
2025-01-16 11:20:12,755 - Simulation - DEBUG - Average after 99 years: 22.00068164369586
2025-01-16 11:20:12,758 - Simulation - DEBUG - Average after 199 years: 21.278324352927676
2025-01-16 11:20:12,763 - Simulation - DEBUG - Average after 299 years: 20.90803167245218
2025-01-16 11:20:12,766 - Simulation - DEBUG - Average after 399 years: 20.393659673460686
2025-01-16 11:20:12,771 - Simulation - DEBUG - Average after 499 years: 20.46502802610955
2025-01-16 11:20:12,773 - Simulation - DEBUG - Average after 599 years: 20.532009764851153
2025-01-16 11:20:12,777 - Simulation - DEBUG - Average after 699 years: 20.34503826463575
2025-01-16 11:20:12,780 - Simulation - DEBUG - Average after 799 years: 20.379597763717364
2025-01-16 11:20:12,784 - Simulation - DEBUG - Average after 899 years: 20.39953403651511
2025-01-16 11:20:12,789 - Simulation - DEBUG - Average after 999 years: 20.037955677224577
2025-01-16 11:20:12,789 - __main__ - INFO - Average annual hurricane loss: 20.017917721547352 Billion
```

## TODO
Testing for logs

Thanks for reading!
