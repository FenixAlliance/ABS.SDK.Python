# openapi_client.DealUnitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_deals_service_deal_units_count_get**](DealUnitsApi.md#api_v2_deals_service_deal_units_count_get) | **GET** /api/v2/DealsService/DealUnits/Count | 
[**api_v2_deals_service_deal_units_deal_unit_id_calculate_put**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_calculate_put) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId}/Calculate | 
[**api_v2_deals_service_deal_units_deal_unit_id_delete**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_delete) | **DELETE** /api/v2/DealsService/DealUnits/{dealUnitId} | 
[**api_v2_deals_service_deal_units_deal_unit_id_extended_get**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_extended_get) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Extended | 
[**api_v2_deals_service_deal_units_deal_unit_id_lines_count_get**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_lines_count_get) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/Count | 
[**api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_calculate_put**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_calculate_put) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId}/Calculate | 
[**api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_delete**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_delete) | **DELETE** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId} | 
[**api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_get**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_get) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId} | 
[**api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_put**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_put) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId} | 
[**api_v2_deals_service_deal_units_deal_unit_id_lines_get**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_lines_get) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines | 
[**api_v2_deals_service_deal_units_deal_unit_id_lines_post**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_lines_post) | **POST** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines | 
[**api_v2_deals_service_deal_units_deal_unit_id_put**](DealUnitsApi.md#api_v2_deals_service_deal_units_deal_unit_id_put) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId} | 
[**api_v2_deals_service_deal_units_extended_get**](DealUnitsApi.md#api_v2_deals_service_deal_units_extended_get) | **GET** /api/v2/DealsService/DealUnits/Extended | 
[**api_v2_deals_service_deal_units_get**](DealUnitsApi.md#api_v2_deals_service_deal_units_get) | **GET** /api/v2/DealsService/DealUnits | 
[**api_v2_deals_service_deal_units_post**](DealUnitsApi.md#api_v2_deals_service_deal_units_post) | **POST** /api/v2/DealsService/DealUnits | 
[**get_deal_unit_async**](DealUnitsApi.md#get_deal_unit_async) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId} | 


# **api_v2_deals_service_deal_units_count_get**
> Int32Envelope api_v2_deals_service_deal_units_count_get(tenant_id)



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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_count_get(tenant_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_count_get: %s\n" % e)
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

# **api_v2_deals_service_deal_units_deal_unit_id_calculate_put**
> EmptyEnvelope api_v2_deals_service_deal_units_deal_unit_id_calculate_put(tenant_id, deal_unit_id)



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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_calculate_put(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

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

# **api_v2_deals_service_deal_units_deal_unit_id_delete**
> EmptyEnvelope api_v2_deals_service_deal_units_deal_unit_id_delete(tenant_id, deal_unit_id)



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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_delete(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

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

# **api_v2_deals_service_deal_units_deal_unit_id_extended_get**
> ExtendedDealUnitDtoEnvelope api_v2_deals_service_deal_units_deal_unit_id_extended_get(tenant_id, deal_unit_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_deal_unit_dto_envelope import ExtendedDealUnitDtoEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_extended_get(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_extended_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_extended_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

### Return type

[**ExtendedDealUnitDtoEnvelope**](ExtendedDealUnitDtoEnvelope.md)

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

# **api_v2_deals_service_deal_units_deal_unit_id_lines_count_get**
> Int32Envelope api_v2_deals_service_deal_units_deal_unit_id_lines_count_get(tenant_id, deal_unit_id)



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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_lines_count_get(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

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

# **api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_calculate_put**
> EmptyEnvelope api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_calculate_put(tenant_id, deal_unit_id, deal_unit_line_id)



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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_calculate_put(tenant_id, deal_unit_id, deal_unit_line_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 

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

# **api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_delete**
> EmptyEnvelope api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_delete(tenant_id, deal_unit_id, deal_unit_line_id)



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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_delete(tenant_id, deal_unit_id, deal_unit_line_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 

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

# **api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_get**
> DealUnitLineDtoEnvelope api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_get(tenant_id, deal_unit_id, deal_unit_line_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_line_dto_envelope import DealUnitLineDtoEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_get(tenant_id, deal_unit_id, deal_unit_line_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 

### Return type

[**DealUnitLineDtoEnvelope**](DealUnitLineDtoEnvelope.md)

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

# **api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_put**
> EmptyEnvelope api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_put(tenant_id, deal_unit_id, deal_unit_line_id, deal_unit_line_update_dto=deal_unit_line_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_line_update_dto import DealUnitLineUpdateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 
    deal_unit_line_update_dto = openapi_client.DealUnitLineUpdateDto() # DealUnitLineUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_put(tenant_id, deal_unit_id, deal_unit_line_id, deal_unit_line_update_dto=deal_unit_line_update_dto)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_deal_unit_line_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 
 **deal_unit_line_update_dto** | [**DealUnitLineUpdateDto**](DealUnitLineUpdateDto.md)|  | [optional] 

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

# **api_v2_deals_service_deal_units_deal_unit_id_lines_get**
> DealUnitLineDtoListEnvelope api_v2_deals_service_deal_units_deal_unit_id_lines_get(tenant_id, deal_unit_id, item_id=item_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_line_dto_list_envelope import DealUnitLineDtoListEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_lines_get(tenant_id, deal_unit_id, item_id=item_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 

### Return type

[**DealUnitLineDtoListEnvelope**](DealUnitLineDtoListEnvelope.md)

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

# **api_v2_deals_service_deal_units_deal_unit_id_lines_post**
> EmptyEnvelope api_v2_deals_service_deal_units_deal_unit_id_lines_post(tenant_id, deal_unit_id, deal_unit_line_create_dto=deal_unit_line_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_line_create_dto import DealUnitLineCreateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_create_dto = openapi_client.DealUnitLineCreateDto() # DealUnitLineCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_lines_post(tenant_id, deal_unit_id, deal_unit_line_create_dto=deal_unit_line_create_dto)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_lines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_create_dto** | [**DealUnitLineCreateDto**](DealUnitLineCreateDto.md)|  | [optional] 

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

# **api_v2_deals_service_deal_units_deal_unit_id_put**
> EmptyEnvelope api_v2_deals_service_deal_units_deal_unit_id_put(tenant_id, deal_unit_id, deal_unit_update_dto=deal_unit_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_update_dto import DealUnitUpdateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_update_dto = openapi_client.DealUnitUpdateDto() # DealUnitUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_deal_unit_id_put(tenant_id, deal_unit_id, deal_unit_update_dto=deal_unit_update_dto)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_deal_unit_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_update_dto** | [**DealUnitUpdateDto**](DealUnitUpdateDto.md)|  | [optional] 

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

# **api_v2_deals_service_deal_units_extended_get**
> ExtendedDealUnitDtoListEnvelope api_v2_deals_service_deal_units_extended_get(tenant_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_deal_unit_dto_list_envelope import ExtendedDealUnitDtoListEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_extended_get(tenant_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_extended_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_extended_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedDealUnitDtoListEnvelope**](ExtendedDealUnitDtoListEnvelope.md)

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

# **api_v2_deals_service_deal_units_get**
> DealUnitDtoListEnvelope api_v2_deals_service_deal_units_get(tenant_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_dto_list_envelope import DealUnitDtoListEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_get(tenant_id)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**DealUnitDtoListEnvelope**](DealUnitDtoListEnvelope.md)

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

# **api_v2_deals_service_deal_units_post**
> EmptyEnvelope api_v2_deals_service_deal_units_post(tenant_id, deal_unit_create_dto=deal_unit_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_create_dto import DealUnitCreateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_create_dto = openapi_client.DealUnitCreateDto() # DealUnitCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_units_post(tenant_id, deal_unit_create_dto=deal_unit_create_dto)
        print("The response of DealUnitsApi->api_v2_deals_service_deal_units_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->api_v2_deals_service_deal_units_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_create_dto** | [**DealUnitCreateDto**](DealUnitCreateDto.md)|  | [optional] 

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

# **get_deal_unit_async**
> DealUnitDtoEnvelope get_deal_unit_async(tenant_id, deal_unit_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_dto_envelope import DealUnitDtoEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        api_response = api_instance.get_deal_unit_async(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->get_deal_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_deal_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

### Return type

[**DealUnitDtoEnvelope**](DealUnitDtoEnvelope.md)

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

