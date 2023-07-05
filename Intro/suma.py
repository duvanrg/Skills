import sys
import termios
import tty
import os

os.system("clear")
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Presione cualquier tecla para continuar...")
getch()

a = (int(input("ingrese el numero a: ")))
b = (int(input("ingrese el numero b: ")))

print(f"la suma de {a} y {b} es {a+b}")

