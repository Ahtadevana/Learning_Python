#making some sort of digital clock with time module
import time
x = int(input("Input seconds: "))

for i in range(x):
    time.sleep(1)
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600) % 24
    days = x // 86400

    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    x -= 1
print("time's up!")