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