# openapi_client.AppraisalStagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appraisal_stage_async**](AppraisalStagesApi.md#create_appraisal_stage_async) | **POST** /api/v2/HrmsService/AppraisalStages | Create an appraisal stage
[**delete_appraisal_stage_async**](AppraisalStagesApi.md#delete_appraisal_stage_async) | **DELETE** /api/v2/HrmsService/AppraisalStages/{stageId} | Delete an appraisal stage
[**get_appraisal_stage_by_id_async**](AppraisalStagesApi.md#get_appraisal_stage_by_id_async) | **GET** /api/v2/HrmsService/AppraisalStages/{stageId} | Get appraisal stage by ID
[**get_appraisal_stages_async**](AppraisalStagesApi.md#get_appraisal_stages_async) | **GET** /api/v2/HrmsService/AppraisalStages | Get appraisal stages
[**get_appraisal_stages_count_async**](AppraisalStagesApi.md#get_appraisal_stages_count_async) | **GET** /api/v2/HrmsService/AppraisalStages/Count | Count appraisal stages
[**update_appraisal_stage_async**](AppraisalStagesApi.md#update_appraisal_stage_async) | **PUT** /api/v2/HrmsService/AppraisalStages/{stageId} | Update an appraisal stage


# **create_appraisal_stage_async**
> EmptyEnvelope create_appraisal_stage_async(tenant_id, api_version=api_version, x_api_version=x_api_version, appraisal_stage_create_dto=appraisal_stage_create_dto)

Create an appraisal stage

Creates a new appraisal stage for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_stage_create_dto import AppraisalStageCreateDto
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
    api_instance = openapi_client.AppraisalStagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    appraisal_stage_create_dto = openapi_client.AppraisalStageCreateDto() # AppraisalStageCreateDto |  (optional)

    try:
        # Create an appraisal stage
        api_response = api_instance.create_appraisal_stage_async(tenant_id, api_version=api_version, x_api_version=x_api_version, appraisal_stage_create_dto=appraisal_stage_create_dto)
        print("The response of AppraisalStagesApi->create_appraisal_stage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalStagesApi->create_appraisal_stage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **appraisal_stage_create_dto** | [**AppraisalStageCreateDto**](AppraisalStageCreateDto.md)|  | [optional] 

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

# **delete_appraisal_stage_async**
> EmptyEnvelope delete_appraisal_stage_async(tenant_id, stage_id, api_version=api_version, x_api_version=x_api_version)

Delete an appraisal stage

Deletes an appraisal stage for the specified tenant.

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
    api_instance = openapi_client.AppraisalStagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    stage_id = 'stage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an appraisal stage
        api_response = api_instance.delete_appraisal_stage_async(tenant_id, stage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalStagesApi->delete_appraisal_stage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalStagesApi->delete_appraisal_stage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **stage_id** | **str**|  | 
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

# **get_appraisal_stage_by_id_async**
> AppraisalStageDtoEnvelope get_appraisal_stage_by_id_async(tenant_id, stage_id, api_version=api_version, x_api_version=x_api_version)

Get appraisal stage by ID

Retrieves a specific appraisal stage by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_stage_dto_envelope import AppraisalStageDtoEnvelope
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
    api_instance = openapi_client.AppraisalStagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    stage_id = 'stage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get appraisal stage by ID
        api_response = api_instance.get_appraisal_stage_by_id_async(tenant_id, stage_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalStagesApi->get_appraisal_stage_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalStagesApi->get_appraisal_stage_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **stage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AppraisalStageDtoEnvelope**](AppraisalStageDtoEnvelope.md)

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

# **get_appraisal_stages_async**
> AppraisalStageDtoListEnvelope get_appraisal_stages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get appraisal stages

Retrieves appraisal stages for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_stage_dto_list_envelope import AppraisalStageDtoListEnvelope
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
    api_instance = openapi_client.AppraisalStagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get appraisal stages
        api_response = api_instance.get_appraisal_stages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalStagesApi->get_appraisal_stages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalStagesApi->get_appraisal_stages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AppraisalStageDtoListEnvelope**](AppraisalStageDtoListEnvelope.md)

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

# **get_appraisal_stages_count_async**
> Int32Envelope get_appraisal_stages_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count appraisal stages

Counts appraisal stages for the specified tenant.

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
    api_instance = openapi_client.AppraisalStagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count appraisal stages
        api_response = api_instance.get_appraisal_stages_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AppraisalStagesApi->get_appraisal_stages_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalStagesApi->get_appraisal_stages_count_async: %s\n" % e)
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

# **update_appraisal_stage_async**
> EmptyEnvelope update_appraisal_stage_async(tenant_id, stage_id, api_version=api_version, x_api_version=x_api_version, appraisal_stage_update_dto=appraisal_stage_update_dto)

Update an appraisal stage

Updates an existing appraisal stage for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.appraisal_stage_update_dto import AppraisalStageUpdateDto
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
    api_instance = openapi_client.AppraisalStagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    stage_id = 'stage_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    appraisal_stage_update_dto = openapi_client.AppraisalStageUpdateDto() # AppraisalStageUpdateDto |  (optional)

    try:
        # Update an appraisal stage
        api_response = api_instance.update_appraisal_stage_async(tenant_id, stage_id, api_version=api_version, x_api_version=x_api_version, appraisal_stage_update_dto=appraisal_stage_update_dto)
        print("The response of AppraisalStagesApi->update_appraisal_stage_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppraisalStagesApi->update_appraisal_stage_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **stage_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **appraisal_stage_update_dto** | [**AppraisalStageUpdateDto**](AppraisalStageUpdateDto.md)|  | [optional] 

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

