# openapi_client.DealUnitFlowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deal_unit_flow_async**](DealUnitFlowsApi.md#create_deal_unit_flow_async) | **POST** /api/v2/DealsService/DealUnitFlows | Create a deal unit flow
[**create_deal_unit_flow_stage_async**](DealUnitFlowsApi.md#create_deal_unit_flow_stage_async) | **POST** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages | Create a deal unit flow stage
[**delete_deal_unit_flow_async**](DealUnitFlowsApi.md#delete_deal_unit_flow_async) | **DELETE** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId} | Delete a deal unit flow
[**delete_deal_unit_flow_stage_async**](DealUnitFlowsApi.md#delete_deal_unit_flow_stage_async) | **DELETE** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/{dealUnitFlowStageId} | Delete a deal unit flow stage
[**get_deal_unit_flow_async**](DealUnitFlowsApi.md#get_deal_unit_flow_async) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId} | Get deal unit flow by ID
[**get_deal_unit_flow_stage_async**](DealUnitFlowsApi.md#get_deal_unit_flow_stage_async) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/{dealUnitFlowStageId} | Get a deal unit flow stage by ID
[**get_deal_unit_flow_stages_async**](DealUnitFlowsApi.md#get_deal_unit_flow_stages_async) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages | Get stages for a deal unit flow
[**get_deal_unit_flow_stages_count_async**](DealUnitFlowsApi.md#get_deal_unit_flow_stages_count_async) | **GET** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/Count | Get stages count for a deal unit flow
[**get_deal_unit_flows_async**](DealUnitFlowsApi.md#get_deal_unit_flows_async) | **GET** /api/v2/DealsService/DealUnitFlows | Get deal unit flows
[**get_deal_unit_flows_count_async**](DealUnitFlowsApi.md#get_deal_unit_flows_count_async) | **GET** /api/v2/DealsService/DealUnitFlows/Count | Get deal unit flows count
[**update_deal_unit_flow_async**](DealUnitFlowsApi.md#update_deal_unit_flow_async) | **PUT** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId} | Update a deal unit flow
[**update_deal_unit_flow_stage_async**](DealUnitFlowsApi.md#update_deal_unit_flow_stage_async) | **PUT** /api/v2/DealsService/DealUnitFlows/{dealUnitFlowId}/Stages/{dealUnitFlowStageId} | Update a deal unit flow stage


# **create_deal_unit_flow_async**
> EmptyEnvelope create_deal_unit_flow_async(tenant_id, deal_unit_flow_create_dto=deal_unit_flow_create_dto)

Create a deal unit flow

Creates a new deal unit flow for the specified tenant.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_create_dto = openapi_client.DealUnitFlowCreateDto() # DealUnitFlowCreateDto |  (optional)

    try:
        # Create a deal unit flow
        api_response = api_instance.create_deal_unit_flow_async(tenant_id, deal_unit_flow_create_dto=deal_unit_flow_create_dto)
        print("The response of DealUnitFlowsApi->create_deal_unit_flow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->create_deal_unit_flow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_create_dto** | [**DealUnitFlowCreateDto**](DealUnitFlowCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deal_unit_flow_stage_async**
> EmptyEnvelope create_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_create_dto=deal_unit_flow_stage_create_dto)

Create a deal unit flow stage

Creates a new stage within a specific deal unit flow.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_stage_create_dto = openapi_client.DealUnitFlowStageCreateDto() # DealUnitFlowStageCreateDto |  (optional)

    try:
        # Create a deal unit flow stage
        api_response = api_instance.create_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_create_dto=deal_unit_flow_stage_create_dto)
        print("The response of DealUnitFlowsApi->create_deal_unit_flow_stage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->create_deal_unit_flow_stage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_stage_create_dto** | [**DealUnitFlowStageCreateDto**](DealUnitFlowStageCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deal_unit_flow_async**
> EmptyEnvelope delete_deal_unit_flow_async(tenant_id, deal_unit_flow_id)

Delete a deal unit flow

Deletes an existing deal unit flow by its unique identifier.

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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 

    try:
        # Delete a deal unit flow
        api_response = api_instance.delete_deal_unit_flow_async(tenant_id, deal_unit_flow_id)
        print("The response of DealUnitFlowsApi->delete_deal_unit_flow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->delete_deal_unit_flow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deal_unit_flow_stage_async**
> EmptyEnvelope delete_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id)

Delete a deal unit flow stage

Deletes an existing stage from a specific deal unit flow.

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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_stage_id = 'deal_unit_flow_stage_id_example' # str | 

    try:
        # Delete a deal unit flow stage
        api_response = api_instance.delete_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id)
        print("The response of DealUnitFlowsApi->delete_deal_unit_flow_stage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->delete_deal_unit_flow_stage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_stage_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_unit_flow_async**
> DealUnitFlowDtoEnvelope get_deal_unit_flow_async(tenant_id, deal_unit_flow_id)

Get deal unit flow by ID

Retrieves a single deal unit flow by its unique identifier.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 

    try:
        # Get deal unit flow by ID
        api_response = api_instance.get_deal_unit_flow_async(tenant_id, deal_unit_flow_id)
        print("The response of DealUnitFlowsApi->get_deal_unit_flow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->get_deal_unit_flow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 

### Return type

[**DealUnitFlowDtoEnvelope**](DealUnitFlowDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_unit_flow_stage_async**
> DealUnitFlowStageDtoEnvelope get_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id)

Get a deal unit flow stage by ID

Retrieves a single stage for a specific deal unit flow by its unique identifier.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_stage_id = 'deal_unit_flow_stage_id_example' # str | 

    try:
        # Get a deal unit flow stage by ID
        api_response = api_instance.get_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id)
        print("The response of DealUnitFlowsApi->get_deal_unit_flow_stage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->get_deal_unit_flow_stage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_stage_id** | **str**|  | 

### Return type

[**DealUnitFlowStageDtoEnvelope**](DealUnitFlowStageDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_unit_flow_stages_async**
> DealUnitFlowStageDtoListEnvelope get_deal_unit_flow_stages_async(tenant_id, deal_unit_flow_id)

Get stages for a deal unit flow

Retrieves a list of stages for a specific deal unit flow with OData query support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 

    try:
        # Get stages for a deal unit flow
        api_response = api_instance.get_deal_unit_flow_stages_async(tenant_id, deal_unit_flow_id)
        print("The response of DealUnitFlowsApi->get_deal_unit_flow_stages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->get_deal_unit_flow_stages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 

### Return type

[**DealUnitFlowStageDtoListEnvelope**](DealUnitFlowStageDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_unit_flow_stages_count_async**
> Int32Envelope get_deal_unit_flow_stages_count_async(tenant_id, deal_unit_flow_id)

Get stages count for a deal unit flow

Returns the total count of stages for a specific deal unit flow with OData filter support.

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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 

    try:
        # Get stages count for a deal unit flow
        api_response = api_instance.get_deal_unit_flow_stages_count_async(tenant_id, deal_unit_flow_id)
        print("The response of DealUnitFlowsApi->get_deal_unit_flow_stages_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->get_deal_unit_flow_stages_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_unit_flows_async**
> DealUnitFlowDtoListEnvelope get_deal_unit_flows_async(tenant_id)

Get deal unit flows

Retrieves a list of deal unit flows for the specified tenant with OData query support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get deal unit flows
        api_response = api_instance.get_deal_unit_flows_async(tenant_id)
        print("The response of DealUnitFlowsApi->get_deal_unit_flows_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->get_deal_unit_flows_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**DealUnitFlowDtoListEnvelope**](DealUnitFlowDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_unit_flows_count_async**
> Int32Envelope get_deal_unit_flows_count_async(tenant_id)

Get deal unit flows count

Returns the total count of deal unit flows for the specified tenant with OData filter support.

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
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get deal unit flows count
        api_response = api_instance.get_deal_unit_flows_count_async(tenant_id)
        print("The response of DealUnitFlowsApi->get_deal_unit_flows_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->get_deal_unit_flows_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deal_unit_flow_async**
> EmptyEnvelope update_deal_unit_flow_async(tenant_id, deal_unit_flow_id, deal_unit_flow_update_dto=deal_unit_flow_update_dto)

Update a deal unit flow

Updates an existing deal unit flow by its unique identifier.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_update_dto = openapi_client.DealUnitFlowUpdateDto() # DealUnitFlowUpdateDto |  (optional)

    try:
        # Update a deal unit flow
        api_response = api_instance.update_deal_unit_flow_async(tenant_id, deal_unit_flow_id, deal_unit_flow_update_dto=deal_unit_flow_update_dto)
        print("The response of DealUnitFlowsApi->update_deal_unit_flow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->update_deal_unit_flow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_update_dto** | [**DealUnitFlowUpdateDto**](DealUnitFlowUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deal_unit_flow_stage_async**
> EmptyEnvelope update_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, deal_unit_flow_stage_update_dto=deal_unit_flow_stage_update_dto)

Update a deal unit flow stage

Updates an existing stage within a specific deal unit flow.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealUnitFlowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_flow_id = 'deal_unit_flow_id_example' # str | 
    deal_unit_flow_stage_id = 'deal_unit_flow_stage_id_example' # str | 
    deal_unit_flow_stage_update_dto = openapi_client.DealUnitFlowStageUpdateDto() # DealUnitFlowStageUpdateDto |  (optional)

    try:
        # Update a deal unit flow stage
        api_response = api_instance.update_deal_unit_flow_stage_async(tenant_id, deal_unit_flow_id, deal_unit_flow_stage_id, deal_unit_flow_stage_update_dto=deal_unit_flow_stage_update_dto)
        print("The response of DealUnitFlowsApi->update_deal_unit_flow_stage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitFlowsApi->update_deal_unit_flow_stage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_flow_id** | **str**|  | 
 **deal_unit_flow_stage_id** | **str**|  | 
 **deal_unit_flow_stage_update_dto** | [**DealUnitFlowStageUpdateDto**](DealUnitFlowStageUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

