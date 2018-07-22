import time


class Person:
    t1 = time.time()

    def __init__(self):
        self.t2 = time.time()

time.sleep(1)

p = Person()

print("t1:", p.t1)
print("t2:", p.t2)

