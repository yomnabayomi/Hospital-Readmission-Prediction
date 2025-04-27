import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read Dataset
df = pd.read_csv(r"N:\Colleague\Project\diabetic_data.csv")
df_mapping = pd.read_csv(r"N:\Colleague\Project\IDs_mapping.csv", header = None)

# # Fix mapping csv format --->
# Lists to store the results
admission_type_id = []
admission_type_id_description = []
discharge_disposition_id = []
discharge_disposition_id_description = []
admission_source_id = []
admission_source_id_description = []

# Iterate over the rows of the DataFrame
i = 0  # Initialize the row index

while i < len(df_mapping):
    row = df_mapping.iloc[i]  # Get the current row
    if row[0] == 'admission_type_id':  # If first column is 'admission_type_id'
        i += 1  # Skip the 'admission_type_id' row
        while i < len(df_mapping) and df_mapping.iloc[i, 0] != 'discharge_disposition_id' and df_mapping.iloc[
            i, 0] != 'admission_source_id':
            admission_type_id.append(df_mapping.iloc[i, 0])  # Add the id
            admission_type_id_description.append(df_mapping.iloc[i, 1])  # Add the description
            i += 1  # Move to the next row

    elif row[0] == 'discharge_disposition_id':  # If first column is 'discharge_disposition_id'
        i += 1  # Skip the 'discharge_disposition_id' row
        while i < len(df_mapping) and df_mapping.iloc[i, 0] != 'admission_source_id':
            discharge_disposition_id.append(df_mapping.iloc[i, 0])  # Add the id
            discharge_disposition_id_description.append(df_mapping.iloc[i, 1])  # Add the description
            i += 1  # Move to the next row

    elif row[0] == 'admission_source_id':  # If first column is 'admission_source_id'
        i += 1  # Skip the 'admission_source_id' row
        while i < len(df_mapping) and df_mapping.iloc[i, 0] is not None:  # Check for None (null)
            admission_source_id.append(df_mapping.iloc[i, 0])  # Add the id
            admission_source_id_description.append(df_mapping.iloc[i, 1])  # Add the description
            i += 1  # Move to the next row

# Create separate DataFrames for each section
admission_type_df = pd.DataFrame({
    'admission_type_id': admission_type_id,
    'admission_type_id_description': admission_type_id_description
})

discharge_disposition_df = pd.DataFrame({
    'discharge_disposition_id': discharge_disposition_id,
    'discharge_disposition_id_description': discharge_disposition_id_description
})

admission_source_df = pd.DataFrame({
    'admission_source_id': admission_source_id,
    'admission_source_id_description': admission_source_id_description
})

## <--- end

# Convert the 'admission_type_id' column in the mapping DataFrame to integers
# First handle NaN values - here I'm filling with -1 as a placeholder
admission_type_df['admission_type_id'] = admission_type_df['admission_type_id'].fillna(-1).astype(int)
discharge_disposition_df['discharge_disposition_id'] = discharge_disposition_df['discharge_disposition_id'].fillna(-1).astype(int)
admission_source_df['admission_source_id'] = admission_source_df['admission_source_id'].fillna(-1).astype(int)

# Create dictionaries from each DataFrame for mapping to change id by description
admission_type_map = dict(zip(admission_type_df['admission_type_id'], admission_type_df['admission_type_id_description']))
discharge_disposition_map = dict(zip(discharge_disposition_df['discharge_disposition_id'], discharge_disposition_df['discharge_disposition_id_description']))
admission_source_map = dict(zip(admission_source_df['admission_source_id'], admission_source_df['admission_source_id_description']))

# Decode the IDs by replacing them with the corresponding descriptions
df['admission_type_id'] = df['admission_type_id'].replace(admission_type_map)
df['discharge_disposition_id'] = df['discharge_disposition_id'].replace(discharge_disposition_map)
df['admission_source_id'] = df['admission_source_id'].replace(admission_source_map)

df['max_glu_serum'] = df['max_glu_serum'].fillna(df['max_glu_serum'].mode()[0])
df['A1Cresult'] = df['A1Cresult'].fillna(df['A1Cresult'].mode()[0])
df['admission_type_id'] = df['admission_type_id'].fillna(df['admission_type_id'].mode()[0])
df['discharge_disposition_id'] = df['discharge_disposition_id'].fillna(df['discharge_disposition_id'].mode()[0])
df['admission_source_id'] = df['admission_source_id'].fillna(df['admission_source_id'].mode()[0])


