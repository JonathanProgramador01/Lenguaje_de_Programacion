import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generar_corazon(t,escala=1.0):
    x = escala*(16*np.sin(t)**3)
    y =escala*(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))
   
    return x,y

data = {
    "centro_x": [0,10,-10,5,-5],
    "centro_y": [0,10,-10,-5,5],
    "escala": [1,0.5,0.75,1.25,1]
    
}

df = pd.DataFrame(data)


fig, ax = plt.subplots()
t = np.linspace(0, 2 * np.pi, 1000)  


for _, row in df.iterrows():
    x, y = generar_corazon(t, row["escala"])
    #ax.fill(x,y)

    ax.plot(x + row["centro_x"], y + row["centro_y"])


ax.set_aspect("equal")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)


plt.show()
