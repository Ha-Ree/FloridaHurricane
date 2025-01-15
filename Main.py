import logging
from Simulation import Simulation

# Configure logging globally
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("simulation.log"),  # Log to a file
        logging.StreamHandler()  # Also print to console
    ]
)

# Main execution
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    sim = Simulation(1.2, 2.0, 0.5, 1.5, 1.8, 0.4)
    sim.simulate(100000)
    sim.simulate(100000, True)
    sim.simulate(10000000, True)
