# openapi_client.TrainingProgramCoursesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_training_program_course_async**](TrainingProgramCoursesApi.md#create_training_program_course_async) | **POST** /api/v2/HrmsService/TrainingProgramCourses | Create a training program course
[**delete_training_program_course_async**](TrainingProgramCoursesApi.md#delete_training_program_course_async) | **DELETE** /api/v2/HrmsService/TrainingProgramCourses/{courseId} | Delete a training program course
[**get_training_program_course_by_id_async**](TrainingProgramCoursesApi.md#get_training_program_course_by_id_async) | **GET** /api/v2/HrmsService/TrainingProgramCourses/{courseId} | Get training program course by ID
[**get_training_program_courses_async**](TrainingProgramCoursesApi.md#get_training_program_courses_async) | **GET** /api/v2/HrmsService/TrainingProgramCourses | Get training program courses
[**get_training_program_courses_count_async**](TrainingProgramCoursesApi.md#get_training_program_courses_count_async) | **GET** /api/v2/HrmsService/TrainingProgramCourses/Count | Count training program courses
[**patch_training_program_course_async**](TrainingProgramCoursesApi.md#patch_training_program_course_async) | **PATCH** /api/v2/HrmsService/TrainingProgramCourses/{courseId} | Patch a training program course
[**update_training_program_course_async**](TrainingProgramCoursesApi.md#update_training_program_course_async) | **PUT** /api/v2/HrmsService/TrainingProgramCourses/{courseId} | Update a training program course


# **create_training_program_course_async**
> EmptyEnvelope create_training_program_course_async(tenant_id, api_version=api_version, x_api_version=x_api_version, training_program_course_create_dto=training_program_course_create_dto)

Create a training program course

Creates a new training program course for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.training_program_course_create_dto import TrainingProgramCourseCreateDto
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
    api_instance = openapi_client.TrainingProgramCoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    training_program_course_create_dto = openapi_client.TrainingProgramCourseCreateDto() # TrainingProgramCourseCreateDto |  (optional)

    try:
        # Create a training program course
        api_response = api_instance.create_training_program_course_async(tenant_id, api_version=api_version, x_api_version=x_api_version, training_program_course_create_dto=training_program_course_create_dto)
        print("The response of TrainingProgramCoursesApi->create_training_program_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramCoursesApi->create_training_program_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **training_program_course_create_dto** | [**TrainingProgramCourseCreateDto**](TrainingProgramCourseCreateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training_program_course_async**
> EmptyEnvelope delete_training_program_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)

Delete a training program course

Deletes a training program course for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.TrainingProgramCoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a training program course
        api_response = api_instance.delete_training_program_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramCoursesApi->delete_training_program_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramCoursesApi->delete_training_program_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_program_course_by_id_async**
> TrainingProgramCourseDtoEnvelope get_training_program_course_by_id_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)

Get training program course by ID

Retrieves a specific training program course by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.training_program_course_dto_envelope import TrainingProgramCourseDtoEnvelope
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
    api_instance = openapi_client.TrainingProgramCoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get training program course by ID
        api_response = api_instance.get_training_program_course_by_id_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramCoursesApi->get_training_program_course_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramCoursesApi->get_training_program_course_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TrainingProgramCourseDtoEnvelope**](TrainingProgramCourseDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_program_courses_async**
> TrainingProgramCourseDtoListEnvelope get_training_program_courses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get training program courses

Retrieves training program courses for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.training_program_course_dto_list_envelope import TrainingProgramCourseDtoListEnvelope
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
    api_instance = openapi_client.TrainingProgramCoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get training program courses
        api_response = api_instance.get_training_program_courses_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramCoursesApi->get_training_program_courses_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramCoursesApi->get_training_program_courses_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TrainingProgramCourseDtoListEnvelope**](TrainingProgramCourseDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_program_courses_count_async**
> Int32Envelope get_training_program_courses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count training program courses

Counts training program courses for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.TrainingProgramCoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count training program courses
        api_response = api_instance.get_training_program_courses_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramCoursesApi->get_training_program_courses_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramCoursesApi->get_training_program_courses_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Int32Envelope**](Int32Envelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_training_program_course_async**
> EmptyEnvelope patch_training_program_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a training program course

Partially updates an existing training program course for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.TrainingProgramCoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a training program course
        api_response = api_instance.patch_training_program_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of TrainingProgramCoursesApi->patch_training_program_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramCoursesApi->patch_training_program_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training_program_course_async**
> EmptyEnvelope update_training_program_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version, training_program_course_update_dto=training_program_course_update_dto)

Update a training program course

Updates an existing training program course for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.training_program_course_update_dto import TrainingProgramCourseUpdateDto
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
    api_instance = openapi_client.TrainingProgramCoursesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_id = 'course_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    training_program_course_update_dto = openapi_client.TrainingProgramCourseUpdateDto() # TrainingProgramCourseUpdateDto |  (optional)

    try:
        # Update a training program course
        api_response = api_instance.update_training_program_course_async(tenant_id, course_id, api_version=api_version, x_api_version=x_api_version, training_program_course_update_dto=training_program_course_update_dto)
        print("The response of TrainingProgramCoursesApi->update_training_program_course_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramCoursesApi->update_training_program_course_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **training_program_course_update_dto** | [**TrainingProgramCourseUpdateDto**](TrainingProgramCourseUpdateDto.md)|  | [optional] 

### Return type

[**EmptyEnvelope**](EmptyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

