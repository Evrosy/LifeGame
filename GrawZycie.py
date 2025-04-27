import tkinter as tk

R = 11

mapa = [[0 for x in range(R)] for y in range(R)]
mapa2 = [[0 for x in range(R)] for y in range(R)]


def krok():
    global mapa 
    mapa2 = [[0 for x in range(R)] for y in range(R)] 
    mapa = tick(mapa,mapa2) #odwołanie do funkcji tick które update mapy 
    ii = 0
   #odwołuje się do każdego przycisku i zmienia kolor według mapa
    while ii<R*R:
        if mapa[ii//R][ii % R] == 0 :
            lst_buttons[ii].config(background='white')
        else :
            lst_buttons[ii].config(background='light blue')
        ii += 1

def koloruj(a):
    my_color = lst_buttons[a].config('background')[-1]
    if my_color == 'light blue':
        lst_buttons[a].config(background='white')
        mapa[a//R][a % R] = 0
    else:
        lst_buttons[a].config(background='light blue')
        mapa[a // R][a % R] = 1

def reset():
    global mapa
    mapa = [[0 for x in range(R)] for y in range(R)]
    krok()

#Sprawdza sąsiadów 
def gra(mapa, mapa2):
    if mapa == 1:
        if mapa2 == 2 or mapa2 == 3:
            mapa = 1
        else:
            mapa = 0
    elif mapa == 0 and mapa2 == 3:
        mapa = 1
    return mapa



def tick(mapa, mapa2):
    ii = 0
    jj = 0
    aa = 0
    bb = 0
    while ii < R:
        while jj < R:
            if ii == 0: #pierwszy rząd 
                mapa2[ii][jj] = mapa[ii][jj + 1] + mapa[ii + 1][jj] + mapa[ii + 1][jj + 1]
                jj = 1
                while jj < R - 1:
                    mapa2[ii][jj] = mapa[ii][jj - 1] + mapa[ii + 1][jj - 1] + mapa[ii][jj + 1] + mapa[ii + 1][jj] + \
                                    mapa[ii + 1][jj + 1]
                    jj += 1
                mapa2[ii][jj] = mapa[ii][jj - 1] + mapa[ii + 1][jj - 1] + mapa[ii + 1][jj]
                jj += 1
            elif ii == R - 1: #Ostatni rząd
                mapa2[ii][jj] = mapa[ii][jj + 1] + mapa[ii - 1][jj] + mapa[ii - 1][jj + 1]
                jj = 1
                while jj <R - 1:
                    mapa2[ii][jj] = mapa[ii][jj - 1] + mapa[ii - 1][jj - 1] + mapa[ii][jj + 1] + mapa[ii - 1][jj] + \
                                    mapa[ii - 1][jj + 1]
                    jj += 1
                mapa2[ii][jj] = mapa[ii][jj - 1] + mapa[ii - 1][jj - 1] + mapa[ii - 1][jj]
                jj += 1
            else: #Pozostałe rzędy
                mapa2[ii][jj] = mapa[ii][jj + 1] + mapa[ii - 1][jj] + mapa[ii - 1][jj + 1] + mapa[ii + 1][jj] + \
                                mapa[ii + 1][jj + 1]
                jj = 1
                while jj < R - 1:
                    mapa2[ii][jj] = mapa[ii][jj - 1] + mapa[ii][jj + 1] + mapa[ii - 1][jj - 1] + mapa[ii - 1][jj] + \
                                    mapa[ii - 1][jj + 1] + mapa[ii + 1][jj - 1] + mapa[ii + 1][jj] + mapa[ii + 1][
                                        jj + 1]
                    jj += 1
                mapa2[ii][jj] = mapa[ii][jj - 1] + mapa[ii - 1][jj - 1] + mapa[ii - 1][jj] + mapa[ii + 1][jj - 1] + \
                                mapa[ii + 1][jj]
                jj += 1
        ii += 1
        jj = 0
    while aa < R:
        while bb < R:
            mapa[aa][bb] = gra(mapa[aa][bb], mapa2[aa][bb])
            bb += 1
        bb = 0
        aa += 1
    return mapa


def serduszko():
    reset()
    temp_lst = [104,94,84,74,64,53,42,30,29,39,49,37,25,24,34,45,56,68,80,92]
    for i in temp_lst:
        koloruj(i)

def krag():
    reset()
    temp_lst = [115,104,93,82,71,102,91,80,79,89,66,56,44,57,58,59,36,35,23,25,14,5,16,27,38,49,61,62,63,64,54,41,40,29,18,31,76,85,84,95,106,97]
    for i in temp_lst:
        koloruj(i)

def strzala():
    reset()
    temp_lst = [35,24,25,47,49,71,73,85,96,95]
    for i in temp_lst:
        koloruj(i)

def statek():
    reset()
    temp_lst = [37,49,50,59,60]
    for i in temp_lst:
        koloruj(i)
        
def plum():
    reset()
    temp_lst = [67,78,79,68,80,75,86,85,74,84,72,61,59,70,39,40,37,36]
    for i in temp_lst:
        koloruj(i)

def mrug():
    reset()
    temp_lst = [25,36,47,29,40,51]
    for i in temp_lst:
        koloruj(i)

def zabka():
    reset()
    temp_lst = [26,37,48,38,49,60]
    for i in temp_lst:
        koloruj(i)

root = tk.Tk()

root.title('Gra w Życie')

#Menu - z wstęnymi ustawieniami
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Wstępne ustawienie', menu=filemenu)
filemenu.add_command(label='Serce', command =  serduszko)
filemenu.add_separator()
filemenu.add_command(label='Krąg Ognia', command = krag)
filemenu.add_separator()
filemenu.add_command(label='Quadpole', command =  strzala)
filemenu.add_separator()
filemenu.add_command(label='Szybowiec', command = statek )
filemenu.add_separator()
filemenu.add_command(label='Fontanna', command = plum )
filemenu.add_separator()
filemenu.add_command(label='Żabka', command = zabka )
filemenu.add_separator()
filemenu.add_command(label='Mruganie', command = mrug )

# 'tytul'
t = tk.Label(root, text='GRA W ŻYCIE')
t.pack(side='top')
t.config(font=("Courier", 25))


# Wyswietlany tekst
Rul = tk.Label(root, text = 'ZASADY' )
Rul.pack()
Rul.config(font=("Courier",15))
Z = tk.Label(root, text="""Komórka ożywa, gdy ma dokładnie trzech sąsiadów żywych.
Komórka przeżywa, gdy ma dwóch lub trzech sąsiadów żywych.
Komórka umiera gdy ma mniej niż dwoje sąsiadów, 
lub gdy ma ich więcej niż czworo.

Klikaj na komórki, aby zmienić ich stan z żywego na martwy i odwrotnie,
kliknij na przycisk pod planszą aby wykonać jeden ruch""")
Z.pack()
Z.config(font=("Courier", 10))

lst_buttons = []
for i in range(R*R):
    if i % R == 0:
        frame = tk.Frame(root)
        frame.pack()
    btn = tk.Button(frame, width=3, font=(15))
    btn.config(command=lambda c=i: koloruj(c))
    btn.pack(side=tk.LEFT)
    lst_buttons.append(btn)

btn_krok = tk.Button(root, text="Przejdź jeden krok", width = 25,)
btn_krok.pack(side='top', anchor='s')
btn_krok.config(command=krok)

btn_rst = tk.Button(root, text = 'Reset', width = 25)
btn_rst.pack()
btn_rst.config(command=reset)

btn_exit = tk.Button(root, text='Exit', width = 25,
                     command=root.destroy)
btn_exit.pack()

root.mainloop()

