from HurricaneSimulator import HurricaneSimulator
import logging
from Utils import valid_positive_integer

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
        TypeError: If variables incorrectly typed
        ValueError: If florida_landfall_rate is not positive.
        ValueError: If florida_stddev is negative.
        ValueError: If gulf_landfall_rate is not positive.
        ValueError: If gulf_stddev is not positive.
    """
    def __init__(
                self, 
                florida_landfall_rate: float, 
                florida_mean: float, 
                florida_stddev: float, 
                gulf_landfall_rate: float, 
                gulf_mean: float, 
                gulf_stddev: float
                ) -> None:        
        self.florida_simulator = HurricaneSimulator(florida_landfall_rate, florida_mean, florida_stddev)
        self.gulf_simulator = HurricaneSimulator(gulf_landfall_rate, gulf_mean, gulf_stddev)
        logger.info("Simulation initialised.")
    
    def simulate(self, years: int) -> float:
        """
        Simulates the average economic loss over a given number of years using a Monte Carlo algorithm.

        Parameters:
            years: int
                The number of years to simulate over.

        Returns:
            float
                The expected annual loss in billions of dollars.
        """
        valid_positive_integer(years)
        total_loss = 0
        for year in range(years):
            simulation_loss = 0
            
            num_florida_cases = self.florida_simulator.get_hurricanes()
            for _ in range(num_florida_cases):
                simulation_loss += self.florida_simulator.simulate()
                
            num_gulf_cases = self.gulf_simulator.get_hurricanes()
            for _ in range(num_gulf_cases):
                simulation_loss += self.gulf_simulator.simulate()
                
            total_loss += simulation_loss
            if (year % 100 == 99):
                logger.debug(f"Average after {year} years: {total_loss / year}")
        return (total_loss / years)
    
    def simulate_fast(self, years: int) -> float:
        """
        Simulates the average economic loss over a given number of years using the CLT and Poisson addition.

        Parameters:
            years: int
                The number of years to simulate over.

        Returns:
            float
                The expected annual loss in billions of dollars.
        """
        
        florida_loss = self.florida_simulator.simulate_fast(years) 
        logger.info(f"Florida simulation completed. Florida loss: {florida_loss:.2f} billion.")
        
        gulf_loss = self.gulf_simulator.simulate_fast(years)
        logger.info(f"Gulf simulation completed. Gulf loss: {gulf_loss:.2f} billion.")
        
        average = (florida_loss + gulf_loss) / years
        logger.info(f"Simulation completed. Average loss: {average:.2f} billion.")
        return (average)
