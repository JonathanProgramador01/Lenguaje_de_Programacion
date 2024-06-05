import pandas as pd
import matplotlib.pyplot as plt

cuerpo_c = {
    "x":[1,1,4,4,1],
    "y":[1,3,3,1,1]
}
techo_c = {
    "x":[1,2.5,4,1],
    "y":[3,4.5,3,3]
}

df_cuerpo = pd.DataFrame(cuerpo_c)
df_techo = pd.DataFrame(techo_c)

plt.plot(df_cuerpo["x"],df_cuerpo["y"], marker = "o")
plt.plot(df_techo["x"],df_techo["y"],marker="o",color = "blue")

plt.title("uso de pandas y matplotlib")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)
plt.axis("equal")
plt.show()
