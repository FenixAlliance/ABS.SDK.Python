# openapi_client.TimezonesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_timezones_async**](TimezonesApi.md#count_timezones_async) | **GET** /api/v2/GlobeService/Timezones/Count | Count timezones
[**get_time_zone_by_id_async**](TimezonesApi.md#get_time_zone_by_id_async) | **GET** /api/v2/GlobeService/Timezones/{timeZoneId} | Get timezone by ID
[**get_time_zones_async**](TimezonesApi.md#get_time_zones_async) | **GET** /api/v2/GlobeService/Timezones | Get all timezones


# **count_timezones_async**
> Int32Envelope count_timezones_async(api_version=api_version, x_api_version=x_api_version)

Count timezones

Returns the total number of supported timezones, with optional OData filtering.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TimezonesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count timezones
        api_response = api_instance.count_timezones_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of TimezonesApi->count_timezones_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimezonesApi->count_timezones_async: %s\n" % e)
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
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_zone_by_id_async**
> TimezoneDtoEnvelope get_time_zone_by_id_async(time_zone_id, api_version=api_version, x_api_version=x_api_version)

Get timezone by ID

Retrieves a single timezone by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.timezone_dto_envelope import TimezoneDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TimezonesApi(api_client)
    time_zone_id = 'time_zone_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get timezone by ID
        api_response = api_instance.get_time_zone_by_id_async(time_zone_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TimezonesApi->get_time_zone_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimezonesApi->get_time_zone_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_zone_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TimezoneDtoEnvelope**](TimezoneDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_zones_async**
> TimezoneDtoListEnvelope get_time_zones_async(api_version=api_version, x_api_version=x_api_version)

Get all timezones

Retrieves the list of all supported timezones with optional OData pagination and filtering.

### Example


```python
import openapi_client
from openapi_client.models.timezone_dto_list_envelope import TimezoneDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TimezonesApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all timezones
        api_response = api_instance.get_time_zones_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of TimezonesApi->get_time_zones_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimezonesApi->get_time_zones_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TimezoneDtoListEnvelope**](TimezoneDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

