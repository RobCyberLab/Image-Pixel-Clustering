import sqlite3
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

# Definirea variabilei globale last_label_id
last_label_id = 0

# Definirea variabilei globale pentru numărul total de apeluri ale funcției de distanță
total_distance_calls = 0

# Funcția pentru convertirea imaginii în matrice de date
def image_to_data(image_path):
    global width, height
    img = Image.open(image_path)
    width, height = img.size
    pixel_array = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if pixel == 0 or pixel == (0, 0, 0, 255):
                pixel_array[y][x] = 1
            else:
                pixel_array[y][x] = 0
    return pixel_array

# Încărcarea imaginii și conversia acesteia în matrice de date
binary_image = np.array(image_to_data(r'D:\facult\A_Master\an1_sem2\SDMSC\Laborator\L8\dataset\stripes.png'))

# Extragerea coordonatelor pixelilor negri
coordinates = np.column_stack(np.where(binary_image == 1))

# Afișăm numărul de puncte negre detectate înainte de clusterizare
print("Numărul de puncte negre detectate:", len(coordinates))

# Clusterează celulele vecine
def clusterize_cells(cells, labels, distance):
    global last_label_id, total_distance_calls
    height, width = cells.shape  # Obține dimensiunile imaginii
    for i in range(height):
        for j in range(width):
            if cells[i, j] == 1 and labels[i, j] == 0:
                cluster = []
                stack = [(i, j)]
                # Incrementăm ID-ul clusterului la fiecare iterație
                last_label_id += 1
                cluster_id = last_label_id
                while stack:
                    x, y = stack.pop()
                    if 0 <= x < height and 0 <= y < width and cells[x, y] == 1 and labels[x, y] == 0:
                        cluster.append((x, y))
                        labels[x, y] = cluster_id
                        # Incrementăm numărul total de apeluri ale funcției de distanță
                        total_distance_calls += 1
                        # Modificăm lista de vecini în funcție de distanța specificată
                        neighbors = [(x + dx, y + dy) for dx in range(-distance, distance + 1) for dy in range(-distance, distance + 1)]
                        neighbors = [(x, y) for x, y in neighbors if 0 <= x < height and 0 <= y < width]
                        stack.extend(neighbors)
    return labels


# Clusterează celulele și actualizează matricea labels
distance = int(input("Introduceți distanța de clusterizare: "))
labels = np.zeros_like(binary_image, dtype=int)  # Creează matricea de etichete folosind dimensiunile imaginii
labels = clusterize_cells(binary_image, labels, distance)
print("Numărul de clustere detectate:", last_label_id)

# Conectarea la baza de date
conn = sqlite3.connect('coord_database.db')
cursor = conn.cursor()

# Crearea tabelului pentru coordonatele punctelor negre
cursor.execute('''CREATE TABLE IF NOT EXISTS black_points
                  (id INTEGER PRIMARY KEY, x INTEGER, y INTEGER)''')

# Inserarea coordonatelor punctelor negre în baza de date
for coord in coordinates:
    x, y = coord
    cursor.execute("INSERT INTO black_points (x, y) VALUES (?, ?)", (int(x), int(y)))  # Convertem coordonatele la întregi


# Salvarea modificărilor și închiderea conexiunii
conn.commit()
conn.close()

# Plotează imaginea originală
plt.figure(figsize=(8, 8))
plt.imshow(binary_image, cmap='gray')
plt.title('Lab9')

# Plotează punctele negre
plt.scatter(coordinates[:, 1], coordinates[:, 0], color='black', s=5)

# Plotează punctele clusterilor detectați
cmap = ListedColormap(np.random.rand(last_label_id, 3))
for i in range(1, last_label_id + 1):
    cluster_points = np.argwhere(labels == i)
    print(f"Cluster {i} are {len(cluster_points)} puncte.")
    for coord in cluster_points:
        x, y = coord
        plt.scatter(y, x, color=cmap(i - 1), s=5)

# Afișează numărul total de apeluri ale funcției de distanță
print("Numărul total de apeluri ale funcției de distanță:", total_distance_calls)

# Adaugă legenda în dreapta plotului
legend_elements = [Patch(facecolor=cmap(i - 1), edgecolor='black', label=f'Cluster {i}') for i in range(1, last_label_id + 1)]
plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))

# Setează poziția axei y la partea de sus a plotului
plt.gca().xaxis.set_ticks_position('top')

# Ajustează spațiul plotului pentru a include întreaga imagine
plt.tight_layout()

# Afișează plot
plt.show()