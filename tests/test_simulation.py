import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Simulation import Simulation

# Most input validation cases done in test_cli and test_hurricanesimulator

def test_rate_zero() -> None:
    np.random.seed(27)
    simulation = Simulation(0, 5, 7, 0, 9, 3) # Rates 0 means no hurricanes
    assert simulation.simulate(1000) == 0
    assert simulation.simulate_fast(100000000) == 0
    