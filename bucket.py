import time
# def insertionSort(b , drawdata,speed  ):
#     # drawdata(b, ['red' for x in range(len(b))])
#     # time.sleep(10*speed)
#     for i in range(1, len(b)):
#         up = b[i]
#         j = i - 1
#         while j >= 0 and b[j] > up:
#             b[j + 1] = b[j]
#             j -= 1
#         b[j + 1] = up

#     return b


# def bucketSort(x,drawdata,speed,draw):
#     arr = []
#     slot_num = 10   
#     # slot's size is 0.1
#     for i in range(slot_num):
#         arr.append([])

#     # Put array elements in different buckets
#     for j in x:
#         index_b = int(slot_num * j)
#         arr[index_b].append(j)
       

#     # Sort individual buckets
#     for i in range(slot_num):
#         # drawdata( arr[i] ,['red' for x in range(len(arr[i]))])
#         # time.sleep(10*speed)
#         arr[i] = insertionSort(arr[i],drawdata,speed)
#     for i in range(slot_num):     
#         drawdata( arr[i] ,['red' for x in range(len(arr[i]))])
def bucketSort(data, drawdata, speed, draw):
    # Get the maximum value from the data
    max_value = max(data)

    # Create a list of empty buckets
    buckets = [[] for _ in range(len(data))]

    # Put each element in the appropriate bucket
    for i in range(len(data)):
        # Calculate the bucket index for the current element
        index = int((len(data) * data[i]) // (max_value + 1))

        # Insert the element in the bucket
        buckets[index].append(data[i])

        # Draw the updated buckets
        drawdata([val for sublist in buckets for val in sublist], ["grey" for i in range(len(data))])  
        time.sleep(speed)

    # Sort the elements in each bucket
    for i in range(len(buckets)):
        drawdata([val for sublist in buckets for val in sublist], ["grey" for i in range(len(data))])
        time.sleep(speed)
        buckets[i] = sorted(buckets[i])

        # Draw the updated buckets
        drawdata([val for sublist in buckets for val in sublist], ["grey" for i in range(len(data))])
        time.sleep(speed)
        # draw(data, [])


    # Concatenate the elements in the buckets
    result = [val for sublist in buckets for val in sublist]

    # Draw the sorted data
    drawdata(result, ["green" for i in range(len(result))])
    draw(len(data)+len(data), len(data))
    # draw(result, [])

