# KMeans_Challenge
Coding Challenge

This coding challenge was given to me to implement a KMeans Clustering Algorithm similar to that in sklearn.

For comparison, I first wrote an example and a few graphs with a randomly generated dataset. Then, I attempted to create my own implementation of the KMeans algorithm with comparable results to that of the sklearn results. This assigment was to be completed within one hour.

Here is an example plot of the clusters. It includes centroid values from both my implementation and the sklearn implementation for comparison:

<p align="center">
  <img src="https://github.com/hrflkner/KMeans_Challenge/blob/main/img/kmeans_clusters_CentroidComparisons.png?raw=true" alt="Clusters with Centroid Plot">
</p>

Here is a table to show the differences in the Centroid values from each implementation:

table, td, th {
  border: 1px solid black;
}

table {
  font-size: 20px;
  text-align: center;
  width: 50%;
  border-collapse: collapse;
}
<table>
  <col>
  <colgroup span="2"></colgroup>
  <colgroup span="2"></colgroup>
  <tr>
    <td rowspan="2"></td>
    <th colspan="2" scope="colgroup">My Implementation</th>
    <th colspan="2" scope="colgroup">sklearn</th>
  </tr>
  <tr>
    <th scope="col">X</th>
    <th scope="col">Y</th>
    <th scope="col">X</th>
    <th scope="col">Y</th>
  </tr>
  <tr>
    <th scope="row">Centroid 1</th>
    <td>1.10041362</td>
    <td>3.05174259</td>
    <td>1.04798811</td>
    <td>1.1345495</td>
  </tr>
  <tr>
    <th scope="row">Centroid 2</th>
    <td>1.00438464</td>
    <td>1.11955788</td>
    <td>3.18576148</td>
    <td>0.9072616</td>
  </tr>
    <tr>
    <th scope="row">Centroid 3</th>
    <td>3.05447363</td>
    <td>2.65856700</td>
    <td>3.05447363</td>
    <td>2.658567</td>
  </tr>
  <tr>
    <th scope="row">Centroid 4</th>
    <td>3.15083859</td>
    <td>0.92733088</td>
    <td>1.10041362</td>
    <td>3.05174259</td>
  </tr>
</table>


To determine the inital number of clusters I also made the following elbow plot:

<p align="center">
  <img src="https://github.com/hrflkner/KMeans_Challenge/blob/main/img/elbow_inertia_visualization.png?raw=true" alt="Clusters with Centroid Plot" width=600px height=auto>
</p>
