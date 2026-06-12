# openapi_client.MarketingLeadsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_marketing_lead_async**](MarketingLeadsApi.md#create_marketing_lead_async) | **POST** /api/v2/MarketingService/MarketingLeads | Create a marketing lead
[**delete_marketing_lead_async**](MarketingLeadsApi.md#delete_marketing_lead_async) | **DELETE** /api/v2/MarketingService/MarketingLeads/{marketingLeadId} | Delete a marketing lead
[**get_marketing_lead_details_async**](MarketingLeadsApi.md#get_marketing_lead_details_async) | **GET** /api/v2/MarketingService/MarketingLeads/{marketingLeadId} | Get marketing lead by ID
[**get_marketing_leads_count_async**](MarketingLeadsApi.md#get_marketing_leads_count_async) | **GET** /api/v2/MarketingService/MarketingLeads/Count | Get marketing leads count
[**get_marketing_leads_o_data_async**](MarketingLeadsApi.md#get_marketing_leads_o_data_async) | **GET** /api/v2/MarketingService/MarketingLeads | Get marketing leads
[**patch_marketing_lead_async**](MarketingLeadsApi.md#patch_marketing_lead_async) | **PATCH** /api/v2/MarketingService/MarketingLeads/{marketingLeadId} | Patch a marketing lead
[**update_marketing_lead_async**](MarketingLeadsApi.md#update_marketing_lead_async) | **PUT** /api/v2/MarketingService/MarketingLeads/{marketingLeadId} | Update a marketing lead


# **create_marketing_lead_async**
> EmptyEnvelope create_marketing_lead_async(tenant_id, marketing_lead_create_dto, api_version=api_version, x_api_version=x_api_version)

Create a marketing lead

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_lead_create_dto import MarketingLeadCreateDto
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
    api_instance = openapi_client.MarketingLeadsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_lead_create_dto = openapi_client.MarketingLeadCreateDto() # MarketingLeadCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create a marketing lead
        api_response = api_instance.create_marketing_lead_async(tenant_id, marketing_lead_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingLeadsApi->create_marketing_lead_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingLeadsApi->create_marketing_lead_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_lead_create_dto** | [**MarketingLeadCreateDto**](MarketingLeadCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

# **delete_marketing_lead_async**
> EmptyEnvelope delete_marketing_lead_async(tenant_id, marketing_lead_id, api_version=api_version, x_api_version=x_api_version)

Delete a marketing lead

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
    api_instance = openapi_client.MarketingLeadsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_lead_id = 'marketing_lead_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a marketing lead
        api_response = api_instance.delete_marketing_lead_async(tenant_id, marketing_lead_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingLeadsApi->delete_marketing_lead_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingLeadsApi->delete_marketing_lead_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_lead_id** | **str**|  | 
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

# **get_marketing_lead_details_async**
> MarketingLeadDtoEnvelope get_marketing_lead_details_async(tenant_id, marketing_lead_id, api_version=api_version, x_api_version=x_api_version)

Get marketing lead by ID

### Example


```python
import openapi_client
from openapi_client.models.marketing_lead_dto_envelope import MarketingLeadDtoEnvelope
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
    api_instance = openapi_client.MarketingLeadsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_lead_id = 'marketing_lead_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing lead by ID
        api_response = api_instance.get_marketing_lead_details_async(tenant_id, marketing_lead_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingLeadsApi->get_marketing_lead_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingLeadsApi->get_marketing_lead_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_lead_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingLeadDtoEnvelope**](MarketingLeadDtoEnvelope.md)

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

# **get_marketing_leads_count_async**
> Int32Envelope get_marketing_leads_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get marketing leads count

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
    api_instance = openapi_client.MarketingLeadsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing leads count
        api_response = api_instance.get_marketing_leads_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingLeadsApi->get_marketing_leads_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingLeadsApi->get_marketing_leads_count_async: %s\n" % e)
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

# **get_marketing_leads_o_data_async**
> MarketingLeadDtoListEnvelope get_marketing_leads_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get marketing leads

Retrieves a collection of marketing leads for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.marketing_lead_dto_list_envelope import MarketingLeadDtoListEnvelope
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
    api_instance = openapi_client.MarketingLeadsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get marketing leads
        api_response = api_instance.get_marketing_leads_o_data_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingLeadsApi->get_marketing_leads_o_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingLeadsApi->get_marketing_leads_o_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**MarketingLeadDtoListEnvelope**](MarketingLeadDtoListEnvelope.md)

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

# **patch_marketing_lead_async**
> EmptyEnvelope patch_marketing_lead_async(tenant_id, marketing_lead_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a marketing lead

Partially updates a marketing lead by its ID using JSON Patch.

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
    api_instance = openapi_client.MarketingLeadsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_lead_id = 'marketing_lead_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a marketing lead
        api_response = api_instance.patch_marketing_lead_async(tenant_id, marketing_lead_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of MarketingLeadsApi->patch_marketing_lead_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingLeadsApi->patch_marketing_lead_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_lead_id** | **str**|  | 
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

# **update_marketing_lead_async**
> EmptyEnvelope update_marketing_lead_async(tenant_id, marketing_lead_id, marketing_lead_update_dto, api_version=api_version, x_api_version=x_api_version)

Update a marketing lead

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.marketing_lead_update_dto import MarketingLeadUpdateDto
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
    api_instance = openapi_client.MarketingLeadsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    marketing_lead_id = 'marketing_lead_id_example' # str | 
    marketing_lead_update_dto = openapi_client.MarketingLeadUpdateDto() # MarketingLeadUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update a marketing lead
        api_response = api_instance.update_marketing_lead_async(tenant_id, marketing_lead_id, marketing_lead_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of MarketingLeadsApi->update_marketing_lead_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingLeadsApi->update_marketing_lead_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **marketing_lead_id** | **str**|  | 
 **marketing_lead_update_dto** | [**MarketingLeadUpdateDto**](MarketingLeadUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

