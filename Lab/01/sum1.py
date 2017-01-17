__author__ = 'luisfediaz'
import time



def sum1(n):
    final_sum = 0
    for x in range(n):
        final_sum += x
    return final_sum

print(sum1(10))


def sum2(n):
    return (n*(n-1))//2

print(sum2(10))


#Check times

def measure_time_sum1(n):
    start = time.time()
    sum1(n)
    stop = time.time()
    return stop - start

def measure_time_sum2(n):

    start = time.time()
    sum2(n)
    stop = time.time()
    return stop - start


def mesure_time():
    for i in range(10):
        print("took %10.7f seconds" %measure_time_sum1(i))
    print(" ")
    for i in range(10):
        print("took %10.7f seconds" %measure_time_sum2(i))

#mesure_time()


#Check average
def check_average():
    n = 10
    sum = 0
    for i in range(n):
        sum += measure_time_sum1(i)
    print(sum/n)

    sum = 0
    for i in range(n):
        sum += measure_time_sum2(i)
    print(sum/n)

#check_average()
