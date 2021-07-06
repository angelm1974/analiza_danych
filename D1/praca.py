from moje_funkcje import make_pizza as mp, suma_opcjonalna as so
import matplotlib.pyplot as plt

mp(34,'szynka','pieczarki','pasta pom')
print(so(44))


dane=[1,4,9,16,25,36]
fig,ax=plt.subplots()
ax.plot(dane)
plt.show()