# openapi_client.TimeLogApprovalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_time_tracker_service_time_log_approvals_approval_id_approver_put**](TimeLogApprovalsApi.md#api_v2_time_tracker_service_time_log_approvals_approval_id_approver_put) | **PUT** /api/v2/TimeTrackerService/TimeLogApprovals/{approvalId}/Approver | 
[**api_v2_time_tracker_service_time_log_approvals_approval_id_status_put**](TimeLogApprovalsApi.md#api_v2_time_tracker_service_time_log_approvals_approval_id_status_put) | **PUT** /api/v2/TimeTrackerService/TimeLogApprovals/{approvalId}/Status | 
[**api_v2_time_tracker_service_time_log_approvals_post**](TimeLogApprovalsApi.md#api_v2_time_tracker_service_time_log_approvals_post) | **POST** /api/v2/TimeTrackerService/TimeLogApprovals | 


# **api_v2_time_tracker_service_time_log_approvals_approval_id_approver_put**
> api_v2_time_tracker_service_time_log_approvals_approval_id_approver_put(approval_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_approver_update_dto=project_hours_approval_approver_update_dto)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.TimeLogApprovalsApi(api_client)
    approval_id = 'approval_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_hours_approval_approver_update_dto = openapi_client.ProjectHoursApprovalApproverUpdateDto() # ProjectHoursApprovalApproverUpdateDto |  (optional)

    try:
        api_instance.api_v2_time_tracker_service_time_log_approvals_approval_id_approver_put(approval_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_approver_update_dto=project_hours_approval_approver_update_dto)
    except Exception as e:
        print("Exception when calling TimeLogApprovalsApi->api_v2_time_tracker_service_time_log_approvals_approval_id_approver_put: %s\n" % e)
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

# **api_v2_time_tracker_service_time_log_approvals_approval_id_status_put**
> api_v2_time_tracker_service_time_log_approvals_approval_id_status_put(tenant_id, approval_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_status_update_dto=project_hours_approval_status_update_dto)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.TimeLogApprovalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    approval_id = 'approval_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_hours_approval_status_update_dto = openapi_client.ProjectHoursApprovalStatusUpdateDto() # ProjectHoursApprovalStatusUpdateDto |  (optional)

    try:
        api_instance.api_v2_time_tracker_service_time_log_approvals_approval_id_status_put(tenant_id, approval_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_status_update_dto=project_hours_approval_status_update_dto)
    except Exception as e:
        print("Exception when calling TimeLogApprovalsApi->api_v2_time_tracker_service_time_log_approvals_approval_id_status_put: %s\n" % e)
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

# **api_v2_time_tracker_service_time_log_approvals_post**
> api_v2_time_tracker_service_time_log_approvals_post(tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_create_dto=project_hours_approval_create_dto)



### Example

* Api Key Authentication (Bearer):

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
    api_instance = openapi_client.TimeLogApprovalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_hours_approval_create_dto = openapi_client.ProjectHoursApprovalCreateDto() # ProjectHoursApprovalCreateDto |  (optional)

    try:
        api_instance.api_v2_time_tracker_service_time_log_approvals_post(tenant_id, api_version=api_version, x_api_version=x_api_version, project_hours_approval_create_dto=project_hours_approval_create_dto)
    except Exception as e:
        print("Exception when calling TimeLogApprovalsApi->api_v2_time_tracker_service_time_log_approvals_post: %s\n" % e)
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

