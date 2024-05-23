from tkinter import *
import math

GREEN = "#A1C398"
YELLOW = "#FEFDED"
RED = "#E72929"
FONT_NAME = "Courier"
WORKING = 40
SHORT_BREAK = 5
LONG_BREAK = 15
reps = 0
timer = None

#RESET
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    titulo.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

#TIMER
def start_timer():
    global reps
    reps += 1

    working_sec = WORKING * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if reps % 2 == 0:
        contagem(short_break_sec)
        titulo.config(text="vai pegar uma aguinha!!", fg=GREEN)
    elif reps % 8 == 0:
        contagem(long_break_sec)
        titulo.config(text="vai cochilar!!", fg=GREEN)
    else:
        contagem(working_sec)
        titulo.config(text="vai trabaia!!", fg=RED)


#CONTAGEM REGRESSIVA
def contagem(count):
    conta_min = math.floor(count / 60)
    conta_seg = count % 60
    if conta_seg < 10:
        conta_seg = f"0{conta_seg}"

    canvas.itemconfig(timer_text, text=f"{conta_min}:{conta_seg}")
    if count > 0:
        global timer
        timer = window.after(1000, contagem, count-1)
    else:
        start_timer()
        check = ""
        for _ in range(math.floor(reps/2)):
            check += "⭒"
        check_marks.config(text=check)


#UI SETUP

window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

canvas = Canvas(width=600, height=500, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(300, 350, image=tomato_img)
timer_text = canvas.create_text(300, 80, text="00:00", fill="black", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

titulo = Label(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 48))
titulo.grid(column=1, row=0)

start_button = Button(text="Start", borderwidth=0, font=(FONT_NAME, 32), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", borderwidth=0, font=(FONT_NAME, 32), command=reset_timer)
reset_button.grid(column=3, row=2)

check_marks = Label(fg=GREEN , bg=YELLOW, font=(FONT_NAME, 50))
check_marks.grid(column=1, row=3)


window.mainloop()
