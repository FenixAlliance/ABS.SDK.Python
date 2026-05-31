# openapi_client.IPLookupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_ip_lookup**](IPLookupsApi.md#delete_system_ip_lookup) | **DELETE** /api/v2/SystemService/IPLookups/{ipLookupId} | Delete a system IP lookup
[**get_system_ip_lookup_by_id**](IPLookupsApi.md#get_system_ip_lookup_by_id) | **GET** /api/v2/SystemService/IPLookups/{ipLookupId} | Retrieve a single system IP lookup by its ID
[**get_system_ip_lookups**](IPLookupsApi.md#get_system_ip_lookups) | **GET** /api/v2/SystemService/IPLookups | Retrieve a list of system IP lookups
[**get_system_ip_lookups_count**](IPLookupsApi.md#get_system_ip_lookups_count) | **GET** /api/v2/SystemService/IPLookups/Count | Get the count of system IP lookups


# **delete_system_ip_lookup**
> EmptyEnvelope delete_system_ip_lookup(ip_lookup_id, api_version=api_version, x_api_version=x_api_version)

Delete a system IP lookup

Delete a system IP lookup by its ID

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.IPLookupsApi(api_client)
    ip_lookup_id = 'ip_lookup_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a system IP lookup
        api_response = api_instance.delete_system_ip_lookup(ip_lookup_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of IPLookupsApi->delete_system_ip_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPLookupsApi->delete_system_ip_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_lookup_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

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

# **get_system_ip_lookup_by_id**
> IPLookupDtoEnvelope get_system_ip_lookup_by_id(ip_lookup_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single system IP lookup by its ID

Retrieve a single system IP lookup by its ID

### Example


```python
import openapi_client
from openapi_client.models.ip_lookup_dto_envelope import IPLookupDtoEnvelope
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
    api_instance = openapi_client.IPLookupsApi(api_client)
    ip_lookup_id = 'ip_lookup_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single system IP lookup by its ID
        api_response = api_instance.get_system_ip_lookup_by_id(ip_lookup_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of IPLookupsApi->get_system_ip_lookup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPLookupsApi->get_system_ip_lookup_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_lookup_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**IPLookupDtoEnvelope**](IPLookupDtoEnvelope.md)

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

# **get_system_ip_lookups**
> IPLookupDtoListEnvelope get_system_ip_lookups(api_version=api_version, x_api_version=x_api_version)

Retrieve a list of system IP lookups

Retrieve a list of all IP lookups in the system

### Example


```python
import openapi_client
from openapi_client.models.ip_lookup_dto_list_envelope import IPLookupDtoListEnvelope
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
    api_instance = openapi_client.IPLookupsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of system IP lookups
        api_response = api_instance.get_system_ip_lookups(api_version=api_version, x_api_version=x_api_version)
        print("The response of IPLookupsApi->get_system_ip_lookups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPLookupsApi->get_system_ip_lookups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**IPLookupDtoListEnvelope**](IPLookupDtoListEnvelope.md)

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

# **get_system_ip_lookups_count**
> Int32Envelope get_system_ip_lookups_count(api_version=api_version, x_api_version=x_api_version)

Get the count of system IP lookups

Get the count of all IP lookups in the system

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
    api_instance = openapi_client.IPLookupsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of system IP lookups
        api_response = api_instance.get_system_ip_lookups_count(api_version=api_version, x_api_version=x_api_version)
        print("The response of IPLookupsApi->get_system_ip_lookups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPLookupsApi->get_system_ip_lookups_count: %s\n" % e)
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

