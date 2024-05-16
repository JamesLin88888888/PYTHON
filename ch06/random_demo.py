import random

# False: off, True: on
lights = [False] * 1000
# print(lights)

for i in range(len(lights)):
    if random.random() < 0.3:
        lights[i] = True


print(f'百分之 {sum(lights) / len(lights)} 的燈泡是亮的')