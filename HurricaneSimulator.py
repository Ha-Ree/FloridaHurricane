import numpy as np
from Utils import log_normal_CLT, poisson_CLT
import logging

logger = logging.getLogger(__name__)

class HurricaneSimulator:
    """
    A class to model and simulate hurricane data for a specific region.

    Parameters:
        rate: float
            The rate at which hurricanes occur per year. Must be positive.
        mean: float
            The mean economic loss from a hurricane, modeled as log-normal, in billions of dollars.
        stddev: float
            The standard deviation of the economic loss from a hurricane, modeled as log-normal, in billions of dollars. Must be non-negative.
    
    Attributes:
        rate: float
            The rate at which hurricanes occur per year.
        mean: float
            The mean economic loss from hurricanes, modeled as log-normal.
        stddev: float
            The standard deviation of economic loss from hurricanes, modeled as log-normal.
            
    Raises:
        ValueError: If rate is not positive.
        ValueError: If stddev is negative.
    """
    def __init__(self, rate: float, mean: float, stddev: float) -> None:
        if rate <= 0:
            rate_error_message = f"Rate must be positive. Rate given: {rate}."
            logger.error(rate_error_message)
            raise ValueError(rate_error_message)
        if stddev < 0:
            stddev_error_message = f"Standard deviation must be non-negative. Deviation given: {stddev}"
            logger.error(stddev_error_message)
            raise ValueError(stddev_error_message)
        self.rate = rate
        self.mean = mean
        self.stddev = stddev
        logger.info(f"HurricaneSimulation initialised with rate={rate}, mean={mean}, stddev={stddev}.")
        
    def get_hurricanes(self) -> int:
        """Returns the number of hurricanes in a year."""
        return np.random.poisson(self.rate, 1)[0]
    
    def simulate(self) -> float:
        """Returns the economical loss of one hurricane."""
        return np.random.lognormal(self.mean, self.stddev, 1)[0]
    
    def simulate_fast(self, years: int) -> float:
        """
        Simulates the total economic loss from hurricanes over a given number of years.

        Parameters:
            years: int
                The number of years to simulate over.

        Returns:
            float
                The total simulated economic loss over the specified number of years, in billions of dollars.
        """
        rate = self.rate * years # Additive property of Poisson distribution
        if rate < 100: # NumPy Poisson fails for rate greater than 2^31. After 100, the CLT very closely approximates the poisson.
            num_events = np.random.poisson(rate, 1)[0]
        else:
            num_events = poisson_CLT(rate)
        logger.info(f"Simulating {num_events} hurricanes.")
        total_loss = log_normal_CLT(self.mean, self.stddev, num_events)
        logger.info(f"Finished simulating. Total loss: {total_loss}.")
        return total_loss
    