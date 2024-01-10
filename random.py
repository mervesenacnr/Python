import random
import time

counter = 0

while counter >= 0:
    counter += 1
    random_number = random.randrange(1000)
    print(random_number)
    time.sleep(1)
    if random_number == 777:
        print('Found the number!')
        break