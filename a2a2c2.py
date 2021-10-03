from datetime import datetime

def testNumbers(nums, updateFreq):
    i = 1
    updateNum = nums / updateFreq
    solutions = []
    while i < nums:
        if ((i**2 + i**2)**(1/2)).is_integer():
            print("solution: " + str(i))
            solutions.append(i)
        if (i % updateFreq == 0):
            print(datetime.now().strftime("%H:%M:%S.%f")[:-3] + ": Program  on " + str(i) + "/" + str(nums) + ", set " + str(int(i/updateFreq)) + "/" + str(int(updateNum)) + " of " + str(updateFreq))
        i += 1
    print("From zero to " + str(nums) + ", found " + str(len(solutions)) + " solutions:")
    print(solutions)
