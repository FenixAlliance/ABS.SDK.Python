# openapi_client.SupportEntitlementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_support_service_support_entitlements_count_get**](SupportEntitlementsApi.md#api_v2_support_service_support_entitlements_count_get) | **GET** /api/v2/SupportService/SupportEntitlements/Count | 
[**api_v2_support_service_support_entitlements_get**](SupportEntitlementsApi.md#api_v2_support_service_support_entitlements_get) | **GET** /api/v2/SupportService/SupportEntitlements | 
[**api_v2_support_service_support_entitlements_post**](SupportEntitlementsApi.md#api_v2_support_service_support_entitlements_post) | **POST** /api/v2/SupportService/SupportEntitlements | 
[**api_v2_support_service_support_entitlements_support_entitlement_id_delete**](SupportEntitlementsApi.md#api_v2_support_service_support_entitlements_support_entitlement_id_delete) | **DELETE** /api/v2/SupportService/SupportEntitlements/{supportEntitlementId} | 
[**api_v2_support_service_support_entitlements_support_entitlement_id_get**](SupportEntitlementsApi.md#api_v2_support_service_support_entitlements_support_entitlement_id_get) | **GET** /api/v2/SupportService/SupportEntitlements/{supportEntitlementId} | 
[**api_v2_support_service_support_entitlements_support_entitlement_id_put**](SupportEntitlementsApi.md#api_v2_support_service_support_entitlements_support_entitlement_id_put) | **PUT** /api/v2/SupportService/SupportEntitlements/{supportEntitlementId} | 


# **api_v2_support_service_support_entitlements_count_get**
> Int32Envelope api_v2_support_service_support_entitlements_count_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_entitlements_count_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->api_v2_support_service_support_entitlements_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->api_v2_support_service_support_entitlements_count_get: %s\n" % e)
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

# **api_v2_support_service_support_entitlements_get**
> SupportEntitlementDtoListEnvelope api_v2_support_service_support_entitlements_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_entitlement_dto_list_envelope import SupportEntitlementDtoListEnvelope
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_entitlements_get(tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->api_v2_support_service_support_entitlements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->api_v2_support_service_support_entitlements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportEntitlementDtoListEnvelope**](SupportEntitlementDtoListEnvelope.md)

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

# **api_v2_support_service_support_entitlements_post**
> EmptyEnvelope api_v2_support_service_support_entitlements_post(support_entitlement_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_entitlement_create_dto import SupportEntitlementCreateDto
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    support_entitlement_create_dto = openapi_client.SupportEntitlementCreateDto() # SupportEntitlementCreateDto | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_entitlements_post(support_entitlement_create_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->api_v2_support_service_support_entitlements_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->api_v2_support_service_support_entitlements_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_entitlement_create_dto** | [**SupportEntitlementCreateDto**](SupportEntitlementCreateDto.md)|  | 
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

# **api_v2_support_service_support_entitlements_support_entitlement_id_delete**
> EmptyEnvelope api_v2_support_service_support_entitlements_support_entitlement_id_delete(support_entitlement_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    support_entitlement_id = 'support_entitlement_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_entitlements_support_entitlement_id_delete(support_entitlement_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->api_v2_support_service_support_entitlements_support_entitlement_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->api_v2_support_service_support_entitlements_support_entitlement_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_entitlement_id** | **str**|  | 
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

# **api_v2_support_service_support_entitlements_support_entitlement_id_get**
> SupportEntitlementDtoEnvelope api_v2_support_service_support_entitlements_support_entitlement_id_get(support_entitlement_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.support_entitlement_dto_envelope import SupportEntitlementDtoEnvelope
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    support_entitlement_id = 'support_entitlement_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_entitlements_support_entitlement_id_get(support_entitlement_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->api_v2_support_service_support_entitlements_support_entitlement_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->api_v2_support_service_support_entitlements_support_entitlement_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_entitlement_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportEntitlementDtoEnvelope**](SupportEntitlementDtoEnvelope.md)

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

# **api_v2_support_service_support_entitlements_support_entitlement_id_put**
> EmptyEnvelope api_v2_support_service_support_entitlements_support_entitlement_id_put(support_entitlement_id, support_entitlement_update_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_entitlement_update_dto import SupportEntitlementUpdateDto
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    support_entitlement_id = 'support_entitlement_id_example' # str | 
    support_entitlement_update_dto = openapi_client.SupportEntitlementUpdateDto() # SupportEntitlementUpdateDto | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_support_service_support_entitlements_support_entitlement_id_put(support_entitlement_id, support_entitlement_update_dto, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->api_v2_support_service_support_entitlements_support_entitlement_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->api_v2_support_service_support_entitlements_support_entitlement_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_entitlement_id** | **str**|  | 
 **support_entitlement_update_dto** | [**SupportEntitlementUpdateDto**](SupportEntitlementUpdateDto.md)|  | 
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

