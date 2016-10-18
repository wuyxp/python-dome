alien_0 = {'color': 'green', 'point': 5}
print alien_0['color']

alien_0['x'] = 0
alien_0['y'] = 100

print alien_0

alien_0['point'] = 10
print alien_0

del alien_0['x']
print alien_0

print alien_0.keys()
print alien_0.values()