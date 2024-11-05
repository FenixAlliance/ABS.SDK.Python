# openapi_client.ProjectTimeLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_time_tracker_service_project_time_logs_by_responsible_contact_get**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_by_responsible_contact_get) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/ByResponsibleContact | 
[**api_v2_time_tracker_service_project_time_logs_created_by_contact_get**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_created_by_contact_get) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/CreatedByContact | 
[**api_v2_time_tracker_service_project_time_logs_for_project_project_id_get**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_for_project_project_id_get) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/ForProject/{projectId} | 
[**api_v2_time_tracker_service_project_time_logs_get**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_get) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs | 
[**api_v2_time_tracker_service_project_time_logs_post**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_post) | **POST** /api/v2/TimeTrackerService/ProjectTimeLogs | 
[**api_v2_time_tracker_service_project_time_logs_time_log_id_delete**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_time_log_id_delete) | **DELETE** /api/v2/TimeTrackerService/ProjectTimeLogs/{timeLogId} | 
[**api_v2_time_tracker_service_project_time_logs_time_log_id_get**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_time_log_id_get) | **GET** /api/v2/TimeTrackerService/ProjectTimeLogs/{timeLogId} | 
[**api_v2_time_tracker_service_project_time_logs_time_log_id_put**](ProjectTimeLogsApi.md#api_v2_time_tracker_service_project_time_logs_time_log_id_put) | **PUT** /api/v2/TimeTrackerService/ProjectTimeLogs/{timeLogId} | 


# **api_v2_time_tracker_service_project_time_logs_by_responsible_contact_get**
> ProjectTimeLogDtoListEnvelope api_v2_time_tracker_service_project_time_logs_by_responsible_contact_get(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_time_tracker_service_project_time_logs_by_responsible_contact_get(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_by_responsible_contact_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_by_responsible_contact_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTimeLogDtoListEnvelope**](ProjectTimeLogDtoListEnvelope.md)

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

# **api_v2_time_tracker_service_project_time_logs_created_by_contact_get**
> ProjectTimeLogDtoListEnvelope api_v2_time_tracker_service_project_time_logs_created_by_contact_get(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_time_tracker_service_project_time_logs_created_by_contact_get(contact_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_created_by_contact_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_created_by_contact_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTimeLogDtoListEnvelope**](ProjectTimeLogDtoListEnvelope.md)

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

# **api_v2_time_tracker_service_project_time_logs_for_project_project_id_get**
> ProjectTimeLogDtoListEnvelope api_v2_time_tracker_service_project_time_logs_for_project_project_id_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    project_id = 'project_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_time_tracker_service_project_time_logs_for_project_project_id_get(project_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_for_project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_for_project_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTimeLogDtoListEnvelope**](ProjectTimeLogDtoListEnvelope.md)

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

# **api_v2_time_tracker_service_project_time_logs_get**
> ProjectTimeLogDtoListEnvelope api_v2_time_tracker_service_project_time_logs_get(tenant_id, project_period_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    project_period_id = 'project_period_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_time_tracker_service_project_time_logs_get(tenant_id, project_period_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **project_period_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTimeLogDtoListEnvelope**](ProjectTimeLogDtoListEnvelope.md)

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

# **api_v2_time_tracker_service_project_time_logs_post**
> api_v2_time_tracker_service_project_time_logs_post(tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_create_dto=project_time_log_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_create_dto import ProjectTimeLogCreateDto
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_time_log_create_dto = openapi_client.ProjectTimeLogCreateDto() # ProjectTimeLogCreateDto |  (optional)

    try:
        api_instance.api_v2_time_tracker_service_project_time_logs_post(tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_create_dto=project_time_log_create_dto)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_time_log_create_dto** | [**ProjectTimeLogCreateDto**](ProjectTimeLogCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_time_tracker_service_project_time_logs_time_log_id_delete**
> api_v2_time_tracker_service_project_time_logs_time_log_id_delete(tenant_id, time_log_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    time_log_id = 'time_log_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_instance.api_v2_time_tracker_service_project_time_logs_time_log_id_delete(tenant_id, time_log_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_time_log_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **time_log_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_time_tracker_service_project_time_logs_time_log_id_get**
> ProjectTimeLogDtoEnvelope api_v2_time_tracker_service_project_time_logs_time_log_id_get(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_dto_envelope import ProjectTimeLogDtoEnvelope
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    time_log_id = 'time_log_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_time_tracker_service_project_time_logs_time_log_id_get(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_time_log_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_time_log_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_log_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProjectTimeLogDtoEnvelope**](ProjectTimeLogDtoEnvelope.md)

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

# **api_v2_time_tracker_service_project_time_logs_time_log_id_put**
> api_v2_time_tracker_service_project_time_logs_time_log_id_put(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_update_dto=project_time_log_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.project_time_log_update_dto import ProjectTimeLogUpdateDto
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
    api_instance = openapi_client.ProjectTimeLogsApi(api_client)
    time_log_id = 'time_log_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    project_time_log_update_dto = openapi_client.ProjectTimeLogUpdateDto() # ProjectTimeLogUpdateDto |  (optional)

    try:
        api_instance.api_v2_time_tracker_service_project_time_logs_time_log_id_put(time_log_id, tenant_id, api_version=api_version, x_api_version=x_api_version, project_time_log_update_dto=project_time_log_update_dto)
    except Exception as e:
        print("Exception when calling ProjectTimeLogsApi->api_v2_time_tracker_service_project_time_logs_time_log_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_log_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **project_time_log_update_dto** | [**ProjectTimeLogUpdateDto**](ProjectTimeLogUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

