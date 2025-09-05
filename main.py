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
remaining_time = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, remaining_time
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text,text= "00:00")
    check_label.config(text= "")
    reps = 0
    remaining_time = 0

# ---------------------------- TIMER PAUSE ------------------------------- #
def pause_timer():
    window.after_cancel(timer)
    title_label.config(text= "Paused")

# ---------------------------- TIMER RESUME ------------------------------- #

def resume_timer():
    global remaining_time
    count_down(remaining_time)
    if reps % 2 != 0:
        title_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
    else:
        title_label.config(text="Break", fg=PINK)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global remaining_time
    remaining_time = count
    count_min = math.floor(count / 60)  #gives back integer less than or equal to count ex. 4.9 gives 4

    if count_min <10:
        count_min = f"0{count_min}"
    count_sec = count %  60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text= f"{count_min}:{count_sec}")

    if count >0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
            check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg= YELLOW)

canvas = Canvas(width=200,height=224,bg= YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill= "white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)


#label
title_label = Label(text="Timer", fg=GREEN, bg= YELLOW, font=(FONT_NAME, 30))
title_label.grid(row=0, column=1)

check_label = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,12,"bold"))
check_label.grid(row=3,column=1)

#button
start_button = Button(text="Start",command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=2,column=2)

pause_button = Button(text="Pause",command=pause_timer)
pause_button.grid(row=4,column=0)

resume_button = Button(text="Resume",command=resume_timer)
resume_button.grid(row=4,column=2)


window.mainloop()