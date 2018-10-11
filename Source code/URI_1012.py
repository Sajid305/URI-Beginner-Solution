
A=input()
B=input()
C=input()
pi = 3.14159
triangulo = (float(A) * float(C))/2                                           # uri 1012
circulo = pi * (float(C)* float(C))
trapezio = float(C) *(float(A) + float(B)) / 2
quadrado = float(B) * float(B)
retangulo = float(A) * float(B)
print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))
