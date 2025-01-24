import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)
y4 = np.tan(x) * 0.1  # Escalado para evitar valores extremos

# Crear un canvas con 2 filas y 2 columnas de subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 filas, 2 columnas

# Gráfico 1 (arriba izquierda)
axs[0, 0].plot(x, y1, color="blue")
axs[0, 0].set_title("Seno")

# Gráfico 2 (arriba derecha)
axs[0, 1].plot(x, y2, color="green")
axs[0, 1].set_title("Coseno")

# Gráfico 3 (abajo izquierda)
axs[1, 0].plot(x, y3, color="orange")
axs[1, 0].set_title("Seno x Coseno")

# Gráfico 4 (abajo derecha)
axs[1, 1].plot(x, y4, color="red")
axs[1, 1].set_title("Tangente (escalada)")

# Mejorar diseño
plt.tight_layout()

# Mostrar los gráficos
plt.show()
