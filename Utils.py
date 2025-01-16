import numpy as np
import logging

logger = logging.getLogger(__name__)

def log_normal_CLT(mean: float, stddev: float, num_events: int) -> float:
    """Approximates the sum of log-normal random variables using the Central Limit Theorem (CLT)."""
    mean_ln = np.exp(mean + (stddev ** 2) / 2)
    var_ln = (np.exp(stddev ** 2) - 1) * np.exp(2 * mean + stddev ** 2)

    total_mean = num_events * mean_ln
    total_stddev = np.sqrt(num_events * var_ln)
    total_loss = np.random.normal(total_mean, total_stddev)
    
    return max(total_loss, 0.0)

def poisson_CLT(rate: float) -> int:
    """Approximates a poisson variable using the Central Limit Theorem (CLT)."""
    stddev = np.sqrt(rate)
    poisson = round(np.random.normal(rate, stddev))
    return max(poisson, 0.0)

def valid_positive_integer(value: int) -> None:
    """Validator that checks if the input is a positive integer."""
    if not isinstance(value, int):
        message = f"{value} is not a valid integer."
        logger.error(message)
        raise TypeError(message)
    if value <= 0:
        message = f"{value} is not a positive integer."
        logger.error(message)
        raise ValueError(message)

def valid_nonnegative_float(value: float) -> None:
    """Validator that checks if the input is a non-negative float or integer."""
    if not isinstance(value, (int, float)):
        message = f"{value} is not a valid float or integer."
        logger.error(message)
        raise TypeError(message)
    if value < 0:
        message =f"{value} is not a non-negative value."
        logger.error(message)
        raise ValueError(message)

def valid_float(value: float) -> None:
    """Validator that checks if the input can be converted to a float."""
    if not isinstance(value, (int, float)):
        message = f"{value} is not a valid float or integer."
        logger.error(message)
        raise TypeError(message)
    