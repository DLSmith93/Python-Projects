
import datetime
import pytz

list = (0,1,2,3,4,5,6,7,8,9,10)

for i in range(0, 4):
    print(list[i])

print("\n")

for i in range(2, 9, 2):
    print(list[i])

print("\n")

for i in reversed(range(4)):
    print(list[i])


portland = datetime.datetime.now()
londonTZ = pytz.timezone("europe/London")
london = datetime.datetime.now(londonTZ)
newYorkTZ = pytz.timezone("America/New_York")
newYork = datetime.datetime.now(newYorkTZ)

print("\n")
print("The business is open from 9:00am to 5:00pm")
if int(portland.strftime("%H")) > 9 and int(portland.strftime("%H")) < 17:
    print("The Portland store is open")
else:
    print("the Portland store is closed")
if int(london.strftime("%H")) > 9 and int(london.strftime("%H")) < 17:
    print("The london store is open")
else:
    print("the London store is closed")
if int(newYork.strftime("%H")) > 9 and int(newYork.strftime("%H")) < 17:
    print("The New York store is open")
else:
    print("the New York store is closed")

print(portland.strftime("%H"))
print(london.strftime("%H"))
print(newYork.strftime("%H"))