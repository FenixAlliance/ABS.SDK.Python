# openapi_client.DealUnitFlowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_deals_service_deal_unit_flows_count_get**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_count_get) | **GET** /api/v2/DealsService/DealUnitFlows/Count | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_delete**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_delete) | **DELETE** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId} | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_get**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_get) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId} | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_put**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_put) | **PUT** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId} | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_count_get**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_count_get) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/Count | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_delete**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_delete) | **DELETE** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/{dealUnitFlowStageId} | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_get**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_get) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/{dealUnitFlowStageId} | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_put**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_put) | **PUT** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/{dealUnitFlowStageId} | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_get**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_get) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages | 
[**api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_post**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_post) | **POST** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages | 
[**api_v2_deals_service_deal_unit_flows_get**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_get) | **GET** /api/v2/DealsService/DealUnitFlows | 
[**api_v2_deals_service_deal_unit_flows_post**](DealUnitFlowsApi.md#api_v2_deals_service_deal_unit_flows_post) | **POST** /api/v2/DealsService/DealUnitFlows | 


# **api_v2_deals_service_deal_unit_flows_count_get**
> Int32Envelope api_v2_deals_service_deal_unit_flows_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_count_get: %s\n" % e)
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_delete**
> EmptyEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_delete(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_delete(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
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

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_get**
> DealUnitFlowDtoEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_get(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_dto_envelope import DealUnitFlowDtoEnvelope
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_get(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DealUnitFlowDtoEnvelope**](DealUnitFlowDtoEnvelope.md)

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

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_put**
> EmptyEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_put(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_update_dto=deal_unit_flow_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_update_dto import DealUnitFlowUpdateDto
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    deal_unit_flow_update_dto = openapi_client.DealUnitFlowUpdateDto() # DealUnitFlowUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_put(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_update_dto=deal_unit_flow_update_dto)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **deal_unit_flow_update_dto** | [**DealUnitFlowUpdateDto**](DealUnitFlowUpdateDto.md)|  | [optional] 

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

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_count_get**
> Int32Envelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_count_get(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_count_get(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_delete**
> EmptyEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_delete(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_stage_id = 'deal_unit_flow_stage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_delete(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_stage_id** | **str**|  | 
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

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_get**
> DealUnitFlowStageDtoEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_get(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_stage_dto_envelope import DealUnitFlowStageDtoEnvelope
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_stage_id = 'deal_unit_flow_stage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_get(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_stage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DealUnitFlowStageDtoEnvelope**](DealUnitFlowStageDtoEnvelope.md)

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

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_put**
> EmptyEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_put(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_stage_update_dto=deal_unit_flow_stage_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_stage_update_dto import DealUnitFlowStageUpdateDto
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_stage_id = 'deal_unit_flow_stage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    deal_unit_flow_stage_update_dto = openapi_client.DealUnitFlowStageUpdateDto() # DealUnitFlowStageUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_put(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_stage_update_dto=deal_unit_flow_stage_update_dto)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_deal_unit_flow_stage_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_stage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **deal_unit_flow_stage_update_dto** | [**DealUnitFlowStageUpdateDto**](DealUnitFlowStageUpdateDto.md)|  | [optional] 

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

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_get**
> DealUnitFlowStageDtoListEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_get(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_stage_dto_list_envelope import DealUnitFlowStageDtoListEnvelope
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_get(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DealUnitFlowStageDtoListEnvelope**](DealUnitFlowStageDtoListEnvelope.md)

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

# **api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_post**
> EmptyEnvelope api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_post(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_stage_create_dto=deal_unit_flow_stage_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_stage_create_dto import DealUnitFlowStageCreateDto
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    deal_unit_flow_stage_create_dto = openapi_client.DealUnitFlowStageCreateDto() # DealUnitFlowStageCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_post(tenant_id, deal_unit_flow_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_stage_create_dto=deal_unit_flow_stage_create_dto)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_deal_unit_flow_id_stages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **deal_unit_flow_stage_create_dto** | [**DealUnitFlowStageCreateDto**](DealUnitFlowStageCreateDto.md)|  | [optional] 

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

# **api_v2_deals_service_deal_unit_flows_get**
> DealUnitFlowDtoListEnvelope api_v2_deals_service_deal_unit_flows_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_dto_list_envelope import DealUnitFlowDtoListEnvelope
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DealUnitFlowDtoListEnvelope**](DealUnitFlowDtoListEnvelope.md)

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

# **api_v2_deals_service_deal_unit_flows_post**
> EmptyEnvelope api_v2_deals_service_deal_unit_flows_post(tenant_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_create_dto=deal_unit_flow_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deal_unit_flow_create_dto import DealUnitFlowCreateDto
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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    deal_unit_flow_create_dto = openapi_client.DealUnitFlowCreateDto() # DealUnitFlowCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_deals_service_deal_unit_flows_post(tenant_id, api_version=api_version, x_api_version=x_api_version, deal_unit_flow_create_dto=deal_unit_flow_create_dto)
        print("The response of DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->api_v2_deals_service_deal_unit_flows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **deal_unit_flow_create_dto** | [**DealUnitFlowCreateDto**](DealUnitFlowCreateDto.md)|  | [optional] 

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

