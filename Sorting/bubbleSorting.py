
class BubbleSorting:

    def __init__(self, array):
        self.array = array


    def sorting(self):
        arr = self.array
        # rang from arrayLingth -1 to 0, with every loop -1
        # After comparing each pair of numbers, we need to do so by looking at the length of the array
        # because in the bad scenario the last element in the array is the small one
        for pass_num in range(len(arr)-1, 0, -1):

            for i in range(pass_num):
                # if current value biger than next value
                if arr[i]>arr[i+1]:
                    # set the biger value in tempraray variable
                    temp = arr[i]
                    # change the current value with next value set the small one in current value
                    arr[i] = arr[i+1]
                    # set the biger value, that stored in tempraray variable in next value
                    arr[i+1] = temp

    def printArr(self):
        print(self.array)


_array = [14,46,43,27,57,41,45,21,70]
bs = BubbleSorting(_array)
bs.sorting()
bs.printArr()