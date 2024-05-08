def sortingalg(array):
    counter = None
    for counter in range(len(array) - 1):  # counter where the max is the max amount of iterations possible
        is_sorted = True  # sets to true at start
        for i in range(
                len(array) - counter - 1):  # in the range of the array, minus the err in len (len does not start at 0) while (i) will
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[
                    i + 1]  # swapping the numbs -- cant do two separate lines as when setting the first equation the second gets ruined
                is_sorted = False
        print(array)
        if is_sorted:
            break
    print("the array took " + str(counter) + " iterations to complete")
    print("Sorted array: " + str(array))


if __name__ == "__main__":
    test1 = [7, 12, 24, 5, 15, 12]
    test2 = [2, 75, .5, 69, 122, 155]
    test3 = [70, 60, 50, 40, 30, 20]
    test4 = [40, 20, 10, 5.5, 11, 22, 33, 55, 67, 650, 22, 11, 555]
    test5 = [1, 2, 3, 4]
    test6 = [6, 2, 3, 1, 5, 4]
    # passes all :)
    sortingalg(test6)

# make an array
# look at two numbers
# check which is greater
# swap the numbers
# I need to write better pseudocode
# questions I asked myself while writing
# 1: why need to iterate max the size of the array? = you can move a number backwards once every iteration so the max times you will need to move a number is the size of the array minus 1 (if u don't do minus 1 you will go over it one more time than needed)
