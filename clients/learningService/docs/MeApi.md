# openapi_client.MeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_average_score_async**](MeApi.md#get_my_average_score_async) | **GET** /api/v2/LearningService/Me/AverageScore | Get current user&#39;s average score
[**get_my_certificates_async**](MeApi.md#get_my_certificates_async) | **GET** /api/v2/LearningService/Me/Certificates | Get current user&#39;s completion certificates
[**get_my_certificates_count_async**](MeApi.md#get_my_certificates_count_async) | **GET** /api/v2/LearningService/Me/Certificates/Count | Get current user&#39;s certificates count
[**get_my_enrollments_async**](MeApi.md#get_my_enrollments_async) | **GET** /api/v2/LearningService/Me/Enrollments | Get current user&#39;s course enrollments
[**get_my_enrollments_count_async**](MeApi.md#get_my_enrollments_count_async) | **GET** /api/v2/LearningService/Me/Enrollments/Count | Get current user&#39;s enrollment count
[**get_my_hours_completed_async**](MeApi.md#get_my_hours_completed_async) | **GET** /api/v2/LearningService/Me/HoursCompleted | Get current user&#39;s completed hours
[**get_my_instructor_courses_async**](MeApi.md#get_my_instructor_courses_async) | **GET** /api/v2/LearningService/Me/InstructorCourses | Get current user&#39;s instructor courses
[**get_my_instructor_courses_count_async**](MeApi.md#get_my_instructor_courses_count_async) | **GET** /api/v2/LearningService/Me/InstructorCourses/Count | Get current user&#39;s instructor courses count
[**get_my_instructor_profiles_async**](MeApi.md#get_my_instructor_profiles_async) | **GET** /api/v2/LearningService/Me/InstructorProfiles | Get current user&#39;s instructor profiles
[**get_my_instructor_profiles_count_async**](MeApi.md#get_my_instructor_profiles_count_async) | **GET** /api/v2/LearningService/Me/InstructorProfiles/Count | Get current user&#39;s instructor profiles count
[**get_my_pending_task_count_async**](MeApi.md#get_my_pending_task_count_async) | **GET** /api/v2/LearningService/Me/PendingTasks | Get current user&#39;s pending task count
[**get_my_student_courses_async**](MeApi.md#get_my_student_courses_async) | **GET** /api/v2/LearningService/Me/Courses | Get current user&#39;s enrolled courses
[**get_my_student_courses_count_async**](MeApi.md#get_my_student_courses_count_async) | **GET** /api/v2/LearningService/Me/Courses/Count | Get current user&#39;s enrolled courses count
[**get_my_student_profiles_async**](MeApi.md#get_my_student_profiles_async) | **GET** /api/v2/LearningService/Me/StudentProfiles | Get current user&#39;s student profiles
[**get_my_student_profiles_count_async**](MeApi.md#get_my_student_profiles_count_async) | **GET** /api/v2/LearningService/Me/StudentProfiles/Count | Get current user&#39;s student profiles count


# **get_my_average_score_async**
> AverageDtoEnvelope get_my_average_score_async(api_version=api_version, x_api_version=x_api_version)

Get current user's average score

### Example


```python
import openapi_client
from openapi_client.models.average_dto_envelope import AverageDtoEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's average score
        api_response = api_instance.get_my_average_score_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_average_score_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_average_score_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AverageDtoEnvelope**](AverageDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_certificates_async**
> CourseCompletionCertificateDtoIReadOnlyListEnvelope get_my_certificates_async(api_version=api_version, x_api_version=x_api_version)

Get current user's completion certificates

### Example


```python
import openapi_client
from openapi_client.models.course_completion_certificate_dto_i_read_only_list_envelope import CourseCompletionCertificateDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's completion certificates
        api_response = api_instance.get_my_certificates_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_certificates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_certificates_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseCompletionCertificateDtoIReadOnlyListEnvelope**](CourseCompletionCertificateDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_certificates_count_async**
> int get_my_certificates_count_async(api_version=api_version, x_api_version=x_api_version)

Get current user's certificates count

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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's certificates count
        api_response = api_instance.get_my_certificates_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_certificates_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_certificates_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_enrollments_async**
> CourseEnrollmentDtoIReadOnlyListEnvelope get_my_enrollments_async(api_version=api_version, x_api_version=x_api_version)

Get current user's course enrollments

### Example


```python
import openapi_client
from openapi_client.models.course_enrollment_dto_i_read_only_list_envelope import CourseEnrollmentDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's course enrollments
        api_response = api_instance.get_my_enrollments_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_enrollments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_enrollments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseEnrollmentDtoIReadOnlyListEnvelope**](CourseEnrollmentDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_enrollments_count_async**
> int get_my_enrollments_count_async(api_version=api_version, x_api_version=x_api_version)

Get current user's enrollment count

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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's enrollment count
        api_response = api_instance.get_my_enrollments_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_enrollments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_enrollments_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_hours_completed_async**
> CountDtoEnvelope get_my_hours_completed_async(api_version=api_version, x_api_version=x_api_version)

Get current user's completed hours

### Example


```python
import openapi_client
from openapi_client.models.count_dto_envelope import CountDtoEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's completed hours
        api_response = api_instance.get_my_hours_completed_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_hours_completed_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_hours_completed_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountDtoEnvelope**](CountDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_instructor_courses_async**
> CourseDtoIReadOnlyListEnvelope get_my_instructor_courses_async(api_version=api_version, x_api_version=x_api_version)

Get current user's instructor courses

### Example


```python
import openapi_client
from openapi_client.models.course_dto_i_read_only_list_envelope import CourseDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's instructor courses
        api_response = api_instance.get_my_instructor_courses_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_instructor_courses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_instructor_courses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseDtoIReadOnlyListEnvelope**](CourseDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_instructor_courses_count_async**
> int get_my_instructor_courses_count_async(api_version=api_version, x_api_version=x_api_version)

Get current user's instructor courses count

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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's instructor courses count
        api_response = api_instance.get_my_instructor_courses_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_instructor_courses_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_instructor_courses_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_instructor_profiles_async**
> InstructorProfileDtoIReadOnlyListEnvelope get_my_instructor_profiles_async(api_version=api_version, x_api_version=x_api_version)

Get current user's instructor profiles

### Example


```python
import openapi_client
from openapi_client.models.instructor_profile_dto_i_read_only_list_envelope import InstructorProfileDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's instructor profiles
        api_response = api_instance.get_my_instructor_profiles_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_instructor_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_instructor_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InstructorProfileDtoIReadOnlyListEnvelope**](InstructorProfileDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_instructor_profiles_count_async**
> int get_my_instructor_profiles_count_async(api_version=api_version, x_api_version=x_api_version)

Get current user's instructor profiles count

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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's instructor profiles count
        api_response = api_instance.get_my_instructor_profiles_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_instructor_profiles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_instructor_profiles_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_pending_task_count_async**
> CountDtoEnvelope get_my_pending_task_count_async(api_version=api_version, x_api_version=x_api_version)

Get current user's pending task count

### Example


```python
import openapi_client
from openapi_client.models.count_dto_envelope import CountDtoEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's pending task count
        api_response = api_instance.get_my_pending_task_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_pending_task_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_pending_task_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountDtoEnvelope**](CountDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_student_courses_async**
> CourseDtoIReadOnlyListEnvelope get_my_student_courses_async(api_version=api_version, x_api_version=x_api_version)

Get current user's enrolled courses

### Example


```python
import openapi_client
from openapi_client.models.course_dto_i_read_only_list_envelope import CourseDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's enrolled courses
        api_response = api_instance.get_my_student_courses_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_student_courses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_student_courses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseDtoIReadOnlyListEnvelope**](CourseDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_student_courses_count_async**
> int get_my_student_courses_count_async(api_version=api_version, x_api_version=x_api_version)

Get current user's enrolled courses count

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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's enrolled courses count
        api_response = api_instance.get_my_student_courses_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_student_courses_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_student_courses_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_student_profiles_async**
> StudentProfileDtoIReadOnlyListEnvelope get_my_student_profiles_async(api_version=api_version, x_api_version=x_api_version)

Get current user's student profiles

### Example


```python
import openapi_client
from openapi_client.models.student_profile_dto_i_read_only_list_envelope import StudentProfileDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's student profiles
        api_response = api_instance.get_my_student_profiles_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_student_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_student_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**StudentProfileDtoIReadOnlyListEnvelope**](StudentProfileDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_student_profiles_count_async**
> int get_my_student_profiles_count_async(api_version=api_version, x_api_version=x_api_version)

Get current user's student profiles count

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
    api_instance = openapi_client.MeApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get current user's student profiles count
        api_response = api_instance.get_my_student_profiles_count_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of MeApi->get_my_student_profiles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_my_student_profiles_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

