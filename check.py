import random

txt = open('cats.txt', 'r')

t = []
for i in txt:
     t.append(i)
name = random.choice(t)
print(name)