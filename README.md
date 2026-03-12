# jaccard-index-tool
Jaccard index calculations leverage statistical computation to derive a similarity index between two datasets. This tool takes advantage of Esri's ArcPy library to pull and manipulate spatially enabled datasets from ArcGIS Pro. Combined with other versatile Python libraries, this source code explores how Jaccard indices can be derived from a shapefile (Guildford_fishnet). It also addresses two major calculation categories; set (categorical) and binary (integer/ 1s & 0s). 

<br>

## Scenario 1 - Binary Calculations

![ArcGIS Pro window showing Guilford fishnet, attribute table, and inputs for jaccard binary calculation](https://github.com/user-attachments/assets/a7a7311e-c567-4991-98ee-39f1057db388) _Figure 1: Guilford_Fishnet binary calculation_

<br>

In this scenario, the symbology represents a theoretical binary distribution of naturally occuring spatial patterns. As seen in the table and the input fields of the geoprocessing tool, the fields being considered for calculation are _Cluster1_ and _Cluster2_. 1s in the field represent a presence in the pattern while 0s represent an absence.

<br>
<br>

![Results of binary calculations](https://github.com/user-attachments/assets/ca8f98a2-8190-45b1-ad69-70a4be1fee62)
<br>
_Figure 2: Results from binary calculations_

<br>
<br>

## Scenario 2 - Set Calculations

![ArcGIS Pro window showing Guilford fishnet, attribute table, and inputs for jaccard set calculation](https://github.com/user-attachments/assets/c4dc13cb-5181-4618-b656-5825b8c5fd49) _Figure 3: Guilford_Fishnet set calculation_

<br>
<br>

The symbology in this scenario represents a theoretical distribution of naturally occuring spatial patterns categorized as sets of uniform values. The fields being considered for calculation are _CLASS4BASE_ and _CLASS4RAND_, which are really randomly generated classifications generated for the sake of simulating pre-classified rasters.

<br>

![set_classification](https://github.com/user-attachments/assets/46c01f18-9058-4b81-9a15-ba6fdcf6b128) 
<br> _Figure 4: Symbology legend_

<br>
<br>

![Results of set calculations](https://github.com/user-attachments/assets/97fcab27-ec50-4ff1-983b-1ed6ee7407a8)
<br> _Figure 5: Results from set calculations_

<br>

## Python libraries
The following Python libraries were used in addition to the *arcpy* import
* *pandas* — preferred for converting ArcGIS Pro's attribute tables into dataframes for easier data manipulation
* *goepandas* — preferred for its ability to preserve spatial relationships of datasets
* *numpy* — provides array of easy to us statistical methods like mean and standard deviation
* *sklearn.metrics* — used to import the *jaccard_score* method
* *libpysal.weights* — used to import the *Queen* and *Rook* methods for assigning/defining neigborhood

<br>

## Configuration notes
Virtual environments play a crucial role in the configuration of this geoprocessing tool. The default environment `arcgispro-py3` is setup to integrate all functionalities of the ArcPy library, the other libraries listed above are required but not pre-installed in this environment. It is not advised to install the additional packages in the ArcGIS default environment to avoid conflicting Python versions. The following steps explain how to install the packages using Conda. 

1. **Create the geoprocessing tool**
   * Open a new project in ArcGIS Pro
   * Locate the catalog pane and right click on the toolbox folder
   * Create a new _Script tool_
   * Name your script tool and set the parameters as follows _insert screenshot of parameters_
   * Locate the _Execution_ side menu item
   * Copy and paste the code from _jaccard_index.py_
   * Save all changes
3. **Install Conda** — visit the official [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and follow the steps to install
4. **Open terminal** — right click the file explorer window in the location of your downloaded 
