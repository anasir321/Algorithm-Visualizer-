import time

global a 

def bubble_sort(data,drawdata,timeTick,draw):
    a=1
    b=1
    for _ in range(len(data)-1): 
        a+=1
        for j  in range(len(data)-1):
            if(data[j]>data[j+1]):
                a=a+1 
                data[j],data[j+1]=data[j+1],data[j]
                drawdata(data,["yellow" if  x==j or x==j+1  else "grey" for x in range(len(data))])
                time.sleep(timeTick)
               
    drawdata(data,["green"for i in range(len(data))])  
    draw(a,b) 
    
    print(a,b)           
    return data               
