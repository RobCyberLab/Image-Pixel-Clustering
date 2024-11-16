from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# Încărcarea imaginii
img = Image.open(r'D:\facult\A_Master\an1_sem2\SDMSC\Laborator\L8\dataset\spots.png').convert('L')

# Convertim imaginea într-un array numpy
data = np.array(img)

# Extragerea coordonatelor pixelilor negri
coordinates = np.column_stack(np.where(data == 0))

# Inițializarea modelului de clustering ierarhic cu legătură simplă
num_clusters = 3  # poți ajusta numărul de clustere conform necesităților
model = AgglomerativeClustering(n_clusters=num_clusters, linkage='single')
model.fit(coordinates)

# Etichetele clusterelor
labels = model.labels_

# Afișăm plot-ul într-o fereastră separată
plt.figure(figsize=(8, 6))
for i in range(num_clusters):
    plt.scatter(coordinates[labels == i, 0], coordinates[labels == i, 1], label=f'Cl{i+1}')
plt.title('Clustering ierarhic cu legătură simplă')
plt.xlabel('X')
plt.ylabel('Y')

# Adăugarea centroidilor
centroids_x = [np.mean(coordinates[labels == i, 0]) for i in range(num_clusters)]
centroids_y = [np.mean(coordinates[labels == i, 1]) for i in range(num_clusters)]
plt.scatter(centroids_x, centroids_y, c='black', s=100, alpha=0.75, label='C')

# Mutarea legendei în afara desenului
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
