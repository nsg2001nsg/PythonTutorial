# Shouldn't be used for security use secret module instead

import random

ran = random.random()  # gives floating point value between 0(included) and 1(excluded)
uni = random.uniform(1, 10)  # gives floating point values between a range
print(ran)
print(uni)
ran = random.randint(1, 6)  # gives integer value between a given range
print(ran)

greetings = ['Hello', 'Namaste', 'Hi', 'Good Morning', 'Hola', 'Hey', 'Howdy']
print(f'{random.choice(greetings)}, Nandini!')  # takes a sequence as arg

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k=10)  # returns multiple random results as a list, every choice equally likely
print(results)

# we can weight values to take odds in consideration
rand_result = random.choices(colors, weights=[4, 4, 13], k=10)
print(rand_result)

deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

card = random.sample(deck, k=5)  # selects unique values
print(card)

# random can be used to generate a large number of dummy data
