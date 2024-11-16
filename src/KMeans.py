import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class KMeansClustering:
    def __init__(self, coordinates, k, threshold=0.01, max_iterations=100):
        self.coordinates = coordinates
        self.k = k
        self.threshold = threshold
        self.max_iterations = max_iterations
        self.total_distance_calls = 0  # Numărul total de apeluri ale funcției de distanță

    def euclidean_distance(self, point1, point2):
        self.total_distance_calls += 1
        x1, y1 = point1
        x2, y2 = point2
        distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance

    def initialize_centroids(self):
        indices = np.random.choice(len(self.coordinates), size=self.k, replace=False)
        centroids = [self.coordinates[i] for i in indices]
        return centroids

    def assign_to_clusters(self, centroids):
        clusters = [[] for _ in range(self.k)]
        for point in self.coordinates:
            distances = [self.euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid_index = np.argmin(distances)
            clusters[closest_centroid_index].append(point)
        return clusters

    def update_centroids(self, clusters):
        centroids = [np.mean(cluster, axis=0) for cluster in clusters]
        return centroids

    def k_means(self):
        centroids = self.initialize_centroids()
        for _ in range(self.max_iterations):
            old_centroids = centroids.copy()
            clusters = self.assign_to_clusters(centroids)
            centroids = self.update_centroids(clusters)
            if np.linalg.norm(np.array(centroids) - np.array(old_centroids)) < self.threshold:
                break
        return clusters

# Încărcarea imaginii
img = Image.open(r'D:\facult\A_Master\an1_sem2\SDMSC\Laborator\L8\dataset\circles.png').convert('L')

# Convertirea imaginii într-un array numpy
data = np.array(img)

# Extrage coordonatele pixelilor negri
coordinates = np.column_stack(np.where(data == 0))

# Parametrul k pentru K-Means
k = 2

# Crearea obiectului KMeansClustering
k_means_clusterer = KMeansClustering(coordinates, k)

# Calcularea numărului total de apeluri ale funcției de distanță
k_means_clusterer.k_means()

# Afișarea numărului total de apeluri ale funcției de distanță
print("Numărul total de apeluri ale funcției de distanță în K-Means:", k_means_clusterer.total_distance_calls)

# Clustering folosind K-Means
clusters = k_means_clusterer.k_means()

# Plotting the image
plt.imshow(data, cmap='gray')

# Adding squares for each cluster
for cluster in clusters:
    cluster_x = [point[1] for point in cluster]  # X coordinates of points in the cluster
    cluster_y = [point[0] for point in cluster]  # Y coordinates of points in the cluster
    plt.scatter(cluster_x, cluster_y, alpha=0.5)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Clustering')

# Inverting the y-axis to have it on top
plt.gca().invert_yaxis()

plt.show()
