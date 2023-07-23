# Data Engineer Assignment Digitiamo

This is the solution of the Data Engineer Assingment from Digitiamo

## Assignment

1. Create a python function with these properties:
   - INPUT one tabular data and a string naming a column of the tabular
   - OUTPUT one tabular data
   - BEHAVIOUR, filter out rows if values in the given column are null values
2. Create a python function with these properties:
   - INPUT one tabular data
   - OUTPUT one tabular data
   - BEHAVIOUR, select and return only rows in which if Cause category is equal to Traffic Control then Cause Subcategory must be equal to Others or Police Controlled. Moreover the function must “clean” the Million Plus Cities column of the selected rows removing all characters that appear between parentheses. Remove the parentheses also.

## Solution - Run in local

To run the solution locally, first of all create and activate a virtual env.

```
python -m venv .digitiamo
source .digitiamo/bin/activate
```

Then, from the root directory do the following.

```
python src/clean_data.py <input_data.csv>
```

This will run the steps 1 and 2 above. It will not save the result anywhere.

## Solution - Run with Docker

Fromt he root directory, build a Docker image with:

```
docker build -t cleaning-api:latest .
```

To run the image built above do:

```
docker run -d --name cleaning_api cleaning-api:latest
```

You have an API up and running in local with 2 endpoints.
The endpoint `/filter_null` for point 1 and `/filter_ctg` for point 2.

To call the service do:

```
curl -F file=@<input_file.csv>  http://localhost:5000/filter_null -o <output_file.csv>

curl -F file=@<input_file.csv>  http://localhost:5000/filter_ctg -o <output_file.csv>
```
