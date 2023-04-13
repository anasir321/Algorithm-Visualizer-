from tkinter import *
from tkinter import ttk
import random
from bubble import bubble_sort
from quick import quick_sort
from insertion import insertion_sort
from merge import mergesort
from heapsort import heapSort
from Adquick import hybrid_quick_sort
from radix import radixSort
from count import count_sort
from book import count_sort1
from bucket import bucketSort
from itertools import chain
data = []


def Generate():
    global data

    print("selected Algorithm: "+selected_algorithm.get())
    lines = []
    with open("file.txt") as file:
        for line in file:
            line = line.strip()

        # Split the line on whitespace to get a list of numbers on the line
        # Convert the strings to integers and floats, respectively
        numbers_on_line = [int(x) if x.isdigit() else float(x)   for x in line.split()]

        # Add the numbers on the line to the list of numbers
        lines.extend(numbers_on_line)
        print(lines)
    data = lines
    drawdata(data, ["grey"for i in range(len(data))])


def startalgo():
    # print("Starting Algorithm: ")
    global data
    if not data:
        return
    if algo_menu.get() == "Quick Sort":

        quick_sort(data, 0, len(data)-1, drawdata, 1/(speedscale.get()), draw)

    elif algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawdata, 1/(speedscale.get()), draw)
    elif algo_menu.get() == "Insertion Sort":
        insertion_sort(data, drawdata, 1/(speedscale.get()), draw)
    elif algo_menu.get() == "Merge Sort":
        mergesort(data, 0, len(data)-1, drawdata, 1/(speedscale.get()), draw)

    elif algo_menu.get() == "Heap Sort":
        heapSort(data, drawdata, 1/(speedscale.get()), draw)

    elif algo_menu.get() == "Advance Quick Sort":

        hybrid_quick_sort(data, 0, len(data)-1, drawdata,   1/(speedscale.get()), draw)
    elif algo_menu.get() == "Count Sort":
        count_sort(data, drawdata, 1/(speedscale.get()), drawdata1, draw)
    elif algo_menu.get() == "Advance Count Sort":
        count_sort1(data, drawdata, 1/(speedscale.get()),    drawdata1, minvalue.get(), maxvalue.get(), draw)
    elif algo_menu.get() == "Radix Sort":
        radixSort(data, drawdata, 1/(speedscale.get()), drawdata1, draw)
    elif algo_menu.get() == "Bucket Sort":
        # bucket_sort(data ,drawdata,1/(speedscale.get()) ,drawdata1 ,draw)
        bucketSort(data, drawdata, 1/(speedscale.get()), draw)


root = Tk()
root.title("Visualizer Algorithm visulalizer")
root.geometry('900x600+200+80')
root.config(bg='grey')


def draw(a, b):
    canvas.create_text(00, 30, anchor=SW, text=str("Time Complexity: "), font=(
        'new_roman', 15, 'italic bold'), fill="orange")
    canvas.create_text(00, 50, anchor=SW, text=str("Space Complexity: "), font=(
        'new_roman', 15, 'italic bold'), fill="orange")
    canvas.create_text(172, 30, anchor=SW, text=str(a), font=(
        'new_roman', 15, 'italic bold'), fill="white")
    canvas.create_text(175, 50, anchor=SW, text=str(b), font=(
        'new_roman', 15, 'italic bold'), fill="white")


root.update_idletasks()


def drawdata(data, colordata):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width/(len(data)+1)
    offset = 10
    normalize_data = [i/max(data) for i in data]
    specing_bet_rec = 10
    for i, height in enumerate(normalize_data):
        x0 = i*x_width+specing_bet_rec
        y0 = canvas_height-height * 400

        x1 = (i+1)*x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colordata[i])
        if (len(data) < 20):
            canvas.create_text(    x0+2, y0, anchor=SW, text=str(data[i]), font=('new_roman', 15, 'italic bold'), fill="orange")
            canvas.create_text(  x0+2, y0, anchor=SW, text=str(data[i]), font=('new_roman', 15, 'italic bold'), fill="orange")
    root.update_idletasks()


def drawdata1(data, colordata):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width/(len(data)+1)
    offset = 10
    normalize_data = [i/max(data) for i in data]
    specing_bet_rec = 10
    for i, height in enumerate(normalize_data):
        x0 = i*x_width+specing_bet_rec
        y0 = canvas_height-height * 400

        x1 = (i+1)*x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colordata[i])

        # canvas.create_text(x0+2,y0,anchor=SW,text=( str (i)   ),font=('new_roman',9,'italic bold') ,fill="red")
        # if  len(data)>50:
        #      canvas.create_text(x0+2,y0,anchor=SW,text=( str (i),str(',') ,str(data[i])  ),font=('new_roman',15,'italic bold') ,fill="orange")
    root.update_idletasks()


selected_algorithm = StringVar()
mainlabel = Label(root, text="Algorithm: ", font=(
    'new_roman', 16, 'italic bold'), bg='white', width=10, fg="black", relief=GROOVE, bd=5)
mainlabel.place(x=0, y=0)


algo_menu = ttk.Combobox(root, width=15, font=('new_roman', 19, 'italic bold'), textvariable=selected_algorithm, values=[   "Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort", "Heap Sort", "Advance Quick Sort", "Count Sort", "Advance Count Sort", "Radix Sort", "Bucket Sort"])
algo_menu.place(x=145, y=0)
algo_menu.current(0)


random_generate = Button(root, text="Generate", bg="#2DAE9A", font=('arial', 12, 'italic bold'),   relief=SUNKEN, activebackground="#05945B", activeforeground="white", bd=5, width=10, command=Generate)
random_generate.place(x=780, y=00)


# sizevaluelabel =Label(root,text="Size: ",font=('new_roman',12,'italic bold'),bg="#0E6DA5",width=10 , fg="black",height= 2,relief=GROOVE,bd=5)
# sizevaluelabel.place(x=0 ,y =40)

#             ##
# sizevalue=Scale(root,from_=0 ,to=30, resolution=1,orient=HORIZONTAL,font=('arial',12,'italic bold'),relief=GROOVE, bd=2,width=10)
# sizevalue.place(x=120,y=60)


minvaluelabel = Label(root, text="Min: ", font=('new_roman', 12, 'italic bold'),      bg="#0E6DA5", width=10, fg="black", height=2, relief=GROOVE, bd=5)
minvaluelabel.place(x=520, y=00)


minvalue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL, font=(
    'arial', 12, 'italic bold'), relief=GROOVE, bd=2, width=10)
minvalue.place(x=520, y=60)


maxvaluelabel = Label(root, text="Max: ", font=('new_roman', 12, 'italic bold'),  bg="#0E6DA5", width=10, fg="black", height=2, relief=GROOVE, bd=5)
maxvaluelabel.place(x=650, y=00)


maxvalue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL, font=(
    'arial', 12, 'italic bold'), relief=GROOVE, bd=2, width=10)
maxvalue.place(x=650, y=60)


start = Button(root, text="Start", bg="#C45B09", font=('arial', 12, 'italic bold'), relief=SUNKEN,   activebackground="#05945B", activeforeground="white", bd=5, width=10, command=startalgo)
start.place(x=780, y=60)


speedlabel = Label(root, text="Speed: ", font=('new_roman', 12, 'italic bold'),           bg="#0E6DA5", width=10, fg="black", height=2, relief=GROOVE, bd=5)
speedlabel.place(x=390, y=0)


speedscale = Scale(root, from_=1, to=10, resolution=1, digits=2, orient=HORIZONTAL, font=(   'arial', 14, 'italic bold'), relief=GROOVE, bd=2, width=10)
speedscale.place(x=390, y=60)

# tc  =Label(root,text="TC : , SC:",font=('new_roman',12,'italic bold'),bg="#0E6DA5",width=10 , fg="black",height= 2,relief=GROOVE,bd=5)
# tc.place(x=10 ,y = 60)

# sc  =Label(root,text="SC ",font=('new_roman',12,'italic bold'),bg="#0E6DA5",width=10 , fg="black",height= 2,relief=GROOVE,bd=5)
# sc.place(x=200 ,y = 60)

canvas = Canvas(root, width=870, height=450, background="black")
canvas.place(x=10, y=130)


root.mainloop()
