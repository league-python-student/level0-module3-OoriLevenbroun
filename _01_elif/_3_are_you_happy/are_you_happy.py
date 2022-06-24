from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    h = simpledialog.askstring(title='H3l!0', prompt='are you happy(this is a yes or no quistoin)')
    if h == 'yes':
        messagebox.showinfo(message='keep doing whatever you are doing')
    elif h == 'no':
        h2 = simpledialog.askstring(title='...', prompt='Do you want to be happy?')
    if h2 == 'yes':
        messagebox.showinfo(message='then change SOMEthing')
    elif h2 == 'no':
        messagebox.showinfo(message='keep doing whatever you are doing')
    pass
