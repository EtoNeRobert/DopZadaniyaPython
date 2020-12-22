from tkinter import *
from tkinter import messagebox
import random
import keyboard
 


colours = ['red','blue','grey','yellow','green','pink','black','orange','purple','red']


c = Canvas(width=1980,height=720,bg='white')
c.grid(row=1, column=1)

objects = []
ii = 1
val = IntVar()
val.set(6)

class Tfigure():
    
    def __init__(self, x, y):
        Tfigure.x = x
        Tfigure.y = y

    
    def moveto(dir, x):
        x = int(val.get())
        if x == 0:
            select = []
            for i in objects: #ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ОБЪЕКТОВ К КЛАССУ КРУГА 
                if isinstance(i,Oval) == 1 and isinstance(i,El) ==0:
                    select.append(i)
        elif x == 1:
            select = []
            for i in objects:  #ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ОБЪЕКТОВ К КЛАССУ ЭЛЛИПС 
                if isinstance(i,El) == 1:
                    select.append(i)
        elif x == 2:
            select = []
            for i in objects:  #ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ОБЪЕКТОВ К КЛАССУ ПРЯМОУГОЛЬНИК 
                if isinstance(i,Pr) == 1:
                    select.append(i)
        elif x == 3:
            select = []
            for i in objects:  #ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ОБЪЕКТОВ К КЛАССУ КВАДРАТ 
                if isinstance(i,Rect) == 1 and isinstance(i,Pr) ==0 and isinstance(i,Romb) ==0:
                    select.append(i)
        elif x == 4:
            select = []
            for i in objects:  #ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ОБЪЕКТОВ К КЛАССУ РОМБ 
                if isinstance(i,Romb) ==1:
                    select.append(i)
        elif x == 5:
            select = []
            for i in objects:  #ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ОБЪЕКТОВ К КЛАССУ ЛИНИЯ 
                if isinstance(i,Line) == 1:
                    select.append(i)
        elif x==6:
            select = objects  #ВЫБОР ВСЕХ ОБЪЕКТОВ
        for i in select:
            if dir == 'up':
                c.move(i.tag, 0, -14)
            elif dir == 'l':
                c.move(i.tag, -14, 0)    
            elif dir == 'r':
                c.move(i.tag, 14, 0)
            elif dir == 'down':
                c.move(i.tag, 0, 14)
        
    


class Oval(Tfigure):
    def __init__(self, x, y, r, colour, tag):
        Tfigure.__init__(self, x, y)
        self.x = x
        self.y = y
        self.tag = tag
        self.r = r
        self.colour = colour
    def show(self):
        ov = c.create_oval(self.x, self.y, self.x+self.r, self.y+self.r, fill=self.colour, tag = self.tag)
        

    def delete(self):
        c.delete(self.tag)
    
class Rect(Tfigure):
    def __init__(self, x, y, r, colour, tag):
        Tfigure.__init__(self, x, y)
        self.x = x
        self.y = y
        self.tag = tag
        self.r = r
        self.colour = colour
    def show(self):
        rec = c.create_rectangle(self.x, self.y, self.x+self.r, self.y+self.r, fill=self.colour, tag = self.tag)
        
    
    def delete(self):
        c.delete(self.tag)
       
class Line(Tfigure):
    def __init__(self, x, y, r, colour, tag):
        Tfigure.__init__(self, x, y)
        self.x = x
        self.y = y
        self.tag = tag
        self.r = r
        self.colour = colour
    def show(self):
        li = c.create_line(self.x, self.y, self.x+self.r, self.y, width=10, fill=self.colour, tag = self.tag)  
    
    def delete(self):
        
        c.delete(self.tag)
       
class El(Oval):
    
    def __init__(self, x, y, r, colour,tag, a):
        Oval.__init__(self, x, y, r, colour,tag)
        self.tag = tag
        self.a = a

    def show(self):
        el = c.create_oval(self.x, self.y, self.x+self.r, self.y+self.a, fill=self.colour, tag = self.tag)
        
    
    def delete(self):
        c.delete(self.tag)
    
    def rotate(xx):
        if xx == 1:
            for i in objects: #ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ОБЪЕКТОВ К КЛАССУ ЭЛЛИПС И ПОСЛЕЛУЮЩИЙ ПОВОРОТ
                if isinstance(i,El) == 1:
                    cords = c.coords(i.tag)
                    c.coords(i.tag, cords[0], cords[1], cords[0]+i.a, cords[1]+i.r)
                    
        
class Pr(Rect):
    def __init__(self, x, y, r, colour, tag, a):
        Rect.__init__(self, x, y,r, colour, tag)
        self.tag = tag
        self.a = a
    def show(self):
        pr = c.create_rectangle(self.x, self.y, self.x+self.r, self.y+self.a, fill=self.colour, tag = self.tag)

    def delete(self):
        
        c.delete(self.tag)
    
class Romb(Rect):
    def __init__(self, x, y, r, colour, tag):
        Rect.__init__(self, x, y,r, colour,tag)
        self.tag = tag
    def show(self):
        coords = [self.x + (self.r)/2, self.y, self.x + self.r, self.y + (self.r)/2,self.x + (self.r)/2, self.y + self.r, self.x, self.y + (self.r)/2]
        pr = c.create_polygon(coords, fill=self.colour, tag = self.tag)
  

    def delete(self):
         
        c.delete(self.tag)



classes = [Oval, El, Pr, Rect, Romb, Line]
objects = []  #СОЗДАНИЕ МАССИВА
check = 0

def cr_objects():
    global ii, objects, check
    if objects != []: #ПРОВЕРКА НА ЗАПОЛНЕННОСТЬ МАССИВА
        messagebox.showerror("Ошибка", "Удалите старый список")
    else:
        for i in range(14):
            r = random.randint(50,150)
            x = random.randint(0,(1980-r))
            y = random.randint(0,(720-r))
            tag = str(ii)
            ii+=1
            colour = colours[random.randint(0,len(colours)-1)]
            cl = classes[random.randint(0,len(classes)-1)]
            if str(cl) != "<class '__main__.Pr'>" and str(cl)!= "<class '__main__.El'>":
                o = cl(x,y,r, colour, tag)
                
                objects.append(o) #ДОБАВЛЕНИЕ ОБЪЕКТА В МАССИВ
            else:
                a = random.randint(30,150)
                o = cl(x,y,r, colour, tag, a)
                
                objects.append(o) #ДОБАВЛЕНИЕ ОБЪЕКТА В МАССИВ
        check = 1

def show_objects():
    global objects, check
    
    if check == 0:
        messagebox.showerror("Ошибка", "Удалите старый список")
    else:
        for i in range(len(objects)): #ПОКАЗ КАЖДОГО ОБЪЕКТА ИЗ МАССИВА
            objects[i].show()
        movebttns()
        check = 0


def dl_objects():
    global check
    objects.clear() #ОЧИЩЕНИЕ МАССИВА
    c.delete(ALL)
    check = 1

_x = StringVar()
_y = StringVar()
entry_x = Entry(textvariable=_x)
entry_y = Entry(textvariable=_y)
entry_x.place(x = 150, y = 730)
entry_y.place(x = 150, y = 760)




rb1 = Radiobutton(text="Круг", variable=val, value=0)
rb1.place(x = 100, y = 850)
rb2 = Radiobutton(text="Эллипс", variable=val, value=1)
rb2.place(x = 100, y = 870)
rb3 = Radiobutton(text="Прямоугольник", variable=val, value=2)
rb3.place(x = 100, y = 890)
rb4 = Radiobutton(text="Квадрат", variable=val, value=3)
rb4.place(x = 100, y = 910)
rb5 = Radiobutton(text="Ромб", variable=val, value=4)
rb5.place(x = 100, y = 930)
rb6 = Radiobutton(text="Линия", variable=val, value=5)
rb6.place(x = 100, y = 950)
rb7 = Radiobutton(text="Всё", variable=val, value=6)
rb7.place(x = 100, y = 970)

def show():
    try:
        c.delete('bck')
    except:
        pass
def hide():
    c.create_rectangle(0,0,1920,770,fill='white',tag='bck')
def movebttns():

    keyboard.add_hotkey('w', lambda:Tfigure.moveto('up',val.get()))
    
    keyboard.add_hotkey('a', lambda:Tfigure.moveto('l',val.get()))
   
    keyboard.add_hotkey('d', lambda:Tfigure.moveto('r',val.get()))
    
    keyboard.add_hotkey('s', lambda:Tfigure.moveto('down',val.get()))
    

def moveto_point(xx,yy):
    for i in objects: #ПЕРЕМЕЩЕНИЕ КАЖДОГО ОБЪЕКТА ИЗ МАССИВА В ТОЧКУ
        if isinstance(i,Romb) ==1:
            c.coords(i.tag, xx + (i.r)/2, yy, xx + i.r, yy + (i.r)/2,xx + (i.r)/2, yy + i.r, xx, yy + (i.r)/2)
        
        else:
            c.coords(i.tag,xx,yy,xx+i.r,yy+i.r)
                
btn1 = Button(text="Создать 14 фигур", command= cr_objects)
btn1.place(x = 10, y = 730)

btn2 = Button(text="Показать фигуры", command= show_objects)
btn2.place(x = 10, y = 760)

btn3 = Button(text="Удалить", command=dl_objects)
btn3.place(x = 10, y = 790)

btn8 = Button(text="Переместить в точку", command= lambda: moveto_point(int(_x.get()),int(_y.get())))
btn8.place(x = 10, y = 820)

btn10 = Button(text= 'Перевернуть', command= lambda: El.rotate(int(val.get())))
btn10.place(x = 560, y = 760,height = 30, width=70)

btn12 = Button(text= 'Скрыть', command= hide)
btn12.place(x = 560, y = 850,height = 30, width=70)
btn13 = Button(text= 'Показать', command= show)
btn13.place(x = 560, y = 880,height = 30, width=70)

mainloop()