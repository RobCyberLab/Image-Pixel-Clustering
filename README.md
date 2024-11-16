# 🌀Image Pixel Clustering📏

Note: Due to privacy policies, I am not allowed to post the dataset publicly.

---

## Table of Contents📋
1. [Overview](#overview)
2. [Clustering Techniques](#clustering-techniques)
3. [Dataset Description](#dataset-description)
4. [Distance Metric](#distance-metric)
5. [Recommended Libraries](#recommended-libraries)
6. [Neighbor-Based Clustering](#neighbor-based-clustering)

---

## Overview📖
In this laboratory, we will test at least two of the following clustering techniques:
- **k-means**
- **Single Linkage**

---

## Clustering Techniques🌀
The focus of this lab is to experiment with and understand the following clustering methods:
1. **k-means**: A partition-based clustering algorithm.
2. **Single Linkage**: A method to build a hierarchy of clusters.

---

## Dataset Description📊
The dataset consists of images containing black pixels. Each point will have the following features:
- **x-coordinate**
- **y-coordinate**

---

## Distance Metric📏
The distance between two points will be calculated using the **Euclidean distance** formula. For performance reasons, extracting the square root can be omitted.

---

## Neighbor-Based Clustering🌍
Perform clustering on points from the previous lab, considering only the points in **neighboring "cells"**. Compare the **number of distance function calls** between this approach and classic methods.

This technique leverages spatial locality to reduce computation overhead, providing insights into the efficiency of clustering based on spatial constraints.

---

