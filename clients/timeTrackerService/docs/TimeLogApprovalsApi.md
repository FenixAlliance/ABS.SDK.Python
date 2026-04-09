# openapi_client.TimeLogApprovalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_project_hours_approval_async**](TimeLogApprovalsApi.md#request_project_hours_approval_async) | **POST** /api/v2/TimeTrackerService/TimeLogApprovals | Request project hours approval
[**update_project_hours_approval_approver_async**](TimeLogApprovalsApi.md#update_project_hours_approval_approver_async) | **PUT** /api/v2/TimeTrackerService/TimeLogApprovals/{approvalId}/Approver | Update approval approver
[**update_project_hours_approval_status_async**](TimeLogApprovalsApi.md#update_project_hours_approval_status_async) | **PUT** /api/v2/TimeTrackerService/TimeLogApprovals/{approvalId}/Status | Update approval status


# **request_project_hours_approval_async**
> request_project_hours_approval_async(tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_create_dto=project_hours_approval_create_dto)

Request project hours approval

Creates a new project hours approval request.

### Example


```python
import openapi_client
from openapi_client.models.project_hours_approval_create_dto import ProjectHoursApprovalCreateDto
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
    api_instance = openapi_client.TimeLogApprovalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_hours_approval_create_dto = openapi_client.ProjectHoursApprovalCreateDto() # ProjectHoursApprovalCreateDto |  (optional)

    try:
        # Request project hours approval
        api_instance.request_project_hours_approval_async(tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_create_dto=project_hours_approval_create_dto)
    except Exception as e:
        print("Exception when calling TimeLogApprovalsApi->request_project_hours_approval_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_hours_approval_create_dto** | [**ProjectHoursApprovalCreateDto**](ProjectHoursApprovalCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

# **update_project_hours_approval_approver_async**
> update_project_hours_approval_approver_async(approval_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_approver_update_dto=project_hours_approval_approver_update_dto)

Update approval approver

Updates the approver of an existing project hours approval.

### Example


```python
import openapi_client
from openapi_client.models.project_hours_approval_approver_update_dto import ProjectHoursApprovalApproverUpdateDto
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
    api_instance = openapi_client.TimeLogApprovalsApi(api_client)
    approval_id = 'approval_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_hours_approval_approver_update_dto = openapi_client.ProjectHoursApprovalApproverUpdateDto() # ProjectHoursApprovalApproverUpdateDto |  (optional)

    try:
        # Update approval approver
        api_instance.update_project_hours_approval_approver_async(approval_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_approver_update_dto=project_hours_approval_approver_update_dto)
    except Exception as e:
        print("Exception when calling TimeLogApprovalsApi->update_project_hours_approval_approver_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_hours_approval_approver_update_dto** | [**ProjectHoursApprovalApproverUpdateDto**](ProjectHoursApprovalApproverUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

# **update_project_hours_approval_status_async**
> update_project_hours_approval_status_async(tenant_id, approval_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_status_update_dto=project_hours_approval_status_update_dto)

Update approval status

Updates the status of an existing project hours approval.

### Example


```python
import openapi_client
from openapi_client.models.project_hours_approval_status_update_dto import ProjectHoursApprovalStatusUpdateDto
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
    api_instance = openapi_client.TimeLogApprovalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    approval_id = 'approval_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_hours_approval_status_update_dto = openapi_client.ProjectHoursApprovalStatusUpdateDto() # ProjectHoursApprovalStatusUpdateDto |  (optional)

    try:
        # Update approval status
        api_instance.update_project_hours_approval_status_async(tenant_id, approval_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_status_update_dto=project_hours_approval_status_update_dto)
    except Exception as e:
        print("Exception when calling TimeLogApprovalsApi->update_project_hours_approval_status_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **approval_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_hours_approval_status_update_dto** | [**ProjectHoursApprovalStatusUpdateDto**](ProjectHoursApprovalStatusUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

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

