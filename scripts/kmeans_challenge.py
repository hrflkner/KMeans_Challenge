# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:45:40 2021

@author: Hunter Faulkner
"""
#%% Imports
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

#%% Generate Data and sklearn Preprocess
# Generate Random Set of 2D Points of Size 100
coordinate_matrix = np.ones((100,2)) * np.random.random_sample((100,2)) * 4

# Initial Visualization of Data
plt.figure(figsize=(8,6))
plt.title("Data without Clusters", fontsize=16)
plt.xlabel("Random x-value")
plt.ylabel("Random y-value")
plt.scatter(coordinate_matrix[:,0], coordinate_matrix[:,1])
plt.show()

sdata = sklearn.preprocessing.scale(coordinate_matrix)

#%% Best Number of Clusters with Elbow Method Heuristic
'''
Fast because of set size but would use GPU or vectorization over
looping to speed up wherever possible.
'''

err = []
elbow_range = range(1, 21)
for i in elbow_range:
    k_means = KMeans(n_clusters=i, random_state=5)
    k_means.fit(coordinate_matrix)
    err.append(k_means.inertia_)

plt.title("Elbow Inertia Plot")
plt.ylabel("Inertia")
plt.xlabel("Number of Clusters")
plt.plot(elbow_range, err)
plt.scatter(elbow_range,err, color='red')
plt.show()

# print(err) To Examine Error Array

#%% Calculate Centroids

'''
After checking for optimal clusters, apply this value for the elbow 

NOTE!! : This will change at runtime since this data is being randomly
         generated. View the elbow and then run this section with the
         appropriate value. 
         
         Would have automated this, but the challenge timed for 1 hour.
'''
elbowval = 4 # Change this value based on the results above.

k_means = KMeans(n_clusters=elbowval)
pred = k_means.fit_predict(coordinate_matrix)

# Centroids
print(k_means.cluster_centers_)

#%% Concatenate and Plot Final Findings

# Use Pandas for Masking
coordinate_df = pd.DataFrame(coordinate_matrix)
coordinate_df['pred'] = pred

# Loop Through Cluster Number to Plot Each
plt.figure(figsize=(8,6))
plt.title("Clusters with Centroids", fontsize=16)
plt.xlabel("Random x-value")
plt.ylabel("Random y-value")
for i in np.unique(pred):
    plt.scatter(coordinate_df[coordinate_df['pred']==i][0],
                coordinate_df[coordinate_df['pred']==i][1],
                label=f"Cluster {i+1}")
plt.scatter(k_means.cluster_centers_[:,0], k_means.cluster_centers_[:,1],
            color='chartreuse', marker='x', s=80, label="Centroid")
plt.legend(fontsize=16,bbox_to_anchor=(1,1), loc="upper left")
plt.show()

#%% Building Function similar to sklearn KMeans

# Calculating Centroids Function for k means
def centroids(data, n):
    xmin = float('inf')
    xmax = float('-inf')
    ymin = float('inf')
    ymax = float('-inf')
    for i in data:
        xmin = min(i[0], xmin)
        xmax = max(i[0], xmax)
        ymin = min(i[0], ymin)
        ymax = max(i[0], ymax)

    c = []
    for i in range(n):
        c.append([
            xmin + ((xmax - xmin) * np.random.random()),
            ymin + ((ymax - ymin) * np.random.random())
            ])
        
    return c
  
def euclid_distance(a, b): # Point a(x, y) & point b(x, y)
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
  
# Minimize Squared Error for Centroids
def c_dist(data, centroid):
    dist = []
    for i in data:
        minimum_dist = float('inf')
        for j, c in enumerate(centroid):
            update_dist = euclid_distance(i, c)
            if minimum_dist > update_dist:
                minimum_dist = update_dist
                d = j
        dist.append(d)
    return dist
    
def cent_updating(data, dist, n):
    new_c = [[0, 0] for i in range(n)]
    counting = [0] * n
    
    for data, dist in zip(data, dist):
        new_c[dist][0] += data[0]
        new_c[dist][1] += data[1]
        counting[dist] += 1
    
    for i, (x, y) in enumerate(new_c):
        new_c[i] = (x / counting[i], y/counting[i])
    return new_c
      
def threshold(old, new):
    z = 0
    for i, j in zip(old, new):
        z += euclid_distance(i, j)
    return z < 1e-3

def my_k_means(data, n):
    centroid = centroids(data, n)
    
    while True:
        oldc = centroid
        dist = c_dist(data, centroid)
        centroid = cent_updating(data, dist, n)
        if threshold(oldc, centroid):
            return dist, centroid

#%%

# My Calculation

my_kmc, centroids = my_k_means(coordinate_matrix, 4)

# Accessing Centroid Tuples

centroid_X = [i[0] for i in centroids]
centroid_Y = [i[1] for i in centroids]

#%% Plotting my Results

# Use Pandas for Masking
my_coordinate_df = pd.DataFrame(coordinate_matrix)
my_coordinate_df['pred'] = my_kmc

# Use Pandas for Masking
coordinate_df = pd.DataFrame(coordinate_matrix)
coordinate_df['pred'] = pred

# Loop Through Cluster Number to Plot Each
plt.figure(figsize=(8,6))
plt.title("Clusters with Centroids", fontsize=16)
plt.xlabel("Random x-value")
plt.ylabel("Random y-value")
for i in np.unique(pred):
    plt.scatter(my_coordinate_df[coordinate_df['pred']==i][0],
                my_coordinate_df[coordinate_df['pred']==i][1],
                label=f"Cluster {i+1}")

# Plot sklearn Centroids and My Implementation's Centroids    
plt.scatter(k_means.cluster_centers_[:,0], k_means.cluster_centers_[:,1],
            color='magenta', marker='x', s=80, label="Centroid")
plt.scatter(centroid_X, 
            centroid_Y,
            color='chartreuse', 
            marker='x', 
            s=80, 
            label="My Centroid")
plt.legend(fontsize=16,bbox_to_anchor=(1,1), loc="upper left")
plt.show()
