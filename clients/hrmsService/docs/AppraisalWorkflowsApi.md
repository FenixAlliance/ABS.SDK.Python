# openapi_client.AppraisalWorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appraisal_workflow_async**](AppraisalWorkflowsApi.md#create_appraisal_workflow_async) | **POST** /api/v2/HrmsService/AppraisalWorkflows | Create an appraisal workflow
[**delete_appraisal_workflow_async**](AppraisalWorkflowsApi.md#delete_appraisal_workflow_async) | **DELETE** /api/v2/HrmsService/AppraisalWorkflows/{workflowId} | Delete an appraisal workflow
[**get_appraisal_workflow_by_id_async**](AppraisalWorkflowsApi.md#get_appraisal_workflow_by_id_async) | **GET** /api/v2/HrmsService/AppraisalWorkflows/{workflowId} | Get appraisal workflow by ID
[**get_appraisal_workflows_async**](AppraisalWorkflowsApi.md#get_appraisal_workflows_async) | **GET** /api/v2/HrmsService/AppraisalWorkflows | Get appraisal workflows
[**get_appraisal_workflows_count_async**](AppraisalWorkflowsApi.md#get_appraisal_workflows_count_async) | **GET** /api/v2/HrmsService/AppraisalWorkflows/Count | Count appraisal workflows
[**update_appraisal_workflow_async**](AppraisalWorkflowsApi.md#update_appraisal_workflow_async) | **PUT** /api/v2/HrmsService/AppraisalWorkflows/{workflowId} | Update an appraisal workflow


# **create_appraisal_workflow_async**
> EmptyEnvelope create_appraisal_workflow_async(tenant_id, api_version=api_version, x_api_version=x_api_version, appraisal_workflow_create_dto=appraisal_workflow_create_dto)

Create an appraisal workflow

Creates a new appraisal workflow for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_workflow_create_dto import AppraisalWorkflowCreateDto
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
    api_instance = openapi_client.AppraisalWorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    appraisal_workflow_create_dto = openapi_client.AppraisalWorkflowCreateDto() # AppraisalWorkflowCreateDto |  (optional)

    try:
        # Create an appraisal workflow
        api_response = api_instance.create_appraisal_workflow_async(tenant_id, api_version=api_version, x_api_version=x_api_version, appraisal_workflow_create_dto=appraisal_workflow_create_dto)
        print("The response of AppraisalWorkflowsApi->create_appraisal_workflow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalWorkflowsApi->create_appraisal_workflow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **appraisal_workflow_create_dto** | [**AppraisalWorkflowCreateDto**](AppraisalWorkflowCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appraisal_workflow_async**
> EmptyEnvelope delete_appraisal_workflow_async(tenant_id, workflow_id, api_version=api_version, x_api_version=x_api_version)

Delete an appraisal workflow

Deletes an appraisal workflow for the specified tenant.

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
    api_instance = openapi_client.AppraisalWorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an appraisal workflow
        api_response = api_instance.delete_appraisal_workflow_async(tenant_id, workflow_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalWorkflowsApi->delete_appraisal_workflow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalWorkflowsApi->delete_appraisal_workflow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **workflow_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appraisal_workflow_by_id_async**
> AppraisalWorkflowDtoEnvelope get_appraisal_workflow_by_id_async(tenant_id, workflow_id, api_version=api_version, x_api_version=x_api_version)

Get appraisal workflow by ID

Retrieves a specific appraisal workflow by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_workflow_dto_envelope import AppraisalWorkflowDtoEnvelope
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
    api_instance = openapi_client.AppraisalWorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get appraisal workflow by ID
        api_response = api_instance.get_appraisal_workflow_by_id_async(tenant_id, workflow_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalWorkflowsApi->get_appraisal_workflow_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalWorkflowsApi->get_appraisal_workflow_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **workflow_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AppraisalWorkflowDtoEnvelope**](AppraisalWorkflowDtoEnvelope.md)

### Authorization

No authorization required

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

# **get_appraisal_workflows_async**
> AppraisalWorkflowDtoListEnvelope get_appraisal_workflows_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get appraisal workflows

Retrieves appraisal workflows for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_workflow_dto_list_envelope import AppraisalWorkflowDtoListEnvelope
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
    api_instance = openapi_client.AppraisalWorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get appraisal workflows
        api_response = api_instance.get_appraisal_workflows_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalWorkflowsApi->get_appraisal_workflows_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalWorkflowsApi->get_appraisal_workflows_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AppraisalWorkflowDtoListEnvelope**](AppraisalWorkflowDtoListEnvelope.md)

### Authorization

No authorization required

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

# **get_appraisal_workflows_count_async**
> Int32Envelope get_appraisal_workflows_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count appraisal workflows

Counts appraisal workflows for the specified tenant.

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
    api_instance = openapi_client.AppraisalWorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count appraisal workflows
        api_response = api_instance.get_appraisal_workflows_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalWorkflowsApi->get_appraisal_workflows_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalWorkflowsApi->get_appraisal_workflows_count_async: %s\n" % e)
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appraisal_workflow_async**
> EmptyEnvelope update_appraisal_workflow_async(tenant_id, workflow_id, api_version=api_version, x_api_version=x_api_version, appraisal_workflow_update_dto=appraisal_workflow_update_dto)

Update an appraisal workflow

Updates an existing appraisal workflow for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_workflow_update_dto import AppraisalWorkflowUpdateDto
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
    api_instance = openapi_client.AppraisalWorkflowsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    appraisal_workflow_update_dto = openapi_client.AppraisalWorkflowUpdateDto() # AppraisalWorkflowUpdateDto |  (optional)

    try:
        # Update an appraisal workflow
        api_response = api_instance.update_appraisal_workflow_async(tenant_id, workflow_id, api_version=api_version, x_api_version=x_api_version, appraisal_workflow_update_dto=appraisal_workflow_update_dto)
        print("The response of AppraisalWorkflowsApi->update_appraisal_workflow_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalWorkflowsApi->update_appraisal_workflow_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **workflow_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **appraisal_workflow_update_dto** | [**AppraisalWorkflowUpdateDto**](AppraisalWorkflowUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

