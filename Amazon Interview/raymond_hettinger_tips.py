# Looping over a range of numbers
for i in xrange(10):
    print i**2

# Looping over a collection
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print color

# Backwards
for color in reversed(colors):
    print color

# Looping over a collection and indices
for i, color in enumerate(colors):
    print i, '->', color

# Looping over two collections
names = ['raymond', 'rachael', 'matthew', 'ben']
for name, color in zip(names, colors):
    print name, '->', color

# Looping in sorted order
for color in sorted(colors):
    print colors

# Backwards..
for color in sorted(colors, reverse=True):
    print color

# Custom sort order (smallest -> largest)
print sorted(names, key=len)

# Call a function until a sentinel value
# blocks = []
# for block in iter(partial(f.read, 32), ''):
# blocks.append(block)