# openapi_client.WarrantyRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_warranty_request_async**](WarrantyRequestsApi.md#create_warranty_request_async) | **POST** /api/v2/SupportService/WarrantyRequests | Create a warranty request
[**delete_warranty_request_async**](WarrantyRequestsApi.md#delete_warranty_request_async) | **DELETE** /api/v2/SupportService/WarrantyRequests/{warrantyRequestId} | Delete a warranty request
[**get_warranty_request_async**](WarrantyRequestsApi.md#get_warranty_request_async) | **GET** /api/v2/SupportService/WarrantyRequests/{warrantyRequestId} | Retrieve a warranty request by ID
[**get_warranty_requests_async**](WarrantyRequestsApi.md#get_warranty_requests_async) | **GET** /api/v2/SupportService/WarrantyRequests | Retrieve warranty requests
[**get_warranty_requests_count_async**](WarrantyRequestsApi.md#get_warranty_requests_count_async) | **GET** /api/v2/SupportService/WarrantyRequests/Count | Get warranty requests count
[**update_warranty_request_async**](WarrantyRequestsApi.md#update_warranty_request_async) | **PUT** /api/v2/SupportService/WarrantyRequests/{warrantyRequestId} | Update a warranty request


# **create_warranty_request_async**
> EmptyEnvelope create_warranty_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, warranty_request_create_dto=warranty_request_create_dto)

Create a warranty request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.warranty_request_create_dto import WarrantyRequestCreateDto
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
    api_instance = openapi_client.WarrantyRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    warranty_request_create_dto = openapi_client.WarrantyRequestCreateDto() # WarrantyRequestCreateDto |  (optional)

    try:
        # Create a warranty request
        api_response = api_instance.create_warranty_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, warranty_request_create_dto=warranty_request_create_dto)
        print("The response of WarrantyRequestsApi->create_warranty_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyRequestsApi->create_warranty_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **warranty_request_create_dto** | [**WarrantyRequestCreateDto**](WarrantyRequestCreateDto.md)|  | [optional] 

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

# **delete_warranty_request_async**
> EmptyEnvelope delete_warranty_request_async(tenant_id, warranty_request_id, api_version=api_version, x_api_version=x_api_version)

Delete a warranty request

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
    api_instance = openapi_client.WarrantyRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warranty_request_id = 'warranty_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a warranty request
        api_response = api_instance.delete_warranty_request_async(tenant_id, warranty_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyRequestsApi->delete_warranty_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyRequestsApi->delete_warranty_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warranty_request_id** | **str**|  | 
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

# **get_warranty_request_async**
> WarrantyRequestDtoEnvelope get_warranty_request_async(tenant_id, warranty_request_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a warranty request by ID

### Example


```python
import openapi_client
from openapi_client.models.warranty_request_dto_envelope import WarrantyRequestDtoEnvelope
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
    api_instance = openapi_client.WarrantyRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warranty_request_id = 'warranty_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a warranty request by ID
        api_response = api_instance.get_warranty_request_async(tenant_id, warranty_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyRequestsApi->get_warranty_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyRequestsApi->get_warranty_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warranty_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WarrantyRequestDtoEnvelope**](WarrantyRequestDtoEnvelope.md)

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

# **get_warranty_requests_async**
> WarrantyRequestDtoListEnvelope get_warranty_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve warranty requests

### Example


```python
import openapi_client
from openapi_client.models.warranty_request_dto_list_envelope import WarrantyRequestDtoListEnvelope
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
    api_instance = openapi_client.WarrantyRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve warranty requests
        api_response = api_instance.get_warranty_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyRequestsApi->get_warranty_requests_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyRequestsApi->get_warranty_requests_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WarrantyRequestDtoListEnvelope**](WarrantyRequestDtoListEnvelope.md)

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

# **get_warranty_requests_count_async**
> Int32Envelope get_warranty_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get warranty requests count

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
    api_instance = openapi_client.WarrantyRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get warranty requests count
        api_response = api_instance.get_warranty_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WarrantyRequestsApi->get_warranty_requests_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyRequestsApi->get_warranty_requests_count_async: %s\n" % e)
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

# **update_warranty_request_async**
> EmptyEnvelope update_warranty_request_async(tenant_id, warranty_request_id, api_version=api_version, x_api_version=x_api_version, warranty_request_update_dto=warranty_request_update_dto)

Update a warranty request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.warranty_request_update_dto import WarrantyRequestUpdateDto
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
    api_instance = openapi_client.WarrantyRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    warranty_request_id = 'warranty_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    warranty_request_update_dto = openapi_client.WarrantyRequestUpdateDto() # WarrantyRequestUpdateDto |  (optional)

    try:
        # Update a warranty request
        api_response = api_instance.update_warranty_request_async(tenant_id, warranty_request_id, api_version=api_version, x_api_version=x_api_version, warranty_request_update_dto=warranty_request_update_dto)
        print("The response of WarrantyRequestsApi->update_warranty_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarrantyRequestsApi->update_warranty_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **warranty_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **warranty_request_update_dto** | [**WarrantyRequestUpdateDto**](WarrantyRequestUpdateDto.md)|  | [optional] 

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

