# openapi_client.CourseEnrollmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_enrollment_async**](CourseEnrollmentsApi.md#create_course_enrollment_async) | **POST** /api/v2/LearningService/CourseEnrollments | Create a new course enrollment
[**delete_course_enrollment_async**](CourseEnrollmentsApi.md#delete_course_enrollment_async) | **DELETE** /api/v2/LearningService/CourseEnrollments/{courseEnrollmentId} | Delete a course enrollment
[**get_course_enrollment_async**](CourseEnrollmentsApi.md#get_course_enrollment_async) | **GET** /api/v2/LearningService/CourseEnrollments/{courseEnrollmentId} | Get course enrollment by ID
[**get_enrollments_async**](CourseEnrollmentsApi.md#get_enrollments_async) | **GET** /api/v2/LearningService/CourseEnrollments | Get all course enrollments
[**get_enrollments_count_async**](CourseEnrollmentsApi.md#get_enrollments_count_async) | **GET** /api/v2/LearningService/CourseEnrollments/Count | Get course enrollments count
[**get_student_course_enrollments_async**](CourseEnrollmentsApi.md#get_student_course_enrollments_async) | **GET** /api/v2/LearningService/CourseEnrollments/Student/{studentProfileId} | Get enrollments by student
[**update_course_enrollment_async**](CourseEnrollmentsApi.md#update_course_enrollment_async) | **PUT** /api/v2/LearningService/CourseEnrollments/{courseEnrollmentId} | Update a course enrollment


# **create_course_enrollment_async**
> create_course_enrollment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_enrollment_create_dto=course_enrollment_create_dto)

Create a new course enrollment

Creates a new course enrollment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_enrollment_create_dto import CourseEnrollmentCreateDto
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
    api_instance = openapi_client.CourseEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_enrollment_create_dto = openapi_client.CourseEnrollmentCreateDto() # CourseEnrollmentCreateDto |  (optional)

    try:
        # Create a new course enrollment
        api_instance.create_course_enrollment_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_enrollment_create_dto=course_enrollment_create_dto)
    except Exception as e:
        print("Exception when calling CourseEnrollmentsApi->create_course_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_enrollment_create_dto** | [**CourseEnrollmentCreateDto**](CourseEnrollmentCreateDto.md)|  | [optional] 

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

# **delete_course_enrollment_async**
> delete_course_enrollment_async(tenant_id, course_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Delete a course enrollment

Deletes a course enrollment for the specified tenant.

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
    api_instance = openapi_client.CourseEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_enrollment_id = 'course_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course enrollment
        api_instance.delete_course_enrollment_async(tenant_id, course_enrollment_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseEnrollmentsApi->delete_course_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_enrollment_id** | **str**|  | 
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

# **get_course_enrollment_async**
> CourseEnrollmentDto get_course_enrollment_async(tenant_id, course_enrollment_id, api_version=api_version, x_api_version=x_api_version)

Get course enrollment by ID

Retrieves a specific course enrollment by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_enrollment_dto import CourseEnrollmentDto
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
    api_instance = openapi_client.CourseEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_enrollment_id = 'course_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course enrollment by ID
        api_response = api_instance.get_course_enrollment_async(tenant_id, course_enrollment_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseEnrollmentsApi->get_course_enrollment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseEnrollmentsApi->get_course_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseEnrollmentDto**](CourseEnrollmentDto.md)

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

# **get_enrollments_async**
> List[CourseEnrollmentDto] get_enrollments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course enrollments

Retrieves all course enrollments for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_enrollment_dto import CourseEnrollmentDto
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
    api_instance = openapi_client.CourseEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course enrollments
        api_response = api_instance.get_enrollments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseEnrollmentsApi->get_enrollments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseEnrollmentsApi->get_enrollments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseEnrollmentDto]**](CourseEnrollmentDto.md)

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

# **get_enrollments_count_async**
> int get_enrollments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course enrollments count

Returns the count of course enrollments for the specified tenant.

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
    api_instance = openapi_client.CourseEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course enrollments count
        api_response = api_instance.get_enrollments_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseEnrollmentsApi->get_enrollments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseEnrollmentsApi->get_enrollments_count_async: %s\n" % e)
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

# **get_student_course_enrollments_async**
> List[CourseEnrollmentDto] get_student_course_enrollments_async(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)

Get enrollments by student

Retrieves all enrollments for a specific student.

### Example


```python
import openapi_client
from openapi_client.models.course_enrollment_dto import CourseEnrollmentDto
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
    api_instance = openapi_client.CourseEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    student_profile_id = 'student_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get enrollments by student
        api_response = api_instance.get_student_course_enrollments_async(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseEnrollmentsApi->get_student_course_enrollments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseEnrollmentsApi->get_student_course_enrollments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **student_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseEnrollmentDto]**](CourseEnrollmentDto.md)

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

# **update_course_enrollment_async**
> update_course_enrollment_async(tenant_id, course_enrollment_id, api_version=api_version, x_api_version=x_api_version, course_enrollment_update_dto=course_enrollment_update_dto)

Update a course enrollment

Updates an existing course enrollment for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_enrollment_update_dto import CourseEnrollmentUpdateDto
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
    api_instance = openapi_client.CourseEnrollmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_enrollment_id = 'course_enrollment_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_enrollment_update_dto = openapi_client.CourseEnrollmentUpdateDto() # CourseEnrollmentUpdateDto |  (optional)

    try:
        # Update a course enrollment
        api_instance.update_course_enrollment_async(tenant_id, course_enrollment_id, api_version=api_version, x_api_version=x_api_version, course_enrollment_update_dto=course_enrollment_update_dto)
    except Exception as e:
        print("Exception when calling CourseEnrollmentsApi->update_course_enrollment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_enrollment_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_enrollment_update_dto** | [**CourseEnrollmentUpdateDto**](CourseEnrollmentUpdateDto.md)|  | [optional] 

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

