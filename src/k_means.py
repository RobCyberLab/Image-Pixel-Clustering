from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Încărcarea imaginii
img = Image.open(r'D:\facult\A_Master\an1_sem2\SDMSC\Laborator\L8\dataset\full.png').convert('L')

# Convertim imaginea într-un array numpy
data = np.array(img)

# Extragerea coordonatelor pixelilor negri
coordinates = np.column_stack(np.where(data == 0))

# Inițializarea modelului KMeans
kmeans = KMeans(n_clusters=10000)  # poți ajusta numărul de clustere conform necesităților
kmeans.fit(coordinates)

# Etichetele clusterelor
labels = kmeans.labels_

# Centroidii clustere
centroids = kmeans.cluster_centers_

# Afișăm plot-ul într-o fereastră separată
plt.figure(figsize=(8, 6))
for i in range(len(centroids)):
    plt.scatter(coordinates[labels == i, 0], coordinates[labels == i, 1], label=f'Cl{i}')
plt.scatter(centroids[:, 0], centroids[:, 1], c='k', s=100, alpha=0.75, label='C')  # Centroidii sunt marcați cu negru
plt.title('K-Means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()