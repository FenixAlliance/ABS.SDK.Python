# openapi_client.CountriesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_countries**](CountriesApi.md#count_countries) | **GET** /api/v2/GlobeService/Countries/Count | Count countries
[**get_all_countries**](CountriesApi.md#get_all_countries) | **GET** /api/v2/GlobeService/Countries | Get all countries
[**get_calling_codes_by_country_id_async**](CountriesApi.md#get_calling_codes_by_country_id_async) | **GET** /api/v2/GlobeService/Countries/{countryId}/CallingCodes | Get calling codes for a country
[**get_cities_by_country_state_id_async**](CountriesApi.md#get_cities_by_country_state_id_async) | **GET** /api/v2/GlobeService/Countries/{countryId}/States/{countryStateId}/Cities | Get cities for a state
[**get_country_by_id**](CountriesApi.md#get_country_by_id) | **GET** /api/v2/GlobeService/Countries/{countryId} | Get country by ID
[**get_country_state_by_id_async**](CountriesApi.md#get_country_state_by_id_async) | **GET** /api/v2/GlobeService/Countries/{countryId}/States/{countryStateId} | Get state by ID
[**get_country_states_async**](CountriesApi.md#get_country_states_async) | **GET** /api/v2/GlobeService/Countries/{countryId}/States | Get states for a country
[**get_enabled_currencies_by_country_id_async**](CountriesApi.md#get_enabled_currencies_by_country_id_async) | **GET** /api/v2/GlobeService/Countries/{countryId}/Currencies | Get currencies for a country
[**get_time_zones_by_country_id_async**](CountriesApi.md#get_time_zones_by_country_id_async) | **GET** /api/v2/GlobeService/Countries/{countryId}/Timezones | Get timezones for a country
[**get_top_level_domains_by_country_id_async**](CountriesApi.md#get_top_level_domains_by_country_id_async) | **GET** /api/v2/GlobeService/Countries/{countryId}/TopLevelDomains | Get top-level domains for a country
[**search_countries_by_name_async**](CountriesApi.md#search_countries_by_name_async) | **GET** /api/v2/GlobeService/Countries/Search | Search countries by name


# **count_countries**
> Int32Envelope count_countries(api_version=api_version, x_api_version=x_api_version)

Count countries

Returns the total number of countries, with optional OData filtering.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count countries
        api_response = api_instance.count_countries(api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->count_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->count_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_countries**
> CountryDtoListEnvelope get_all_countries(api_version=api_version, x_api_version=x_api_version)

Get all countries

Retrieves a list of all countries with optional OData pagination and filtering.

### Example


```python
import openapi_client
from openapi_client.models.country_dto_list_envelope import CountryDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all countries
        api_response = api_instance.get_all_countries(api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_all_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_all_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryDtoListEnvelope**](CountryDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calling_codes_by_country_id_async**
> CountryCallingCodeDtoListEnvelope get_calling_codes_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)

Get calling codes for a country

Retrieves the list of international telephone calling codes associated with the specified country.

### Example


```python
import openapi_client
from openapi_client.models.country_calling_code_dto_list_envelope import CountryCallingCodeDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get calling codes for a country
        api_response = api_instance.get_calling_codes_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_calling_codes_by_country_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_calling_codes_by_country_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryCallingCodeDtoListEnvelope**](CountryCallingCodeDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cities_by_country_state_id_async**
> CityDtoListEnvelope get_cities_by_country_state_id_async(country_state_id, country_id, api_version=api_version, x_api_version=x_api_version)

Get cities for a state

Retrieves the list of cities belonging to the specified state or province.

### Example


```python
import openapi_client
from openapi_client.models.city_dto_list_envelope import CityDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_state_id = 'country_state_id_example' # str | 
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get cities for a state
        api_response = api_instance.get_cities_by_country_state_id_async(country_state_id, country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_cities_by_country_state_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_cities_by_country_state_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_state_id** | **str**|  | 
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CityDtoListEnvelope**](CityDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_by_id**
> CountryDtoEnvelope get_country_by_id(country_id, api_version=api_version, x_api_version=x_api_version)

Get country by ID

Retrieves a single country by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.country_dto_envelope import CountryDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get country by ID
        api_response = api_instance.get_country_by_id(country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_country_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_country_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryDtoEnvelope**](CountryDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_state_by_id_async**
> CountryStateDtoEnvelope get_country_state_by_id_async(country_state_id, country_id, api_version=api_version, x_api_version=x_api_version)

Get state by ID

Retrieves a single state or province by its unique identifier within a country.

### Example


```python
import openapi_client
from openapi_client.models.country_state_dto_envelope import CountryStateDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_state_id = 'country_state_id_example' # str | 
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get state by ID
        api_response = api_instance.get_country_state_by_id_async(country_state_id, country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_country_state_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_country_state_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_state_id** | **str**|  | 
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryStateDtoEnvelope**](CountryStateDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_states_async**
> CountryStateDtoListEnvelope get_country_states_async(country_id, api_version=api_version, x_api_version=x_api_version)

Get states for a country

Retrieves the list of states or provinces belonging to the specified country.

### Example


```python
import openapi_client
from openapi_client.models.country_state_dto_list_envelope import CountryStateDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get states for a country
        api_response = api_instance.get_country_states_async(country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_country_states_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_country_states_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryStateDtoListEnvelope**](CountryStateDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enabled_currencies_by_country_id_async**
> CurrencyDtoListEnvelope get_enabled_currencies_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)

Get currencies for a country

Retrieves the list of enabled currencies for the specified country.

### Example


```python
import openapi_client
from openapi_client.models.currency_dto_list_envelope import CurrencyDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get currencies for a country
        api_response = api_instance.get_enabled_currencies_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_enabled_currencies_by_country_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_enabled_currencies_by_country_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CurrencyDtoListEnvelope**](CurrencyDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_zones_by_country_id_async**
> TimezoneDtoListEnvelope get_time_zones_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)

Get timezones for a country

Retrieves the list of timezones associated with the specified country.

### Example


```python
import openapi_client
from openapi_client.models.timezone_dto_list_envelope import TimezoneDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get timezones for a country
        api_response = api_instance.get_time_zones_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_time_zones_by_country_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_time_zones_by_country_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TimezoneDtoListEnvelope**](TimezoneDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_level_domains_by_country_id_async**
> CountryTopLevelDomainDtoListEnvelope get_top_level_domains_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)

Get top-level domains for a country

Retrieves the list of internet top-level domains (TLDs) associated with the specified country.

### Example


```python
import openapi_client
from openapi_client.models.country_top_level_domain_dto_list_envelope import CountryTopLevelDomainDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_id = 'country_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get top-level domains for a country
        api_response = api_instance.get_top_level_domains_by_country_id_async(country_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->get_top_level_domains_by_country_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->get_top_level_domains_by_country_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryTopLevelDomainDtoListEnvelope**](CountryTopLevelDomainDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_countries_by_name_async**
> CountryDtoListEnvelope search_countries_by_name_async(country_name, api_version=api_version, x_api_version=x_api_version)

Search countries by name

Searches for countries whose name matches the specified search term.

### Example


```python
import openapi_client
from openapi_client.models.country_dto_list_envelope import CountryDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CountriesApi(api_client)
    country_name = 'country_name_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Search countries by name
        api_response = api_instance.search_countries_by_name_async(country_name, api_version=api_version, x_api_version=x_api_version)
        print("The response of CountriesApi->search_countries_by_name_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountriesApi->search_countries_by_name_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_name** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryDtoListEnvelope**](CountryDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

