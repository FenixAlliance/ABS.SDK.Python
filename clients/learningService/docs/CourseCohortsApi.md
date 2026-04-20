# openapi_client.CourseCohortsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_cohort_async**](CourseCohortsApi.md#create_course_cohort_async) | **POST** /api/v2/LearningService/CourseCohorts | Create a new course cohort
[**delete_course_cohort_async**](CourseCohortsApi.md#delete_course_cohort_async) | **DELETE** /api/v2/LearningService/CourseCohorts/{cohortId} | Delete a course cohort
[**get_course_cohort_by_id_async**](CourseCohortsApi.md#get_course_cohort_by_id_async) | **GET** /api/v2/LearningService/CourseCohorts/{cohortId} | Get course cohort by ID
[**get_course_cohorts_async**](CourseCohortsApi.md#get_course_cohorts_async) | **GET** /api/v2/LearningService/CourseCohorts | Get all course cohorts
[**get_course_cohorts_count_async**](CourseCohortsApi.md#get_course_cohorts_count_async) | **GET** /api/v2/LearningService/CourseCohorts/Count | Get course cohorts count
[**update_course_cohort_async**](CourseCohortsApi.md#update_course_cohort_async) | **PUT** /api/v2/LearningService/CourseCohorts/{cohortId} | Update a course cohort


# **create_course_cohort_async**
> create_course_cohort_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_cohort_create_dto=course_cohort_create_dto)

Create a new course cohort

Creates a new course cohort for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_cohort_create_dto import CourseCohortCreateDto
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
    api_instance = openapi_client.CourseCohortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_cohort_create_dto = openapi_client.CourseCohortCreateDto() # CourseCohortCreateDto |  (optional)

    try:
        # Create a new course cohort
        api_instance.create_course_cohort_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_cohort_create_dto=course_cohort_create_dto)
    except Exception as e:
        print("Exception when calling CourseCohortsApi->create_course_cohort_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_cohort_create_dto** | [**CourseCohortCreateDto**](CourseCohortCreateDto.md)|  | [optional] 

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

# **delete_course_cohort_async**
> delete_course_cohort_async(tenant_id, cohort_id, api_version=api_version, x_api_version=x_api_version)

Delete a course cohort

Deletes a course cohort for the specified tenant.

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
    api_instance = openapi_client.CourseCohortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cohort_id = 'cohort_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course cohort
        api_instance.delete_course_cohort_async(tenant_id, cohort_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseCohortsApi->delete_course_cohort_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cohort_id** | **str**|  | 
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

# **get_course_cohort_by_id_async**
> CourseCohortDto get_course_cohort_by_id_async(cohort_id, api_version=api_version, x_api_version=x_api_version)

Get course cohort by ID

Retrieves a specific course cohort by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_cohort_dto import CourseCohortDto
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
    api_instance = openapi_client.CourseCohortsApi(api_client)
    cohort_id = 'cohort_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course cohort by ID
        api_response = api_instance.get_course_cohort_by_id_async(cohort_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCohortsApi->get_course_cohort_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCohortsApi->get_course_cohort_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cohort_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseCohortDto**](CourseCohortDto.md)

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

# **get_course_cohorts_async**
> List[CourseCohortDto] get_course_cohorts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course cohorts

Retrieves all course cohorts for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_cohort_dto import CourseCohortDto
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
    api_instance = openapi_client.CourseCohortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course cohorts
        api_response = api_instance.get_course_cohorts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCohortsApi->get_course_cohorts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCohortsApi->get_course_cohorts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseCohortDto]**](CourseCohortDto.md)

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

# **get_course_cohorts_count_async**
> int get_course_cohorts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course cohorts count

Returns the count of course cohorts for the specified tenant.

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
    api_instance = openapi_client.CourseCohortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course cohorts count
        api_response = api_instance.get_course_cohorts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCohortsApi->get_course_cohorts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCohortsApi->get_course_cohorts_count_async: %s\n" % e)
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

# **update_course_cohort_async**
> update_course_cohort_async(tenant_id, cohort_id, api_version=api_version, x_api_version=x_api_version, course_cohort_update_dto=course_cohort_update_dto)

Update a course cohort

Updates an existing course cohort for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_cohort_update_dto import CourseCohortUpdateDto
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
    api_instance = openapi_client.CourseCohortsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    cohort_id = 'cohort_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_cohort_update_dto = openapi_client.CourseCohortUpdateDto() # CourseCohortUpdateDto |  (optional)

    try:
        # Update a course cohort
        api_instance.update_course_cohort_async(tenant_id, cohort_id, api_version=api_version, x_api_version=x_api_version, course_cohort_update_dto=course_cohort_update_dto)
    except Exception as e:
        print("Exception when calling CourseCohortsApi->update_course_cohort_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **cohort_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_cohort_update_dto** | [**CourseCohortUpdateDto**](CourseCohortUpdateDto.md)|  | [optional] 

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

