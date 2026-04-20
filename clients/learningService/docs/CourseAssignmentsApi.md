# openapi_client.CourseAssignmentsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_assignment_async**](CourseAssignmentsApi.md#create_course_assignment_async) | **POST** /api/v2/LearningService/CourseAssignments | Create a new course assignment
[**delete_course_assignment_async**](CourseAssignmentsApi.md#delete_course_assignment_async) | **DELETE** /api/v2/LearningService/CourseAssignments/{assignmentId} | Delete a course assignment
[**get_course_assignment_by_id_async**](CourseAssignmentsApi.md#get_course_assignment_by_id_async) | **GET** /api/v2/LearningService/CourseAssignments/{assignmentId} | Get course assignment by ID
[**get_course_assignments_async**](CourseAssignmentsApi.md#get_course_assignments_async) | **GET** /api/v2/LearningService/CourseAssignments | Get all course assignments
[**get_course_assignments_count_async**](CourseAssignmentsApi.md#get_course_assignments_count_async) | **GET** /api/v2/LearningService/CourseAssignments/Count | Get course assignments count
[**update_course_assignment_async**](CourseAssignmentsApi.md#update_course_assignment_async) | **PUT** /api/v2/LearningService/CourseAssignments/{assignmentId} | Update a course assignment


# **create_course_assignment_async**
> create_course_assignment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_assignment_create_dto=course_assignment_create_dto)

Create a new course assignment

Creates a new course assignment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_create_dto import CourseAssignmentCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CourseAssignmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_assignment_create_dto = openapi_client.CourseAssignmentCreateDto() # CourseAssignmentCreateDto |  (optional)

    try:
        # Create a new course assignment
        api_instance.create_course_assignment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_assignment_create_dto=course_assignment_create_dto)
    except Exception as e:
        print("Exception when calling CourseAssignmentsApi->create_course_assignment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_assignment_create_dto** | [**CourseAssignmentCreateDto**](CourseAssignmentCreateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_assignment_async**
> delete_course_assignment_async(tenant_id, assignment_id, api_version=api_version, x_api_version=x_api_version)

Delete a course assignment

Deletes a course assignment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CourseAssignmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    assignment_id = 'assignment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course assignment
        api_instance.delete_course_assignment_async(tenant_id, assignment_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseAssignmentsApi->delete_course_assignment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **assignment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_assignment_by_id_async**
> CourseAssignmentDto get_course_assignment_by_id_async(assignment_id, api_version=api_version, x_api_version=x_api_version)

Get course assignment by ID

Retrieves a specific course assignment by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_dto import CourseAssignmentDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CourseAssignmentsApi(api_client)
    assignment_id = 'assignment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignment by ID
        api_response = api_instance.get_course_assignment_by_id_async(assignment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentsApi->get_course_assignment_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentsApi->get_course_assignment_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseAssignmentDto**](CourseAssignmentDto.md)

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

# **get_course_assignments_async**
> List[CourseAssignmentDto] get_course_assignments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course assignments

Retrieves all course assignments for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_dto import CourseAssignmentDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CourseAssignmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course assignments
        api_response = api_instance.get_course_assignments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentsApi->get_course_assignments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentsApi->get_course_assignments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseAssignmentDto]**](CourseAssignmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_assignments_count_async**
> int get_course_assignments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course assignments count

Returns the count of course assignments for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CourseAssignmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignments count
        api_response = api_instance.get_course_assignments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentsApi->get_course_assignments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentsApi->get_course_assignments_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_course_assignment_async**
> update_course_assignment_async(tenant_id, assignment_id, api_version=api_version, x_api_version=x_api_version, course_assignment_update_dto=course_assignment_update_dto)

Update a course assignment

Updates an existing course assignment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_update_dto import CourseAssignmentUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://absuite.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://absuite.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CourseAssignmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    assignment_id = 'assignment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_assignment_update_dto = openapi_client.CourseAssignmentUpdateDto() # CourseAssignmentUpdateDto |  (optional)

    try:
        # Update a course assignment
        api_instance.update_course_assignment_async(tenant_id, assignment_id, api_version=api_version, x_api_version=x_api_version, course_assignment_update_dto=course_assignment_update_dto)
    except Exception as e:
        print("Exception when calling CourseAssignmentsApi->update_course_assignment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **assignment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_assignment_update_dto** | [**CourseAssignmentUpdateDto**](CourseAssignmentUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

