# openapi_client.CourseGradingRubricsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_grading_rubric_async**](CourseGradingRubricsApi.md#create_course_grading_rubric_async) | **POST** /api/v2/LearningService/CourseGradingRubrics | Create a course grading rubric
[**delete_course_grading_rubric_async**](CourseGradingRubricsApi.md#delete_course_grading_rubric_async) | **DELETE** /api/v2/LearningService/CourseGradingRubrics/{rubricId} | Delete a course grading rubric
[**get_course_grading_rubric_by_id_async**](CourseGradingRubricsApi.md#get_course_grading_rubric_by_id_async) | **GET** /api/v2/LearningService/CourseGradingRubrics/{rubricId} | Get course grading rubric by ID
[**get_course_grading_rubrics_async**](CourseGradingRubricsApi.md#get_course_grading_rubrics_async) | **GET** /api/v2/LearningService/CourseGradingRubrics | Get all course grading rubrics
[**get_course_grading_rubrics_count_async**](CourseGradingRubricsApi.md#get_course_grading_rubrics_count_async) | **GET** /api/v2/LearningService/CourseGradingRubrics/Count | Get course grading rubrics count
[**update_course_grading_rubric_async**](CourseGradingRubricsApi.md#update_course_grading_rubric_async) | **PUT** /api/v2/LearningService/CourseGradingRubrics/{rubricId} | Update a course grading rubric


# **create_course_grading_rubric_async**
> create_course_grading_rubric_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_grading_rubric_create_dto=course_grading_rubric_create_dto)

Create a course grading rubric

Creates a new course grading rubric for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_grading_rubric_create_dto import CourseGradingRubricCreateDto
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
    api_instance = openapi_client.CourseGradingRubricsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_grading_rubric_create_dto = openapi_client.CourseGradingRubricCreateDto() # CourseGradingRubricCreateDto |  (optional)

    try:
        # Create a course grading rubric
        api_instance.create_course_grading_rubric_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_grading_rubric_create_dto=course_grading_rubric_create_dto)
    except Exception as e:
        print("Exception when calling CourseGradingRubricsApi->create_course_grading_rubric_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_grading_rubric_create_dto** | [**CourseGradingRubricCreateDto**](CourseGradingRubricCreateDto.md)|  | [optional] 

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

# **delete_course_grading_rubric_async**
> delete_course_grading_rubric_async(tenant_id, rubric_id, api_version=api_version, x_api_version=x_api_version)

Delete a course grading rubric

Deletes a course grading rubric by its ID.

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
    api_instance = openapi_client.CourseGradingRubricsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    rubric_id = 'rubric_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course grading rubric
        api_instance.delete_course_grading_rubric_async(tenant_id, rubric_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseGradingRubricsApi->delete_course_grading_rubric_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **rubric_id** | **str**|  | 
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

# **get_course_grading_rubric_by_id_async**
> CourseGradingRubricDto get_course_grading_rubric_by_id_async(rubric_id, api_version=api_version, x_api_version=x_api_version)

Get course grading rubric by ID

Retrieves a specific course grading rubric by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_grading_rubric_dto import CourseGradingRubricDto
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
    api_instance = openapi_client.CourseGradingRubricsApi(api_client)
    rubric_id = 'rubric_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course grading rubric by ID
        api_response = api_instance.get_course_grading_rubric_by_id_async(rubric_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseGradingRubricsApi->get_course_grading_rubric_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseGradingRubricsApi->get_course_grading_rubric_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rubric_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseGradingRubricDto**](CourseGradingRubricDto.md)

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

# **get_course_grading_rubrics_async**
> List[CourseGradingRubricDto] get_course_grading_rubrics_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course grading rubrics

Retrieves all course grading rubrics for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_grading_rubric_dto import CourseGradingRubricDto
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
    api_instance = openapi_client.CourseGradingRubricsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course grading rubrics
        api_response = api_instance.get_course_grading_rubrics_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseGradingRubricsApi->get_course_grading_rubrics_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseGradingRubricsApi->get_course_grading_rubrics_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseGradingRubricDto]**](CourseGradingRubricDto.md)

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

# **get_course_grading_rubrics_count_async**
> int get_course_grading_rubrics_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course grading rubrics count

Returns the count of course grading rubrics for the specified tenant.

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
    api_instance = openapi_client.CourseGradingRubricsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course grading rubrics count
        api_response = api_instance.get_course_grading_rubrics_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseGradingRubricsApi->get_course_grading_rubrics_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseGradingRubricsApi->get_course_grading_rubrics_count_async: %s\n" % e)
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

# **update_course_grading_rubric_async**
> update_course_grading_rubric_async(tenant_id, rubric_id, api_version=api_version, x_api_version=x_api_version, course_grading_rubric_update_dto=course_grading_rubric_update_dto)

Update a course grading rubric

Updates an existing course grading rubric.

### Example


```python
import openapi_client
from openapi_client.models.course_grading_rubric_update_dto import CourseGradingRubricUpdateDto
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
    api_instance = openapi_client.CourseGradingRubricsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    rubric_id = 'rubric_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_grading_rubric_update_dto = openapi_client.CourseGradingRubricUpdateDto() # CourseGradingRubricUpdateDto |  (optional)

    try:
        # Update a course grading rubric
        api_instance.update_course_grading_rubric_async(tenant_id, rubric_id, api_version=api_version, x_api_version=x_api_version, course_grading_rubric_update_dto=course_grading_rubric_update_dto)
    except Exception as e:
        print("Exception when calling CourseGradingRubricsApi->update_course_grading_rubric_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **rubric_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_grading_rubric_update_dto** | [**CourseGradingRubricUpdateDto**](CourseGradingRubricUpdateDto.md)|  | [optional] 

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

