import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,1000)
y=np.sin(2*np.pi*1*x)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)


plt.show()