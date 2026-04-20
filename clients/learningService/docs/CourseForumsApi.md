# openapi_client.CourseForumsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_forum_async**](CourseForumsApi.md#create_course_forum_async) | **POST** /api/v2/LearningService/CourseForums | Create a course forum
[**delete_course_forum_async**](CourseForumsApi.md#delete_course_forum_async) | **DELETE** /api/v2/LearningService/CourseForums/{forumId} | Delete a course forum
[**get_course_forum_by_id_async**](CourseForumsApi.md#get_course_forum_by_id_async) | **GET** /api/v2/LearningService/CourseForums/{forumId} | Get course forum by ID
[**get_course_forums_async**](CourseForumsApi.md#get_course_forums_async) | **GET** /api/v2/LearningService/CourseForums | Get all course forums
[**get_course_forums_count_async**](CourseForumsApi.md#get_course_forums_count_async) | **GET** /api/v2/LearningService/CourseForums/Count | Get course forums count
[**update_course_forum_async**](CourseForumsApi.md#update_course_forum_async) | **PUT** /api/v2/LearningService/CourseForums/{forumId} | Update a course forum


# **create_course_forum_async**
> CourseForumDto create_course_forum_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_forum_create_dto=course_forum_create_dto)

Create a course forum

Creates a new course forum for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_forum_create_dto import CourseForumCreateDto
from openapi_client.models.course_forum_dto import CourseForumDto
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
    api_instance = openapi_client.CourseForumsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_forum_create_dto = openapi_client.CourseForumCreateDto() # CourseForumCreateDto |  (optional)

    try:
        # Create a course forum
        api_response = api_instance.create_course_forum_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_forum_create_dto=course_forum_create_dto)
        print("The response of CourseForumsApi->create_course_forum_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseForumsApi->create_course_forum_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_forum_create_dto** | [**CourseForumCreateDto**](CourseForumCreateDto.md)|  | [optional] 

### Return type

[**CourseForumDto**](CourseForumDto.md)

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

# **delete_course_forum_async**
> delete_course_forum_async(tenant_id, forum_id, api_version=api_version, x_api_version=x_api_version)

Delete a course forum

Deletes a course forum by its ID.

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
    api_instance = openapi_client.CourseForumsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    forum_id = 'forum_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course forum
        api_instance.delete_course_forum_async(tenant_id, forum_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseForumsApi->delete_course_forum_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **forum_id** | **str**|  | 
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

# **get_course_forum_by_id_async**
> CourseForumDto get_course_forum_by_id_async(forum_id, api_version=api_version, x_api_version=x_api_version)

Get course forum by ID

Retrieves a specific course forum by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_forum_dto import CourseForumDto
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
    api_instance = openapi_client.CourseForumsApi(api_client)
    forum_id = 'forum_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course forum by ID
        api_response = api_instance.get_course_forum_by_id_async(forum_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseForumsApi->get_course_forum_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseForumsApi->get_course_forum_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forum_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseForumDto**](CourseForumDto.md)

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

# **get_course_forums_async**
> List[CourseForumDto] get_course_forums_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course forums

Retrieves all course forums for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_forum_dto import CourseForumDto
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
    api_instance = openapi_client.CourseForumsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course forums
        api_response = api_instance.get_course_forums_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseForumsApi->get_course_forums_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseForumsApi->get_course_forums_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseForumDto]**](CourseForumDto.md)

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

# **get_course_forums_count_async**
> int get_course_forums_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course forums count

Returns the count of course forums for the specified tenant.

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
    api_instance = openapi_client.CourseForumsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course forums count
        api_response = api_instance.get_course_forums_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseForumsApi->get_course_forums_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseForumsApi->get_course_forums_count_async: %s\n" % e)
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

# **update_course_forum_async**
> CourseForumDto update_course_forum_async(tenant_id, forum_id, api_version=api_version, x_api_version=x_api_version, course_forum_update_dto=course_forum_update_dto)

Update a course forum

Updates an existing course forum.

### Example


```python
import openapi_client
from openapi_client.models.course_forum_dto import CourseForumDto
from openapi_client.models.course_forum_update_dto import CourseForumUpdateDto
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
    api_instance = openapi_client.CourseForumsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    forum_id = 'forum_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_forum_update_dto = openapi_client.CourseForumUpdateDto() # CourseForumUpdateDto |  (optional)

    try:
        # Update a course forum
        api_response = api_instance.update_course_forum_async(tenant_id, forum_id, api_version=api_version, x_api_version=x_api_version, course_forum_update_dto=course_forum_update_dto)
        print("The response of CourseForumsApi->update_course_forum_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseForumsApi->update_course_forum_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **forum_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_forum_update_dto** | [**CourseForumUpdateDto**](CourseForumUpdateDto.md)|  | [optional] 

### Return type

[**CourseForumDto**](CourseForumDto.md)

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

