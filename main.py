import time
import math

def carre(taille):
    pensize(taille)
    fd(taille)
    pensize(1)

def triangle(base):
    height = base
    precision = 1
    current_base = 0

    for i in range(int(height * precision)):
        slope = base / (2 * height * precision)
        current_base = i * slope

        lt(90); fd(current_base); bk(current_base * 2); fd(current_base)
        rt(90); fd(1 / precision)

def ligne(base, taille, n):
    for _ in range(n):
        triangle(base)
        carre(taille)

def spirale(base, taille, nbFormes):
    current_nbFormes = 1

    while current_nbFormes <= nbFormes:
        for _ in range(2):
            # for forme in range(current_nbFormes):
            #     triangle(base)
            #     carre(taille)
            ligne(base, taille, current_nbFormes)
            lt(90)
        current_nbFormes += 1

def spiraleTournante(base, taille, nbFormes, vAng):
    fps = 100
    angle = 0
    i = 0
    while i < 1000:
        clear()
        rt(angle)
        start = time.time()
        spirale(base, taille, nbFormes)
        angle += vAng
        #if i >= 10: print('Hello')
        i += 1
        
  
        
        #elapsed_time = time.time() - start
        #print(elapsed_time)
        while (time.time() - start) < 0.25:#(1 / fps):
            time.sleep(0.1)
            pass

if __name__ == '__main__':
    #carre_codeboot(100)
    #triangle(100)
    #goto(-100, 0); ligne(20, 10, 5)
    #spirale(10, 10, 10)
    spiraleTournante(15, 10, 10, 2)
