from tkinter.tix import Tree
import pandas as pd

cerebra_label_details = pd.read_csv('CerebrA_LabelDetails.csv')
label_details = pd.read_csv('label_details.csv')
results_per_region = pd.read_csv('results_per_region.csv')

# Example of merging dat frames on Mindboggle ID (adjust as necessary)
# merged_data = pd.merge(cerebra_label_details, label_details,
                    #    left_on='Mindboggle ID (left)', right_on='Mindboggle ID', how='inner')

# merged_data.to_clipboard()
# print("CerebrA_LabelDetails columns:", cerebra_label_details.columns.tolist())
# print("Label_details columns:", label_details.columns.tolist())
# print("results_per_region columns:", results_per_region.columns.tolist())

# Drop unwanted columns
cerebra_label_details.drop(columns=[
    'Unnamed: 3', 'Notes', 'Unnamed: 6', 'Unnamed: 8'
], errors='ignore', inplace=True)

# Rename columns if needed
cerebra_label_details.rename(columns={
    'CerebrA ID': 'CerebrA ID - LH Labels',
    'CerebrA ID.1': 'CerebrA ID - RH Labels'
}, inplace=True)

# Check the columns
print("CerbrA_LabelDetails columns after cleaning:", cerebra_label_details.columns.tolist())
print(cerebra_label_details.head())

# Clean Label_details
# Drop unwanted columns
label_details.drop(columns=[
    'Unnamed: 0',
    'Resource CubeID',
    'BrainRegion/Cerebra A',
    'Mindboggle ID.1'
    
], errors='ignore', inplace=True)
# Check the columns
print("Label_details columns after cleaning:", label_details.columns.tolist())
print(label_details.head())

# Clean results_per_region
# Drop unwanted columns
results_per_region.drop(columns=[
    'Unnamed: 0'
], errors='ignore', inplace=True)
#Check the columns
print("result_per_region columns after cleaning:", results_per_region.columns.tolist())
print(results_per_region)