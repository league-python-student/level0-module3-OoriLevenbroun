from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    a = simpledialog.askstring(title='...', prompt='this is a chose your own adventure story do you wish to proceed')
    if a == 'yes':
        pass
    elif a == 'no':
        exit(0)
# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
