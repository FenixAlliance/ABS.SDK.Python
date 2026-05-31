# openapi_client.CourseHandoutsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_handout_async**](CourseHandoutsApi.md#create_course_handout_async) | **POST** /api/v2/LearningService/CourseHandouts | Create a course handout
[**delete_course_handout_async**](CourseHandoutsApi.md#delete_course_handout_async) | **DELETE** /api/v2/LearningService/CourseHandouts/{handoutId} | Delete a course handout
[**get_course_handout_by_id_async**](CourseHandoutsApi.md#get_course_handout_by_id_async) | **GET** /api/v2/LearningService/CourseHandouts/{handoutId} | Get course handout by ID
[**get_course_handouts_async**](CourseHandoutsApi.md#get_course_handouts_async) | **GET** /api/v2/LearningService/CourseHandouts | Get all course handouts
[**get_course_handouts_count_async**](CourseHandoutsApi.md#get_course_handouts_count_async) | **GET** /api/v2/LearningService/CourseHandouts/Count | Get course handouts count
[**update_course_handout_async**](CourseHandoutsApi.md#update_course_handout_async) | **PUT** /api/v2/LearningService/CourseHandouts/{handoutId} | Update a course handout


# **create_course_handout_async**
> CourseHandoutDto create_course_handout_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_handout_create_dto=course_handout_create_dto)

Create a course handout

Creates a new course handout for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_handout_create_dto import CourseHandoutCreateDto
from openapi_client.models.course_handout_dto import CourseHandoutDto
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
    api_instance = openapi_client.CourseHandoutsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_handout_create_dto = openapi_client.CourseHandoutCreateDto() # CourseHandoutCreateDto |  (optional)

    try:
        # Create a course handout
        api_response = api_instance.create_course_handout_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_handout_create_dto=course_handout_create_dto)
        print("The response of CourseHandoutsApi->create_course_handout_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseHandoutsApi->create_course_handout_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_handout_create_dto** | [**CourseHandoutCreateDto**](CourseHandoutCreateDto.md)|  | [optional] 

### Return type

[**CourseHandoutDto**](CourseHandoutDto.md)

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

# **delete_course_handout_async**
> delete_course_handout_async(tenant_id, handout_id, api_version=api_version, x_api_version=x_api_version)

Delete a course handout

Deletes a course handout by its ID.

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
    api_instance = openapi_client.CourseHandoutsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    handout_id = 'handout_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course handout
        api_instance.delete_course_handout_async(tenant_id, handout_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseHandoutsApi->delete_course_handout_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **handout_id** | **str**|  | 
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

# **get_course_handout_by_id_async**
> CourseHandoutDto get_course_handout_by_id_async(handout_id, api_version=api_version, x_api_version=x_api_version)

Get course handout by ID

Retrieves a specific course handout by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_handout_dto import CourseHandoutDto
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
    api_instance = openapi_client.CourseHandoutsApi(api_client)
    handout_id = 'handout_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course handout by ID
        api_response = api_instance.get_course_handout_by_id_async(handout_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseHandoutsApi->get_course_handout_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseHandoutsApi->get_course_handout_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handout_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseHandoutDto**](CourseHandoutDto.md)

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

# **get_course_handouts_async**
> List[CourseHandoutDto] get_course_handouts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course handouts

Retrieves all course handouts for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_handout_dto import CourseHandoutDto
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
    api_instance = openapi_client.CourseHandoutsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course handouts
        api_response = api_instance.get_course_handouts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseHandoutsApi->get_course_handouts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseHandoutsApi->get_course_handouts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseHandoutDto]**](CourseHandoutDto.md)

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

# **get_course_handouts_count_async**
> int get_course_handouts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course handouts count

Returns the count of course handouts for the specified tenant.

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
    api_instance = openapi_client.CourseHandoutsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course handouts count
        api_response = api_instance.get_course_handouts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseHandoutsApi->get_course_handouts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseHandoutsApi->get_course_handouts_count_async: %s\n" % e)
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

# **update_course_handout_async**
> CourseHandoutDto update_course_handout_async(tenant_id, handout_id, api_version=api_version, x_api_version=x_api_version, course_handout_update_dto=course_handout_update_dto)

Update a course handout

Updates an existing course handout.

### Example


```python
import openapi_client
from openapi_client.models.course_handout_dto import CourseHandoutDto
from openapi_client.models.course_handout_update_dto import CourseHandoutUpdateDto
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
    api_instance = openapi_client.CourseHandoutsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    handout_id = 'handout_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_handout_update_dto = openapi_client.CourseHandoutUpdateDto() # CourseHandoutUpdateDto |  (optional)

    try:
        # Update a course handout
        api_response = api_instance.update_course_handout_async(tenant_id, handout_id, api_version=api_version, x_api_version=x_api_version, course_handout_update_dto=course_handout_update_dto)
        print("The response of CourseHandoutsApi->update_course_handout_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseHandoutsApi->update_course_handout_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **handout_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_handout_update_dto** | [**CourseHandoutUpdateDto**](CourseHandoutUpdateDto.md)|  | [optional] 

### Return type

[**CourseHandoutDto**](CourseHandoutDto.md)

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

