# openapi_client.MarketingListsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_marketing_service_marketing_lists_count_get**](MarketingListsApi.md#api_v2_marketing_service_marketing_lists_count_get) | **GET** /api/v2/MarketingService/MarketingLists/Count | 
[**api_v2_marketing_service_marketing_lists_get**](MarketingListsApi.md#api_v2_marketing_service_marketing_lists_get) | **GET** /api/v2/MarketingService/MarketingLists | 
[**api_v2_marketing_service_marketing_lists_marketinglist_id_delete**](MarketingListsApi.md#api_v2_marketing_service_marketing_lists_marketinglist_id_delete) | **DELETE** /api/v2/MarketingService/MarketingLists/{marketinglistId} | 
[**api_v2_marketing_service_marketing_lists_marketinglist_id_get**](MarketingListsApi.md#api_v2_marketing_service_marketing_lists_marketinglist_id_get) | **GET** /api/v2/MarketingService/MarketingLists/{marketinglistId} | 
[**api_v2_marketing_service_marketing_lists_marketinglist_id_put**](MarketingListsApi.md#api_v2_marketing_service_marketing_lists_marketinglist_id_put) | **PUT** /api/v2/MarketingService/MarketingLists/{marketinglistId} | 
[**api_v2_marketing_service_marketing_lists_post**](MarketingListsApi.md#api_v2_marketing_service_marketing_lists_post) | **POST** /api/v2/MarketingService/MarketingLists | 


# **api_v2_marketing_service_marketing_lists_count_get**
> Int32Envelope api_v2_marketing_service_marketing_lists_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_lists_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->api_v2_marketing_service_marketing_lists_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->api_v2_marketing_service_marketing_lists_count_get: %s\n" % e)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_lists_get**
> MarketingListDtoListEnvelope api_v2_marketing_service_marketing_lists_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.marketing_list_dto_list_envelope import MarketingListDtoListEnvelope
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_lists_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->api_v2_marketing_service_marketing_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->api_v2_marketing_service_marketing_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingListDtoListEnvelope**](MarketingListDtoListEnvelope.md)

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

# **api_v2_marketing_service_marketing_lists_marketinglist_id_delete**
> EmptyEnvelope api_v2_marketing_service_marketing_lists_marketinglist_id_delete(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketinglist_id = 'marketinglist_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_lists_marketinglist_id_delete(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->api_v2_marketing_service_marketing_lists_marketinglist_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->api_v2_marketing_service_marketing_lists_marketinglist_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketinglist_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_lists_marketinglist_id_get**
> MarketingListDtoEnvelope api_v2_marketing_service_marketing_lists_marketinglist_id_get(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.marketing_list_dto_envelope import MarketingListDtoEnvelope
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketinglist_id = 'marketinglist_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_lists_marketinglist_id_get(tenant_id, marketinglist_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->api_v2_marketing_service_marketing_lists_marketinglist_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->api_v2_marketing_service_marketing_lists_marketinglist_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketinglist_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingListDtoEnvelope**](MarketingListDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_lists_marketinglist_id_put**
> EmptyEnvelope api_v2_marketing_service_marketing_lists_marketinglist_id_put(tenant_id, marketinglist_id, marketing_list_update_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_list_update_dto import MarketingListUpdateDto
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketinglist_id = 'marketinglist_id_example' # str | 
    marketing_list_update_dto = openapi_client.MarketingListUpdateDto() # MarketingListUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_lists_marketinglist_id_put(tenant_id, marketinglist_id, marketing_list_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->api_v2_marketing_service_marketing_lists_marketinglist_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->api_v2_marketing_service_marketing_lists_marketinglist_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketinglist_id** | **str**|  | 
 **marketing_list_update_dto** | [**MarketingListUpdateDto**](MarketingListUpdateDto.md)|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_marketing_service_marketing_lists_post**
> EmptyEnvelope api_v2_marketing_service_marketing_lists_post(tenant_id, marketing_list_create_dto, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_list_create_dto import MarketingListCreateDto
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
    api_instance = openapi_client.MarketingListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_list_create_dto = openapi_client.MarketingListCreateDto() # MarketingListCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_marketing_service_marketing_lists_post(tenant_id, marketing_list_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingListsApi->api_v2_marketing_service_marketing_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingListsApi->api_v2_marketing_service_marketing_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_list_create_dto** | [**MarketingListCreateDto**](MarketingListCreateDto.md)|  | 
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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

