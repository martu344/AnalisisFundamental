import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from indicadores.cpi import df
from indicadores.tasas_de_interes import df_tasas
from indicadores.desempleo import df_desempleo
from indicadores.consumidor import df_sentimiento

# Crear un canvas con 2 filas y 2 columnas de subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 filas, 2 columnas

# Gráfico 1 (arriba izquierda)
axs[0, 0].plot(df["Fecha"], df["CPI"], marker="o", color="blue")
axs[0, 0].set_title("CPI")

# Gráfico 2 (arriba derecha)
axs[0, 1].plot(df_tasas["Fecha"], df_tasas["Tasa"], marker="o", color="blue")
axs[0, 1].set_title("Tasas")

# Gráfico 3 (abajo izquierda)
axs[1, 0].plot(df_desempleo["Fecha"], df_desempleo["desempleo"], marker="o", color="blue")
axs[1, 0].set_title("Desempleo")

# Gráfico 4 (abajo derecha)
axs[1, 1].plot(df_sentimiento["Fecha"], df_sentimiento["sentimiento"], marker="o", color="blue")
axs[1, 1].set_title("Sentimiento")

# Ajustar el tamaño del texto
plt.rcParams.update({'font.size': 6})

# Añadir cursores a cada subplot
cursors = []
for ax in axs.flat:
    cursor = Cursor(ax, useblit=True, color='red', linewidth=1, linestyle='--')
    cursors.append(cursor)

# Mejorar diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()
