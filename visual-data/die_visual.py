import pygal
from die import Die

# Create two D6 dice.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D8 and a D8 1000 times."
hist.x_labels = [i for i in range(2, die_1.num_sides + die_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8 + D18', frequencies)
hist.render_to_file('die_visual.svg')