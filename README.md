# Python API Testing - Readme

This is a simple RESTful APIs test exercise using the Python requests library and the pytest unit testing framework.

The pytest framework makes it easy to write simple tests and scale to support complex functional testing of applications.

The API used for this test is available at [restcountries.eu](https://restcountries.eu/), which shows vital information about the different countries in the world.

## Usage

To get started, clone or download the project. We then need to open the project in our IDE (PyCharm, but any decent IDE works) by browsing to the download folder directory. We need a python interpreter to run this test if you do not have this in your IDE, click [HERE](https://www.python.org/downloads/) to download

Now, the following are python modules that needs to be installed to successfully execute  test. Use the python package installer [pip](https://pip.pypa.io/en/stable/) to install the following modules: **requests**, **jsonpath** and **pytest**. From the terminal run the following commands:


```python
pip install requests
```

```python
pip install jsonpath
```

```python
pip install pytest
```

# Code Structure

* PythonAPITest/
  * countries/
       * __init__.py
       * test_countries.py
  * main.py

The test_countries.py file consists of 5 basic tests(functions) with some assertions included.

1. *test_get_all_countries* : Function to test for all the available countries
1. *test_search_by_country_name* : Function to test for search by country name.
1. *test_search_by_invalid_country_name* : As the function name suggest, test to search for country by passing invalid name criteria
1. *test_get_country_name_by_currency_code* : Test to retrieve country by passing valid currency code
1. *test_search_by_list_of_codes_all_invalid_codes* : Function to test for search for country by list of (different) codes by passing invalid codes 

# Run Test
The test can be run using any IDE or from the command line. On the IDE, you can run the test from the project root folder *(PythonAPITest/)* using  the command

```python
py.test 
```
OR using

```python
py.test countries/test_countries.py

```
results of the test is displayed on the console showing the number of test passed (and if any failed)
        
