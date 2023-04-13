import time 
def insertion_sort(arr, low, n,drawdata,timeTick):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            drawdata( arr, [  'pink' if a == i else 'green' if a <= j   else'grey' for a in range(len(arr))])
            time.sleep(timeTick)            
            j-= 1
        arr[j]= val 
        drawdata( arr, [  'blue' if a == i else 'pink' if a <= j   else'grey' for a in range(len(arr))]) 
        time.sleep(timeTick)  
    drawdata( arr, ['green' for a in range(len(arr))]) 
    time.sleep(timeTick)                 

def partition(arr, low, high,drawdata,timeTick):
    pivot = arr[high]
    border=high
    i = j = low
    drawdata(arr,colordata(len(arr),high,low,border,border))
    time.sleep(timeTick)   
    for i in range(low, high):
        if arr[i]<pivot:
            arr[i], arr[j]= arr[j], arr[i]
               
            j+= 1
    drawdata(arr,colordata(len(arr),high,low,border,low,True))
    time.sleep(timeTick)                     
    arr[j], arr[high]= arr[high],arr[j]
    return j
 
 
def quick_sort(arr, low, high,drawdata,timeTick):
    if low<high:
        pivot = partition(arr, low, high,drawdata,timeTick)
        quick_sort(arr, low, pivot-1,drawdata,timeTick)
        quick_sort(arr, pivot + 1, high,drawdata,timeTick)
        return arr
 
# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high,drawdata,timeTick, draw):
    while low<high:
  
        if high-low + 1<10:
            insertion_sort(arr, low, high,drawdata,timeTick)
            break
 
        else:
            pivot = partition(arr, low, high,drawdata,timeTick)
 
    
            if pivot-low<high-pivot:
                hybrid_quick_sort(arr, low, pivot-1,drawdata,timeTick,draw)
                low = pivot + 1
            else:
          
                hybrid_quick_sort(arr, pivot + 1, high,drawdata,timeTick,draw)
                high = pivot-1
    drawdata( arr, [   'green' for  a in range(len(arr))])       
    draw(len(arr)**2,len(arr))           
    return arr            
def colordata(datalen,head ,tail,border ,curridex,isswapping=False):
    colordata=[]
    for i in range(datalen):


        if(i>=head and i<=tail):
            colordata.append("gray")
        else:
            colordata.append("white")    
        if i==tail:
            colordata==("orange")
        elif i ==border:
            colordata[i]=="red"        
        elif i==curridex :
            colordata[i]=="yellow"
        if isswapping:
            if i==border or i ==curridex:
                colordata[i]="green"    
    return colordata

