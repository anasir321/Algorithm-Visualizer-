import time

def countingSort(data, exp1, drawdata, speed,drawdata1): 

    n = len(data)

    output = [0] * (n) 
    count = [0] * (10)

    for i in range(0, n):
        index = (data[i] / exp1) 
        count[int(index % 10)] += 1
    # drawdata1(count, ['cyan' for x in range(len(count))]) 
    # time.sleep(10*speed)          

    for i in range(1, 10): 
        count[i] += count[i - 1]
    # drawdata1(count, ['grey' for x in range(len(count))]) 
    # time.sleep(10*speed)  
    i = n - 1
    narr=[0 for _ in range(len(data))]
    while i >= 0: 
        index = (data[i] / exp1) 
        output[count[int(index % 10)] - 1] = data[i] 
        drawdata(output, [    'red' for x in range(len(output))])
        time.sleep(5*speed)        
        count[int(index % 10)] -= 1
        # drawdata1(count, ['red' if x== (count[int(index % 10)] - 1)else 'grey' for x in range(len(count))]) 
        # time.sleep(10*speed)         
        i -= 1

    for i in range(0, len(data)): 
        data[i] = output[i]

    drawdata(data, ['blue' for x in range(len(data))])
    time.sleep(15*speed)

def radixSort(data, drawdata, speed,drawdata1,draw): 

    max1 = max(data)

    exp = 1
    numss = len(str(max(data)))

    while numss != 0: 
        countingSort(data, exp, drawdata, speed,drawdata1) 
        exp *= 10
        numss -= 1
    drawdata(data, ['green' for x in range(len(data))])     
    draw( ( len(data)*max(data)) , ( len(data)+max(data)) )

    return data

    # This code is contributed by Mohit Kumra
    #visualoze the code at https://www.geeksforgeeks.org/radix-sort/