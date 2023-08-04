from ..simulators import InningSimulator

class BasicInningSimulatorEngine:
    def __init__(self, simulator: InningSimulator):
        self._simulator = simulator

    def run(self, iterations = 10000) -> float:
        runs = 0
        for _ in range(iterations):
            runs += self._simulator.play().current_state.runs

        return runs / iterations
