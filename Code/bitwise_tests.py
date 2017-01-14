import time

current_milli_time = lambda: int(round(time.time() * 1000))


REPS = 1000000

a1 = current_milli_time()
for i in range(REPS):
    f = i / 4
b1 = current_milli_time()

print(b1 - a1)

a2 = current_milli_time()
for i in range(REPS):
    f1 = i >> 2
b2 = current_milli_time()

print(b2 - a2)


