# DataTypes
Python script to find the length of all the variables contained in a dataframe.
This script will also the variables and recommend wether or not to set them as categorical variables (pandas type 'category').  
The purpose behind this script is to help you to define the right data types and variable length when creating your database. For example, in MySQL, you define these data types and lengths in the 'schema' file.

## Files in my repository:
- schema_join.sql = the schema file for my DB structure
- data_join.sql = the data file for my DB data loading and join testing
- customers.csv = table customers containing a few rows
- orders.csv = table orders containing a few rows

### Prerequisites
- Python (I use version 3.7.2)
- An IDE for Python (I use Jupyter Notebook but you can use any other IDE or code editor).

### To run the MaxLength function :
1- Copy and paste the function in your code editor.
2- Call the function with one argument which is the name of the dataframe you wish to analyse (exp : MaxLength(my_df)
3- You're done ! A table will be displayed providing you with the information mentioned in this Readme file.

## Contributing
Do not hesitate to suggest improvements or report any bug !

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Author
MESSOUS Kada
(Datartisan at Simplon.co)
