# Heroscape Statistics

A simple tool for generating the probability distributions of skulls, shields and wounds

## Dependencies

 - python
 - termgraph
 - numpy
 - unittest

## Tests

To run tests:
```
python dice_stats_tests.py
```

## Example

![microcorp.png](images/microcorp.png)

Lone Microcorp Agent is choosing whether to attack a Tagawa Samurai or Raelin. If he can inflict some damage, the rest of his team may stand a chance. His choices are:

 - Attack Raelin. He has 2 attack, she has 3 + height advantage is 4 defense: `heroscape 2 4`

![heroscape 2 4](images/heroscape_2_4.png)

 - Take height advantage and attack Tagawa. He has 2 + height advantage + sighting is 4 attack, the samurai has 5 defense: `heroscape 4 5`

![heroscape 4 5](images/heroscape_4_5.png)

The agent's mission is to do damage and moving adjacent to the samurai is 20% more likely to do at least 1 wound (ie: not get 0 wounds): 

 - 46.3% vs 24.69%
