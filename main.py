from turtle import pu as penup
from turtle import pd as pendown
from turtle import *

def carre(taille):
    begin_fill()
    for _ in range(4):
        forward(taille)
        right(90)
    end_fill()

def main():
    carre(100)

    mainloop()

if __name__ == '__main__':
    main()