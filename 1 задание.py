from tkinter import *


dictionary = {"Й":".---","Ц":"-.-.","У":"..-","К":"-.-","Е":".","Н":"-.","Г":"--.","Ш":"----","Щ":"--.-","З":"--..","Х":"....","Ъ":".--.-.","Ф":"..-.","Ы":".-..","В":".--","А":".-","П":".--.","Р":".-.","О":"---","Л":".-..","Д":"-..","Ж":"...-","Э":"..-..","Я":".-.-","Ч":"---.","С":"...","М":"--","И":"..","Т":"-","Б":"-...","Ю":".--","Я":".-.-"}
root = Tk()
def translate():   
    x = tex.get()
    x = x.upper()
    x = x.split()
    result = ''
    for i in range(len(x)):
        for j in range(len(x[i])):
            result+=dictionary[x[i][j]] + ' '
        result+='   '
    
    res = Label(root, text = result, font = "Arial 30")
    res.pack()

tex = StringVar()
root.geometry('800x800')
ent = Entry(root, width=50, bd=10, textvariable = tex)
ent.pack()
but1 = Button(root, text = "Перевести", width = 25, height = 10,command = translate)
but1.pack()

mainloop()