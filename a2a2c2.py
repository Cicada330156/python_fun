from datetime import datetime

def testNumbers(nums, updateFreq):
    #initialize variables; index variable, number of times the program will output an update, array to store all the solutions.
    i = 1
    updateNum = nums / updateFreq
    solutions = []

    #while loop; checks every number from one to the input top value.
    while i < nums:
        #if statement tests whether the square root of (i squared + i squared) is an integer type
        if ((i**2 + i**2)**(1/2)).is_integer():
            #outputs the solution if it is found, then adds it to the array of solutions for future reference
            print("solution: " + str(i))
            solutions.append(i)

        #updates on multiples of the input update value. includes a timestamp, the number out of the total numbers which will be tested, the update over those which will be shown, and lastly, the update frequency
        if (i % updateFreq == 0):
            print(datetime.now().strftime("%H:%M:%S.%f")[:-3] + ": Program  on " + str(i) + "/" + str(nums) + ", set " + str(int(i/updateFreq)) + "/" + str(int(updateNum)) + " of " + str(updateFreq))
        i += 1

    #outputs the number of solutions found, and prints the array of them
    print("From zero to " + str(nums) + ", found " + str(len(solutions)) + " solutions:")
    print(solutions)
