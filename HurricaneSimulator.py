from typing import Optional
import numpy as np
from LogNormalCLT import log_normal_CLT
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
    
    def simulate(self, years: int, batch_size: Optional[int] = 1000, use_CLT: Optional[bool] = False) -> float:
        """
        Simulates the total economic loss from hurricanes over a given number of years.

        Parameters:
            years: int
                The number of years to simulate over.
            batch_size: Optional[int]
                The maximum number of events to process in a single batch to conserve memory. Default is 1000.
            use_CLT: Optional[bool]
                Whether to directly simulate or to use the Central Limit Theorem for efficiency. Default is False.

        Returns:
            float
                The total simulated economic loss over the specified number of years, in billions of dollars.
        """
        rate = self.rate * years # Additive property of Poisson distribution
        num_events = np.random.poisson(rate, 1)[0]
        logger.info(f"Simulating {num_events} hurricanes.")
        if use_CLT:
            logger.info("Simulating using CLT.")
            total_loss = log_normal_CLT(self.mean, self.stddev, num_events)
            logger.info(f"Finished simulating. Total loss: {total_loss}.")
            return total_loss
        
        total_loss = 0
        while num_events > 0:
            batch = min(batch_size, num_events)
            total_loss += np.sum(np.random.lognormal(self.mean, self.stddev, batch))
            num_events -= batch_size
            logger.debug(f"Processed batch of size {batch}. Current loss: {total_loss}.")
        
        logger.info(f"Finished simulating. Total loss: {total_loss}.")
        return total_loss
    