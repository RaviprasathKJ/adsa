# taken selection sort algorithm 
# this algorithm repeatedly shits the smallest element to the left most point in each loop
# thus is sorts the array in ascending order

# implementing the function for sorting this function does not return anything but changes the array in ascending order
def selection_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[j]<nums[i]):
                # swap the position 
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

# main code 
# take the input .input is given by space seperated integers 
nums = list(map(int,input().strip().split()))
# call the function to sort and pass the argument as nums 
selection_sort(nums)
# output
print(nums)

# sample 
# input 5 2 9 1 5 6
# output 1 2 5 5 6 9

# analysing the time complexity 
# here the time complexity is O(n**2) 
# advantages its stable and no memory is required space complexity O(1)
# when we compare the tc with the mergesort the tc of mergesort is O(nlogn) so its the most used algo in various languages stable for large inputs
# but the python inbuilt sort arr.sort() is the combination of both the merge sort and the insertion sort which have the tc of O(nlogn)
# so i prefer the merge sort instead of the selection sort

