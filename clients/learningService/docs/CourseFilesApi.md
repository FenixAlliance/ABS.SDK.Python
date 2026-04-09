# openapi_client.CourseFilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_file_async**](CourseFilesApi.md#create_course_file_async) | **POST** /api/v2/LearningService/CourseFiles | Create a new course file
[**delete_course_file_async**](CourseFilesApi.md#delete_course_file_async) | **DELETE** /api/v2/LearningService/CourseFiles/{fileId} | Delete a course file
[**get_course_file_by_id_async**](CourseFilesApi.md#get_course_file_by_id_async) | **GET** /api/v2/LearningService/CourseFiles/{fileId} | Get course file by ID
[**get_course_files_async**](CourseFilesApi.md#get_course_files_async) | **GET** /api/v2/LearningService/CourseFiles | Get all course files
[**get_course_files_count_async**](CourseFilesApi.md#get_course_files_count_async) | **GET** /api/v2/LearningService/CourseFiles/Count | Get course files count
[**update_course_file_async**](CourseFilesApi.md#update_course_file_async) | **PUT** /api/v2/LearningService/CourseFiles/{fileId} | Update a course file


# **create_course_file_async**
> create_course_file_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_file_create_dto=course_file_create_dto)

Create a new course file

Creates a new course file for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_file_create_dto import CourseFileCreateDto
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
    api_instance = openapi_client.CourseFilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_file_create_dto = openapi_client.CourseFileCreateDto() # CourseFileCreateDto |  (optional)

    try:
        # Create a new course file
        api_instance.create_course_file_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_file_create_dto=course_file_create_dto)
    except Exception as e:
        print("Exception when calling CourseFilesApi->create_course_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_file_create_dto** | [**CourseFileCreateDto**](CourseFileCreateDto.md)|  | [optional] 

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

# **delete_course_file_async**
> delete_course_file_async(tenant_id, file_id, api_version=api_version, x_api_version=x_api_version)

Delete a course file

Deletes a course file for the specified tenant.

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
    api_instance = openapi_client.CourseFilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    file_id = 'file_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course file
        api_instance.delete_course_file_async(tenant_id, file_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseFilesApi->delete_course_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **file_id** | **str**|  | 
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

# **get_course_file_by_id_async**
> CourseFileDto get_course_file_by_id_async(file_id, api_version=api_version, x_api_version=x_api_version)

Get course file by ID

Retrieves a specific course file by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_file_dto import CourseFileDto
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
    api_instance = openapi_client.CourseFilesApi(api_client)
    file_id = 'file_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course file by ID
        api_response = api_instance.get_course_file_by_id_async(file_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseFilesApi->get_course_file_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseFilesApi->get_course_file_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseFileDto**](CourseFileDto.md)

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

# **get_course_files_async**
> List[CourseFileDto] get_course_files_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course files

Retrieves all course files for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_file_dto import CourseFileDto
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
    api_instance = openapi_client.CourseFilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course files
        api_response = api_instance.get_course_files_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseFilesApi->get_course_files_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseFilesApi->get_course_files_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseFileDto]**](CourseFileDto.md)

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

# **get_course_files_count_async**
> int get_course_files_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course files count

Returns the count of course files for the specified tenant.

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
    api_instance = openapi_client.CourseFilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course files count
        api_response = api_instance.get_course_files_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseFilesApi->get_course_files_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseFilesApi->get_course_files_count_async: %s\n" % e)
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

# **update_course_file_async**
> update_course_file_async(tenant_id, file_id, api_version=api_version, x_api_version=x_api_version, course_file_update_dto=course_file_update_dto)

Update a course file

Updates an existing course file for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_file_update_dto import CourseFileUpdateDto
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
    api_instance = openapi_client.CourseFilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    file_id = 'file_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_file_update_dto = openapi_client.CourseFileUpdateDto() # CourseFileUpdateDto |  (optional)

    try:
        # Update a course file
        api_instance.update_course_file_async(tenant_id, file_id, api_version=api_version, x_api_version=x_api_version, course_file_update_dto=course_file_update_dto)
    except Exception as e:
        print("Exception when calling CourseFilesApi->update_course_file_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **file_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_file_update_dto** | [**CourseFileUpdateDto**](CourseFileUpdateDto.md)|  | [optional] 

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

