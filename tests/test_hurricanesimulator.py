import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from HurricaneSimulator import HurricaneSimulator

def test_stddev_zero() -> None:
    """Should be exact value with no deviation"""
    test_mean = 5
    hurricane_dummy = HurricaneSimulator(10, test_mean, 0)
    assert hurricane_dummy.simulate() == np.exp(test_mean)
    
def test_invalid_rate() -> None:
    """Rates must be nonnegative"""
    test_rate_1 = "a"
    test_rate_2 = -1
    
    with pytest.raises(TypeError):
        HurricaneSimulator(test_rate_1, 1, 1)
    with pytest.raises(ValueError):
        HurricaneSimulator(test_rate_2, 1, 1)

    test_rate_3 = 0 
    test_rate_4 = 2.7 

    HurricaneSimulator(test_rate_3, 1, 1)
    HurricaneSimulator(test_rate_4, 1, 1)

    
def test_invalid_mean() -> None:
    test_rate_1 = "a"
    
    with pytest.raises(TypeError):
        HurricaneSimulator(1, test_rate_1, 1)
    
    test_rate_2 = -1
    test_rate_3 = 0 
    test_rate_4 = 2.7 
    
    HurricaneSimulator(1, test_rate_2, 1)
    HurricaneSimulator(1, test_rate_3, 1)
    HurricaneSimulator(1, test_rate_4, 1)


def test_invalid_stddev() -> None:
    test_rate_1 = "a"
    test_rate_2 = -1
    
    with pytest.raises(TypeError):
        HurricaneSimulator(1, 1, test_rate_1)
    with pytest.raises(ValueError):
        HurricaneSimulator(1, 1, test_rate_2)
    
    test_rate_3 = 0 
    test_rate_4 = 2.7 
    
    HurricaneSimulator(1, 1, test_rate_3)
    HurricaneSimulator(1, 1, test_rate_4)

def test_bad_years() -> None:
    dummy_simulator = HurricaneSimulator(1, 1, 1)
    with pytest.raises(TypeError):
        dummy_simulator.simulate_fast("abc")
    with pytest.raises(ValueError):
        dummy_simulator.simulate_fast(0)
        dummy_simulator.simulate_fast(-1)
    dummy_simulator.simulate_fast(2)
    