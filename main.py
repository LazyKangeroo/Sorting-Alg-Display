import random
import tkinter
import turtle
import time

class Main:
    def __init__(self):
        self.array = []
        self.tk = tkinter
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.bgcolor('black')
        turtle.tracer(4)

    def run(self):
        self.getList()
        self.draw(0,False)
        self.bubble()
        self.tk.mainloop()

    def bubble(self):
        flag = False
        while not flag:
            flag = True
            for i in range(len(self.array) - 1):
                temp = 0
                if self.array[i] > self.array[i+1]:
                    temp = self.array[i]
                    self.array[i] = self.array[i +1]
                    self.array[i+1] = temp
                    flag = False
                    self.draw(i+1,True)
        print(self.array)

    def getList(self):
        for i in range(1,15):
            self.array.append(i)
            random.shuffle(self.array)
        print(self.array)

    def draw(self,sort,beingSorted):
        time.sleep(1)
        self.t.clear()
        for index,item in enumerate(self.array):
            self.move(index,item * 20)
            if beingSorted and sort == index:
                self.t.fillcolor('pink')
                self.t.begin_fill()
                self.draw_sorting(index)
                self.t.end_fill()
            else:
                self.t.fillcolor('green')
                self.t.begin_fill()
                self.draw_sorting(index)
                self.t.end_fill()

    def draw_sorting(self,index):
        for i in range(4):
            if i % 2 == 0:
                self.t.forward(20)
                self.t.right(90)
            else:
                self.t.forward(20 * self.array[index])
                self.t.right(90)

    def move(self,index,height):
        self.t.penup()
        self.t.goto(index * 22, -50 + height)
        self.t.pendown()

if __name__ == '__main__':
    main = Main()
    main.run()