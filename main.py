import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random

# Main Window
root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
screen = str(w) + "x" + str(h)
root.geometry(screen)
root.config(bg = 'steel blue')
root.title("Så Ska Det Låta!")
root.option_add('*Dialog.msg.font', 'Helvetica 24')
root.filename = filedialog.askopenfilename(title = "Select file")

def t1_plus():
    temp = points_1.get('1.0','end')
    points_1.delete('1.0', 'end')
    points_1.insert('end',str(int(temp) + 1), 'tc')

def t1_minus():
    temp = points_1.get('1.0','end')
    points_1.delete('1.0', 'end')
    points_1.insert('end',str(int(temp) - 1), 'tc')

def t2_plus():
    temp = points_2.get('1.0','end')
    points_2.delete('1.0', 'end')
    points_2.insert('end',str(int(temp) + 1), 'tc')

def t2_minus():
    temp = points_2.get('1.0','end')
    points_2.delete('1.0', 'end')
    points_2.insert('end',str(int(temp) - 1), 'tc')


# Toggle box function 1
def tg_1():
    nbr = 1
    index = int(lbl_index.cget('text'))
    red = red_square[index][nbr-1]
    if red:
        bt_1.config(bg = 'red')
    else:
        bt_1.config(bg = 'green')
    song = song_list[index]
    bt_1.config(text = song[nbr-1])

# Toggle box function 2
def tg_2():
    nbr = 2
    index = int(lbl_index.cget('text'))
    red = red_square[index][nbr-1]
    if red:
        bt_2.config(bg = 'red')
    else:
        bt_2.config(bg = 'green')
    song = song_list[index]
    bt_2.config(text = song[nbr-1])

# Toggle box function 3
def tg_3():
    nbr = 3
    index = int(lbl_index.cget('text'))
    red = red_square[index][nbr-1]
    if red:
        bt_3.config(bg = 'red')
    else:
        bt_3.config(bg = 'green')
    song = song_list[index]
    bt_3.config(text = song[nbr-1])

# Toggle box function 4
def tg_4():
    nbr = 4
    index = int(lbl_index.cget('text'))
    red = red_square[index][nbr-1]
    if red:
        bt_4.config(bg = 'red')
    else:
        bt_4.config(bg = 'green')
    song = song_list[index]
    bt_4.config(text = song[nbr-1])

# Toggle box function 5
def tg_5():
    nbr = 5
    index = int(lbl_index.cget('text'))
    red = red_square[index][nbr-1]
    if red:
        bt_5.config(bg = 'red')
    else:
        bt_5.config(bg = 'green')
    song = song_list[index]
    bt_5.config(text = song[nbr-1])

# Next song button command
def new_song():
    bt_1.config(bg = 'blue', text = '1')
    bt_2.config(bg = 'blue', text = '2')
    bt_3.config(bg = 'blue', text = '3')
    bt_4.config(bg = 'blue', text = '4')
    bt_5.config(bg = 'blue', text = '5')
    index = int(lbl_index.cget('text'))+1;
    if index == len(song_list):
        index = index - 1
    lbl_index.config(text = str(index))
    if index == 4:
        file  = open('Tolken.txt', 'r')
        tolken_list = []
        for line in file:
            tolken_list.append(line)
        file.close()
        messagebox.showinfo('Lightning Round!', 'Det har blivit dags att spela Tolken!')
        messagebox.askokcancel('Tolken', tolken_list[0])
        messagebox.askokcancel('Tolken', tolken_list[1])
        messagebox.askokcancel('Tolken', tolken_list[2])
        messagebox.askokcancel('Tolken', tolken_list[3])
        messagebox.askokcancel('Tolken', tolken_list[4])
        messagebox.askokcancel('Tolken', tolken_list[5])
        messagebox.askokcancel('Tolken', tolken_list[6])
        messagebox.askokcancel('Tolken', tolken_list[7])
        messagebox.askokcancel('Tolken', tolken_list[8])
    elif index == 9:
        messagebox.showinfo('Lightning Round!', 'Det har blivit dags att spela Norsk kareoke!')
    elif index == 14:
        messagebox.showinfo('Lightning Round!', 'Det har blivit dags att spela Eläkeläiset!')

# Correct song button command
def correct():
    if bt_1.cget('bg') == 'blue':
        tg_1()
    if bt_2.cget('bg') == 'blue':
        tg_2()
    if bt_3.cget('bg') == 'blue':
        tg_3()
    if bt_4.cget('bg') == 'blue':
        tg_4()
    if bt_5.cget('bg') == 'blue':
        tg_5()
    index = int(lbl_index.cget('text'))
    song = song_list[index]
    messagebox.askokcancel(song[7], song[5])
    messagebox.askokcancel(song[7], song[6])
    new_song()

#Input file
file  = open(root.filename, 'r')
song_list = []
for line in file:
    song = line.split(';')
    song_list.append(song)
file.close()

red_square = []
for i in range(0,len(song_list)):
    temp = [0, 0, 0, 0, 0]
    first = random.randint(0,4)
    second = random.randint(0,4)
    while second == first:
        second = random.randint(0,4)
    temp[first] = 1
    temp[second] = 1
    red_square.append(temp)

lbl_name = tk.Label(root, font = ('arial', 60, 'bold'), text = "Så Ska Det Låta!", fg = "black", bd = 10, bg = 'steel blue', anchor = 'w')
lbl_name.place(x = w/2, y = 60, anchor = 'center')

# Invisible labels to hold song index and used songs
lbl_index = tk.Label(root, text = '0')

# Correct song button
bt_corr = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 20, 'bold'), text = "Rätt!", bg = "blue", command = correct, width = 10, height = 2)
bt_corr.place(x = w/2, y = 2*h/3, anchor = 'center')

# Toggle box button 1
bt_1 = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "1", bg = "blue", command = tg_1, width = 20, height = 10)
bt_1.place(x = int(0.10*w), y = h/2-100, anchor = 'center')
# Toggle box button 2
bt_2 = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "2", bg = "blue", command = tg_2, width = 20, height = 10)
bt_2.place(x = int(0.30*w), y = h/2-100, anchor = 'center')
# Toggle box button 3
bt_3 = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "3", bg = "blue", command = tg_3, width = 20, height = 10)
bt_3.place(x = w/2, y = h/2-100, anchor = 'center')
# Toggle box button 4
bt_4 = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "4", bg = "blue", command = tg_4, width = 20, height = 10)
bt_4.place(x = int(0.70*w), y = h/2-100, anchor = 'center')
# Toggle box button 5
bt_5 = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "5", bg = "blue", command = tg_5, width = 20, height = 10)
bt_5.place(x = int(0.90*w), y = h/2-100, anchor = 'center')

# Team names
team_1_name = tk.StringVar()
team_1_entry = tk.Entry(root, font = ('arial', 26), fg = 'black' , insertbackground = 'black', textvariable = team_1_name, bd = 4, insertwidth = 1, bg = 'steel blue', justify = 'center', width = 16)
team_1_entry.place(x = int(0.20*w), y = 2*h/3, anchor = 'center')
team_1_name.set('Lag 1')

team_2_name = tk.StringVar()
team_2_entry = tk.Entry(root, font = ('arial', 26), fg = 'black' , insertbackground = 'black', textvariable = team_2_name, bd = 4, insertwidth = 1, bg = 'steel blue', justify = 'center', width = 16)
team_2_entry.place(x = int(0.80*w), y = 2*h/3, anchor = 'center')
team_2_name.set('Lag 2')

#Points
points_1 = tk.Text(root, font = ('arial', 26), padx = 10, pady = 4, bd = 4, height = 1, width = 5, bg = 'steel blue', fg = 'black', insertbackground = 'black')
points_1.place(x = int(0.20*w), y = 3*h/4, anchor = 'center')
points_1.tag_configure('tc', justify = 'center')
points_1.insert('end', '0', 'tc')

bt1_plus = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "+", bg = "blue", command = t1_plus, width = 2)
bt1_plus.place(x = int(0.20*w)+90, y = 3*h/4, anchor = 'center')
bt1_minus = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "-", bg = "blue", command = t1_minus, width = 2)
bt1_minus.place(x = int(0.20*w)-90, y = 3*h/4, anchor = 'center')

points_2 = tk.Text(root, font = ('arial', 26), padx = 10, pady = 4, bd = 4, height = 1, width = 5, bg = 'steel blue', fg = 'black', insertbackground = 'black')
points_2.place(x = int(0.80*w), y = 3*h/4, anchor = 'center')
points_2.tag_configure('tc', justify = 'center')
points_2.insert('end', '0', 'tc')

bt2_plus = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "+", bg = "blue", command = t2_plus, width = 2)
bt2_plus.place(x = int(0.80*w)+90, y = 3*h/4, anchor = 'center')
bt2_minus = tk.Button(root, padx = 4, pady = 4, bd = 3, fg = "white", font = ('arial', 12, 'bold'), text = "-", bg = "blue", command = t2_minus, width = 2)
bt2_minus.place(x = int(0.80*w)-90, y = 3*h/4, anchor = 'center')


root.mainloop()
