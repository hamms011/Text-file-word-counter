from tkinter import *
from tkinter import filedialog

main = Tk()
main.title(".TXT File Word Counter")
main.resizable(height=FALSE, width=FALSE)
main.geometry('500x400')
main.configure(bg='#757575')

labelfont = ("Arial", 14, "bold")

result = dict()

def clear_text():
    textfield.delete(0, END)
    ShowCountedWords.delete(1.0, END)

def open_file():
    main.filename = filedialog.askopenfilename()

def count_word(file):
    fileOpen = open(str(file), 'r')
    fullText = fileOpen.readlines()
    fileOpen.close()
    for word in textfield.get().split(', '):
        for text in fullText:
            if word in result:
                result[word] = result[word] + text.count(word)
            else:
                result[word] = text.count(word)
    ShowCountedWords.delete(1.0, END)
    for key, value in result.items():
        ShowCountedWords.insert('1.0', '{0} : {1} \n'.format(key, value))

    result.clear()


heading = Label(main, text=".TXT File Word Counter")
heading.place(x=150, y=2)
heading.config(bg="#757575", font=labelfont, fg="#ffffff")

textfield = Entry()
textfield.place(x=3, y=30)
textfield.config(width=81, borderwidth=2)

btnSelectFile = Button(main, text="Select .txt File", command=lambda : open_file())
btnSelectFile.place(x=4, y=60)
btnSelectFile.config(width=20, bg="#66BB6A")

btnCount = Button(main, text="Count Words", command=lambda : count_word(main.filename))
btnCount.place(x=173, y=60)
btnCount.config(width=20, bg="#42A5F5")

btnClear = Button(main, text="Clear", command=lambda : clear_text())
btnClear.place(x=344, y=60)
btnClear.config(width=20, bg="#ef5350")

ShowCountedWords = Text(main, height=18, width=61)
ShowCountedWords.place(x=4, y=100)
ShowCountedWords.config(bg="#616161", fg="#ffffff")


main.mainloop()