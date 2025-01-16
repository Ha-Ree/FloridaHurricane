import logging
from Simulation import Simulation
import argparse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("simulation.log"),  # Log to a file
        logging.StreamHandler()  # Also print to console
    ]
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
        description="Calculate the average annual hurricane loss in $Billions for a simple hurricane model."
    )
    
    parser.add_argument(
        'florida_landfall_rate', type=float,
        help="The annual rate of landfalling hurricanes in Florida."
    )
    parser.add_argument(
        'florida_mean', type=float,
        help="The mean of the economic loss in Florida when modeled as log-normal."
    )
    parser.add_argument(
        'florida_stddev', type=float,
        help="The standard deviation of the economic loss in Florida when modeled as log-normal."
    )
    parser.add_argument(
        'gulf_landfall_rate', type=float,
        help="The annual rate of landfalling hurricanes in the Gulf States."
    )
    parser.add_argument(
        'gulf_mean', type=float,
        help="The mean of the economic loss in Gulf States when modeled as log-normal."
    )
    parser.add_argument(
        'gulf_stddev', type=float,
        help="The standard deviation of the economic loss in Gulf States when modeled as log-normal."
    )
    
    parser.add_argument(
        '-n', '--num_monte_carlo_samples', type=int, default=1000,
        help="Number of samples (i.e., simulation years) to run. Default is 1000."
    )
    
    parser.add_argument(
        '--fast', action='store_true',
        help="Use Central Limit Theorem (CLT) and the additive property of poisson to speed up simulation. Use for large inputs."
    )
    
    args = parser.parse_args()
    
    logger.info(f"Received arguments: {args}")
    logger.info(f"Starting simulation for {args.num_monte_carlo_samples} years.")
    
    sim = Simulation(
        args.florida_landfall_rate,
        args.florida_mean,
        args.florida_stddev,
        args.gulf_landfall_rate,
        args.gulf_mean,
        args.gulf_stddev
    )
    if (args.fast):
        average_loss = sim.simulate_fast(args.num_monte_carlo_samples)
    else:
        average_loss = sim.simulate(args.num_monte_carlo_samples)
    
    logger.info(f"Average annual hurricane loss: {average_loss} Billion")
    
if __name__ == "__main__":
    main()
    