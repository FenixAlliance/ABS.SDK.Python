# openapi_client.CourseAssignmentComponentsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_assignment_component_async**](CourseAssignmentComponentsApi.md#create_course_assignment_component_async) | **POST** /api/v2/LearningService/CourseAssignmentComponents | Create a course assignment component
[**delete_course_assignment_component_async**](CourseAssignmentComponentsApi.md#delete_course_assignment_component_async) | **DELETE** /api/v2/LearningService/CourseAssignmentComponents/{componentId} | Delete a course assignment component
[**get_course_assignment_component_by_id_async**](CourseAssignmentComponentsApi.md#get_course_assignment_component_by_id_async) | **GET** /api/v2/LearningService/CourseAssignmentComponents/{componentId} | Get course assignment component by ID
[**get_course_assignment_components_async**](CourseAssignmentComponentsApi.md#get_course_assignment_components_async) | **GET** /api/v2/LearningService/CourseAssignmentComponents | Get all course assignment components
[**get_course_assignment_components_count_async**](CourseAssignmentComponentsApi.md#get_course_assignment_components_count_async) | **GET** /api/v2/LearningService/CourseAssignmentComponents/Count | Get course assignment components count
[**update_course_assignment_component_async**](CourseAssignmentComponentsApi.md#update_course_assignment_component_async) | **PUT** /api/v2/LearningService/CourseAssignmentComponents/{componentId} | Update a course assignment component


# **create_course_assignment_component_async**
> create_course_assignment_component_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_assignment_component_create_dto=course_assignment_component_create_dto)

Create a course assignment component

Creates a new course assignment component for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_component_create_dto import CourseAssignmentComponentCreateDto
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
    api_instance = openapi_client.CourseAssignmentComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_assignment_component_create_dto = openapi_client.CourseAssignmentComponentCreateDto() # CourseAssignmentComponentCreateDto |  (optional)

    try:
        # Create a course assignment component
        api_instance.create_course_assignment_component_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_assignment_component_create_dto=course_assignment_component_create_dto)
    except Exception as e:
        print("Exception when calling CourseAssignmentComponentsApi->create_course_assignment_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_assignment_component_create_dto** | [**CourseAssignmentComponentCreateDto**](CourseAssignmentComponentCreateDto.md)|  | [optional] 

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

# **delete_course_assignment_component_async**
> delete_course_assignment_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version)

Delete a course assignment component

Deletes a course assignment component by its ID.

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
    api_instance = openapi_client.CourseAssignmentComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    component_id = 'component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course assignment component
        api_instance.delete_course_assignment_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseAssignmentComponentsApi->delete_course_assignment_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **component_id** | **str**|  | 
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

# **get_course_assignment_component_by_id_async**
> CourseAssignmentComponentDto get_course_assignment_component_by_id_async(component_id, api_version=api_version, x_api_version=x_api_version)

Get course assignment component by ID

Retrieves a specific course assignment component by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_component_dto import CourseAssignmentComponentDto
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
    api_instance = openapi_client.CourseAssignmentComponentsApi(api_client)
    component_id = 'component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignment component by ID
        api_response = api_instance.get_course_assignment_component_by_id_async(component_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentComponentsApi->get_course_assignment_component_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentComponentsApi->get_course_assignment_component_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseAssignmentComponentDto**](CourseAssignmentComponentDto.md)

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

# **get_course_assignment_components_async**
> List[CourseAssignmentComponentDto] get_course_assignment_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course assignment components

Retrieves all course assignment components for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_component_dto import CourseAssignmentComponentDto
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
    api_instance = openapi_client.CourseAssignmentComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course assignment components
        api_response = api_instance.get_course_assignment_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentComponentsApi->get_course_assignment_components_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentComponentsApi->get_course_assignment_components_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseAssignmentComponentDto]**](CourseAssignmentComponentDto.md)

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

# **get_course_assignment_components_count_async**
> int get_course_assignment_components_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course assignment components count

Returns the count of course assignment components for the specified tenant.

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
    api_instance = openapi_client.CourseAssignmentComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course assignment components count
        api_response = api_instance.get_course_assignment_components_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseAssignmentComponentsApi->get_course_assignment_components_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseAssignmentComponentsApi->get_course_assignment_components_count_async: %s\n" % e)
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

# **update_course_assignment_component_async**
> update_course_assignment_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version, course_assignment_component_update_dto=course_assignment_component_update_dto)

Update a course assignment component

Updates an existing course assignment component.

### Example


```python
import openapi_client
from openapi_client.models.course_assignment_component_update_dto import CourseAssignmentComponentUpdateDto
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
    api_instance = openapi_client.CourseAssignmentComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    component_id = 'component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_assignment_component_update_dto = openapi_client.CourseAssignmentComponentUpdateDto() # CourseAssignmentComponentUpdateDto |  (optional)

    try:
        # Update a course assignment component
        api_instance.update_course_assignment_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version, course_assignment_component_update_dto=course_assignment_component_update_dto)
    except Exception as e:
        print("Exception when calling CourseAssignmentComponentsApi->update_course_assignment_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **component_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_assignment_component_update_dto** | [**CourseAssignmentComponentUpdateDto**](CourseAssignmentComponentUpdateDto.md)|  | [optional] 

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

