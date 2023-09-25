import tkinter as tk
import math

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


def reset_timer():
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks_label.config(text=marks)


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", font=(FONT_NAME, 10), relief="flat", borderwidth=0, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 10), relief="flat", borderwidth=0, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks_label = tk.Label(fg=GREEN, bg=YELLOW)
checkmarks_label.grid(row=3, column=1)

window.mainloop()
