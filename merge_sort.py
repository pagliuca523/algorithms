#Implementing merge Sort Algorithm using as a guide,
#tutorial from realpython.com (https://realpython.com/sorting-algorithms-python/)

def merge(left,right):
    #Checking if the first array it's empty, then nothing needs to be merged
    #The result will return the second array

    if len (left) == 0:
        return right

    #Checking if the second array it's empty, then nothing needs to be merged
    #The result will return the first array

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    #Next step is going through both arrays until all the elements
    #make it into the resultant array

    while len(result) < len(left) + len (right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1

        else:
            result.append(right[index_right])
            index_right += 1

         # If you reach the end of either array, then you can
         # add the remaining elements from the other array to
         # the result and break the loop  

        if index_right == len(right):
             result += left[index_left:]
             break

        if index_left == len(left):
            result += right[index_right:] 
            break

        return result
    
    def merge_sort(array):
       # If the input array contains fewer than two elements,
       # then return it as the result of the function
        if len(array) < 2 :
            return array

        midpoint = len (array) // 2

        # Sort the array by recursively splitting the input
        # into two equal halves, sorting each half and merging them
        # together into the final result

        return merge(
            left = merge_sort(array[:midpoint]),
            right = merge_sort(array[midpoint:]))


        




