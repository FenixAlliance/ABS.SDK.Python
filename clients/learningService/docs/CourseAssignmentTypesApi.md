# openapi_client.CourseAssignmentTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_assignment_type_async**](CourseAssignmentTypesApi.md#create_course_assignment_type_async) | **POST** /api/v2/LearningService/CourseAssignmentTypes | Create a course assignment type
[**delete_course_assignment_type_async**](CourseAssignmentTypesApi.md#delete_course_assignment_type_async) | **DELETE** /api/v2/LearningService/CourseAssignmentTypes/{assignmentTypeId} | Delete a course assignment type
[**get_course_assignment_type_by_id_async**](CourseAssignmentTypesApi.md#get_course_assignment_type_by_id_async) | **GET** /api/v2/LearningService/CourseAssignmentTypes/{assignmentTypeId} | Get course assignment type by ID
[**get_course_assignment_types_async**](CourseAssignmentTypesApi.md#get_course_assignment_types_async) | **GET** /api/v2/LearningService/CourseAssignmentTypes | Get all course assignment types
[**get_course_assignment_types_count_async**](CourseAssignmentTypesApi.md#get_course_assignment_types_count_async) | **GET** /api/v2/LearningService/CourseAssignmentTypes/Count | Get course assignment types count
[**update_course_assignment_type_async**](CourseAssignmentTypesApi.md#update_course_assignment_type_async) | **PUT** /api/v2/LearningService/CourseAssignmentTypes/{assignmentTypeId} | Update a course assignment type


# **create_course_assignment_type_async**
> create_course_assignment_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_assignment_type_create_dto=course_assignment_type_create_dto)

Create a course assignment type

Creates a new course assignment type for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_type_create_dto import CourseAssignmentTypeCreateDto
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
    api_instance = openapi_client.CourseAssignmentTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_assignment_type_create_dto = openapi_client.CourseAssignmentTypeCreateDto() # CourseAssignmentTypeCreateDto |  (optional)

    try:
        # Create a course assignment type
        api_instance.create_course_assignment_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_assignment_type_create_dto=course_assignment_type_create_dto)
    except Exception as e:
        print("Exception when calling CourseAssignmentTypesApi->create_course_assignment_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_assignment_type_create_dto** | [**CourseAssignmentTypeCreateDto**](CourseAssignmentTypeCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_assignment_type_async**
> delete_course_assignment_type_async(tenant_id, assignment_type_id, api_version=api_version, x_api_version=x_api_version)

Delete a course assignment type

Deletes a course assignment type by its ID.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CourseAssignmentTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    assignment_type_id = 'assignment_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course assignment type
        api_instance.delete_course_assignment_type_async(tenant_id, assignment_type_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseAssignmentTypesApi->delete_course_assignment_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **assignment_type_id** | **str**|  | 
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

# **get_course_assignment_type_by_id_async**
> CourseAssignmentTypeDto get_course_assignment_type_by_id_async(assignment_type_id, api_version=api_version, x_api_version=x_api_version)

Get course assignment type by ID

Retrieves a specific course assignment type by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_type_dto import CourseAssignmentTypeDto
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
    api_instance = openapi_client.CourseAssignmentTypesApi(api_client)
    assignment_type_id = 'assignment_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignment type by ID
        api_response = api_instance.get_course_assignment_type_by_id_async(assignment_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentTypesApi->get_course_assignment_type_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentTypesApi->get_course_assignment_type_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseAssignmentTypeDto**](CourseAssignmentTypeDto.md)

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

# **get_course_assignment_types_async**
> List[CourseAssignmentTypeDto] get_course_assignment_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course assignment types

Retrieves all course assignment types for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_type_dto import CourseAssignmentTypeDto
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
    api_instance = openapi_client.CourseAssignmentTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course assignment types
        api_response = api_instance.get_course_assignment_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentTypesApi->get_course_assignment_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentTypesApi->get_course_assignment_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseAssignmentTypeDto]**](CourseAssignmentTypeDto.md)

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

# **get_course_assignment_types_count_async**
> int get_course_assignment_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course assignment types count

Returns the count of course assignment types for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CourseAssignmentTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignment types count
        api_response = api_instance.get_course_assignment_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentTypesApi->get_course_assignment_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentTypesApi->get_course_assignment_types_count_async: %s\n" % e)
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

# **update_course_assignment_type_async**
> update_course_assignment_type_async(tenant_id, assignment_type_id, api_version=api_version, x_api_version=x_api_version, course_assignment_type_update_dto=course_assignment_type_update_dto)

Update a course assignment type

Updates an existing course assignment type.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_type_update_dto import CourseAssignmentTypeUpdateDto
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
    api_instance = openapi_client.CourseAssignmentTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    assignment_type_id = 'assignment_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_assignment_type_update_dto = openapi_client.CourseAssignmentTypeUpdateDto() # CourseAssignmentTypeUpdateDto |  (optional)

    try:
        # Update a course assignment type
        api_instance.update_course_assignment_type_async(tenant_id, assignment_type_id, api_version=api_version, x_api_version=x_api_version, course_assignment_type_update_dto=course_assignment_type_update_dto)
    except Exception as e:
        print("Exception when calling CourseAssignmentTypesApi->update_course_assignment_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **assignment_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_assignment_type_update_dto** | [**CourseAssignmentTypeUpdateDto**](CourseAssignmentTypeUpdateDto.md)|  | [optional] 

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

