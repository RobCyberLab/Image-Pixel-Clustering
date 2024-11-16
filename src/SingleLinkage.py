import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math


class SingleLinkageClustering:
    def __init__(self, coordinates, threshold):
        self.coordinates = coordinates
        self.threshold = threshold
        self.total_distance_calls = 0  # Numărul total de apeluri ale funcției de distanță

    def euclidean_distance(self, point1, point2):
        self.total_distance_calls += 1
        x1, y1 = point1
        x2, y2 = point2
        distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance

    def calculate_total_distance_calls(self):
        n = len(self.coordinates)
        self.total_distance_calls = math.comb(n, 2)

    def single_linkage(self):
        clusters = [[(x, y)] for x, y in self.coordinates]
        while len(clusters) > 1:
            min_distance = float('inf')
            closest_clusters = None

            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    for point1 in clusters[i]:
                        for point2 in clusters[j]:
                            distance = self.euclidean_distance(point1, point2)
                            if distance < min_distance:
                                min_distance = distance
                                closest_clusters = (i, j)

            if min_distance > self.threshold:
                break

            i, j = closest_clusters
            clusters[i].extend(clusters[j])
            del clusters[j]

        return clusters


# Încărcarea imaginii
img = Image.open(r'D:\facult\A_Master\an1_sem2\SDMSC\Laborator\L8\dataset\spots.png').convert('L')

# Convertirea imaginii într-un array numpy
data = np.array(img)

# Extrage coordonatele pixelilor negri
coordinates = np.column_stack(np.where(data == 0))

# Parametrul threshold
threshold = 100

# Crearea obiectului SingleLinkageClustering
single_linkage_clusterer = SingleLinkageClustering(coordinates, threshold)

# Calcularea numărului total de apeluri ale funcției de distanță
single_linkage_clusterer.calculate_total_distance_calls()

# Afișarea progresului în calculul numărului total de apeluri ale funcției de distanță
print("Calculul numărului total de apeluri ale funcției de distanță...")
print("Progres:", end=" ")

for i in range(single_linkage_clusterer.total_distance_calls):
    if i % 100 == 0:  # Afișăm progresul la fiecare 100 de apeluri
        print(i, end=" ")
print(single_linkage_clusterer.total_distance_calls)

# Clustering folosind single linkage
clusters = single_linkage_clusterer.single_linkage()

# Afisarea numărului total de apeluri ale funcției de distanță
print("\nNumărul total de apeluri ale funcției de distanță:", single_linkage_clusterer.total_distance_calls)

# Plotting the image
plt.imshow(data, cmap='gray')

# Adding squares for each cluster
for cluster in clusters:
    cluster_x = [point[1] for point in cluster]  # X coordinates of points in the cluster
    cluster_y = [point[0] for point in cluster]  # Y coordinates of points in the cluster
    plt.scatter(cluster_x, cluster_y, alpha=0.5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Single Linkage Clustering')

# Inverting the y-axis to have it on top
plt.gca().invert_yaxis()

plt.show()