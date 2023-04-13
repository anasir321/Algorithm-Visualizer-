import time
 
def count_sort1(arr,drawdata , speed , drawdata1 ,aa,bb,draw    ):
    
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
    # drawdata1(count_arr, ['cyan' for x in range(len(count_arr))]) 
    # time.sleep(10*speed)      
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    # drawdata1(count_arr, ['grey' for x in range(len(count_arr))]) 
    # time.sleep(10*speed)         
    narr = [0 for _ in range(len(arr))]
 

    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        # drawdata(arr, ['blue' for x in range(len(arr))]) 
        narr[count_arr[arr[i] - min_element] - 1] = arr[i]
        drawdata(narr, ['blue' if  count_arr[arr[i] - min_element] - 1==x  else 'red' for x in range(len(narr))])
        time.sleep(10*speed)
        count_arr[arr[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    drawdata(arr, ['green' if arr[x]>=aa and arr[x]<=bb  else 'grey'  for x in range(len(narr))]) 
    # time.sleep(10*speed)

    draw( ( len(arr)+max(arr)) , (max_element-min_element+1) )
    # time.sleep(10*speed)  
    return arr
  