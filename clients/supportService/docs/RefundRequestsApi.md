# openapi_client.RefundRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_refund_request_async**](RefundRequestsApi.md#create_refund_request_async) | **POST** /api/v2/SupportService/RefundRequests | Create a refund request
[**delete_refund_request_async**](RefundRequestsApi.md#delete_refund_request_async) | **DELETE** /api/v2/SupportService/RefundRequests/{refundRequestId} | Delete a refund request
[**get_refund_request_async**](RefundRequestsApi.md#get_refund_request_async) | **GET** /api/v2/SupportService/RefundRequests/{refundRequestId} | Retrieve a refund request by ID
[**get_refund_requests_async**](RefundRequestsApi.md#get_refund_requests_async) | **GET** /api/v2/SupportService/RefundRequests | Retrieve refund requests
[**get_refund_requests_count_async**](RefundRequestsApi.md#get_refund_requests_count_async) | **GET** /api/v2/SupportService/RefundRequests/Count | Get refund requests count
[**patch_refund_request_async**](RefundRequestsApi.md#patch_refund_request_async) | **PATCH** /api/v2/SupportService/RefundRequests/{refundRequestId} | Patch a refund request
[**update_refund_request_async**](RefundRequestsApi.md#update_refund_request_async) | **PUT** /api/v2/SupportService/RefundRequests/{refundRequestId} | Update a refund request


# **create_refund_request_async**
> EmptyEnvelope create_refund_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, refund_request_create_dto=refund_request_create_dto)

Create a refund request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.refund_request_create_dto import RefundRequestCreateDto
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
    api_instance = openapi_client.RefundRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    refund_request_create_dto = openapi_client.RefundRequestCreateDto() # RefundRequestCreateDto |  (optional)

    try:
        # Create a refund request
        api_response = api_instance.create_refund_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, refund_request_create_dto=refund_request_create_dto)
        print("The response of RefundRequestsApi->create_refund_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->create_refund_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **refund_request_create_dto** | [**RefundRequestCreateDto**](RefundRequestCreateDto.md)|  | [optional] 

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

# **delete_refund_request_async**
> EmptyEnvelope delete_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version)

Delete a refund request

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
    api_instance = openapi_client.RefundRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    refund_request_id = 'refund_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a refund request
        api_response = api_instance.delete_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundRequestsApi->delete_refund_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->delete_refund_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **refund_request_id** | **str**|  | 
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

# **get_refund_request_async**
> RefundRequestDtoEnvelope get_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a refund request by ID

### Example


```python
import openapi_client
from openapi_client.models.refund_request_dto_envelope import RefundRequestDtoEnvelope
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
    api_instance = openapi_client.RefundRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    refund_request_id = 'refund_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a refund request by ID
        api_response = api_instance.get_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundRequestsApi->get_refund_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->get_refund_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **refund_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RefundRequestDtoEnvelope**](RefundRequestDtoEnvelope.md)

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

# **get_refund_requests_async**
> RefundRequestDtoListEnvelope get_refund_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve refund requests

### Example


```python
import openapi_client
from openapi_client.models.refund_request_dto_list_envelope import RefundRequestDtoListEnvelope
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
    api_instance = openapi_client.RefundRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve refund requests
        api_response = api_instance.get_refund_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundRequestsApi->get_refund_requests_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->get_refund_requests_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**RefundRequestDtoListEnvelope**](RefundRequestDtoListEnvelope.md)

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

# **get_refund_requests_count_async**
> Int32Envelope get_refund_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get refund requests count

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
    api_instance = openapi_client.RefundRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get refund requests count
        api_response = api_instance.get_refund_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RefundRequestsApi->get_refund_requests_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->get_refund_requests_count_async: %s\n" % e)
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

# **patch_refund_request_async**
> EmptyEnvelope patch_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a refund request

Partially updates an existing refund request by its unique identifier.

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
    api_instance = openapi_client.RefundRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    refund_request_id = 'refund_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a refund request
        api_response = api_instance.patch_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of RefundRequestsApi->patch_refund_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->patch_refund_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **refund_request_id** | **str**|  | 
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

# **update_refund_request_async**
> EmptyEnvelope update_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version, refund_request_update_dto=refund_request_update_dto)

Update a refund request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.refund_request_update_dto import RefundRequestUpdateDto
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
    api_instance = openapi_client.RefundRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    refund_request_id = 'refund_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    refund_request_update_dto = openapi_client.RefundRequestUpdateDto() # RefundRequestUpdateDto |  (optional)

    try:
        # Update a refund request
        api_response = api_instance.update_refund_request_async(tenant_id, refund_request_id, api_version=api_version, x_api_version=x_api_version, refund_request_update_dto=refund_request_update_dto)
        print("The response of RefundRequestsApi->update_refund_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->update_refund_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **refund_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **refund_request_update_dto** | [**RefundRequestUpdateDto**](RefundRequestUpdateDto.md)|  | [optional] 

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

