# openapi_client.QuotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_quotes_service_quotes_count_get**](QuotesApi.md#api_v2_quotes_service_quotes_count_get) | **GET** /api/v2/QuotesService/Quotes/Count | 
[**api_v2_quotes_service_quotes_extended_get**](QuotesApi.md#api_v2_quotes_service_quotes_extended_get) | **GET** /api/v2/QuotesService/Quotes/Extended | 
[**api_v2_quotes_service_quotes_get**](QuotesApi.md#api_v2_quotes_service_quotes_get) | **GET** /api/v2/QuotesService/Quotes | 
[**api_v2_quotes_service_quotes_post**](QuotesApi.md#api_v2_quotes_service_quotes_post) | **POST** /api/v2/QuotesService/Quotes | 
[**api_v2_quotes_service_quotes_quote_id_calculate_put**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_calculate_put) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Calculate | 
[**api_v2_quotes_service_quotes_quote_id_delete**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_delete) | **DELETE** /api/v2/QuotesService/Quotes/{quoteId} | 
[**api_v2_quotes_service_quotes_quote_id_lines_count_get**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_lines_count_get) | **GET** /api/v2/QuotesService/Quotes/{quoteId}/Lines/Count | 
[**api_v2_quotes_service_quotes_quote_id_lines_get**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_lines_get) | **GET** /api/v2/QuotesService/Quotes/{quoteId}/Lines | 
[**api_v2_quotes_service_quotes_quote_id_lines_post**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_lines_post) | **POST** /api/v2/QuotesService/Quotes/{quoteId}/Lines | 
[**api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_calculate_put**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_calculate_put) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId}/Calculate | 
[**api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_delete**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_delete) | **DELETE** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId} | 
[**api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_get**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_get) | **GET** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId} | 
[**api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_put**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_put) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId} | 
[**api_v2_quotes_service_quotes_quote_id_put**](QuotesApi.md#api_v2_quotes_service_quotes_quote_id_put) | **PUT** /api/v2/QuotesService/Quotes/{quoteId} | 
[**get_quote_async**](QuotesApi.md#get_quote_async) | **GET** /api/v2/QuotesService/Quotes/{quoteId} | 


# **api_v2_quotes_service_quotes_count_get**
> Int32Envelope api_v2_quotes_service_quotes_count_get(tenant_id)



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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_count_get(tenant_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_quotes_service_quotes_extended_get**
> ExtendedQuoteDtoListEnvelope api_v2_quotes_service_quotes_extended_get(tenant_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_quote_dto_list_envelope import ExtendedQuoteDtoListEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_extended_get(tenant_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_extended_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_extended_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedQuoteDtoListEnvelope**](ExtendedQuoteDtoListEnvelope.md)

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

# **api_v2_quotes_service_quotes_get**
> QuoteDtoListEnvelope api_v2_quotes_service_quotes_get(tenant_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.quote_dto_list_envelope import QuoteDtoListEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_get(tenant_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**QuoteDtoListEnvelope**](QuoteDtoListEnvelope.md)

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

# **api_v2_quotes_service_quotes_post**
> EmptyEnvelope api_v2_quotes_service_quotes_post(tenant_id, quote_create_dto=quote_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_create_dto import QuoteCreateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_create_dto = openapi_client.QuoteCreateDto() # QuoteCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_post(tenant_id, quote_create_dto=quote_create_dto)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_create_dto** | [**QuoteCreateDto**](QuoteCreateDto.md)|  | [optional] 

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

# **api_v2_quotes_service_quotes_quote_id_calculate_put**
> EmptyEnvelope api_v2_quotes_service_quotes_quote_id_calculate_put(tenant_id, quote_id)



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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_calculate_put(tenant_id, quote_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

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

# **api_v2_quotes_service_quotes_quote_id_delete**
> EmptyEnvelope api_v2_quotes_service_quotes_quote_id_delete(quote_id, tenant_id)



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
    api_instance = openapi_client.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_delete(quote_id, tenant_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **tenant_id** | **str**|  | 

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

# **api_v2_quotes_service_quotes_quote_id_lines_count_get**
> Int32Envelope api_v2_quotes_service_quotes_quote_id_lines_count_get(tenant_id, quote_id)



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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_lines_count_get(tenant_id, quote_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_quotes_service_quotes_quote_id_lines_get**
> QuoteLineDtoListEnvelope api_v2_quotes_service_quotes_quote_id_lines_get(tenant_id, quote_id, item_id=item_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.quote_line_dto_list_envelope import QuoteLineDtoListEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_lines_get(tenant_id, quote_id, item_id=item_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 

### Return type

[**QuoteLineDtoListEnvelope**](QuoteLineDtoListEnvelope.md)

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

# **api_v2_quotes_service_quotes_quote_id_lines_post**
> EmptyEnvelope api_v2_quotes_service_quotes_quote_id_lines_post(tenant_id, quote_id, quote_line_create_dto=quote_line_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_line_create_dto import QuoteLineCreateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_create_dto = openapi_client.QuoteLineCreateDto() # QuoteLineCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_lines_post(tenant_id, quote_id, quote_line_create_dto=quote_line_create_dto)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_create_dto** | [**QuoteLineCreateDto**](QuoteLineCreateDto.md)|  | [optional] 

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

# **api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_calculate_put**
> EmptyEnvelope api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_calculate_put(tenant_id, quote_id, quote_line_id)



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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_calculate_put(tenant_id, quote_id, quote_line_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 

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

# **api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_delete**
> EmptyEnvelope api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_delete(tenant_id, quote_id, quote_line_id)



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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_delete(tenant_id, quote_id, quote_line_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 

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

# **api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_get**
> QuoteLineDtoEnvelope api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_get(tenant_id, quote_id, quote_line_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.quote_line_dto_envelope import QuoteLineDtoEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_get(tenant_id, quote_id, quote_line_id)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 

### Return type

[**QuoteLineDtoEnvelope**](QuoteLineDtoEnvelope.md)

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

# **api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_put**
> EmptyEnvelope api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_put(tenant_id, quote_id, quote_line_id, quote_line_update_dto=quote_line_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_line_update_dto import QuoteLineUpdateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 
    quote_line_update_dto = openapi_client.QuoteLineUpdateDto() # QuoteLineUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_put(tenant_id, quote_id, quote_line_id, quote_line_update_dto=quote_line_update_dto)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_lines_quote_line_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 
 **quote_line_update_dto** | [**QuoteLineUpdateDto**](QuoteLineUpdateDto.md)|  | [optional] 

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

# **api_v2_quotes_service_quotes_quote_id_put**
> EmptyEnvelope api_v2_quotes_service_quotes_quote_id_put(tenant_id, quote_id, quote_update_dto=quote_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_update_dto import QuoteUpdateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_update_dto = openapi_client.QuoteUpdateDto() # QuoteUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_quotes_service_quotes_quote_id_put(tenant_id, quote_id, quote_update_dto=quote_update_dto)
        print("The response of QuotesApi->api_v2_quotes_service_quotes_quote_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->api_v2_quotes_service_quotes_quote_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_update_dto** | [**QuoteUpdateDto**](QuoteUpdateDto.md)|  | [optional] 

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

# **get_quote_async**
> QuoteDtoEnvelope get_quote_async(tenant_id, quote_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.quote_dto_envelope import QuoteDtoEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        api_response = api_instance.get_quote_async(tenant_id, quote_id)
        print("The response of QuotesApi->get_quote_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

### Return type

[**QuoteDtoEnvelope**](QuoteDtoEnvelope.md)

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

