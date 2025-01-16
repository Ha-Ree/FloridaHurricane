from unittest.mock import patch
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Simulation import Simulation

EPSILON = 1e-6

"""
This file is ensuring that the right functions are being called and that, 
given some 'random' numbers, we are recieving the correct outputs. No unit
testing is done with real randomness to ensure it cannot ever fail by chance.
"""

def test_random_loss_generation_slow():
    with patch('numpy.random.normal') as mock_normal, \
        patch('numpy.random.poisson') as mock_poisson, \
        patch('numpy.random.lognormal') as mock_lognormal:
        
        mock_normal.return_value = 3.14
        mock_poisson.return_value = [2]
        mock_lognormal.return_value = [89.29]
        
        simulator = Simulation(3, 1, 10, 5, 9, 6.6)
        
        assert abs(simulator.simulate(100) - 89.29*2*2) < EPSILON
        mock_normal.assert_not_called()
        mock_poisson.assert_any_call(3, 1)
        mock_poisson.assert_any_call(5, 1)
        mock_lognormal.assert_any_call(1, 10, 1)
        mock_lognormal.assert_any_call(9, 6.6, 1)
   
def test_random_loss_generation_fast():
    with patch('numpy.random.normal') as mock_normal, \
        patch('numpy.random.poisson') as mock_poisson, \
        patch('numpy.random.lognormal') as mock_lognormal:
        
        mock_normal.return_value = 3.14
        mock_poisson.return_value = [2]
        mock_lognormal.return_value = [89.29]
        
        simulator = Simulation(3, 1, 10, 5, 9, 6.6)     
        assert abs(simulator.simulate_fast(100) - 3.14*2/100) < EPSILON
        mock_normal.assert_any_call(300, np.sqrt(300))
        mock_normal.assert_any_call(500, np.sqrt(500))
        mean = np.exp(1 + (10 ** 2) / 2)*3
        stddev = np.sqrt(3 * (np.exp(10 ** 2) - 1) * np.exp(2 * 1 + 10 ** 2))
        mock_normal.assert_any_call(mean , stddev)
        mock_poisson.assert_not_called()
        mock_lognormal.assert_not_called()
        
def test_random_loss_generation_fast_under_100():
    with patch('numpy.random.normal') as mock_normal, \
        patch('numpy.random.poisson') as mock_poisson, \
        patch('numpy.random.lognormal') as mock_lognormal:
        
        mock_normal.return_value = 3.14
        mock_poisson.return_value = [2]
        mock_lognormal.return_value = [89.29]
        
        simulator = Simulation(3, 1, 10, 5, 9, 6.6)     
        assert abs(simulator.simulate_fast(10) - 3.14*2/10) < EPSILON
        mock_poisson.assert_called()
        