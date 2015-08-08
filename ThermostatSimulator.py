import argparse
import random

VALID = 0
INVALID = 1

class ThermostatSimulator:
    def __init__(self):
        self.current_state = VALID
        self.transition_matrix = [[0.9, 0.1], [0.5, 0.5]]
        self.true_temperature = 11
        self.failure_probability = 0.1

    """
    
    """
    def tick(self):
        transition_vector = self.transition_matrix[self.current_state]
        random_value = random.random()
        self.current_state = VALID if (random_value <= transition_vector[VALID]) else INVALID

    def read_value(self):
        return self.true_temperature if self.current_state == VALID else self.bad_value()

    def bad_value(self):
        return None if (random.random() <= self.failure_probability) else random.randint(-273, +273)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n_thermostats", required=True, help="number of thermostats to simulate", type=int)
    parser.add_argument("-n_ticks",       required=True, help="number of ticks to simulate", type=int)
    parser.add_argument("-output_name",   required=True, help="file name to write the output to")

    args = parser.parse_args()

    f = open(args.output_name, 'a')
    simulators = []
    for i in range(0, args.n_thermostats):
        simulators.append(ThermostatSimulator())

    for j in range (0, args.n_ticks):
        row = []
        for i in range(0, args.n_thermostats):
            simulator = simulators[i]
            simulator.tick()
            value = simulator.read_value()
            row.append(str(value) if value else 'None')
        f.write(','.join(row))
        f.write("\n")
    f.close()
