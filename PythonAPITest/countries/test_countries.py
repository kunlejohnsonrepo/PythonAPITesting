import requests
import pytest

base_url = 'https://restcountries.eu/rest/v2'


def test_get_all_countries():
    response = requests.get(base_url+'/all')
    print(f'endpoint:' + response.url)
    print(response)
    http_code = response.status_code
    print(http_code)
    assert http_code == 200, 'HTTP status code is not 200'
    print(f'status code assertion is PASSED')
    print(response.json()[13])
    assert (response.json()[13]['name']) == 'Australia', 'Country is not Australia'
    assert (response.json()[13]['region']) == 'Oceania', 'Region is not Oceania'
    assert (response.json()[62]['name']) == 'Denmark', 'Country is not Denmark'
    assert (response.json()[84]['name']) == 'Germany', 'Country is not Germany'
    assert (response.json()[84]['callingCodes'][0]) == '49', 'Calling code does not match'
    print(f'response body assertion is PASSED')
    print(f'Get All Countries test was executed successfully')

# Search by country passing partial country name
def test_search_by_country_name():
    response = requests.get(base_url+'/name/south')
    print(f'endpoint:'+response.url)
    http_code = response.status_code
    print(http_code)
    assert http_code == 200, 'HTTP status code is not 200'
    print(f'status code assertion is PASSED')
    print(response.json())
    assert (response.json()[0]['name']) == 'French Southern Territories', 'Country is not French Southern Territories'
    assert (response.json()[1]['name']) == 'South Africa', 'Country is not South Africa'
    assert (response.json()[1]['population']) == 55653654, 'Population does not match'
    print(f'response bogy assertions passed')
    print(f'Search Countries by name test was executed successfully')

#negative test scenario: Search by passing invalid input (country name)
def test_search_by_invalid_country_name():
    response = requests.get(base_url+'/name/qpy')
    print(f'endpoint:'+response.url)
    http_code = response.status_code
    print(http_code)
    assert http_code == 404, 'HTTP status code is not 404'
    print(f'Search by name criteria: status code assertion is PASSED')
    print(response.json())
    assert (response.json()['status']) == 404, 'Status does not match'
    assert (response.json()['message']) == 'Not Found', 'message does not match'
    print(f'response body assertions passed')
    print(f'Search Countries by invalid name test was executed successfully')

# get countries by passing currency code
def test_get_country_name_by_currency_code():
    response = requests.get(base_url+'/currency/eur')
    print(f'endpoint:'+response.url)
    http_code = response.status_code
    print(http_code)
    assert http_code == 200, 'HTTP status code is not 200'
    print(f'status code assertion is PASSED')
    print(response.json())
    assert (response.json()[3]['name']) == 'Belgium', 'Country is not Belgium'
    assert (response.json()[7]['name']) == 'France', 'Country is not France'
    assert (response.json()[7]['currencies'][0]['code']) == 'EUR', 'Currency is not Euro'
    print(f'response body assertions passed')
    print(f'Search Countries by currency code test was executed successfully')

#negative test scenario: Search by passing invalid alpha codes
def test_search_by_list_of_codes_all_invalid_codes():
    response = requests.get(base_url+'/alpha?codes=djp;pkk;xxq')
    print(f'endpoint:'+response.url)
    http_code = response.status_code
    print(http_code)
    assert http_code == 200, 'HTTP status code is not 200'
    print(f'status code assertion is PASSED')
    print(response.json())
    assert response.json() == [None], 'response body does not match'
    print(f'response body assertions passed')
    print(f'Search by List of codes passing all invalid codes test was executed successfully')