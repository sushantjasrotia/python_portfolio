from tkinter import *

#Logic

user_text = ""
timer = None


# method to do the main calculations
def start_calculating(event):

    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)

    # keysym property of event simply tell us which key was pressed
    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]

    # we access the character of the key using char property.
    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)

    return

def reset_app():
    # get the global variable timer and set it to none again
    global timer, user_text

    typing_area.delete('1.0', 'end')
    #1.0 is starting text and end is last text
    user_text = ""
    timer = None
    return

def save_text():
    global user_text
    if user_text == "":
        return
    try:
        f = open('writeups.txt', 'r')
    except FileNotFoundError:
        f = open('writeups.txt', 'w')
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'

        with open('writeups.txt', 'a') as f :
            f.write(text_to_write)
            user_text = ""
    finally:
        return






# colors

BORDER = "#BDBDBD"
FG = "khaki"
BG = "#607D8B"

#font families
FONT_FAMILY1 = 'Calibri'
FONT_FAMILY2 = 'Helvetica'

#font size
FONT_SIZE1 = 14
FONT_SIZE2 = 18
FONT_SIZE3 = 24

# Font styles

FONT_STYLE1 = 'normal'
FONT_STYLE2 = 'italic'
FONT_STYLE3 = 'bold'

# creating a font from family, style and size for the UI
PARA_FONT = (FONT_FAMILY1, FONT_SIZE1, FONT_STYLE3)
PARA_FONT2 = (FONT_FAMILY1, 12, FONT_SIZE2)
HEAD_FONT = (FONT_FAMILY2, FONT_SIZE3, FONT_STYLE1)

# welcoming heading of our UI
heading = "WRITE WITH MAGICAL INK"
# instruction to use app
instruction = ("If you don't press any key for 5 seconds,"
               "the text you have written  will disappear")


# CREATING THE WINDOW IN WHICH OUR PROGRAM IS SEEN.

window = Tk()
window.title('Disappearing Text Destop App')
window.config(bg=BG, padx=20, pady=10)

# CREATING WIDGET FOR OUR APPLICATION

#heading.
heading = Label(text=heading, font=HEAD_FONT,
                bg=BG, fg=FG, padx=10, pady=10)

#instruction
instruction = Label(text=instruction, font=HEAD_FONT ,
                   fg=FG, bg=BG, pady=10)

typing_area = Text(font=PARA_FONT, bg=BG, fg=FG,
                   width=100, height=15, wrap='w',
                   highlightcolor=BORDER,
                   highlightthickness=4,
                   highlightbackground=BORDER,
                   padx=5, pady=5)

# adding function to text area, this used for calucalion for the applicaiton

typing_area.bind('<KeyPress>', start_calculating)

#reset button for reset the application

reset_btn = Button(text='Reset', fg=FG, bg=BG, font=PARA_FONT,
                   highlightbackground=FG,
                   highlightcolor=FG,
                   highlightthickness=0, border=3,
                   command=reset_app, width=50)

#a save button for user to save his text in a text file
save_btn = Button(text='Save', fg=FG, bg=BG,
                  font=PARA_FONT,
                  highlightbackground=FG,
                  highlightcolor=FG, highlightthickness=0,
                  border=3,
                  command=save_text, width=50)

# Placing the widgets on the window
heading.grid(row=0, column=0, columnspan=3)
instruction.grid(row=2, column=0, columnspan=3)
typing_area.grid(row=3, column=0, columnspan=3)
reset_btn.grid(row=4, column=0)
save_btn.grid(row=4, column=2)


window.mainloop()























