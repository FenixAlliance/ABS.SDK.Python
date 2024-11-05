# openapi_client.SupportTicketTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_support_service_support_ticket_types_count_get**](SupportTicketTypesApi.md#api_v2_support_service_support_ticket_types_count_get) | **GET** /api/v2/SupportService/SupportTicketTypes/Count | 
[**api_v2_support_service_support_ticket_types_get**](SupportTicketTypesApi.md#api_v2_support_service_support_ticket_types_get) | **GET** /api/v2/SupportService/SupportTicketTypes | 
[**api_v2_support_service_support_ticket_types_post**](SupportTicketTypesApi.md#api_v2_support_service_support_ticket_types_post) | **POST** /api/v2/SupportService/SupportTicketTypes | 
[**api_v2_support_service_support_ticket_types_support_ticket_type_id_delete**](SupportTicketTypesApi.md#api_v2_support_service_support_ticket_types_support_ticket_type_id_delete) | **DELETE** /api/v2/SupportService/SupportTicketTypes/{supportTicketTypeId} | 
[**api_v2_support_service_support_ticket_types_support_ticket_type_id_get**](SupportTicketTypesApi.md#api_v2_support_service_support_ticket_types_support_ticket_type_id_get) | **GET** /api/v2/SupportService/SupportTicketTypes/{supportTicketTypeId} | 
[**api_v2_support_service_support_ticket_types_support_ticket_type_id_put**](SupportTicketTypesApi.md#api_v2_support_service_support_ticket_types_support_ticket_type_id_put) | **PUT** /api/v2/SupportService/SupportTicketTypes/{supportTicketTypeId} | 


# **api_v2_support_service_support_ticket_types_count_get**
> Int32Envelope api_v2_support_service_support_ticket_types_count_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_ticket_types_count_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->api_v2_support_service_support_ticket_types_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->api_v2_support_service_support_ticket_types_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_ticket_types_get**
> SupportTicketTypeDtoListEnvelope api_v2_support_service_support_ticket_types_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_ticket_type_dto_list_envelope import SupportTicketTypeDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_ticket_types_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->api_v2_support_service_support_ticket_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->api_v2_support_service_support_ticket_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketTypeDtoListEnvelope**](SupportTicketTypeDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_ticket_types_post**
> EmptyEnvelope api_v2_support_service_support_ticket_types_post(support_ticket_type_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_type_create_dto import SupportTicketTypeCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    support_ticket_type_create_dto = openapi_client.SupportTicketTypeCreateDto() # SupportTicketTypeCreateDto | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_ticket_types_post(support_ticket_type_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->api_v2_support_service_support_ticket_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->api_v2_support_service_support_ticket_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_type_create_dto** | [**SupportTicketTypeCreateDto**](SupportTicketTypeCreateDto.md)|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_ticket_types_support_ticket_type_id_delete**
> EmptyEnvelope api_v2_support_service_support_ticket_types_support_ticket_type_id_delete(support_ticket_type_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    support_ticket_type_id = 'support_ticket_type_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_ticket_types_support_ticket_type_id_delete(support_ticket_type_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->api_v2_support_service_support_ticket_types_support_ticket_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->api_v2_support_service_support_ticket_types_support_ticket_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_type_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_ticket_types_support_ticket_type_id_get**
> SupportTicketTypeDtoEnvelope api_v2_support_service_support_ticket_types_support_ticket_type_id_get(support_ticket_type_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_ticket_type_dto_envelope import SupportTicketTypeDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    support_ticket_type_id = 'support_ticket_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_ticket_types_support_ticket_type_id_get(support_ticket_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->api_v2_support_service_support_ticket_types_support_ticket_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->api_v2_support_service_support_ticket_types_support_ticket_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportTicketTypeDtoEnvelope**](SupportTicketTypeDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **api_v2_support_service_support_ticket_types_support_ticket_type_id_put**
> EmptyEnvelope api_v2_support_service_support_ticket_types_support_ticket_type_id_put(support_ticket_type_id, support_ticket_type_update_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_ticket_type_update_dto import SupportTicketTypeUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SupportTicketTypesApi(api_client)
    support_ticket_type_id = 'support_ticket_type_id_example' # str | 
    support_ticket_type_update_dto = openapi_client.SupportTicketTypeUpdateDto() # SupportTicketTypeUpdateDto | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_ticket_types_support_ticket_type_id_put(support_ticket_type_id, support_ticket_type_update_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportTicketTypesApi->api_v2_support_service_support_ticket_types_support_ticket_type_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportTicketTypesApi->api_v2_support_service_support_ticket_types_support_ticket_type_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_ticket_type_id** | **str**|  | 
 **support_ticket_type_update_dto** | [**SupportTicketTypeUpdateDto**](SupportTicketTypeUpdateDto.md)|  | 
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

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

