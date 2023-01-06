import time

i = 0
start = time.time()

while True:
    i += 1
    print(f"{i} wciągnieta kreska mefedronu")
    if i == 100000:
        break
stop = time.time()
wholetime = (stop - start)
print(round(wholetime, 2))