# openapi_client.CoursePagesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_page_async**](CoursePagesApi.md#create_course_page_async) | **POST** /api/v2/LearningService/CoursePages | Create a new course page
[**delete_course_page_async**](CoursePagesApi.md#delete_course_page_async) | **DELETE** /api/v2/LearningService/CoursePages/{pageId} | Delete a course page
[**get_course_page_by_id_async**](CoursePagesApi.md#get_course_page_by_id_async) | **GET** /api/v2/LearningService/CoursePages/{pageId} | Get course page by ID
[**get_course_pages_async**](CoursePagesApi.md#get_course_pages_async) | **GET** /api/v2/LearningService/CoursePages | Get all course pages
[**get_course_pages_count_async**](CoursePagesApi.md#get_course_pages_count_async) | **GET** /api/v2/LearningService/CoursePages/Count | Get course pages count
[**update_course_page_async**](CoursePagesApi.md#update_course_page_async) | **PUT** /api/v2/LearningService/CoursePages/{pageId} | Update a course page


# **create_course_page_async**
> create_course_page_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_page_create_dto=course_page_create_dto)

Create a new course page

Creates a new course page for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_page_create_dto import CoursePageCreateDto
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
    api_instance = openapi_client.CoursePagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_page_create_dto = openapi_client.CoursePageCreateDto() # CoursePageCreateDto |  (optional)

    try:
        # Create a new course page
        api_instance.create_course_page_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_page_create_dto=course_page_create_dto)
    except Exception as e:
        print("Exception when calling CoursePagesApi->create_course_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_page_create_dto** | [**CoursePageCreateDto**](CoursePageCreateDto.md)|  | [optional] 

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

# **delete_course_page_async**
> delete_course_page_async(tenant_id, page_id, api_version=api_version, x_api_version=x_api_version)

Delete a course page

Deletes a course page for the specified tenant.

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
    api_instance = openapi_client.CoursePagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page_id = 'page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course page
        api_instance.delete_course_page_async(tenant_id, page_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CoursePagesApi->delete_course_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **page_id** | **str**|  | 
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

# **get_course_page_by_id_async**
> CoursePageDto get_course_page_by_id_async(page_id, api_version=api_version, x_api_version=x_api_version)

Get course page by ID

Retrieves a specific course page by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_page_dto import CoursePageDto
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
    api_instance = openapi_client.CoursePagesApi(api_client)
    page_id = 'page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course page by ID
        api_response = api_instance.get_course_page_by_id_async(page_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursePagesApi->get_course_page_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursePagesApi->get_course_page_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CoursePageDto**](CoursePageDto.md)

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

# **get_course_pages_async**
> List[CoursePageDto] get_course_pages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course pages

Retrieves all course pages for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_page_dto import CoursePageDto
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
    api_instance = openapi_client.CoursePagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course pages
        api_response = api_instance.get_course_pages_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursePagesApi->get_course_pages_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursePagesApi->get_course_pages_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CoursePageDto]**](CoursePageDto.md)

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

# **get_course_pages_count_async**
> int get_course_pages_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course pages count

Returns the count of course pages for the specified tenant.

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
    api_instance = openapi_client.CoursePagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course pages count
        api_response = api_instance.get_course_pages_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CoursePagesApi->get_course_pages_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursePagesApi->get_course_pages_count_async: %s\n" % e)
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

# **update_course_page_async**
> update_course_page_async(tenant_id, page_id, api_version=api_version, x_api_version=x_api_version, course_page_update_dto=course_page_update_dto)

Update a course page

Updates an existing course page for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_page_update_dto import CoursePageUpdateDto
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
    api_instance = openapi_client.CoursePagesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page_id = 'page_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_page_update_dto = openapi_client.CoursePageUpdateDto() # CoursePageUpdateDto |  (optional)

    try:
        # Update a course page
        api_instance.update_course_page_async(tenant_id, page_id, api_version=api_version, x_api_version=x_api_version, course_page_update_dto=course_page_update_dto)
    except Exception as e:
        print("Exception when calling CoursePagesApi->update_course_page_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **page_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_page_update_dto** | [**CoursePageUpdateDto**](CoursePageUpdateDto.md)|  | [optional] 

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

