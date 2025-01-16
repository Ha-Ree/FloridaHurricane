import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Simulation import Simulation

def test_rate_zero():
    np.random.seed(27)
    simulation = Simulation(0, 5, 7, 0, 9, 3) # Rates 0 means no hurricanes
    assert simulation.simulate(1000) == 0
    assert simulation.simulate_fast(100000000) == 0
    
