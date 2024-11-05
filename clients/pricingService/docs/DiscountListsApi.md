# openapi_client.DiscountListsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_pricing_service_discount_lists_count_get**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_count_get) | **GET** /api/v2/PricingService/DiscountLists/Count | 
[**api_v2_pricing_service_discount_lists_discount_list_id_delete**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_delete) | **DELETE** /api/v2/PricingService/DiscountLists/{discountListId} | 
[**api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/Count | 
[**api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete) | **DELETE** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | 
[**api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put) | **PUT** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | 
[**api_v2_pricing_service_discount_lists_discount_list_id_discounts_get**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_get) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts | 
[**api_v2_pricing_service_discount_lists_discount_list_id_discounts_post**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_discounts_post) | **POST** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts | 
[**api_v2_pricing_service_discount_lists_discount_list_id_get**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_get) | **GET** /api/v2/PricingService/DiscountLists/{discountListId} | 
[**api_v2_pricing_service_discount_lists_discount_list_id_put**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_discount_list_id_put) | **PUT** /api/v2/PricingService/DiscountLists/{discountListId} | 
[**api_v2_pricing_service_discount_lists_get**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_get) | **GET** /api/v2/PricingService/DiscountLists | 
[**api_v2_pricing_service_discount_lists_post**](DiscountListsApi.md#api_v2_pricing_service_discount_lists_post) | **POST** /api/v2/PricingService/DiscountLists | 
[**get_discount_list_entry**](DiscountListsApi.md#get_discount_list_entry) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | 


# **api_v2_pricing_service_discount_lists_count_get**
> Int32Envelope api_v2_pricing_service_discount_lists_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_count_get: %s\n" % e)
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_delete**
> EmptyEnvelope api_v2_pricing_service_discount_lists_discount_list_id_delete(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_delete(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get**
> Int32Envelope api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete**
> EmptyEnvelope api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete(tenant_id, discount_list_id, discount_list_entry_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_list_entry_id = 'discount_list_entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete(tenant_id, discount_list_id, discount_list_entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_list_entry_id** | **str**|  | 
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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put**
> EmptyEnvelope api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put(tenant_id, discount_list_id, discount_list_entry_id, api_version=api_version, x_api_version=x_api_version, discount_update_dto=discount_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_update_dto import DiscountUpdateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_list_entry_id = 'discount_list_entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    discount_update_dto = openapi_client.DiscountUpdateDto() # DiscountUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put(tenant_id, discount_list_id, discount_list_entry_id, api_version=api_version, x_api_version=x_api_version, discount_update_dto=discount_update_dto)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_discount_list_entry_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_list_entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **discount_update_dto** | [**DiscountUpdateDto**](DiscountUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_discounts_get**
> DiscountDtoListEnvelope api_v2_pricing_service_discount_lists_discount_list_id_discounts_get(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_dto_list_envelope import DiscountDtoListEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_discounts_get(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DiscountDtoListEnvelope**](DiscountDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_discounts_post**
> EmptyEnvelope api_v2_pricing_service_discount_lists_discount_list_id_discounts_post(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version, discount_create_dto=discount_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_create_dto import DiscountCreateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    discount_create_dto = openapi_client.DiscountCreateDto() # DiscountCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_discounts_post(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version, discount_create_dto=discount_create_dto)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_discounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **discount_create_dto** | [**DiscountCreateDto**](DiscountCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_get**
> DiscountListDtoEnvelope api_v2_pricing_service_discount_lists_discount_list_id_get(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_list_dto_envelope import DiscountListDtoEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_get(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DiscountListDtoEnvelope**](DiscountListDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_discount_list_id_put**
> EmptyEnvelope api_v2_pricing_service_discount_lists_discount_list_id_put(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version, discount_list_update_dto=discount_list_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_list_update_dto import DiscountListUpdateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    discount_list_update_dto = openapi_client.DiscountListUpdateDto() # DiscountListUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_discount_list_id_put(tenant_id, discount_list_id, api_version=api_version, x_api_version=x_api_version, discount_list_update_dto=discount_list_update_dto)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_discount_list_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **discount_list_update_dto** | [**DiscountListUpdateDto**](DiscountListUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_get**
> DiscountListDtoListEnvelope api_v2_pricing_service_discount_lists_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_list_dto_list_envelope import DiscountListDtoListEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DiscountListDtoListEnvelope**](DiscountListDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_pricing_service_discount_lists_post**
> EmptyEnvelope api_v2_pricing_service_discount_lists_post(tenant_id, api_version=api_version, x_api_version=x_api_version, discount_list_create_dto=discount_list_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_list_create_dto import DiscountListCreateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    discount_list_create_dto = openapi_client.DiscountListCreateDto() # DiscountListCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_pricing_service_discount_lists_post(tenant_id, api_version=api_version, x_api_version=x_api_version, discount_list_create_dto=discount_list_create_dto)
        print("The response of DiscountListsApi->api_v2_pricing_service_discount_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->api_v2_pricing_service_discount_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **discount_list_create_dto** | [**DiscountListCreateDto**](DiscountListCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_list_entry**
> DiscountDtoEnvelope get_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.discount_dto_envelope import DiscountDtoEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_list_entry_id = 'discount_list_entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.get_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DiscountListsApi->get_discount_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->get_discount_list_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_list_entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DiscountDtoEnvelope**](DiscountDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

