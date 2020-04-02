'''
NASA Turbofan Failure Prediction - Dataset Import

This file supports datset importation and visualisation.

'''

###################################
# Module Importations (A - Z Format)
###################################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Constants
filename_string = r'C:\Developer\PMetcalf\nasa_turbofan_failure_prediction\Raw Data\train_FD001.txt'

dataset_columns = ('Unit Number', 'Time-Cycles',
                    'Setting 1', 'Setting 2', 'Setting 3', 
                    'Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'Sensor 7',
                    'Sensor 8', 'Sensor 9', 'Sensor 10', 'Sensor 11', 'Sensor 12', 'Sensor 13', 'Sensor 14',
                    'Sensor 15', 'Sensor 16', 'Sensor 17', 'Sensor 18', 'Sensor 19', 'Sensor 20', 'Sensor 21' ) 

# Import the files
def import_dataset():

    # Import the raw data as an array.
    raw_data_array = np.loadtxt(filename_string, delimiter = ' ', usecols = range(26))

    # Convert array into dataframe, to add column names and create index.
    raw_data_df = pd.DataFrame(raw_data_array, index = None, columns = dataset_columns)

    print(raw_data_df)

    return raw_data_df

# Peek at limited selection of raw data
def peek_dataset(data_df):

    engine_unit_numbers = (1.0, 5.0, 12.0)

    # Use dataframe methods to peek at data in dataframe.
    for number in engine_unit_numbers:
        is_number = data_df['Unit Number'] == number

        filtered_df = data_df[is_number]

        filtered_df.plot(kind = 'scatter', x = 'Time-Cycles', y = 'Sensor 17')

        plt.show()


    