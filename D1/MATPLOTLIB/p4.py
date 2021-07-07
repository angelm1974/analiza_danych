import matplotlib.pyplot as plt
import numpy as np

fig, axl = plt.subplots(figsize=(8, 4))
r = np.linspace(0, 5, 100)
a = 4 * np.pi * r ** 2
v = (4 * np.pi/3) * r ** 3
axl.set_title("Powierzchnia i objętość kuli", fontsize=16)
axl.set_xlabel("Promień [m]", fontsize=14)
axl.plot(r, a, lw=2, color='blue')
axl.set_ylabel(r"Powierzchnia ($m^2$)", fontsize=14, color='blue')
for label in axl.get_yticklabels():
    label.set_color("blue")

ax2=axl.twinx()
ax2.plot(r,v, lw=2, color='red')
ax2.set_ylabel(r"Objętość ($m^3$)", fontsize=14, color='red')
for label in ax2.get_yticklabels():
    label.set_color("red")

plt.show()
