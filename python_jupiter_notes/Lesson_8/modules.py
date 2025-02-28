import random
import sys
from python_jupiter_notes.utils import helper as hell


print(f'Your price is {int(random.random() * 100)}')
print(random.randint(1, 100))  # Both 1 and 100 included
print(random.randrange(0, 101, 10))  # 100 not included

users = ['user1', 'user2', 'user3']
print(random.choice(users))

print(sys.platform)

print(hell.help_me())
print(hell.variable)
