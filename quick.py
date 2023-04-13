import time
import numpy as np
def partition(data, head, tail , drawdata,timetick):
    border=head
    pivot=data[tail]

    drawdata(data,colordata(len(data),head,tail,border,border))
    time.sleep(timetick)
    for j in range(head, tail):
        if(data[j]<pivot):
            drawdata(data,colordata(len(data),head,tail,border,j,True))
            time.sleep(timetick)
            data[border],data[j]=data[j],data[border]
            border+=1
        drawdata(data,colordata(len(data),head,tail,border,j ))
        time.sleep(timetick)
        


    drawdata(data,colordata(len(data),head,tail,border,tail,True))
    time.sleep(timetick)      
    data[border],data[tail]=   data[tail],  data[border]   
    return border



def quick_sort(data, head, tail , drawdata,timetick,draw):
    if(head <tail ):
        partition_index=partition(data, head, tail , drawdata,timetick)


        quick_sort(data,head,partition_index-1 , drawdata,timetick,draw)    
        quick_sort(data,partition_index+1,tail , drawdata,timetick,draw) 
    drawdata(data,["green"for i in range(len(data))])  
    a=len(data)*np.log2(len(data)) 
    draw(a,len(data))            
    # return data        

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

