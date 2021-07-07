import matplotlib.pyplot as plt

godziny=range(1,10)
plt.style.use('seaborn-darkgrid')
fig,ax=plt.subplots()
ax.pie(godziny)

plt.show()