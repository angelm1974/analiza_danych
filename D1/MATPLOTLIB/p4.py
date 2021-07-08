import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots(figsize=(8, 4))

r = np.linspace(0, 5, 100) #podobnie działa jak range
a = 4 * np.pi * r ** 2 # wzór na powierzchnie
v = (4 * np.pi/3) * r ** 3 #wzór na objętość kuli
ax1.set_title("Powierzchnia i objętość kuli", fontsize=16) #tytuł
ax1.set_xlabel("Promień [m]", fontsize=14) #oś x etykietka
ax1.plot(r, a, lw=2, color='blue') #pierwsza krzywa
ax1.set_ylabel(r"Powierzchnia ($m^2$)", fontsize=14, color='blue') # oś y etykietka
for label in ax1.get_yticklabels(): # tutaj pętelka po etykietach ale na osi
    label.set_color("blue") #ustawiamy kolorek 

ax2 = ax1.twinx() #ustawienie drugiej osi y
ax2.plot(r, v, lw=2, color='red') 
ax2.set_ylabel(r"Objętość ($m^3$)", fontsize=14, color='red')
for label in ax2.get_yticklabels():
    label.set_color("red")

ax1.annotate("Tu są cuda <3", family='serif', fontsize=12, xy=(2, 50), xycoords='data',
             xytext=(+20, +50), textcoords='offset points',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5')) # a tu bonusik
plt.show() 
