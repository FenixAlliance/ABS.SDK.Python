# openapi_client.CourseProblemSetsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_problem_set_async**](CourseProblemSetsApi.md#create_course_problem_set_async) | **POST** /api/v2/LearningService/CourseProblemSets | Create a new course problem set
[**delete_course_problem_set_async**](CourseProblemSetsApi.md#delete_course_problem_set_async) | **DELETE** /api/v2/LearningService/CourseProblemSets/{problemSetId} | Delete a course problem set
[**get_course_problem_set_by_id_async**](CourseProblemSetsApi.md#get_course_problem_set_by_id_async) | **GET** /api/v2/LearningService/CourseProblemSets/{problemSetId} | Get course problem set by ID
[**get_course_problem_sets_async**](CourseProblemSetsApi.md#get_course_problem_sets_async) | **GET** /api/v2/LearningService/CourseProblemSets | Get all course problem sets
[**get_course_problem_sets_count_async**](CourseProblemSetsApi.md#get_course_problem_sets_count_async) | **GET** /api/v2/LearningService/CourseProblemSets/Count | Get course problem sets count
[**update_course_problem_set_async**](CourseProblemSetsApi.md#update_course_problem_set_async) | **PUT** /api/v2/LearningService/CourseProblemSets/{problemSetId} | Update a course problem set


# **create_course_problem_set_async**
> create_course_problem_set_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_problem_set_create_dto=course_problem_set_create_dto)

Create a new course problem set

Creates a new course problem set for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_problem_set_create_dto import CourseProblemSetCreateDto
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
    api_instance = openapi_client.CourseProblemSetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_problem_set_create_dto = openapi_client.CourseProblemSetCreateDto() # CourseProblemSetCreateDto |  (optional)

    try:
        # Create a new course problem set
        api_instance.create_course_problem_set_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_problem_set_create_dto=course_problem_set_create_dto)
    except Exception as e:
        print("Exception when calling CourseProblemSetsApi->create_course_problem_set_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_problem_set_create_dto** | [**CourseProblemSetCreateDto**](CourseProblemSetCreateDto.md)|  | [optional] 

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

# **delete_course_problem_set_async**
> delete_course_problem_set_async(tenant_id, problem_set_id, api_version=api_version, x_api_version=x_api_version)

Delete a course problem set

Deletes a course problem set for the specified tenant.

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
    api_instance = openapi_client.CourseProblemSetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    problem_set_id = 'problem_set_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course problem set
        api_instance.delete_course_problem_set_async(tenant_id, problem_set_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseProblemSetsApi->delete_course_problem_set_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **problem_set_id** | **str**|  | 
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

# **get_course_problem_set_by_id_async**
> CourseProblemSetDto get_course_problem_set_by_id_async(problem_set_id, api_version=api_version, x_api_version=x_api_version)

Get course problem set by ID

Retrieves a specific course problem set by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_problem_set_dto import CourseProblemSetDto
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
    api_instance = openapi_client.CourseProblemSetsApi(api_client)
    problem_set_id = 'problem_set_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course problem set by ID
        api_response = api_instance.get_course_problem_set_by_id_async(problem_set_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseProblemSetsApi->get_course_problem_set_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseProblemSetsApi->get_course_problem_set_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_set_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseProblemSetDto**](CourseProblemSetDto.md)

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

# **get_course_problem_sets_async**
> List[CourseProblemSetDto] get_course_problem_sets_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course problem sets

Retrieves all course problem sets for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_problem_set_dto import CourseProblemSetDto
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
    api_instance = openapi_client.CourseProblemSetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course problem sets
        api_response = api_instance.get_course_problem_sets_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseProblemSetsApi->get_course_problem_sets_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseProblemSetsApi->get_course_problem_sets_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseProblemSetDto]**](CourseProblemSetDto.md)

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

# **get_course_problem_sets_count_async**
> int get_course_problem_sets_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course problem sets count

Returns the count of course problem sets for the specified tenant.

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
    api_instance = openapi_client.CourseProblemSetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course problem sets count
        api_response = api_instance.get_course_problem_sets_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseProblemSetsApi->get_course_problem_sets_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseProblemSetsApi->get_course_problem_sets_count_async: %s\n" % e)
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

# **update_course_problem_set_async**
> update_course_problem_set_async(tenant_id, problem_set_id, api_version=api_version, x_api_version=x_api_version, course_problem_set_update_dto=course_problem_set_update_dto)

Update a course problem set

Updates an existing course problem set for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_problem_set_update_dto import CourseProblemSetUpdateDto
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
    api_instance = openapi_client.CourseProblemSetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    problem_set_id = 'problem_set_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_problem_set_update_dto = openapi_client.CourseProblemSetUpdateDto() # CourseProblemSetUpdateDto |  (optional)

    try:
        # Update a course problem set
        api_instance.update_course_problem_set_async(tenant_id, problem_set_id, api_version=api_version, x_api_version=x_api_version, course_problem_set_update_dto=course_problem_set_update_dto)
    except Exception as e:
        print("Exception when calling CourseProblemSetsApi->update_course_problem_set_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **problem_set_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_problem_set_update_dto** | [**CourseProblemSetUpdateDto**](CourseProblemSetUpdateDto.md)|  | [optional] 

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

