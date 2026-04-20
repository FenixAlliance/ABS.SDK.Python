# openapi_client.CourseLibrariesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_library_async**](CourseLibrariesApi.md#create_course_library_async) | **POST** /api/v2/LearningService/CourseLibraries | Create a course library
[**delete_course_library_async**](CourseLibrariesApi.md#delete_course_library_async) | **DELETE** /api/v2/LearningService/CourseLibraries/{libraryId} | Delete a course library
[**get_course_libraries_async**](CourseLibrariesApi.md#get_course_libraries_async) | **GET** /api/v2/LearningService/CourseLibraries | Get all course libraries
[**get_course_libraries_count_async**](CourseLibrariesApi.md#get_course_libraries_count_async) | **GET** /api/v2/LearningService/CourseLibraries/Count | Get course libraries count
[**get_course_library_by_id_async**](CourseLibrariesApi.md#get_course_library_by_id_async) | **GET** /api/v2/LearningService/CourseLibraries/{libraryId} | Get course library by ID
[**update_course_library_async**](CourseLibrariesApi.md#update_course_library_async) | **PUT** /api/v2/LearningService/CourseLibraries/{libraryId} | Update a course library


# **create_course_library_async**
> CourseLibraryDto create_course_library_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_library_create_dto=course_library_create_dto)

Create a course library

Creates a new course library for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_library_create_dto import CourseLibraryCreateDto
from openapi_client.models.course_library_dto import CourseLibraryDto
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
    api_instance = openapi_client.CourseLibrariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_library_create_dto = openapi_client.CourseLibraryCreateDto() # CourseLibraryCreateDto |  (optional)

    try:
        # Create a course library
        api_response = api_instance.create_course_library_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_library_create_dto=course_library_create_dto)
        print("The response of CourseLibrariesApi->create_course_library_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseLibrariesApi->create_course_library_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_library_create_dto** | [**CourseLibraryCreateDto**](CourseLibraryCreateDto.md)|  | [optional] 

### Return type

[**CourseLibraryDto**](CourseLibraryDto.md)

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

# **delete_course_library_async**
> delete_course_library_async(tenant_id, library_id, api_version=api_version, x_api_version=x_api_version)

Delete a course library

Deletes a course library by its ID.

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
    api_instance = openapi_client.CourseLibrariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    library_id = 'library_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course library
        api_instance.delete_course_library_async(tenant_id, library_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseLibrariesApi->delete_course_library_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **library_id** | **str**|  | 
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

# **get_course_libraries_async**
> List[CourseLibraryDto] get_course_libraries_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course libraries

Retrieves all course libraries for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_library_dto import CourseLibraryDto
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
    api_instance = openapi_client.CourseLibrariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course libraries
        api_response = api_instance.get_course_libraries_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseLibrariesApi->get_course_libraries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseLibrariesApi->get_course_libraries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseLibraryDto]**](CourseLibraryDto.md)

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

# **get_course_libraries_count_async**
> int get_course_libraries_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course libraries count

Returns the count of course libraries for the specified tenant.

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
    api_instance = openapi_client.CourseLibrariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course libraries count
        api_response = api_instance.get_course_libraries_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseLibrariesApi->get_course_libraries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseLibrariesApi->get_course_libraries_count_async: %s\n" % e)
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

# **get_course_library_by_id_async**
> CourseLibraryDto get_course_library_by_id_async(library_id, api_version=api_version, x_api_version=x_api_version)

Get course library by ID

Retrieves a specific course library by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_library_dto import CourseLibraryDto
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
    api_instance = openapi_client.CourseLibrariesApi(api_client)
    library_id = 'library_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course library by ID
        api_response = api_instance.get_course_library_by_id_async(library_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseLibrariesApi->get_course_library_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseLibrariesApi->get_course_library_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseLibraryDto**](CourseLibraryDto.md)

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

# **update_course_library_async**
> CourseLibraryDto update_course_library_async(tenant_id, library_id, api_version=api_version, x_api_version=x_api_version, course_library_update_dto=course_library_update_dto)

Update a course library

Updates an existing course library.

### Example


```python
import openapi_client
from openapi_client.models.course_library_dto import CourseLibraryDto
from openapi_client.models.course_library_update_dto import CourseLibraryUpdateDto
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
    api_instance = openapi_client.CourseLibrariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    library_id = 'library_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_library_update_dto = openapi_client.CourseLibraryUpdateDto() # CourseLibraryUpdateDto |  (optional)

    try:
        # Update a course library
        api_response = api_instance.update_course_library_async(tenant_id, library_id, api_version=api_version, x_api_version=x_api_version, course_library_update_dto=course_library_update_dto)
        print("The response of CourseLibrariesApi->update_course_library_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseLibrariesApi->update_course_library_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **library_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_library_update_dto** | [**CourseLibraryUpdateDto**](CourseLibraryUpdateDto.md)|  | [optional] 

### Return type

[**CourseLibraryDto**](CourseLibraryDto.md)

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

