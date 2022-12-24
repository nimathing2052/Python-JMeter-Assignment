

# scripts

## python task
to execute python task use:
* `make  init`  // setup virtual env
* `make run` // run python3 src/main.py


to run in windows:

`python3 src/main.py`


** update** <br />
*  Code has been made os independent
*  Removed f-string with %-string  and walrus operator has been removed to make it compactable with older version of python.
*  Readme document has been updated.
* added extra print in end to guide user to data folder at the end of the operation.
* added dist/
* added egg files for windows and whl files for linux.
* added steps to make create the logs folder automatically. 

The output of  will be in ./data/folder

## Jmeter
Jmeter task is in ./jmeter folder

<br />

# Assignment 

Write a python script to meet the following requirements: <br /> <br />
(Include code level comments to explain major steps of the code)<br />
Input File: A sample txt file with multiple rows of data (attached). <br />
 Each data is tab separated and each record is separated by new line.
 ## 1.    Task 1:
 a.    Convert the txt file to csv format. </br>
 b.    Change the record delimiter from tab to comma delimited for each row.</br>
 
 ## 2.    Task 2:
  a.    Count the number of rows in the csv file (excluding the header row)</br>
  b.    Calculate the checksum of the csv filec.    Append the checksum and row count to the header and footer of the csv file.

## 3.    Task 3:

Using the csv file generated in task 1, create a JSON object array/file of the first 5 rows of data from the .csv file. Here's the JSON object format:</br>

{    "Country": "Nepal",    "Product": "Carretera",    "DiscountBand": "None",    "UnitsSold": "1618.5",    "ManufacturingPrice": "$3.00",    "SalePrice": "$20.00",    "GrossSales": "$32",    "SalesQty": "370.00"}  

<br />


##  JMeter Assignment:


Create an API validatio n script for following REST API’s usingdummyapi.io website. After you log into the site, you can generate an app-id which you can use in your API request header to send the API requests below.
## 1.     
  https://dummyapi.io/data/api/user?limit=10 (GET)
a.       Verify if the API is throwing 200 OK as status code </br>
b.       Verify if id, lastName, firstName, email, title, picture JSON object keys are being populated or not.</br>
c.       Get value of id for user “Margarita” and use it to send API request in b.</br>

## 2.    
   https://dummyapi.io/data/api/user/{id_taken_from step a}
a.       Verify response code is 200 OK
b.       Verify if the firstName matches as expected(“Margarita”). </br>




