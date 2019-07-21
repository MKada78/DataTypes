def max_length(df_original):
    ''' 
    This function takes a data frame to return the max nbr of characters for each column.
    You will need the following libraries : pandas, numpy and HTML.
    To import HTML run this < from IPython.display import display, HTML >,
    To import numpy run this <import numpy as np>,
    To import pandas run this <import pandas as pd>.
    '''

    # Initializing data frames used to gather necessary info : 
    df_col_name = []  # df to store col names.
    df_col_dtype = []  # df to store col data type.
    df_max_length = []  # df to store the max for a col.
    df_min_length = []  # df to store the min for a col.
    df_before_dot = []
    df_after_dot = []

    df_header = ["Col Name", "Col Type", "Min" ,"Max", "Digit before .", "Digit after ."]  # df to display col name of final result.
    
    #Create a copy of the df:
    df = df_original.copy()
    
    # Entering FOR loop to process our df :
    for col in df:
        df_col_name.append(col)  # Stores current col name.
        
        nb_unique_values = len(df[col].unique())  # Count number of unique values for the current col.
        if nb_unique_values < 11:
            print("Column {} has {} unique values, it's worth considering data type category for this variable".format(col, nb_unique_values))
            nb_values = df[col].unique()
            print("Unique values for column {} are {}".format(col, nb_values), end='\n\n')
            
        # Case if column type is object:
        if df[col].dtypes.kind == 'O':
            df_col_dtype.append('object (nb caracters)')  # Store the data type for the current col.
            max = df[col].str.len().max()  # Get the max nbr of characters for the current col. 
            df_max_length.append(max)  # Stores the max value.
            min = df[col].str.len().min()  # Get the min nbr of characters for the current col. 
            df_min_length.append(min)  # Stores the max value.
            df_before_dot.append('N/A')
            df_after_dot.append('N/A')

        
        # Case if column type is integer :
        elif df[col].dtypes.kind == 'i':
            df_col_dtype.append('int64 (max min)')  # Store the data type for the current col.
            max = df[col].replace('None', 0).max()  # Get the max number of  the current col (NaN removed). 
            df_max_length.append(max)  # Stores the max value.
            min = df[col].replace('None', 0).min()  # Get the min number of the current col (NaN removed).
            df_min_length.append(min)  # Stores the min value.
            df_before_dot.append('N/A')
            df_after_dot.append('N/A')
            
        elif df[col].dtypes.kind == 'f':
            df_col_dtype.append('float64 (max min)') # Store the data type for the current col.
            max = df[col].replace('None', 0).max()  # Get the max  max number of current col (NaN removed). 
            df_max_length.append(max)  # Stores the max value.
            min = df[col].replace('None', 0).min()  # Get the min number of the current col (NaN removed).
            df_min_length.append(min)  # Stores the min value.
            # Count number of digits before and after the decimal point:
            nb_before = len(str(int(max)))
            df_before_dot.append(nb_before)
            df['AFTER DECIMAL'] = df[col].astype(str).str.split('.').str[1]
            nb_after = df['AFTER DECIMAL'].astype(str).apply(lambda x: len(x)).max()
#             nb_after = df[col].astype(str).str.split('.').str[1].max()
#             nb_after = len(str(int(nb_after)))
            df_after_dot.append(nb_after)
            
        # Case if column type is DATE TIME :
        elif df[col].dtypes.kind == 'M':
            df_col_dtype.append('date/time (oldest most recent)') # Store the data type for the current col.
            max = df[col].replace('None', 0).max()  # Get the max  max number of current col (NaN removed).
            df_max_length.append(max)
            min = df[col].replace('None', 0).min()  # Get the max  max number of current col (NaN removed).
            df_min_length.append(min)
            df_before_dot.append('N/A')
            df_after_dot.append('N/A')


            # Exiting FOR loop to display the results : 
    result = list(zip(df_col_name, df_col_dtype, df_min_length, df_max_length, df_before_dot, df_after_dot)) # Merges the lists containing col names & max values.
    df_result = pd.DataFrame(result, columns = df_header) # Creates df from merged list & title columns.
    
    display(HTML(df_result.to_html())) # Displays result as html table.

# END OF FUNCTION