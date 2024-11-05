# openapi_client.SalesLiteraturesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_deals_service_sales_literatures_extended_get**](SalesLiteraturesApi.md#api_v2_deals_service_sales_literatures_extended_get) | **GET** /api/v2/DealsService/SalesLiteratures/Extended | 
[**api_v2_deals_service_sales_literatures_get**](SalesLiteraturesApi.md#api_v2_deals_service_sales_literatures_get) | **GET** /api/v2/DealsService/SalesLiteratures | 
[**api_v2_deals_service_sales_literatures_post**](SalesLiteraturesApi.md#api_v2_deals_service_sales_literatures_post) | **POST** /api/v2/DealsService/SalesLiteratures | 
[**api_v2_deals_service_sales_literatures_sales_literature_id_delete**](SalesLiteraturesApi.md#api_v2_deals_service_sales_literatures_sales_literature_id_delete) | **DELETE** /api/v2/DealsService/SalesLiteratures/{salesLiteratureId} | 
[**api_v2_deals_service_sales_literatures_sales_literature_id_get**](SalesLiteraturesApi.md#api_v2_deals_service_sales_literatures_sales_literature_id_get) | **GET** /api/v2/DealsService/SalesLiteratures/{salesLiteratureId} | 
[**api_v2_deals_service_sales_literatures_sales_literature_id_put**](SalesLiteraturesApi.md#api_v2_deals_service_sales_literatures_sales_literature_id_put) | **PUT** /api/v2/DealsService/SalesLiteratures/{salesLiteratureId} | 


# **api_v2_deals_service_sales_literatures_extended_get**
> ExtendedSalesLiteratureDtoListEnvelope api_v2_deals_service_sales_literatures_extended_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_sales_literature_dto_list_envelope import ExtendedSalesLiteratureDtoListEnvelope
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_sales_literatures_extended_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalesLiteraturesApi->api_v2_deals_service_sales_literatures_extended_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->api_v2_deals_service_sales_literatures_extended_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedSalesLiteratureDtoListEnvelope**](ExtendedSalesLiteratureDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_deals_service_sales_literatures_get**
> SalesLiteratureDtoListEnvelope api_v2_deals_service_sales_literatures_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.sales_literature_dto_list_envelope import SalesLiteratureDtoListEnvelope
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_sales_literatures_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalesLiteraturesApi->api_v2_deals_service_sales_literatures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->api_v2_deals_service_sales_literatures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SalesLiteratureDtoListEnvelope**](SalesLiteratureDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_deals_service_sales_literatures_post**
> EmptyEnvelope api_v2_deals_service_sales_literatures_post(tenant_id, api_version=api_version, x_api_version=x_api_version, sales_literature_create_dto=sales_literature_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.sales_literature_create_dto import SalesLiteratureCreateDto
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    sales_literature_create_dto = openapi_client.SalesLiteratureCreateDto() # SalesLiteratureCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_sales_literatures_post(tenant_id, api_version=api_version, x_api_version=x_api_version, sales_literature_create_dto=sales_literature_create_dto)
        print("The response of SalesLiteraturesApi->api_v2_deals_service_sales_literatures_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->api_v2_deals_service_sales_literatures_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **sales_literature_create_dto** | [**SalesLiteratureCreateDto**](SalesLiteratureCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_deals_service_sales_literatures_sales_literature_id_delete**
> EmptyEnvelope api_v2_deals_service_sales_literatures_sales_literature_id_delete(tenant_id, sales_literature_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sales_literature_id = 'sales_literature_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_sales_literatures_sales_literature_id_delete(tenant_id, sales_literature_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalesLiteraturesApi->api_v2_deals_service_sales_literatures_sales_literature_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->api_v2_deals_service_sales_literatures_sales_literature_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sales_literature_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_deals_service_sales_literatures_sales_literature_id_get**
> SalesLiteratureDtoEnvelope api_v2_deals_service_sales_literatures_sales_literature_id_get(sales_literature_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.sales_literature_dto_envelope import SalesLiteratureDtoEnvelope
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    sales_literature_id = 'sales_literature_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_sales_literatures_sales_literature_id_get(sales_literature_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalesLiteraturesApi->api_v2_deals_service_sales_literatures_sales_literature_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->api_v2_deals_service_sales_literatures_sales_literature_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_literature_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SalesLiteratureDtoEnvelope**](SalesLiteratureDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_deals_service_sales_literatures_sales_literature_id_put**
> EmptyEnvelope api_v2_deals_service_sales_literatures_sales_literature_id_put(tenant_id, sales_literature_id, api_version=api_version, x_api_version=x_api_version, sales_literature_update_dto=sales_literature_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.sales_literature_update_dto import SalesLiteratureUpdateDto
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sales_literature_id = 'sales_literature_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    sales_literature_update_dto = openapi_client.SalesLiteratureUpdateDto() # SalesLiteratureUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_sales_literatures_sales_literature_id_put(tenant_id, sales_literature_id, api_version=api_version, x_api_version=x_api_version, sales_literature_update_dto=sales_literature_update_dto)
        print("The response of SalesLiteraturesApi->api_v2_deals_service_sales_literatures_sales_literature_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->api_v2_deals_service_sales_literatures_sales_literature_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sales_literature_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **sales_literature_update_dto** | [**SalesLiteratureUpdateDto**](SalesLiteratureUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

