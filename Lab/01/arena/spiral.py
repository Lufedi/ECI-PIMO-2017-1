__author__ = 'luisfediaz'


from sys import stdin
import math
def main():
    lines =  stdin.readlines()
    for l in lines:
        data = l.split(" ")
        size = int(data[0])
        p = int(data[1])
        if(size + p != 0):
            x = size/2+1
            y=size/2+1
            I=1
            i=I
            pmo=1
            J=1
            j=J
            why=True
            p-=1
            while(p > 0):
                if(why):
                    y += pmo
                else:
                    x += pmo
                i-=1
                j-=1
                if(i==0):
                    I+=2
                    i = I
                    pmo *= -1
                if(j==0):
                    if(not why):J += 1
                    j = J;
                    why =  not why;
                p-=1
            print("Line = %d, column = %d."% (y,x))

def main2():
    lines =  stdin.readlines()
    for l in lines:
        data = l.split(" ")
        N = int(data[0])
        num = int(data[1])
        if(N + num != 0):
            cont = 1
            avance = 1
            i  =  N / 2
            j = N / 2
            orFil = True
            dir = True
            seguir = True
            while(seguir):
                for l in range(0,2):
                    if(seguir):
                        if(orFil):
                            if(dir):
                                i-= avance
                            else:
                                i+= avance
                        else:
                            if(dir):
                                j-= avance
                            else:
                                j+= avance;
                        cont+= avance
                        if(cont >= num):
                            dif = cont - num
                            if(orFil):
                                if(dir):
                                    i+= dif
                                else:
                                    i-= dif
                            else:
                                if(dir):
                                    j+= dif
                                else:
                                    j-= dif
                            seguir = False
                        orFil = not orFil
                dir = not dir
                avance+=1
            print("Line = %d, column = %d."%((N - i)+1, (j + 1)))

main2()