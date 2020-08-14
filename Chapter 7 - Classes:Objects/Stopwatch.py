from datetime import datetime


class Stopwatch:
    def __init__(self, startTime = 0):
        self.startTime = startTime
        self.endTime = 0

    def start(self):
        self.startTime = datetime.now()

    def stop(self):
        self.endTime = datetime.now()

    def getElapsedTime(self):
        return self.endTime - self.startTime


def main():
    time1 = Stopwatch()

    time1.start()
    print("The current time is:", time1.startTime)
    # stop = eval(input("The stopwatch has started. Enter 0 when ready to stop: "))
    # if stop == 0:
    #     time1.stop()
    number = 0
    print("Number is", number)
    for i in range (1, 1_000_001):
        number += i
    print("Number is now", number)
    time1.stop()
    print("The stop time is:", time1.endTime)
    print(time1.getElapsedTime(), "has elapsed.")


main()  # Invoke main method


'''
The current time is: 2018-10-18 22:01:16.340323
Number is 0
Number is now 500000500000
The stop time is: 2018-10-18 22:01:16.429783
0:00:00.089460 has elapsed.

Process finished with exit code 0


The current time is: 2018-10-18 15:08:28.244316
Time has started. Enter 0 when ready to stop: 0
The stop time is: 2018-10-18 15:08:31.479698
0:00:03.235382 has elapsed.

Process finished with exit code 0
'''