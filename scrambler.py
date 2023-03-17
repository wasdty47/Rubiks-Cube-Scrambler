import tkinter as tk
import tkinter.ttk as ttk
from typing import Counter
import kociemba
import random

# turns /////////////////////////////////////////////////////////////////////////////////////////////////////////



def turn_R():
    list_f_red = []
            
    for i in list_red:
        list_f_red.append(i["bg"])
            
    list_red[0]["bg"] = list_f_red[6]
    list_red[1]["bg"] = list_f_red[3]
    list_red[2]["bg"] = list_f_red[0]
    list_red[3]["bg"] = list_f_red[7]
    list_red[4]["bg"] = list_f_red[4]
    list_red[5]["bg"] = list_f_red[1]
    list_red[6]["bg"] = list_f_red[8]
    list_red[7]["bg"] = list_f_red[5]
    list_red[8]["bg"] = list_f_red[2]
            
    f_white_2 = list_white[2]["bg"]
    f_white_5 = list_white[5]["bg"]
    f_white_8 = list_white[8]["bg"]
    
    f_green_2 = list_green[2]["bg"]
    f_green_5 = list_green[5]["bg"]
    f_green_8 = list_green[8]["bg"]
     
    f_yellow_2 = list_yellow[2]["bg"]
    f_yellow_5 = list_yellow[5]["bg"]
    f_yellow_8 = list_yellow[8]["bg"]
        
    f_blue_0 = list_blue[0]["bg"]
    f_blue_3 = list_blue[3]["bg"]
    f_blue_6 = list_blue[6]["bg"]          
        
    list_white[2]["bg"] = f_green_2
    list_white[5]["bg"] = f_green_5
    list_white[8]["bg"] = f_green_8
        
    list_green[2]["bg"] = f_yellow_2
    list_green[5]["bg"] = f_yellow_5
    list_green[8]["bg"] = f_yellow_8
        
    list_yellow[2]["bg"] = f_blue_6
    list_yellow[5]["bg"] = f_blue_3
    list_yellow[8]["bg"] = f_blue_0
        
    list_blue[0]["bg"] = f_white_8
    list_blue[3]["bg"] = f_white_5
    list_blue[6]["bg"] = f_white_2
        
def turn_R2():
    for i in range(2):
        turn_R()

def turn_Rprime():
    for i in range(3):
        turn_R()

def turn_L():
    list_f_orange = []
    
    for i in list_orange:
        list_f_orange.append(i["bg"])
    
    list_orange[0]["bg"] = list_f_orange[6]
    list_orange[1]["bg"] = list_f_orange[3]
    list_orange[2]["bg"] = list_f_orange[0]
    list_orange[3]["bg"] = list_f_orange[7]
    list_orange[4]["bg"] = list_f_orange[4]
    list_orange[5]["bg"] = list_f_orange[1]
    list_orange[6]["bg"] = list_f_orange[8]
    list_orange[7]["bg"] = list_f_orange[5]
    list_orange[8]["bg"] = list_f_orange[2]
    
    f_white_0 = list_white[0]["bg"]
    f_white_3 = list_white[3]["bg"]
    f_white_6 = list_white[6]["bg"]
    
    f_green_0 = list_green[0]["bg"]
    f_green_3 = list_green[3]["bg"]
    f_green_6 = list_green[6]["bg"]
    
    f_yellow_0 = list_yellow[0]["bg"]
    f_yellow_3 = list_yellow[3]["bg"]
    f_yellow_6 = list_yellow[6]["bg"]
    
    f_blue_2 = list_blue[2]["bg"]
    f_blue_5 = list_blue[5]["bg"]
    f_blue_8 = list_blue[8]["bg"]
    
    list_white[0]["bg"] = f_blue_8
    list_white[3]["bg"] = f_blue_5
    list_white[6]["bg"] = f_blue_2
    
    list_green[0]["bg"] = f_white_0
    list_green[3]["bg"] = f_white_3
    list_green[6]["bg"] = f_white_6            
    
    list_yellow[0]["bg"] = f_green_0
    list_yellow[3]["bg"] = f_green_3
    list_yellow[6]["bg"] = f_green_6            
    
    list_blue[2]["bg"] = f_yellow_6
    list_blue[5]["bg"] = f_yellow_3            
    list_blue[8]["bg"] = f_yellow_0

def turn_L2():
    for i in range(2):
        turn_L()

def turn_Lprime():
    for i in range(3):
        turn_L()

def turn_F():
    list_f_green = []
    
    for i in list_green:
        list_f_green.append(i["bg"])
    
    list_green[0]["bg"] = list_f_green[6]
    list_green[1]["bg"] = list_f_green[3]
    list_green[2]["bg"] = list_f_green[0]
    list_green[3]["bg"] = list_f_green[7]
    list_green[4]["bg"] = list_f_green[4]
    list_green[5]["bg"] = list_f_green[1]
    list_green[6]["bg"] = list_f_green[8]
    list_green[7]["bg"] = list_f_green[5]
    list_green[8]["bg"] = list_f_green[2]
    
    f_white_6 = list_white[6]["bg"]
    f_white_7 = list_white[7]["bg"]
    f_white_8 = list_white[8]["bg"]
    
    f_orange_2 = list_orange[2]["bg"]
    f_orange_5 = list_orange[5]["bg"]
    f_orange_8 = list_orange[8]["bg"]
    
    f_yellow_0 = list_yellow[0]["bg"]
    f_yellow_1 = list_yellow[1]["bg"]            
    f_yellow_2 = list_yellow[2]["bg"]

    f_red_0 = list_red[0]["bg"]
    f_red_3 = list_red[3]["bg"]
    f_red_6 = list_red[6]["bg"]
    
    list_white[6]["bg"] = f_orange_8
    list_white[7]["bg"] = f_orange_5
    list_white[8]["bg"] = f_orange_2
    
    list_orange[2]["bg"] = f_yellow_0
    list_orange[5]["bg"] = f_yellow_1
    list_orange[8]["bg"] = f_yellow_2            
    
    list_yellow[0]["bg"] = f_red_6
    list_yellow[1]["bg"] = f_red_3
    list_yellow[2]["bg"] = f_red_0
    
    list_red[0]["bg"] = f_white_6
    list_red[3]["bg"] = f_white_7
    list_red[6]["bg"] = f_white_8

def turn_F2():
    for i in range(2):
        turn_F()

def turn_Fprime():
    for i in range(3):
        turn_F()

def turn_B():
    list_f_blue = []
    
    for i in list_blue:
        list_f_blue.append(i["bg"])
    
    list_blue[0]["bg"] = list_f_blue[6]
    list_blue[1]["bg"] = list_f_blue[3]
    list_blue[2]["bg"] = list_f_blue[0]
    list_blue[3]["bg"] = list_f_blue[7]
    list_blue[4]["bg"] = list_f_blue[4]
    list_blue[5]["bg"] = list_f_blue[1]
    list_blue[6]["bg"] = list_f_blue[8]
    list_blue[7]["bg"] = list_f_blue[5]
    list_blue[8]["bg"] = list_f_blue[2]
    
    f_white_0 = list_white[0]["bg"]
    f_white_1 = list_white[1]["bg"]
    f_white_2 = list_white[2]["bg"]
    
    f_orange_0 = list_orange[0]["bg"]
    f_orange_3 = list_orange[3]["bg"]
    f_orange_6 = list_orange[6]["bg"]
    
    f_yellow_6 = list_yellow[6]["bg"]
    f_yellow_7 = list_yellow[7]["bg"]
    f_yellow_8 = list_yellow[8]["bg"]
    
    f_red_2 = list_red[2]["bg"]
    f_red_5 = list_red[5]["bg"]
    f_red_8 = list_red[8]["bg"]
    
    list_white[0]["bg"] = f_red_2
    list_white[1]["bg"] = f_red_5
    list_white[2]["bg"] = f_red_8
    
    list_orange[0]["bg"] = f_white_2
    list_orange[3]["bg"] = f_white_1
    list_orange[6]["bg"] = f_white_0
    
    list_yellow[6]["bg"] = f_orange_0
    list_yellow[7]["bg"] = f_orange_3
    list_yellow[8]["bg"] = f_orange_6
    
    list_red[2]["bg"] = f_yellow_8
    list_red[5]["bg"] = f_yellow_7
    list_red[8]["bg"] = f_yellow_6

def turn_B2():
    for i in range(2):
        turn_B()

def turn_Bprime():
    for i in range(3):
        turn_B()

def turn_U():
    list_f_white = []
    
    for i in list_white:
        list_f_white.append(i["bg"])
    
    list_white[0]["bg"] = list_f_white[6]
    list_white[1]["bg"] = list_f_white[3]
    list_white[2]["bg"] = list_f_white[0]
    list_white[3]["bg"] = list_f_white[7]
    list_white[4]["bg"] = list_f_white[4]
    list_white[5]["bg"] = list_f_white[1]
    list_white[6]["bg"] = list_f_white[8]
    list_white[7]["bg"] = list_f_white[5]
    list_white[8]["bg"] = list_f_white[2]
    
    f_green_0 = list_green[0]["bg"]
    f_green_1 = list_green[1]["bg"]
    f_green_2 = list_green[2]["bg"]
    
    f_orange_0 = list_orange[0]["bg"]
    f_orange_1 = list_orange[1]["bg"]
    f_orange_2 = list_orange[2]["bg"]
    
    f_blue_0 = list_blue[0]["bg"]
    f_blue_1 = list_blue[1]["bg"]
    f_blue_2 = list_blue[2]["bg"]            
    
    f_red_0 = list_red[0]["bg"]
    f_red_1 = list_red[1]["bg"]
    f_red_2 = list_red[2]["bg"]
    
    list_green[0]["bg"] = f_red_0
    list_green[1]["bg"] = f_red_1
    list_green[2]["bg"] = f_red_2
    
    list_orange[0]["bg"] = f_green_0
    list_orange[1]["bg"] = f_green_1
    list_orange[2]["bg"] = f_green_2
     
    list_blue[0]["bg"] = f_orange_0
    list_blue[1]["bg"] = f_orange_1
    list_blue[2]["bg"] = f_orange_2

    list_red[0]["bg"] = f_blue_0
    list_red[1]["bg"] = f_blue_1
    list_red[2]["bg"] = f_blue_2

def turn_U2():
    for i in range(2):
        turn_U()

def turn_Uprime():
    for i in range(3):
        turn_U()

def turn_D():
    list_f_yellow = []
    
    for i in list_yellow:
        list_f_yellow.append(i["bg"])
    
    list_yellow[0]["bg"] = list_f_yellow[6]
    list_yellow[1]["bg"] = list_f_yellow[3]
    list_yellow[2]["bg"] = list_f_yellow[0]
    list_yellow[3]["bg"] = list_f_yellow[7]
    list_yellow[4]["bg"] = list_f_yellow[4]
    list_yellow[5]["bg"] = list_f_yellow[1]
    list_yellow[6]["bg"] = list_f_yellow[8]
    list_yellow[7]["bg"] = list_f_yellow[5]
    list_yellow[8]["bg"] = list_f_yellow[2]
    
    f_green_6 = list_green[6]["bg"]
    f_green_7 = list_green[7]["bg"]
    f_green_8 = list_green[8]["bg"]

    f_red_6 = list_red[6]["bg"]
    f_red_7 = list_red[7]["bg"]
    f_red_8 = list_red[8]["bg"]
    
    f_blue_6 = list_blue[6]["bg"]
    f_blue_7 = list_blue[7]["bg"]
    f_blue_8 = list_blue[8]["bg"]
    
    f_orange_6 = list_orange[6]["bg"]
    f_orange_7 = list_orange[7]["bg"]
    f_orange_8 = list_orange[8]["bg"]
    
    list_green[6]["bg"] = f_orange_6
    list_green[7]["bg"] = f_orange_7
    list_green[8]["bg"] = f_orange_8
    
    list_red[6]["bg"] = f_green_6
    list_red[7]["bg"] = f_green_7
    list_red[8]["bg"] = f_green_8
    
    list_blue[6]["bg"] = f_red_6
    list_blue[7]["bg"] = f_red_7
    list_blue[8]["bg"] = f_red_8
    
    list_orange[6]["bg"] = f_blue_6
    list_orange[7]["bg"] = f_blue_7
    list_orange[8]["bg"] = f_blue_8

def turn_D2():
    for i in range(2):
        turn_D()

def turn_Dprime():
    for i in range(3):
        turn_D()

# end //////////////////////////////////////////////////////////////////////////////////////////////

def scramble():
    
    for i in range(9):
        list_white[i]["bg"] = "white"
        list_green[i]["bg"] = "green"
        list_yellow[i]["bg"] = "yellow"
        list_orange[i]["bg"] = "orange"
        list_red[i]["bg"] = "red"
        list_blue[i]["bg"] = "blue"
        
    move = [" R"," R2"," R'",
            " L"," L2"," L'",
            " F"," F2"," F'",
            " B"," B2"," B'",
            " U"," U2"," U'",
            " D"," D2"," D'"]
    
    move_r = [" R"," R2"," R'"]
    move_l = [" L"," L2"," L'"]
    move_f = [" F"," F2"," F'"]
    move_b = [" B"," B2"," B'"]
    move_u = [" U"," U2"," U'"]
    move_d = [" D"," D2"," D'"]
    
    scramble = []
    
    #generate scramble
    for i in range(18):
        scramble.append(move[random.randint(0,17)])
        
        if len(scramble) != 1:
            
            while scramble[i] in move_r and scramble[i-1] in move_r:
                del scramble[i]
                scramble.append(move[random.randint(0,17)])
                
            while scramble[i] in move_l and scramble[i-1] in move_l:
                del scramble[i]
                scramble.append(move[random.randint(0,17)])
    
            while scramble[i] in move_f and scramble[i-1] in move_f:
                del scramble[i]
                scramble.append(move[random.randint(0,17)])
        
            while scramble[i] in move_b and scramble[i-1] in move_b:
                del scramble[i]
                scramble.append(move[random.randint(0,17)])
        
            while scramble[i] in move_u and scramble[i-1] in move_u:
                del scramble[i]
                scramble.append(move[random.randint(0,17)])
        
            while scramble[i] in move_d and scramble[i-1] in move_d:
                del scramble[i]
                scramble.append(move[random.randint(0,17)])
    
    #list to string
    scramble_str = ""
    for i in scramble:
        scramble_str += i

    lbl_scramble["text"] = scramble_str
    
    # checking turns in scramble and apply functions
    for turn in scramble:
        
        if turn == " R":
            turn_R()
            
        if turn == " R2":
            turn_R2()

        if turn == " R'":
            turn_Rprime()
        
        if turn == " L":
            turn_L()
            
        if turn == " L2":
            turn_L2()
            
        if turn == " L'":
            turn_Lprime()
            
        if turn == " F":
            turn_F()
            
        if turn == " F2":
            turn_F2()
            
        if turn == " F'":
            turn_Fprime()
            
        if turn == " B":
            turn_B()
            
        if turn == " B2":
            turn_B2()
            
        if turn == " B'":
            turn_Bprime()
            
        if turn == " U":
            turn_U()

        if turn == " U2":
            turn_U2()
                
        if turn == " U'":
            turn_Uprime()
        
        if turn == " D":
            turn_D()
            
        if turn == " D2":
            turn_D2()
            
        if turn == " D'":
            turn_Dprime()

    solve()
            
# ui with tkinter

window = tk.Tk()
window.title("Rubik's Cube Scrambler")
frm_cube = tk.Frame(master = window)
frm_cube.grid(row = 0, column = 0, padx = 10, pady = 10)
     
frm_white = tk.Frame(master = frm_cube)
frm_white.grid(row = 0, column = 1, padx = 10, pady = 10)
frm_green = tk.Frame(master = frm_cube)
frm_green.grid(row = 1, column = 1, padx = 10, pady = 10)
frm_yellow = tk.Frame(master = frm_cube)
frm_yellow.grid(row = 2, column = 1, padx = 10, pady = 10)
frm_orange = tk.Frame(master = frm_cube)
frm_orange.grid(row = 1, column = 0, padx = 10, pady = 10)
frm_red = tk.Frame(master = frm_cube)
frm_red.grid(row = 1, column = 2, padx = 10, pady = 10)
frm_blue = tk.Frame(master = frm_cube)
frm_blue.grid(row = 1, column = 3, padx = 10, pady = 10)

list_white = []
list_green = []
list_yellow = []
list_orange = []
list_red = []
list_blue = []


list_frm = [frm_white, frm_green, frm_yellow, frm_orange, frm_red, frm_blue]






list_color_lists = [list_white, list_red, list_green, list_yellow, list_orange, list_blue]

kociemba_input = ""

# turning scramble to string for kociemba solve() method

def generate_kociemba_input():
    global kociemba_input
    kociemba_input = ""
    for face in list_color_lists:
        for i in face:
            if i["bg"] == "white":
                kociemba_input += "U"
            elif i["bg"] == "red":
                kociemba_input += "R"
            elif i["bg"] == "green":
                kociemba_input += "F"
            elif i["bg"] == "yellow":
                kociemba_input += "D"
            elif i["bg"] == "orange":
                kociemba_input += "L"
            elif i["bg"] == "blue":
                kociemba_input += "B"

def solve():
    generate_kociemba_input()
    solve = kociemba.solve(kociemba_input)
    lbl_solve["text"] = solve

for frm in list_frm:
    frm.rowconfigure([0,1,2], minsize = 50, weight = 0)
    frm.columnconfigure([0,1,2], minsize = 50, weight = 0)

# creating and giving default colors to frms /////////////////////////////////////////////////////////////////////////////////////////////

for i in range(3):
    for j in range(3):
        label = tk.Label(master = frm_white, bg = "white", relief = tk.SUNKEN)
        list_white.append(label)
        label.grid(row = i, column = j, sticky = "nsew")
        
for i in range(3):
    for j in range(3):
        label = tk.Label(master = frm_green, bg = "green", relief = tk.SUNKEN)
        list_green.append(label)
        label.grid(row = i, column = j, sticky = "nsew")

for i in range(3):
    for j in range(3):
        label = tk.Label(master = frm_yellow, bg = "yellow", relief = tk.SUNKEN)
        list_yellow.append(label)
        label.grid(row = i, column = j, sticky = "nsew")

for i in range(3):
    for j in range(3):
        label = tk.Label(master = frm_orange, bg = "orange", relief = tk.SUNKEN)
        list_orange.append(label)
        label.grid(row = i, column = j, sticky = "nsew")

for i in range(3):
    for j in range(3):
        label = tk.Label(master = frm_red, bg = "red", relief = tk.SUNKEN)
        list_red.append(label)
        label.grid(row = i, column = j, sticky = "nsew")
        
for i in range(3):
    for j in range(3):
        label = tk.Label(master = frm_blue, bg = "blue", relief = tk.SUNKEN)
        list_blue.append(label)
        label.grid(row = i, column = j, sticky = "nsew")
        
# scramble and solve frame /////////////////////////////////////////////////////////////////////////////////////////////////////

frm_scramble = tk.Frame(master = window)
frm_scramble.grid(row = 1, column = 0, sticky = "nsew")
frm_scramble.rowconfigure([0,1,2], minsize = 50, weight = 0)
frm_scramble.columnconfigure([0,1], minsize = 100, weight = 0)

lbl_scramble = tk.Label(master = frm_scramble, text = "Press new scramble button", bg = "white", relief = tk.SUNKEN)
lbl_scramble.grid(row = 0, column = 1, sticky = "nsew")
btn_new_scramble = ttk.Button(master = frm_scramble, text = "New Scramble", command = scramble)
btn_new_scramble.grid(row = 0, column = 0, sticky = "nsew")

lbl_solve = tk.Label(master = frm_scramble, text = "Press solve button", bg = "white", relief = tk.SUNKEN)
lbl_solve.grid(row = 1, column = 1, sticky = "nsew")
lbl_solve_txt = tk.Label(master = frm_scramble, text = "Solve", bg = "white")
lbl_solve_txt.grid(row = 1, column = 0, sticky = "nsew")


window.mainloop()
