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
   * Click on _New_
   * Create a new _Script tool_
   * Name your script tool and set the parameters as follows
     
   <img width="733" height="297" alt="scriptTool_params" src="https://github.com/user-attachments/assets/d3d07338-69bd-45df-8235-5f9c27048ee2" />
   
   * Locate the _Execution_ side menu item
     
    <img width="696" height="479" alt="scriptTool_execution" src="https://github.com/user-attachments/assets/0e3cccae-dc41-4cdc-91f3-fbfdf3db22d4" />

   * Copy and paste the code from _jaccard_index.py_
   * Save all changes
3. **Install Conda** — visit the official [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and follow the steps to install
4. **Open terminal** — right click on your ArcGIS Pro app icon, select _Open file location_, click on the _Python Command Prompt_ shortcut
5. **Check Conda version** — confirm that you have conda installed by running this command `conda --version`
6. **Check virtual environments** — check the list of environments by running this command `conda env list`
7. **Clone ArcGIS environment** — clone the `arcgispro-py3` environment using this command `conda create --name <your_env_name> --clone arcgispro-py3`

<br>

> You can not clone an active environment. Active environments are usually indicated by an asterik(*) in the list of environments. If _arcgispro-py3_ is active, run this command `conda deactivate`

<br>

8. **Install packages** — once the _arcgispro-py3_ environment has been cloned successfully, install the required packages using this command `conda install pandas geopandas numpy sklearn.metrics libpysal.weights`
9. **Change environment** — after successfully installing the pacakges, open your _Jaccard_ ArcGIS Pro project, click on the _Project_ menu in the top left corner, locate the _Package Manager_ menu item, change the active environment to your new one.

<img width="1909" height="982" alt="package_mngr" src="https://github.com/user-attachments/assets/da722c92-4aee-444e-8787-0adb656b9089" />

10. **Restart project & Run** — restart your project for the changes to take effect, after restart, locate the script tool in _Catalog > Toolbox_, right click the script tool, click _Open_, plug in your inputs as seen in either scenario up top, hit _Run_.

<br>

> If you still get a _ModuleNotFoundError_ from the tool message box, make sure you are in the right environment by confirming in the _Package Manager_ menu and in the _Python Command Prompt_ terminal. Run `conda activate <correct_env_name>` in the terminal to switch to the right environment. The close and restart your ArcGIS Pro project.
