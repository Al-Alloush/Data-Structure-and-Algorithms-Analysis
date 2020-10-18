# python3
import random
import time

def max_pairwise_product_old(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
# ****** the solution from data University of California San Diego course
def max_pairwise_product_slower(numbers):
    n = len(numbers)
    max_product = 0
    index1 = -1
    index2 = -1

    for i in range(n):
        if index1 == -1 or numbers[i] > numbers[index1]:
            index1 = i

    for i in range(n):
        if numbers[i] != numbers[index1] and (index1 == -1 or numbers[i] > numbers[index2]):
            index2 = i
    
    return numbers[index1] * numbers[index2]

# ****** the solution from me
def max_pairwise_product(numbers):
    index1 = -1
    index2 = -1
    for i in range(len(numbers)):
        if index1 == -1 or numbers[i] >  numbers[index1]:
            if index1 != -1 : 
                index2 = index1
            index1 = i

        elif index2 == -1 or numbers[i] > numbers[index2]:
            index2 = i

    return numbers[index1] * numbers[index2]

if __name__ == '__main__':
    # n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product_slower(input_numbers))
    
    # the stress test
    n = 10000000
    a = list(random.randint(0, 9999999) for r in range(n))
    
    # test function 1
    start_time1 = time.time()
    faster = max_pairwise_product(a)
    print("faster : "+str(faster) + f" in time : {str(time.time() - start_time1)}")

    # test function 2
    start_time2 = time.time()
    slower = max_pairwise_product_slower(a)
    print("slower : "+str(slower) + f" in time : {str(time.time() - start_time2)}")

    

    
    


