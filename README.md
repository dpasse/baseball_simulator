# Baseball Simulator

> built using simulation parameters from [Mathletics](https://www.amazon.com/Mathletics-Gamblers-Enthusiasts-Mathematics-Basketball/dp/0691154589/ref=sr_1_1?crid=Y0XZXKV75A5Y&keywords=matheletics&qid=1691059094&sprefix=mathletics%2Caps%2C125&sr=8-1) <br />
> see [Mathletics Event Probabilities](https://github.com/dpasse/baseball_simulator/blob/main/src/setups/mathletics.py) for the complete tree of event probabilities

## How many runs would a team of Ichiro's from 2004 create?

```python
from bball import InningSimulator, \
                  MonteCarloInningEngine, \
                  BatterStats

from bball.setups import MathleticsSimpleEventGenerator


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

simulator = InningSimulator(
    MathleticsSimpleEventGenerator().create(batter)
)

ichiro_runs = MonteCarloInningEngine(simulator).run()

print(ichiro_runs * avg_innings_per_game, 'runs per game')
```

### ~ 6.575791999999999 runs per game
