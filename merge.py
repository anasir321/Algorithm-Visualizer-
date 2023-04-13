import time
import numpy as np


def mergesort(data, left, right, drawdata, timetick, draw):
    if left < right:
        m = (left+right)//2
        mergesort(data, left, m, drawdata, timetick, draw)
        mergesort(data, m+1, right, drawdata, timetick, draw)

        j = m+1
        if data[m] <= data[m+1]:
            return

        while left <= m and j <= right:
            drawdata(data, ['blue' if x == left or x ==  j else 'grey' for x in range(len(data))])
            time.sleep(timetick)
            if data[left] <= data[j]:
                left += 1
            else:
                drawdata(data, ['red' if x == left or x ==        j else 'grey' for x in range(len(data))])

                time.sleep(timetick)
                temp = data[j]

                # storing the smaller element in temp variable
                i = j
                while i != left:
                    data[i] = data[i-1]
                    drawdata(data, ['red' if x == i or x ==    j else 'grey' for x in range(len(data))])
                    time.sleep(timetick)
                    i -= 1

                data[left] = temp

                drawdata(data, ['green' if x == left or x ==     j else 'grey' for x in range(len(data))])
                time.sleep(timetick)
                left += 1
                m += 1
                j += 1
    drawdata(data, ['green' for a in range(len(data))])
    a = len(data)*np.log2(len(data))
    draw(a, len(data))
    return data
