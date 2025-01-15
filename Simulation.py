from typing import Optional
from HurricaneSimulator import HurricaneSimulator
import logging

logger = logging.getLogger(__name__)

class Simulation:
    """
    A model to simulate economic loss from hurricanes in Florida and Gulf States.
    
    Parameters:
        florida_landfall_rate: float
            The rate at which hurricanes hit Florida per year.
        florida_mean: float
            The mean of the economic loss in Florida when modelled as log-normal, in billions of dollars.
        florida_stddev: float
            The standard deviation of the economic loss in Florida when modelled as log-normal, in billions of dollars.
        gulf_landfall_rate: float
            The rate at which hurricanes hit Gulf States per year.
        gulf_mean: float 
            The mean of the economic loss in Gulf States when modelled as log-normal, in billions of dollars.
        gulf_stddev: float 
            The standard deviation of the economic loss in Gulf States when modelled as log-normal, in billions of dollars.
        
    Attributes:
        florida: HurricaneSimulator
            Contains landfall rate, mean and standard deviation for Florida and enables simulation.
        gulf: HurricaneSimulator
            Contains landfall rate, mean and standard deviation for Gulf States and enables simulation.
            
    Raises:
        ValueError: If florida_landfall_rate is not positive.
        ValueError: If florida_stddev is negative.
        ValueError: If gulf_landfall_rate is not positive.
        ValueError: If gulf_stddev is not positive.
    """
    def __init__(self, florida_landfall_rate: float, florida_mean: float, florida_stddev: float, gulf_landfall_rate: float, gulf_mean: float, gulf_stddev: float) -> None:        
        self.florida = HurricaneSimulator(florida_landfall_rate, florida_mean, florida_stddev)
        self.gulf = HurricaneSimulator(gulf_landfall_rate, gulf_mean, gulf_stddev)
        logger.info("Simulation initialised.")
    
    def simulate(self, years: int, use_CLT: Optional[bool] = False) -> float:
        """
        Simulates the average economic loss over a given number of years.

        Parameters:
            years: int
                The number of years to simulate over.
            use_CLT: Optional[bool]
                whether to use the Central Limit Theorem (CLT) to speed up simulation. Default is False.

        Returns:
            float
                The expected annual loss in billions of dollars.
        """
        if years <= 0:
            logger.info("Simulation for no time.")
            return 0
        
        logger.info(f"Starting simulation for {years} years.")
        
        florida_loss = self.florida.simulate(years, use_CLT=use_CLT) # More efficient to simulate all at once than to loop over years with no/low hurricanes.
        logger.info(f"Florida simulation completed. Florida loss: {florida_loss:.2f} billion.")
        
        gulf_loss = self.gulf.simulate(years, use_CLT=use_CLT)
        logger.info(f"Gulf simulation completed. Gulf loss: {gulf_loss:.2f} billion.")
        
        average = (florida_loss + gulf_loss) / years
        logger.info(f"Simulation completed. Average loss: {average:.2f} billion.")
        return (average)
