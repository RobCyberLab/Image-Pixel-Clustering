# 🌀Image Pixel Clustering📏

Note: Due to privacy policies, I am not allowed to post the dataset publicly.

---

## Table of Contents📋
1. [Overview](#overview)
2. [Clustering Techniques](#clustering-techniques)
3. [Dataset Description](#dataset-description)
4. [Distance Metric](#distance-metric)
5. [Neighbor-Based Clustering](#neighbor-based-clustering)

---

## Overview📖
In this laboratory, we will test at least two of the following clustering techniques:
- **k-means**
- **Single Linkage**

---

## Clustering Techniques🌀
The focus of this lab is to experiment with and understand the following clustering methods:

1. **k-means**  
   - **Description**: A partition-based clustering algorithm that divides data into `k` clusters, where each data point belongs to the cluster with the nearest mean (centroid).  
   - **Steps**:
     1. Initialize `k` centroids randomly or using specific initialization methods (e.g., k-means++).
     2. Assign each point to the nearest centroid using a distance metric (e.g., Euclidean distance).
     3. Update centroids by calculating the mean position of points in each cluster.
     4. Repeat steps 2-3 until convergence (i.e., centroids stabilize or a maximum number of iterations is reached).
   - **Key Benefits**: Simple and efficient for large datasets.
   - **Limitations**: Sensitive to the initial placement of centroids and may converge to a local minimum.

2. **Single Linkage**  
   - **Description**: A hierarchical clustering method that merges clusters based on the minimum distance between any two points in the clusters.
   - **Steps**:
     1. Treat each data point as an individual cluster.
     2. Compute the distance between all pairs of clusters.
     3. Merge the two clusters with the smallest distance.
     4. Repeat steps 2-3 until all points are in a single cluster or the desired number of clusters is achieved.
   - **Key Feature**: Preserves spatial relationships by linking clusters through their closest members.
   - **Applications**: Effective for identifying elongated or irregularly shaped clusters.
   - **Limitation**: Can be sensitive to outliers, as single linkage focuses only on the nearest points.

---

## Dataset Description📊
The dataset consists of images containing black pixels. Each point will have the following features:
- **x-coordinate**
- **y-coordinate**

---

## Distance Metric📏
### Euclidean Distance Formula 🌐

The Euclidean distance measures how far apart two points are in a space. For two points on a 2D plane, we can think of them as having **x** and **y** coordinates. To find out how far apart the two points are, we use this formula:

$$
text{Distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

Where:
- **(x₁, y₁)** and **(x₂, y₂)** are the coordinates of the two points.
- **(x₂ - x₁)** is the horizontal distance between the points.
- **(y₂ - y₁)** is the vertical distance between the points.
- Squaring the differences and adding them together gives the total squared distance.
- Finally, we take the square root to get the actual distance between the points.

---

### Simple Steps to Calculate:
1. **Subtract** the x-coordinates of the two points: \( x_2 - x_1 \)
2. **Subtract** the y-coordinates of the two points: \( y_2 - y_1 \)
3. **Square** each difference.
4. **Add** the squared differences.
5. **Take the square root** of the sum to get the distance.

This will give you the "straight line" distance between the two points, as if you were measuring with a ruler.

---

## Neighbor-Based Clustering🌍
Perform clustering on points from the previous lab, considering only the points in **neighboring "cells"**. Compare the **number of distance function calls** between this approach and classic methods.

This technique leverages spatial locality to reduce computation overhead, providing insights into the efficiency of clustering based on spatial constraints.

---
