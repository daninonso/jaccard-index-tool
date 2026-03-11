import arcpy
import pandas as pd
import numpy as np     
import geopandas as gpd
from sklearn.metrics import jaccard_score
from libpysal.weights import Queen, Rook
from libpysal.weights.util import lat2W

from arcpy import env
def ScriptTool(param0, param1):
    # Script execution code goes here
    return

# This is used to execute code if the file was run but not imported
if __name__ == '__main__':
    # Tool parameter accessed with GetParameter or GetParameterAsText
    inputLayer = arcpy.GetParameterAsText(0)
    Field1 = arcpy.GetParameterAsText(1)
    Field2 = arcpy.GetParameterAsText(2)
    Field3 = arcpy.GetParameterAsText(3)
    Field4 = arcpy.GetParameterAsText(4)
    Field5 = arcpy.GetParameterAsText(5)
    Field6 = arcpy.GetParameterAsText(6)


    fields = (Field1, Field2)

    CalType = str(Field3) # defining a variable for the calculation type (set/binary vector)
    shp_file = str(Field4) # defining a variable to receive a shape file for spatial calculation
    weight = str(Field5) # defining a variable for holding spatial weight (Queen/Rook)
    no_perm = int(Field6) # defining a variable for the number of permutations

    # Initializing counts to zero
    count = 0
    A = 0 # A - values in Set 1, but not in Set 2
    B = 0 # B - values in Set 2, but not in Set 1
    C = 0 # C - values both in Set 1 and Set 2
    D = 0 # D - values neither in Set 1 nor Set 2


    # Total count of all features in the sample field
    countFeatures = int(arcpy.GetCount_management(inputLayer).getOutput(0))
    arcpy.AddMessage(str(inputLayer) + " has " + str(countFeatures) + " features")

    
    # Iterating through each row using SearchCursor to return an array of row inputs
    set_data = [row for row in arcpy.da.SearchCursor(inputLayer, fields)]
    # arcpy.AddMessage(set_data) #array of arrays with each row for both cols

    # Converting set_data into a pandas dataframe
    set_df = pd.DataFrame(set_data, columns=fields)

    # Jaccard Index for sets
    if CalType == "Set":

        arcpy.AddMessage("**** Jaccard Index of two sets of columns ***") 
        arcpy.AddMessage("Selected Columns: " + str(Field1) + " | " + str(Field2))

        # Calculating the intersection and union of the sets
        intersection = sum(set_df[Field1] == set_df[Field2])
        union = len(set_data)
        arcpy.AddMessage("Intersection for selected columns: " + str(intersection)) 
        arcpy.AddMessage("Union for selected columns: " + str(union)) 

        # Calculating the Jaccard score
        jaccard_score = intersection / union
        arcpy.AddMessage("The Jaccard index for the set of columns is " + str(jaccard_score))
        

    # Jaccard Index for binary vectors
    elif CalType == "Binary Vector":
        def jaccard_index(set_a, set_b):
            union = np.logical_or(set_a, set_b).sum()
            intersection = np.logical_and(set_a, set_b).sum()
            if union == 0:
                return 0.0
            return intersection / union
    
        a_vals = set_df[Field1].values.astype(int)
        b_vals = set_df[Field2].values.astype(int)

        # Calculate Observed Jaccard
        j_obs = jaccard_index(a_vals, b_vals)

        arcpy.AddMessage("**** Output for Binary Vector ***") 
        arcpy.AddMessage("Jaccard Index for Binary Vectors = " + str(j_obs))    


        #### Attaching a P-value for the calculated Jaccard Index ####

        # Function to run the permutations of Jaccard indices
        def jaccard_permutation_test(
            gdf,
            col_a,
            col_b,
            weight_type,
            n_permutations,
            spatial=True,
            seed=None,
            return_distribution=False
        ):
            rng = np.random.default_rng(seed)

            gdf = gdf.copy()

            a_vals = gdf[col_a].values.astype(int)
            b_vals = gdf[col_b].values.astype(int)
            n_cells = len(gdf)


            # Performing calculations based on spatial weights
            if spatial:
                if weight_type == 'Queen':
                    w = Queen.from_dataframe(gdf) # uses vertices to determine neigbors
                elif weight_type == 'Rook':
                    w = Rook.from_dataframe(gdf) # uses edges to determine neigbors
                else:
                    raise ValueError("weight_type must be 'queen' or 'rook'")
                
                # Dictionary comprehension to create a key-value pair for cells and their neighbors
                neighbors = {i: list(w.neighbors[i]) for i in w.neighbors} 
                # arcpy.AddMessage(neighbors)
            else:
                neighbors = None  # random global

            jaccard_null = [] # Initialize null distribution of Jaccard Indices

            # Permutation function
            def permute_fixed_ones(n_ones, neighbors=None):

                # Start with zero array
                permuted = np.zeros(n_cells, dtype=bool)

                if neighbors:
                    flat_neighbors = list(set(i for nb in neighbors.values() for i in nb)) # flatten the values in neighbors key-value pair
                    perm_indices = rng.choice(flat_neighbors, size=n_ones, replace=False) # Randomly select a set of indexes equal to the original number of Trues
                else:
                    perm_indices = rng.choice(n_cells, size=n_ones, replace=False)
                permuted[perm_indices] = True # change the values in the position of the randomly selected
                return permuted

            # Generate permutations based on supplied number of iterations
            for _ in range(n_permutations):
                a_perm = permute_fixed_ones(a_vals.sum(), neighbors if spatial else None)  
                b_perm = permute_fixed_ones(b_vals.sum(), neighbors if spatial else None)
                j_rand = jaccard_index(a_perm, b_perm)
                jaccard_null.append(j_rand)

            jaccard_null = np.array(jaccard_null)
            p_value = np.mean(jaccard_null >= j_obs)
            expected = np.mean(jaccard_null)
            std_dev = np.std(jaccard_null)
            centered = j_obs - expected
            z_score = (j_obs - expected) / std_dev if std_dev > 0 else np.nan

            result = {
                'Observed Jaccard': j_obs,
                'Expected Jaccard': expected,
                'Centered Coefficient': centered,
                'Standard Deviation': std_dev,
                'Z-score': z_score,
                'P-value (empirical)': p_value
            }

            if return_distribution:
                result['Null Distribution'] = jaccard_null

            return result
        
        # Calling the permutation function to create p-value result
        gdf = gpd.read_file(shp_file)

        results = jaccard_permutation_test(
            gdf,
            Field1,
            Field2,
            weight,
            no_perm,
            spatial=True,
            seed=42,
            return_distribution=False
        )

        arcpy.AddMessage("**** Calculating P-value for Jaccard Index ***")
        arcpy.AddMessage(results)

    else: arcpy.AddMessage("Could not compute")    



# Extract keys and counts of each list to a list
list1_size = len(pd.unique(set_df[Field1]))
list1_keys = set_df[Field1].value_counts().keys().tolist()
list1_count = set_df[Field1].value_counts().tolist()
list2_size = len(pd.unique(set_df[Field2]))
list2_keys = set_df[Field2].value_counts().keys().tolist()
list2_count = set_df[Field2].value_counts().tolist()

# Get unique values list and frequencies from Set 1 and Set 2
arcpy.AddMessage("**** Unique value list for datasets ***") 
arcpy.AddMessage("Set 1 Size = " + str(list1_size))
arcpy.AddMessage("Set 1 Values = " + str(list1_keys))
arcpy.AddMessage("Set 1 Frequencies = " + str(list1_count))
arcpy.AddMessage("Set 2 Size = " + str(list2_size))
arcpy.AddMessage("Set 2 Values = " + str(list2_keys))
arcpy.AddMessage("Set 2 Frequencies = " + str(list2_count))



