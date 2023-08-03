# Baseball Simulator

## How many runs would a team of Ichiro's from 2004 create?

```python
from src.poco import BatterStats
from src.engines import InningSimulator

avg_innings_per_game = (26.72 / 3)
def run_simulation(batter: BatterStats, iterations=50000):
    inning_simulator = InningSimulator(
        batter,
        MathleticsSimpleEventGenerator().create(batter)
    )

    runs = 0
    for i in range(iterations):
        inning = inning_simulator.play()
        runs += inning.history[-1].scenario.runs

    return runs / iterations

```

```python

from src.setups import MathleticsSimpleEventGenerator

player = BatterStats.create('ichiro', {
    'AB': 704, ## Appearance
    'SH': 2, ## Sac Bunts
    'SF': 3, ## Sac Flys
    'K': 63,
    'BB': 49,
    'HBP': 4,
    '1B': 225,
    '2B': 24,
    '3B': 5,
    'HR': 8
})

ichiro_runs = run_simulation(player)

print(ichiro_runs * avg_innings_per_game, 'runs per game')
```

### ~ 6.575791999999999 runs per game
