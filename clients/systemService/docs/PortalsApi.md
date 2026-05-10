# openapi_client.PortalsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_system_portal**](PortalsApi.md#create_system_portal) | **POST** /api/v2/SystemService/Portals | Create a new system portal
[**delete_system_portal**](PortalsApi.md#delete_system_portal) | **DELETE** /api/v2/SystemService/Portals/{portalId} | Delete a system portal
[**get_system_portal_by_id**](PortalsApi.md#get_system_portal_by_id) | **GET** /api/v2/SystemService/Portals/{portalId} | Retrieve a single system portal by its ID
[**get_system_portals**](PortalsApi.md#get_system_portals) | **GET** /api/v2/SystemService/Portals | Retrieve a list of system portals
[**get_system_portals_count**](PortalsApi.md#get_system_portals_count) | **GET** /api/v2/SystemService/Portals/Count | Get the count of system portals
[**update_system_portal**](PortalsApi.md#update_system_portal) | **PUT** /api/v2/SystemService/Portals/{portalId} | Update a system portal


# **create_system_portal**
> EmptyEnvelope create_system_portal(api_version=api_version, x_api_version=x_api_version, web_portal_create_dto=web_portal_create_dto)

Create a new system portal

Create a new web portal in the system

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_portal_create_dto import WebPortalCreateDto
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
    api_instance = openapi_client.PortalsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_portal_create_dto = openapi_client.WebPortalCreateDto() # WebPortalCreateDto |  (optional)

    try:
        # Create a new system portal
        api_response = api_instance.create_system_portal(api_version=api_version, x_api_version=x_api_version, web_portal_create_dto=web_portal_create_dto)
        print("The response of PortalsApi->create_system_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->create_system_portal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_portal_create_dto** | [**WebPortalCreateDto**](WebPortalCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_portal**
> EmptyEnvelope delete_system_portal(portal_id, api_version=api_version, x_api_version=x_api_version)

Delete a system portal

Delete a web portal from the system

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.PortalsApi(api_client)
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a system portal
        api_response = api_instance.delete_system_portal(portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->delete_system_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->delete_system_portal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
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

# **get_system_portal_by_id**
> WebPortalDtoEnvelope get_system_portal_by_id(portal_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single system portal by its ID

Retrieve a single system portal by its ID

### Example


```python
import openapi_client
from openapi_client.models.web_portal_dto_envelope import WebPortalDtoEnvelope
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
    api_instance = openapi_client.PortalsApi(api_client)
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single system portal by its ID
        api_response = api_instance.get_system_portal_by_id(portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_system_portal_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_system_portal_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPortalDtoEnvelope**](WebPortalDtoEnvelope.md)

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

# **get_system_portals**
> WebPortalDtoListEnvelope get_system_portals(api_version=api_version, x_api_version=x_api_version)

Retrieve a list of system portals

Retrieve a list of all web portals in the system

### Example


```python
import openapi_client
from openapi_client.models.web_portal_dto_list_envelope import WebPortalDtoListEnvelope
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
    api_instance = openapi_client.PortalsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of system portals
        api_response = api_instance.get_system_portals(api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_system_portals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_system_portals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WebPortalDtoListEnvelope**](WebPortalDtoListEnvelope.md)

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

# **get_system_portals_count**
> Int32Envelope get_system_portals_count(api_version=api_version, x_api_version=x_api_version)

Get the count of system portals

Get the count of all web portals in the system

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
    api_instance = openapi_client.PortalsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of system portals
        api_response = api_instance.get_system_portals_count(api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_system_portals_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_system_portals_count: %s\n" % e)
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

# **update_system_portal**
> EmptyEnvelope update_system_portal(portal_id, api_version=api_version, x_api_version=x_api_version, web_portal_update_dto=web_portal_update_dto)

Update a system portal

Update an existing web portal in the system

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.web_portal_update_dto import WebPortalUpdateDto
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
    api_instance = openapi_client.PortalsApi(api_client)
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_portal_update_dto = openapi_client.WebPortalUpdateDto() # WebPortalUpdateDto |  (optional)

    try:
        # Update a system portal
        api_response = api_instance.update_system_portal(portal_id, api_version=api_version, x_api_version=x_api_version, web_portal_update_dto=web_portal_update_dto)
        print("The response of PortalsApi->update_system_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->update_system_portal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **web_portal_update_dto** | [**WebPortalUpdateDto**](WebPortalUpdateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

