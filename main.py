from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    # window after stops
    window.after_cancel(timer)

    # set to timer
    label.config(text="Timer", fg=GREEN)

    # check marks reset
    marks = ""
    check_mark.config(text=marks)

    # time reset 00:00
    canvas.itemconfig(timer_item, text=f"00:00")

    # reps to 0
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    for i in range(0, 10):
        if count_sec == i:
            count_sec = f"0{i}"
        if count_min == i:
            count_min = f"0{i}"
    canvas.itemconfig(timer_item, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_time()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# image setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_item = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 28, "bold"), fill="white")
canvas.grid(column=2, row=2)

# start Button
start_but = Button(text="Start", highlightthickness=0, command=start_time)
start_but.grid(column=1, row=3)


# reset button
reset_but = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_but.grid(column=3, row=3)

# Label Timer
label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label.grid(column=2, row=1)

# label check marks
check_mark = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_mark.grid(column=2, row=4)


window.mainloop()