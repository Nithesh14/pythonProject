import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x,np.sin(x));
plt.plot(x,np.sin(x-0))
plt.plot(x,np.sin(x-1))
plt.plot(x,np.sin(x-2))
plt.plot(x,np.sin(x-3))
plt.plot(x,np.sin(x-4))
plt.plot(x,np.sin(x-5))
