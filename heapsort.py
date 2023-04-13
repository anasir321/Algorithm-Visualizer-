import time
import numpy as np

def heapify(data, n, i,drawdata,timeTick):
    largest = i   
    l = 2 * i + 1   
    r = 2 * i + 2  

 

    if l < n and data[i] < data[l]:
        largest = l

 

    if r < n and data[largest] < data[r]:
        largest = r
 

    if largest != i:
        (data[i], data[largest]) = (data[largest], data[i])   
        drawdata( data, ['red' if x == i or x==   largest else 'grey' for x in range(len(data))])
        time.sleep(timeTick)         


        heapify(data, n, largest,drawdata,timeTick)

 

def heapSort(data,drawdata,timeTick,draw):
    n = len(data)
 

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i,drawdata,timeTick)
    # return arr    

 

    for i in range(n - 1, 0, -1):
        (data[i], data[0]) = (data[0], data[i])  # swap
        drawdata( data, ['blue' if x == i or data[i] ==   data[0] else 'grey' for x in range(len(data))])
        time.sleep(timeTick)     
        heapify(data, i, 0,drawdata,timeTick)

    drawdata( data, ['green'   for x in range(len(data))])
    a=len(data)*np.log2(len(data)) 
    draw(a,len(data))
    return data   
 