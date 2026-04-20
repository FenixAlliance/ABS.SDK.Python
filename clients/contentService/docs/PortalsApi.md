# openapi_client.PortalsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_portals_async**](PortalsApi.md#count_portals_async) | **GET** /api/v2/ContentService/Portals/Count | Count portals
[**create_web_portal_async**](PortalsApi.md#create_web_portal_async) | **POST** /api/v2/ContentService/Portals | Create a new web portal
[**delete_web_portal_async**](PortalsApi.md#delete_web_portal_async) | **DELETE** /api/v2/ContentService/Portals/{portalId} | Delete a web portal
[**get_current_web_portal_async**](PortalsApi.md#get_current_web_portal_async) | **GET** /api/v2/ContentService/Portals/Current | Get the current portal
[**get_current_web_portal_options_async**](PortalsApi.md#get_current_web_portal_options_async) | **GET** /api/v2/ContentService/Portals/Current/Options | Get the current portal&#39;s options
[**get_portals_async**](PortalsApi.md#get_portals_async) | **GET** /api/v2/ContentService/Portals | Get portals
[**get_root_web_portal_async**](PortalsApi.md#get_root_web_portal_async) | **GET** /api/v2/ContentService/Portals/Root | Get the root portal
[**get_web_portal_by_id_async**](PortalsApi.md#get_web_portal_by_id_async) | **GET** /api/v2/ContentService/Portals/{portalId} | Get a web portal by its ID
[**get_web_portal_options_async**](PortalsApi.md#get_web_portal_options_async) | **GET** /api/v2/ContentService/Portals/{portalId}/Options | Get a web portal&#39;s options by its ID
[**get_web_portal_settings_async**](PortalsApi.md#get_web_portal_settings_async) | **GET** /api/v2/ContentService/Portals/{portalId}/Settings | Get a web portal&#39;s settings by its ID
[**initialize_current_web_portal_async**](PortalsApi.md#initialize_current_web_portal_async) | **POST** /api/v2/ContentService/Portals/Initialize | Initialize the current portal
[**patch_web_portal_async**](PortalsApi.md#patch_web_portal_async) | **PATCH** /api/v2/ContentService/Portals/{portalId} | Partially update a web portal
[**search_web_portal_async**](PortalsApi.md#search_web_portal_async) | **GET** /api/v2/ContentService/Portals/Search | Search for a portal by its domain
[**update_web_portal_async**](PortalsApi.md#update_web_portal_async) | **PUT** /api/v2/ContentService/Portals/{portalId} | Update an existing web portal


# **count_portals_async**
> Int32Envelope count_portals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count portals

Counts all portals for the specified tenant.

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
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count portals
        api_response = api_instance.count_portals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->count_portals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->count_portals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **create_web_portal_async**
> EmptyEnvelope create_web_portal_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_portal_create_dto=web_portal_create_dto)

Create a new web portal

Create a new web portal

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
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_portal_create_dto = openapi_client.WebPortalCreateDto() # WebPortalCreateDto |  (optional)

    try:
        # Create a new web portal
        api_response = api_instance.create_web_portal_async(tenant_id, api_version=api_version, x_api_version=x_api_version, web_portal_create_dto=web_portal_create_dto)
        print("The response of PortalsApi->create_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->create_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **delete_web_portal_async**
> EmptyEnvelope delete_web_portal_async(tenant_id, portal_id, api_version=api_version, x_api_version=x_api_version)

Delete a web portal

Delete a web portal

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
    tenant_id = 'tenant_id_example' # str | 
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a web portal
        api_response = api_instance.delete_web_portal_async(tenant_id, portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->delete_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->delete_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_current_web_portal_async**
> WebPortalDtoEnvelope get_current_web_portal_async(api_version=api_version, x_api_version=x_api_version)

Get the current portal

Get the current portal of the this server instance

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
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the current portal
        api_response = api_instance.get_current_web_portal_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_current_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_current_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_current_web_portal_options_async**
> PortalOptionsEnvelope get_current_web_portal_options_async(api_version=api_version, x_api_version=x_api_version)

Get the current portal's options

Get the current portal's options for the current user.

### Example


```python
import openapi_client
from openapi_client.models.portal_options_envelope import PortalOptionsEnvelope
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
        # Get the current portal's options
        api_response = api_instance.get_current_web_portal_options_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_current_web_portal_options_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_current_web_portal_options_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PortalOptionsEnvelope**](PortalOptionsEnvelope.md)

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

# **get_portals_async**
> WebPortalDtoListEnvelope get_portals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get portals

Retrieves all portals for the specified tenant.

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
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get portals
        api_response = api_instance.get_portals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_portals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_portals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **get_root_web_portal_async**
> WebPortalDtoEnvelope get_root_web_portal_async(api_version=api_version, x_api_version=x_api_version)

Get the root portal

Get the root portal of the this server instance

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
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the root portal
        api_response = api_instance.get_root_web_portal_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_root_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_root_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_web_portal_by_id_async**
> WebPortalDtoEnvelope get_web_portal_by_id_async(portal_id, api_version=api_version, x_api_version=x_api_version)

Get a web portal by its ID

Get a web portal by its ID

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
        # Get a web portal by its ID
        api_response = api_instance.get_web_portal_by_id_async(portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_web_portal_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_web_portal_by_id_async: %s\n" % e)
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

# **get_web_portal_options_async**
> PortalOptionsEnvelope get_web_portal_options_async(portal_id, api_version=api_version, x_api_version=x_api_version)

Get a web portal's options by its ID

Get a web portal's options by its ID

### Example


```python
import openapi_client
from openapi_client.models.portal_options_envelope import PortalOptionsEnvelope
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
        # Get a web portal's options by its ID
        api_response = api_instance.get_web_portal_options_async(portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_web_portal_options_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_web_portal_options_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PortalOptionsEnvelope**](PortalOptionsEnvelope.md)

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

# **get_web_portal_settings_async**
> PortalSettingsEnvelope get_web_portal_settings_async(portal_id, api_version=api_version, x_api_version=x_api_version)

Get a web portal's settings by its ID

Get a web portal's settings by its ID

### Example


```python
import openapi_client
from openapi_client.models.portal_settings_envelope import PortalSettingsEnvelope
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
        # Get a web portal's settings by its ID
        api_response = api_instance.get_web_portal_settings_async(portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->get_web_portal_settings_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->get_web_portal_settings_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PortalSettingsEnvelope**](PortalSettingsEnvelope.md)

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

# **initialize_current_web_portal_async**
> WebPortalDtoEnvelope initialize_current_web_portal_async(api_version=api_version, x_api_version=x_api_version)

Initialize the current portal

Initialize the current portal for the current user.

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
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Initialize the current portal
        api_response = api_instance.initialize_current_web_portal_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->initialize_current_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->initialize_current_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **patch_web_portal_async**
> EmptyEnvelope patch_web_portal_async(tenant_id, portal_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Partially update a web portal

Partially update a web portal

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    tenant_id = 'tenant_id_example' # str | 
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Partially update a web portal
        api_response = api_instance.patch_web_portal_async(tenant_id, portal_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of PortalsApi->patch_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->patch_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **portal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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

# **search_web_portal_async**
> WebPortalDtoEnvelope search_web_portal_async(domain, api_version=api_version, x_api_version=x_api_version)

Search for a portal by its domain

Search for a portal by its domain

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
    domain = 'domain_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Search for a portal by its domain
        api_response = api_instance.search_web_portal_async(domain, api_version=api_version, x_api_version=x_api_version)
        print("The response of PortalsApi->search_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->search_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 
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

# **update_web_portal_async**
> EmptyEnvelope update_web_portal_async(tenant_id, portal_id, api_version=api_version, x_api_version=x_api_version, web_portal_update_dto=web_portal_update_dto)

Update an existing web portal

Update an existing web portal

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
    tenant_id = 'tenant_id_example' # str | 
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    web_portal_update_dto = openapi_client.WebPortalUpdateDto() # WebPortalUpdateDto |  (optional)

    try:
        # Update an existing web portal
        api_response = api_instance.update_web_portal_async(tenant_id, portal_id, api_version=api_version, x_api_version=x_api_version, web_portal_update_dto=web_portal_update_dto)
        print("The response of PortalsApi->update_web_portal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalsApi->update_web_portal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

