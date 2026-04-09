# openapi_client.CourseUpdatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_update_async**](CourseUpdatesApi.md#create_course_update_async) | **POST** /api/v2/LearningService/CourseUpdates | Create a new course update
[**delete_course_update_async**](CourseUpdatesApi.md#delete_course_update_async) | **DELETE** /api/v2/LearningService/CourseUpdates/{updateId} | Delete a course update
[**get_course_update_by_id_async**](CourseUpdatesApi.md#get_course_update_by_id_async) | **GET** /api/v2/LearningService/CourseUpdates/{updateId} | Get course update by ID
[**get_course_updates_async**](CourseUpdatesApi.md#get_course_updates_async) | **GET** /api/v2/LearningService/CourseUpdates | Get all course updates
[**get_course_updates_count_async**](CourseUpdatesApi.md#get_course_updates_count_async) | **GET** /api/v2/LearningService/CourseUpdates/Count | Get course updates count
[**update_course_update_async**](CourseUpdatesApi.md#update_course_update_async) | **PUT** /api/v2/LearningService/CourseUpdates/{updateId} | Update a course update


# **create_course_update_async**
> create_course_update_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_news_create_dto=course_news_create_dto)

Create a new course update

Creates a new course update for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_news_create_dto import CourseNewsCreateDto
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
    api_instance = openapi_client.CourseUpdatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_news_create_dto = openapi_client.CourseNewsCreateDto() # CourseNewsCreateDto |  (optional)

    try:
        # Create a new course update
        api_instance.create_course_update_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_news_create_dto=course_news_create_dto)
    except Exception as e:
        print("Exception when calling CourseUpdatesApi->create_course_update_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_news_create_dto** | [**CourseNewsCreateDto**](CourseNewsCreateDto.md)|  | [optional] 

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

# **delete_course_update_async**
> delete_course_update_async(tenant_id, update_id, api_version=api_version, x_api_version=x_api_version)

Delete a course update

Deletes a course update for the specified tenant.

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
    api_instance = openapi_client.CourseUpdatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    update_id = 'update_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course update
        api_instance.delete_course_update_async(tenant_id, update_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseUpdatesApi->delete_course_update_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **update_id** | **str**|  | 
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

# **get_course_update_by_id_async**
> CourseNewsDto get_course_update_by_id_async(update_id, api_version=api_version, x_api_version=x_api_version)

Get course update by ID

Retrieves a specific course update by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_news_dto import CourseNewsDto
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
    api_instance = openapi_client.CourseUpdatesApi(api_client)
    update_id = 'update_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course update by ID
        api_response = api_instance.get_course_update_by_id_async(update_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUpdatesApi->get_course_update_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUpdatesApi->get_course_update_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseNewsDto**](CourseNewsDto.md)

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

# **get_course_updates_async**
> List[CourseNewsDto] get_course_updates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course updates

Retrieves all course updates for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_news_dto import CourseNewsDto
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
    api_instance = openapi_client.CourseUpdatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course updates
        api_response = api_instance.get_course_updates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUpdatesApi->get_course_updates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUpdatesApi->get_course_updates_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseNewsDto]**](CourseNewsDto.md)

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

# **get_course_updates_count_async**
> int get_course_updates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course updates count

Returns the count of course updates for the specified tenant.

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
    api_instance = openapi_client.CourseUpdatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course updates count
        api_response = api_instance.get_course_updates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUpdatesApi->get_course_updates_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUpdatesApi->get_course_updates_count_async: %s\n" % e)
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

# **update_course_update_async**
> update_course_update_async(tenant_id, update_id, api_version=api_version, x_api_version=x_api_version, course_news_update_dto=course_news_update_dto)

Update a course update

Updates an existing course update for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_news_update_dto import CourseNewsUpdateDto
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
    api_instance = openapi_client.CourseUpdatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    update_id = 'update_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_news_update_dto = openapi_client.CourseNewsUpdateDto() # CourseNewsUpdateDto |  (optional)

    try:
        # Update a course update
        api_instance.update_course_update_async(tenant_id, update_id, api_version=api_version, x_api_version=x_api_version, course_news_update_dto=course_news_update_dto)
    except Exception as e:
        print("Exception when calling CourseUpdatesApi->update_course_update_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **update_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_news_update_dto** | [**CourseNewsUpdateDto**](CourseNewsUpdateDto.md)|  | [optional] 

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

