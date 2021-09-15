from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Tk
from tkinter import Button


root = Tk()
root.title("TicTacToe Game")
pixel_image = PhotoImage(width=1, height=1)


def x_clicked(button):
    global x_or_o
    if button['text'] == ' ':
        button['text'] = 'X'
        button.configure(bg="blue", fg="white")
        x_or_o = 'O'
        check_win()
    else:
        messagebox.showerror("Error", "Already taken! Choose again.")


def o_clicked(button):
    global x_or_o
    if button['text'] == ' ':
        button['text'] = 'O'
        button.configure(bg="red", fg="white")
        x_or_o = 'X'
        check_win()
    else:
        messagebox.showerror("Error", "Already taken! Choose again.")


def user_clicked_button(button, x_or_o):
    if x_or_o == 'X':
        x_clicked(button)
    else:
        o_clicked(button)


def check_win():
    #  horizontal win
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    #  vertical win
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    #  diagonal win
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        messagebox.showinfo("Winner!", "X Won")
        startgame()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        messagebox.showinfo("Winner!", "O Won")
        startgame()
    #  Tie
    elif b1['text'] != ' ' and b2['text'] != ' ' and b3['text'] != ' ' and b4['text'] != ' ' and b5['text'] != ' ' and \
            b6['text'] != ' ' and b7['text'] != ' ' and b8['text'] != ' ' and b9['text'] != ' ':
        messagebox.showinfo("Tie!", "There is no winner.")
        startgame()


# Buttons
def startgame():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global x_or_o

    x_or_o = 'X'  # Who starts.

    # Buttons
    b1 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b1, x_or_o))
    b2 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b2, x_or_o))
    b3 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b3, x_or_o))
    b4 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b4, x_or_o))
    b5 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b5, x_or_o))
    b6 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b6, x_or_o))
    b7 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b7, x_or_o))
    b8 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b8, x_or_o))
    b9 = Button(root, text=' ', height=100, width=100, font=("Arial", 40), image=pixel_image, compound='c',
                command=lambda: user_clicked_button(b9, x_or_o))

    # Grid
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


startgame()
root.mainloop()

