# openapi_client.InquiryRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inquiry_request_async**](InquiryRequestsApi.md#create_inquiry_request_async) | **POST** /api/v2/SupportService/InquiryRequests | Create an inquiry request
[**delete_inquiry_request_async**](InquiryRequestsApi.md#delete_inquiry_request_async) | **DELETE** /api/v2/SupportService/InquiryRequests/{inquiryRequestId} | Delete an inquiry request
[**get_inquiry_request_async**](InquiryRequestsApi.md#get_inquiry_request_async) | **GET** /api/v2/SupportService/InquiryRequests/{inquiryRequestId} | Retrieve an inquiry request by ID
[**get_inquiry_requests_async**](InquiryRequestsApi.md#get_inquiry_requests_async) | **GET** /api/v2/SupportService/InquiryRequests | Retrieve inquiry requests
[**get_inquiry_requests_count_async**](InquiryRequestsApi.md#get_inquiry_requests_count_async) | **GET** /api/v2/SupportService/InquiryRequests/Count | Get inquiry requests count
[**patch_inquiry_request_async**](InquiryRequestsApi.md#patch_inquiry_request_async) | **PATCH** /api/v2/SupportService/InquiryRequests/{inquiryRequestId} | Patch an inquiry request
[**update_inquiry_request_async**](InquiryRequestsApi.md#update_inquiry_request_async) | **PUT** /api/v2/SupportService/InquiryRequests/{inquiryRequestId} | Update an inquiry request


# **create_inquiry_request_async**
> EmptyEnvelope create_inquiry_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, inquiry_request_create_dto=inquiry_request_create_dto)

Create an inquiry request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.inquiry_request_create_dto import InquiryRequestCreateDto
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
    api_instance = openapi_client.InquiryRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    inquiry_request_create_dto = openapi_client.InquiryRequestCreateDto() # InquiryRequestCreateDto |  (optional)

    try:
        # Create an inquiry request
        api_response = api_instance.create_inquiry_request_async(tenant_id, api_version=api_version, x_api_version=x_api_version, inquiry_request_create_dto=inquiry_request_create_dto)
        print("The response of InquiryRequestsApi->create_inquiry_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InquiryRequestsApi->create_inquiry_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **inquiry_request_create_dto** | [**InquiryRequestCreateDto**](InquiryRequestCreateDto.md)|  | [optional] 

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

# **delete_inquiry_request_async**
> EmptyEnvelope delete_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version)

Delete an inquiry request

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
    api_instance = openapi_client.InquiryRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    inquiry_request_id = 'inquiry_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an inquiry request
        api_response = api_instance.delete_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InquiryRequestsApi->delete_inquiry_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InquiryRequestsApi->delete_inquiry_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **inquiry_request_id** | **str**|  | 
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

# **get_inquiry_request_async**
> InquiryRequestDtoEnvelope get_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version)

Retrieve an inquiry request by ID

### Example


```python
import openapi_client
from openapi_client.models.inquiry_request_dto_envelope import InquiryRequestDtoEnvelope
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
    api_instance = openapi_client.InquiryRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    inquiry_request_id = 'inquiry_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve an inquiry request by ID
        api_response = api_instance.get_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InquiryRequestsApi->get_inquiry_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InquiryRequestsApi->get_inquiry_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **inquiry_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InquiryRequestDtoEnvelope**](InquiryRequestDtoEnvelope.md)

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

# **get_inquiry_requests_async**
> InquiryRequestDtoListEnvelope get_inquiry_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve inquiry requests

### Example


```python
import openapi_client
from openapi_client.models.inquiry_request_dto_list_envelope import InquiryRequestDtoListEnvelope
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
    api_instance = openapi_client.InquiryRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve inquiry requests
        api_response = api_instance.get_inquiry_requests_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InquiryRequestsApi->get_inquiry_requests_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InquiryRequestsApi->get_inquiry_requests_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InquiryRequestDtoListEnvelope**](InquiryRequestDtoListEnvelope.md)

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

# **get_inquiry_requests_count_async**
> Int32Envelope get_inquiry_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get inquiry requests count

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
    api_instance = openapi_client.InquiryRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get inquiry requests count
        api_response = api_instance.get_inquiry_requests_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InquiryRequestsApi->get_inquiry_requests_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InquiryRequestsApi->get_inquiry_requests_count_async: %s\n" % e)
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

# **patch_inquiry_request_async**
> EmptyEnvelope patch_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an inquiry request

Partially updates an existing inquiry request by its unique identifier.

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
    api_instance = openapi_client.InquiryRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    inquiry_request_id = 'inquiry_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an inquiry request
        api_response = api_instance.patch_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of InquiryRequestsApi->patch_inquiry_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InquiryRequestsApi->patch_inquiry_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **inquiry_request_id** | **str**|  | 
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

# **update_inquiry_request_async**
> EmptyEnvelope update_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version, inquiry_request_update_dto=inquiry_request_update_dto)

Update an inquiry request

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.inquiry_request_update_dto import InquiryRequestUpdateDto
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
    api_instance = openapi_client.InquiryRequestsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    inquiry_request_id = 'inquiry_request_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    inquiry_request_update_dto = openapi_client.InquiryRequestUpdateDto() # InquiryRequestUpdateDto |  (optional)

    try:
        # Update an inquiry request
        api_response = api_instance.update_inquiry_request_async(tenant_id, inquiry_request_id, api_version=api_version, x_api_version=x_api_version, inquiry_request_update_dto=inquiry_request_update_dto)
        print("The response of InquiryRequestsApi->update_inquiry_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InquiryRequestsApi->update_inquiry_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **inquiry_request_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **inquiry_request_update_dto** | [**InquiryRequestUpdateDto**](InquiryRequestUpdateDto.md)|  | [optional] 

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

