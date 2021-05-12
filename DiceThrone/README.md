# Dice Throne

| Dependencies         |
| ---                  |
| `pip install pyyaml` |

| Script           | Board Game Geek                                            |
| ---              | ---                                                        |
| `dice_throne.py` | https://www.boardgamegeek.com/boardgame/268201/dice-throne |

| Usage                                     | Description                                                                                       |
| ---                                       | ---                                                                                               |
| `dice_throne.py Character`                | Show the probability of the character's powers                                                    |
| `dice_throne.py Character --dice a b c`   | Show the probability of the character's powers given the dice `a`, `b` and `c` have been reserved |
| `dice_throne.py Character --rolls-left x` | Show the probability* of the character's powers given a number of reroll attempts                 |

\* For x > 1, this is a lower bound on the probability of success. Each subsequent roll, rolls all the unreserved dice without reserving new helpful results.
