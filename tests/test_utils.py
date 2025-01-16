import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Utils import (
log_normal_CLT, 
poisson_CLT, 
valid_float, 
valid_nonnegative_float, 
valid_positive_integer,
)

def test_log_normal_CLT() -> None:
    num_events = 27
    assert log_normal_CLT(0, 1, num_events) >= 0
    assert isinstance(log_normal_CLT(0, 1, num_events), float)
    assert log_normal_CLT(0, 0, num_events) == num_events

def test_poisson_CLT() -> None:
    assert poisson_CLT(27) >= 0
    assert isinstance(poisson_CLT(27), int)
    assert poisson_CLT(0) == 0

def test_valid_positive_integer() -> None:
    valid_positive_integer(27)
    with pytest.raises(TypeError):
        valid_positive_integer("abc")
    with pytest.raises(TypeError):
        valid_positive_integer(3.14)
    with pytest.raises(ValueError):
        valid_positive_integer(0)

def test_valid_nonnegative_float() -> None:
    valid_nonnegative_float(27)
    valid_nonnegative_float(0)
    valid_nonnegative_float(2.718)    
    with pytest.raises(TypeError):
        valid_nonnegative_float("abc")
    with pytest.raises(ValueError):
        valid_nonnegative_float(-5)

def test_valid_float() -> None:
    valid_float(5.0)
    valid_float(-26.35)
    valid_float(0)
    with pytest.raises(TypeError):
        valid_float("abc")
        