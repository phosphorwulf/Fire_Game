"""
  _________  __  __ _____  _____   ______ __  __ _____  ______ __ __ __ __  __ __     ______
  \_  ___  // / / // __  // ____\ \ __  // / / // __  // __  // // // // / / // /    / ____/
   / /__/ // /_/ // / / // /__   / /_/ // /_/ // / / // /_/ // // // // / / // /    / /__
  / _____// __  // / / / \___ \ / ____// __  // / / // _  _// // // // / / // /    / ___/
 / /     / / / // /_/ /_____/ // /    / / / // /_/ // / \ \ \ V  V // /_/ // /___ / /
/_/     /_/ /_//_____//______//_/    /_/ /_//_____//_/  \_\ \__/\_/\_____//_____//_/
"""
import tkinter as tk


fire_array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def restart_btn():
    fire_array[0] = 1
    fire_array[1] = 1
    fire_array[2] = 1
    fire_array[3] = 1
    fire_array[4] = 1
    fire_array[5] = 1
    fire_array[6] = 1
    fire_array[7] = 1
    fire_array[8] = 1
    fire_array[9] = 1
    fire_array[10] = 1
    fire_array[11] = 1
    fire_array[12] = 1
    fire_array[13] = 1
    fire_array[14] = 1
    fire_array[15] = 1
    fire0.config(state='active', image=FireLit)
    fire1.config(state='active', image=FireLit)
    fire2.config(state='active', image=FireLit)
    fire3.config(state='active', image=FireLit)
    fire4.config(state='active', image=FireLit)
    fire5.config(state='active', image=FireLit)
    fire6.config(state='active', image=FireLit)
    fire7.config(state='active', image=FireLit)
    fire8.config(state='active', image=FireLit)
    fire9.config(state='active', image=FireLit)
    fire10.config(state='active', image=FireLit)
    fire11.config(state='active', image=FireLit)
    fire12.config(state='active', image=FireLit)
    fire13.config(state='active', image=FireLit)
    fire14.config(state='active', image=FireLit)
    fire15.config(state='active', image=FireLit)


def quit_btn():
    root.destroy()


def game_over():
    if sum(fire_array) == 0:
        print("you win")
        # set window to image
        # sleep few seconds
        root.destroy()


def press_fire0():
    fire0.config(state='disabled', image=FireOut)
    fire_array[0] = 0
    if fire_array[1]:
        fire1.config(state='disabled', image=FireOut)
        fire_array[1] = 0
    else:
        fire1.config(state='active', image=FireLit)
        fire_array[1] = 1
    if fire_array[4]:
        fire4.config(state='disabled', image=FireOut)
        fire_array[4] = 0
    else:
        fire4.config(state='active', image=FireLit)
        fire_array[4] = 1
    game_over()


def press_fire1():
    fire1.config(state='disabled', image=FireOut)
    fire_array[1] = 0
    if fire_array[0]:
        fire0.config(state='disabled', image=FireOut)
        fire_array[0] = 0
    else:
        fire0.config(state='active', image=FireLit)
        fire_array[0] = 1
    if fire_array[2]:
        fire2.config(state='disabled', image=FireOut)
        fire_array[2] = 0
    else:
        fire2.config(state='active', image=FireLit)
        fire_array[2] = 1
    if fire_array[5]:
        fire5.config(state='disabled', image=FireOut)
        fire_array[5] = 0
    else:
        fire5.config(state='active', image=FireLit)
        fire_array[5] = 1
    game_over()


def press_fire2():
    fire2.config(state='disabled', image=FireOut)
    fire_array[2] = 0
    if fire_array[1]:
        fire1.config(state='disabled', image=FireOut)
        fire_array[1] = 0
    else:
        fire1.config(state='active', image=FireLit)
        fire_array[1] = 1
    if fire_array[3]:
        fire3.config(state='disabled', image=FireOut)
        fire_array[3] = 0
    else:
        fire3.config(state='active', image=FireLit)
        fire_array[3] = 1
    if fire_array[6]:
        fire6.config(state='disabled', image=FireOut)
        fire_array[6] = 0
    else:
        fire6.config(state='active', image=FireLit)
        fire_array[6] = 1
    game_over()


def press_fire3():
    fire3.config(state='disabled', image=FireOut)
    fire_array[3] = 0
    if fire_array[2]:
        fire2.config(state='disabled', image=FireOut)
        fire_array[2] = 0
    else:
        fire2.config(state='active', image=FireLit)
        fire_array[2] = 1
    if fire_array[7]:
        fire7.config(state='disabled', image=FireOut)
        fire_array[7] = 0
    else:
        fire7.config(state='active', image=FireLit)
        fire_array[7] = 1
    game_over()


def press_fire4():
    fire4.config(state='disabled', image=FireOut)
    fire_array[4] = 0
    if fire_array[0]:
        fire0.config(state='disabled', image=FireOut)
        fire_array[0] = 0
    else:
        fire0.config(state='active', image=FireLit)
        fire_array[0] = 1
    if fire_array[5]:
        fire5.config(state='disabled', image=FireOut)
        fire_array[5] = 0
    else:
        fire5.config(state='active', image=FireLit)
        fire_array[5] = 1
    if fire_array[8]:
        fire8.config(state='disabled', image=FireOut)
        fire_array[8] = 0
    else:
        fire8.config(state='active', image=FireLit)
        fire_array[8] = 1
    game_over()


def press_fire5():
    fire5.config(state='disabled', image=FireOut)
    fire_array[5] = 0
    if fire_array[1]:
        fire1.config(state='disabled', image=FireOut)
        fire_array[1] = 0
    else:
        fire1.config(state='active', image=FireLit)
        fire_array[1] = 1
    if fire_array[4]:
        fire4.config(state='disabled', image=FireOut)
        fire_array[4] = 0
    else:
        fire4.config(state='active', image=FireLit)
        fire_array[4] = 1
    if fire_array[6]:
        fire6.config(state='disabled', image=FireOut)
        fire_array[6] = 0
    else:
        fire6.config(state='active', image=FireLit)
        fire_array[6] = 1
    if fire_array[9]:
        fire9.config(state='disabled', image=FireOut)
        fire_array[9] = 0
    else:
        fire9.config(state='active', image=FireLit)
        fire_array[9] = 1
    game_over()


def press_fire6():
    fire6.config(state='disabled', image=FireOut)
    fire_array[6] = 0
    if fire_array[2]:
        fire2.config(state='disabled', image=FireOut)
        fire_array[2] = 0
    else:
        fire2.config(state='active', image=FireLit)
        fire_array[2] = 1
    if fire_array[5]:
        fire5.config(state='disabled', image=FireOut)
        fire_array[5] = 0
    else:
        fire5.config(state='active', image=FireLit)
        fire_array[5] = 1
    if fire_array[7]:
        fire7.config(state='disabled', image=FireOut)
        fire_array[7] = 0
    else:
        fire7.config(state='active', image=FireLit)
        fire_array[7] = 1
    if fire_array[10]:
        fire10.config(state='disabled', image=FireOut)
        fire_array[10] = 0
    else:
        fire10.config(state='active', image=FireLit)
        fire_array[10] = 1
    game_over()


def press_fire7():
    fire7.config(state='disabled', image=FireOut)
    fire_array[7] = 0
    if fire_array[3]:
        fire3.config(state='disabled', image=FireOut)
        fire_array[3] = 0
    else:
        fire3.config(state='active', image=FireLit)
        fire_array[3] = 1
    if fire_array[6]:
        fire6.config(state='disabled', image=FireOut)
        fire_array[6] = 0
    else:
        fire6.config(state='active', image=FireLit)
        fire_array[6] = 1
    if fire_array[11]:
        fire11.config(state='disabled', image=FireOut)
        fire_array[11] = 0
    else:
        fire11.config(state='active', image=FireLit)
        fire_array[11] = 1
    game_over()


def press_fire8():
    fire8.config(state='disabled', image=FireOut)
    fire_array[8] = 0
    if fire_array[4]:
        fire4.config(state='disabled', image=FireOut)
        fire_array[4] = 0
    else:
        fire4.config(state='active', image=FireLit)
        fire_array[4] = 1
    if fire_array[9]:
        fire9.config(state='disabled', image=FireOut)
        fire_array[9] = 0
    else:
        fire9.config(state='active', image=FireLit)
        fire_array[9] = 1
    if fire_array[12]:
        fire12.config(state='disabled', image=FireOut)
        fire_array[12] = 0
    else:
        fire12.config(state='active', image=FireLit)
        fire_array[12] = 1
    game_over()


def press_fire9():
    fire9.config(state='disabled', image=FireOut)
    fire_array[9] = 0
    if fire_array[5]:
        fire5.config(state='disabled', image=FireOut)
        fire_array[5] = 0
    else:
        fire5.config(state='active', image=FireLit)
        fire_array[5] = 1
    if fire_array[8]:
        fire8.config(state='disabled', image=FireOut)
        fire_array[8] = 0
    else:
        fire8.config(state='active', image=FireLit)
        fire_array[8] = 1
    if fire_array[10]:
        fire10.config(state='disabled', image=FireOut)
        fire_array[10] = 0
    else:
        fire10.config(state='active', image=FireLit)
        fire_array[10] = 1
    if fire_array[13]:
        fire13.config(state='disabled', image=FireOut)
        fire_array[13] = 0
    else:
        fire13.config(state='active', image=FireLit)
        fire_array[13] = 1
    game_over()


def press_fire10():
    fire10.config(state='disabled', image=FireOut)
    fire_array[10] = 0
    if fire_array[6]:
        fire6.config(state='disabled', image=FireOut)
        fire_array[6] = 0
    else:
        fire6.config(state='active', image=FireLit)
        fire_array[6] = 1
    if fire_array[9]:
        fire9.config(state='disabled', image=FireOut)
        fire_array[9] = 0
    else:
        fire9.config(state='active', image=FireLit)
        fire_array[9] = 1
    if fire_array[11]:
        fire11.config(state='disabled', image=FireOut)
        fire_array[11] = 0
    else:
        fire11.config(state='active', image=FireLit)
        fire_array[11] = 1
    if fire_array[14]:
        fire14.config(state='disabled', image=FireOut)
        fire_array[14] = 0
    else:
        fire14.config(state='active', image=FireLit)
        fire_array[14] = 1
    game_over()


def press_fire11():
    fire11.config(state='disabled', image=FireOut)
    fire_array[11] = 0
    if fire_array[7]:
        fire7.config(state='disabled', image=FireOut)
        fire_array[7] = 0
    else:
        fire7.config(state='active', image=FireLit)
        fire_array[7] = 1
    if fire_array[10]:
        fire10.config(state='disabled', image=FireOut)
        fire_array[10] = 0
    else:
        fire10.config(state='active', image=FireLit)
        fire_array[10] = 1
    if fire_array[15]:
        fire15.config(state='disabled', image=FireOut)
        fire_array[15] = 0
    else:
        fire15.config(state='active', image=FireLit)
        fire_array[15] = 1
    game_over()


def press_fire12():
    fire12.config(state='disabled', image=FireOut)
    fire_array[12] = 0
    if fire_array[8]:
        fire8.config(state='disabled', image=FireOut)
        fire_array[8] = 0
    else:
        fire8.config(state='active', image=FireLit)
        fire_array[8] = 1
    if fire_array[13]:
        fire13.config(state='disabled', image=FireOut)
        fire_array[13] = 0
    else:
        fire13.config(state='active', image=FireLit)
        fire_array[13] = 1
    game_over()


def press_fire13():
    fire13.config(state='disabled', image=FireOut)
    fire_array[13] = 0
    if fire_array[9]:
        fire9.config(state='disabled', image=FireOut)
        fire_array[9] = 0
    else:
        fire9.config(state='active', image=FireLit)
        fire_array[9] = 1
    if fire_array[12]:
        fire12.config(state='disabled', image=FireOut)
        fire_array[12] = 0
    else:
        fire12.config(state='active', image=FireLit)
        fire_array[12] = 1
    if fire_array[14]:
        fire14.config(state='disabled', image=FireOut)
        fire_array[14] = 0
    else:
        fire14.config(state='active', image=FireLit)
        fire_array[14] = 1
    game_over()


def press_fire14():
    fire14.config(state='disabled', image=FireOut)
    fire_array[14] = 0
    if fire_array[10]:
        fire10.config(state='disabled', image=FireOut)
        fire_array[10] = 0
    else:
        fire10.config(state='active', image=FireLit)
        fire_array[10] = 1
    if fire_array[13]:
        fire13.config(state='disabled', image=FireOut)
        fire_array[13] = 0
    else:
        fire13.config(state='active', image=FireLit)
        fire_array[13] = 1
    if fire_array[15]:
        fire15.config(state='disabled', image=FireOut)
        fire_array[15] = 0
    else:
        fire15.config(state='active', image=FireLit)
        fire_array[15] = 1
    game_over()


def press_fire15():
    fire15.config(state='disabled', image=FireOut)
    fire_array[15] = 0
    if fire_array[11]:
        fire11.config(state='disabled', image=FireOut)
        fire_array[11] = 0
    else:
        fire11.config(state='active', image=FireLit)
        fire_array[11] = 1
    if fire_array[14]:
        fire14.config(state='disabled', image=FireOut)
        fire_array[14] = 0
    else:
        fire14.config(state='active', image=FireLit)
        fire_array[14] = 1
    game_over()


root = tk.Tk()  # (m)
root.title("fires Out")  # ū

# YouWin = tk.PhotoImage(file='firesOutYouWin.png')
FireLit = tk.PhotoImage(file='FireLit.png')
FireOut = tk.PhotoImage(file='FireOut.png')

btn_frame = tk.Frame(root)
btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)
btn_frame.columnconfigure(3, weight=1)
btn_frame.pack(fill='x')

fire0 = tk.Button(btn_frame, image=FireLit, command=press_fire0)
fire0.grid(column=0, row=0)
fire1 = tk.Button(btn_frame, image=FireLit, command=press_fire1)
fire1.grid(column=1, row=0)
fire2 = tk.Button(btn_frame, image=FireLit, command=press_fire2)
fire2.grid(column=2, row=0)
fire3 = tk.Button(btn_frame, image=FireLit, command=press_fire3)
fire3.grid(column=3, row=0)
fire4 = tk.Button(btn_frame, image=FireLit, command=press_fire4)
fire4.grid(column=0, row=1)
fire5 = tk.Button(btn_frame, image=FireLit, command=press_fire5)
fire5.grid(column=1, row=1)
fire6 = tk.Button(btn_frame, image=FireLit, command=press_fire6)
fire6.grid(column=2, row=1)
fire7 = tk.Button(btn_frame, image=FireLit, command=press_fire7)
fire7.grid(column=3, row=1)
fire8 = tk.Button(btn_frame, image=FireLit, command=press_fire8)
fire8.grid(column=0, row=2)
fire9 = tk.Button(btn_frame, image=FireLit, command=press_fire9)
fire9.grid(column=1, row=2)
fire10 = tk.Button(btn_frame, image=FireLit, command=press_fire10)
fire10.grid(column=2, row=2)
fire11 = tk.Button(btn_frame, image=FireLit, command=press_fire11)
fire11.grid(column=3, row=2)
fire12 = tk.Button(btn_frame, image=FireLit, command=press_fire12)
fire12.grid(column=0, row=3)
fire13 = tk.Button(btn_frame, image=FireLit, command=press_fire13)
fire13.grid(column=1, row=3)
fire14 = tk.Button(btn_frame, image=FireLit, command=press_fire14)
fire14.grid(column=2, row=3)
fire15 = tk.Button(btn_frame, image=FireLit, command=press_fire15)
fire15.grid(column=3, row=3)

restart = tk.Button(root, text="Restart", command=restart_btn)
restart.pack()
close = tk.Button(root, text="Quit", command=quit_btn)
close.pack()

root.mainloop()
