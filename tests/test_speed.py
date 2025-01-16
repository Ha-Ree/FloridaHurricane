import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Simulation import Simulation

SLOWEST_TIME = 5

def test_speed():
    test_simulation = Simulation(1.7, 2.9, 3.1, 4.2, 1.1, 0.8)
    start = time.time()
    test_simulation.simulate_fast(1000000000000000000000000000)
    test_simulation.simulate(10000)
    assert (time.time() - start) < SLOWEST_TIME