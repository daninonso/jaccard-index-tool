# jaccard-index-tool
Jaccard index calculations leverage statistical computation to derive a similarity index between two datasets. This tool takes advantage of Esri's ArcPy library to pull and manipulate spatially enabled datasets from ArcGIS Pro. Combined with other versatile Python libraries, this source code explores how Jaccard indices can be derived from a shapefile (Guildford_fishnet). It also addresses two major calculation categories; set (categorical) and binary (integer/ 1s & 0s). 


## Python libraries
The following Python libraries were used in addition to the *arcpy* import
* *pandas* — preferred for converting ArcGIS Pro's attribute tables into dataframes for easier data manipulation
* *goepandas* — preferred for its ability to preserve spatial relationships of datasets
* *numpy* — provides array of easy to us statistical methods like mean and standard deviation
* *sklearn.metrics* — used to import the *jaccard_score* method
* *libpysal.weights* — used to import the *Queen* and *Rook* methods for assigning/defining neigborhood

## Tool in action
### Scenario - Binary Calculations
![ArcGIS Pro window showing Guilford fishnet, attribute table, and inputs for jaccard binary calculation](https://github.com/user-attachments/assets/a7a7311e-c567-4991-98ee-39f1057db388) _Figure 1: Guilford_Fishnet binary calculation_

> In this scenario, the symbology represents a theoretical binary distribution of naturally occuring spatial patterns. As seen in the table and the input fields of the geoprocessing tool, the fields being considered for calculation are _Cluster1_ and _Cluster2_. 1s in the field represent a presence in the pattern while 0s represent an absence.

_placeholder for result_

### Scenario - Set Calculations
![ArcGIS Pro window showing Guilford fishnet, attribute table, and inputs for jaccard set calculation](https://github.com/user-attachments/assets/c4dc13cb-5181-4618-b656-5825b8c5fd49) _Figure 3: Guilford_Fishnet set calculation_

> The symbology in this scenario represents a theoretical distribution of naturally occuring spatial patterns categorized as sets of uniform values. The fields being considered for calculation are _CLASS4BASE_ and _CLASS4RAND_, which are really randomly generated classifications generated for the sake of simulating pre-classified rasters.

![set_classification](https://github.com/user-attachments/assets/46c01f18-9058-4b81-9a15-ba6fdcf6b128) 
<br> _Figure 4: Symbology legend_
