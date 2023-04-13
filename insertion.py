import time
a=0;
def insertion_sort(data,drawdata,timeTick,draw):
    a=0
    b=1
    for j in range(1, len(data)):
                key = data[j]
                a+=1 
                i = j-1
                # drawdata( data, ['yellow' if a == i or a == i +     1 else 'green' if a <= j   else'cyan' for a in range(len(data))])
                time.sleep(timeTick)
                while i >= 0 and data[i] > key:
                    data[i+1] = data[i]
                    a+=1
                    drawdata( data, [  'pink' if a == i else 'green' if a <= j   else'grey' for a in range(len(data))])
                    time.sleep(timeTick)
                    i -= 1
                data[i+1] = key   
    drawdata( data, [   'green' for  a in range(len(data))])   
    draw(a,1)              
    return data             
