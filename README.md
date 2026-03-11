# jaccard-index-tool
Jaccard index calculations leverage statistical computation to derive a similarity index between two datasets. This tool takes advantage of Esri's ArcPy library to pull and manipulate spatially enabled datasets from ArcGIS Pro. Combined with other versatile Python libraries, this source code explores how Jaccard indices can be derived from a shapefile (Guildford_fishnet). It also addresses two major calculation categories; set (categorical) and binary (integer/ 1s & 0s). 


## Python libraries
The following Python libraries were used in addition to the *arcpy* import
* *pandas* — preferred for converting ArcGIS Pro's attribute tables into dataframes for easier data manipulation
* *goepandas* — preferred for its ability to preserve spatial relationships of datasets
* *numpy* — provides array of easy to us statistical methods like mean and standard deviation
* *sklearn.metrics* — used to import the *jaccard_score* method
* *libpysal.weights* — used to import the *Queen* and *Rook* methods for assigning/defining neigborhood

## Images
![ArcGIS Pro window showing Guilford fishnet, attribute table, and inputs for jaccard binary calculation using the Cluster1 and Cluster2 fields](<img width="1889" height="859" alt="guilford_binary" src="https://github.com/user-attachments/assets/a7a7311e-c567-4991-98ee-39f1057db388" />)
