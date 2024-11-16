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
The distance between two points is calculated using the **Euclidean distance** formula:

\[
d(p, q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

Where:
- \(p = (x_1, y_1)\) and \(q = (x_2, y_2)\) are the coordinates of two points.

**Optimization**: To improve performance, the square root can be omitted for comparison purposes since it does not affect the relative order of distances.

---

## Neighbor-Based Clustering🌍
Perform clustering on points from the previous lab, considering only the points in **neighboring "cells"**. Compare the **number of distance function calls** between this approach and classic methods.

This technique leverages spatial locality to reduce computation overhead, providing insights into the efficiency of clustering based on spatial constraints.

---
