# openapi_client.CourseContentGroupsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_content_group_async**](CourseContentGroupsApi.md#create_course_content_group_async) | **POST** /api/v2/LearningService/CourseContentGroups | Create a new course content group
[**delete_course_content_group_async**](CourseContentGroupsApi.md#delete_course_content_group_async) | **DELETE** /api/v2/LearningService/CourseContentGroups/{groupId} | Delete a course content group
[**get_course_content_group_by_id_async**](CourseContentGroupsApi.md#get_course_content_group_by_id_async) | **GET** /api/v2/LearningService/CourseContentGroups/{groupId} | Get course content group by ID
[**get_course_content_groups_async**](CourseContentGroupsApi.md#get_course_content_groups_async) | **GET** /api/v2/LearningService/CourseContentGroups | Get all course content groups
[**get_course_content_groups_by_course_async**](CourseContentGroupsApi.md#get_course_content_groups_by_course_async) | **GET** /api/v2/LearningService/Courses/{courseId}/ContentGroups | Get course content groups by course
[**get_course_content_groups_by_course_count_async**](CourseContentGroupsApi.md#get_course_content_groups_by_course_count_async) | **GET** /api/v2/LearningService/Courses/{courseId}/ContentGroups/Count | Get course content groups count by course
[**get_course_content_groups_count_async**](CourseContentGroupsApi.md#get_course_content_groups_count_async) | **GET** /api/v2/LearningService/CourseContentGroups/Count | Get course content groups count
[**update_course_content_group_async**](CourseContentGroupsApi.md#update_course_content_group_async) | **PUT** /api/v2/LearningService/CourseContentGroups/{groupId} | Update a course content group


# **create_course_content_group_async**
> create_course_content_group_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_content_group_create_dto=course_content_group_create_dto)

Create a new course content group

Creates a new course content group for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_content_group_create_dto import CourseContentGroupCreateDto
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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_content_group_create_dto = openapi_client.CourseContentGroupCreateDto() # CourseContentGroupCreateDto |  (optional)

    try:
        # Create a new course content group
        api_instance.create_course_content_group_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_content_group_create_dto=course_content_group_create_dto)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->create_course_content_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_content_group_create_dto** | [**CourseContentGroupCreateDto**](CourseContentGroupCreateDto.md)|  | [optional] 

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

# **delete_course_content_group_async**
> delete_course_content_group_async(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version)

Delete a course content group

Deletes a course content group for the specified tenant.

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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    group_id = 'group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course content group
        api_instance.delete_course_content_group_async(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->delete_course_content_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **group_id** | **str**|  | 
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

# **get_course_content_group_by_id_async**
> CourseContentGroupDto get_course_content_group_by_id_async(group_id, api_version=api_version, x_api_version=x_api_version)

Get course content group by ID

Retrieves a specific course content group by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_content_group_dto import CourseContentGroupDto
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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course content group by ID
        api_response = api_instance.get_course_content_group_by_id_async(group_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseContentGroupsApi->get_course_content_group_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->get_course_content_group_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseContentGroupDto**](CourseContentGroupDto.md)

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

# **get_course_content_groups_async**
> List[CourseContentGroupDto] get_course_content_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course content groups

Retrieves all course content groups for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_content_group_dto import CourseContentGroupDto
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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course content groups
        api_response = api_instance.get_course_content_groups_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseContentGroupsApi->get_course_content_groups_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->get_course_content_groups_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseContentGroupDto]**](CourseContentGroupDto.md)

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

# **get_course_content_groups_by_course_async**
> List[CourseContentGroupDto] get_course_content_groups_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course content groups by course

Retrieves all course content groups for a specific course.

### Example


```python
import openapi_client
from openapi_client.models.course_content_group_dto import CourseContentGroupDto
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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course content groups by course
        api_response = api_instance.get_course_content_groups_by_course_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseContentGroupsApi->get_course_content_groups_by_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->get_course_content_groups_by_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseContentGroupDto]**](CourseContentGroupDto.md)

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

# **get_course_content_groups_by_course_count_async**
> int get_course_content_groups_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)

Get course content groups count by course

Returns the count of course content groups for a specific course.

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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course content groups count by course
        api_response = api_instance.get_course_content_groups_by_course_count_async(course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseContentGroupsApi->get_course_content_groups_by_course_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->get_course_content_groups_by_course_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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

# **get_course_content_groups_count_async**
> int get_course_content_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course content groups count

Returns the count of course content groups for the specified tenant.

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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course content groups count
        api_response = api_instance.get_course_content_groups_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseContentGroupsApi->get_course_content_groups_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->get_course_content_groups_count_async: %s\n" % e)
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

# **update_course_content_group_async**
> update_course_content_group_async(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version, course_content_group_update_dto=course_content_group_update_dto)

Update a course content group

Updates an existing course content group for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_content_group_update_dto import CourseContentGroupUpdateDto
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
    api_instance = openapi_client.CourseContentGroupsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    group_id = 'group_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_content_group_update_dto = openapi_client.CourseContentGroupUpdateDto() # CourseContentGroupUpdateDto |  (optional)

    try:
        # Update a course content group
        api_instance.update_course_content_group_async(tenant_id, group_id, api_version=api_version, x_api_version=x_api_version, course_content_group_update_dto=course_content_group_update_dto)
    except Exception as e:
        print("Exception when calling CourseContentGroupsApi->update_course_content_group_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **group_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_content_group_update_dto** | [**CourseContentGroupUpdateDto**](CourseContentGroupUpdateDto.md)|  | [optional] 

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

