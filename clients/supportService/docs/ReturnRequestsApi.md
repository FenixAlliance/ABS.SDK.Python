# openapi_client.ReturnRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_return_request_async**](ReturnRequestsApi.md#create_return_request_async) | **POST** /api/v2/SupportService/ReturnRequests | Create a return request
[**delete_return_request_async**](ReturnRequestsApi.md#delete_return_request_async) | **DELETE** /api/v2/SupportService/ReturnRequests/{returnRequestId} | Delete a return request
[**get_return_request_async**](ReturnRequestsApi.md#get_return_request_async) | **GET** /api/v2/SupportService/ReturnRequests/{returnRequestId} | Retrieve a return request by ID
[**get_return_requests_async**](ReturnRequestsApi.md#get_return_requests_async) | **GET** /api/v2/SupportService/ReturnRequests | Retrieve return requests
[**get_return_requests_count_async**](ReturnRequestsApi.md#get_return_requests_count_async) | **GET** /api/v2/SupportService/ReturnRequests/Count | Get return requests count
[**patch_return_request_async**](ReturnRequestsApi.md#patch_return_request_async) | **PATCH** /api/v2/SupportService/ReturnRequests/{returnRequestId} | Patch a return request
[**update_return_request_async**](ReturnRequestsApi.md#update_return_request_async) | **PUT** /api/v2/SupportService/ReturnRequests/{returnRequestId} | Update a return request


# **create_return_request_async**
> EmptyEnvelope create_return_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, return_request_create_dto=return_request_create_dto)

Create a return request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.return_request_create_dto import ReturnRequestCreateDto
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
    api_instance = openapi_client.ReturnRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    return_request_create_dto = openapi_client.ReturnRequestCreateDto() # ReturnRequestCreateDto |  (optional)

    try:
        # Create a return request
        api_response = api_instance.create_return_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, return_request_create_dto=return_request_create_dto)
        print("The response of ReturnRequestsApi->create_return_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnRequestsApi->create_return_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **return_request_create_dto** | [**ReturnRequestCreateDto**](ReturnRequestCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_return_request_async**
> EmptyEnvelope delete_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version)

Delete a return request

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
    api_instance = openapi_client.ReturnRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    return_request_id = 'return_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a return request
        api_response = api_instance.delete_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnRequestsApi->delete_return_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnRequestsApi->delete_return_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **return_request_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_request_async**
> ReturnRequestDtoEnvelope get_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a return request by ID

### Example


```python
import openapi_client
from openapi_client.models.return_request_dto_envelope import ReturnRequestDtoEnvelope
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
    api_instance = openapi_client.ReturnRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    return_request_id = 'return_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a return request by ID
        api_response = api_instance.get_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnRequestsApi->get_return_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnRequestsApi->get_return_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **return_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ReturnRequestDtoEnvelope**](ReturnRequestDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_requests_async**
> ReturnRequestDtoListEnvelope get_return_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve return requests

### Example


```python
import openapi_client
from openapi_client.models.return_request_dto_list_envelope import ReturnRequestDtoListEnvelope
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
    api_instance = openapi_client.ReturnRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve return requests
        api_response = api_instance.get_return_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnRequestsApi->get_return_requests_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnRequestsApi->get_return_requests_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ReturnRequestDtoListEnvelope**](ReturnRequestDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return_requests_count_async**
> Int32Envelope get_return_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get return requests count

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
    api_instance = openapi_client.ReturnRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get return requests count
        api_response = api_instance.get_return_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ReturnRequestsApi->get_return_requests_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnRequestsApi->get_return_requests_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_return_request_async**
> EmptyEnvelope patch_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a return request

Partially updates an existing return request by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.ReturnRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    return_request_id = 'return_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a return request
        api_response = api_instance.patch_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ReturnRequestsApi->patch_return_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnRequestsApi->patch_return_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **return_request_id** | **str**|  | 
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

# **update_return_request_async**
> EmptyEnvelope update_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version, return_request_update_dto=return_request_update_dto)

Update a return request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.return_request_update_dto import ReturnRequestUpdateDto
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
    api_instance = openapi_client.ReturnRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    return_request_id = 'return_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    return_request_update_dto = openapi_client.ReturnRequestUpdateDto() # ReturnRequestUpdateDto |  (optional)

    try:
        # Update a return request
        api_response = api_instance.update_return_request_async(tenant_id, return_request_id, api_version=api_version, x_api_version=x_api_version, return_request_update_dto=return_request_update_dto)
        print("The response of ReturnRequestsApi->update_return_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnRequestsApi->update_return_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **return_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **return_request_update_dto** | [**ReturnRequestUpdateDto**](ReturnRequestUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

