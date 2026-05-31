# openapi_client.StudentProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_learning_service_student_profiles_count_get**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_count_get) | **GET** /api/v2/LearningService/StudentProfiles/Count | 
[**api_v2_learning_service_student_profiles_get**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_get) | **GET** /api/v2/LearningService/StudentProfiles | 
[**api_v2_learning_service_student_profiles_post**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_post) | **POST** /api/v2/LearningService/StudentProfiles | 
[**api_v2_learning_service_student_profiles_student_profile_id_average_get**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_student_profile_id_average_get) | **GET** /api/v2/LearningService/StudentProfiles/{studentProfileId}/Average | 
[**api_v2_learning_service_student_profiles_student_profile_id_delete**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_student_profile_id_delete) | **DELETE** /api/v2/LearningService/StudentProfiles/{studentProfileId} | 
[**api_v2_learning_service_student_profiles_student_profile_id_get**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_student_profile_id_get) | **GET** /api/v2/LearningService/StudentProfiles/{studentProfileId} | 
[**api_v2_learning_service_student_profiles_student_profile_id_hours_completed_get**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_student_profile_id_hours_completed_get) | **GET** /api/v2/LearningService/StudentProfiles/{studentProfileId}/HoursCompleted | 
[**api_v2_learning_service_student_profiles_student_profile_id_put**](StudentProfilesApi.md#api_v2_learning_service_student_profiles_student_profile_id_put) | **PUT** /api/v2/LearningService/StudentProfiles/{studentProfileId} | 


# **api_v2_learning_service_student_profiles_count_get**
> int api_v2_learning_service_student_profiles_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_student_profiles_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of StudentProfilesApi->api_v2_learning_service_student_profiles_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_count_get: %s\n" % e)
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

# **api_v2_learning_service_student_profiles_get**
> List[StudentProfileDto] api_v2_learning_service_student_profiles_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.student_profile_dto import StudentProfileDto
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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_student_profiles_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of StudentProfilesApi->api_v2_learning_service_student_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[StudentProfileDto]**](StudentProfileDto.md)

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

# **api_v2_learning_service_student_profiles_post**
> api_v2_learning_service_student_profiles_post(tenant_id, api_version=api_version, x_api_version=x_api_version, student_profile_create_dto=student_profile_create_dto)



### Example


```python
import openapi_client
from openapi_client.models.student_profile_create_dto import StudentProfileCreateDto
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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    student_profile_create_dto = openapi_client.StudentProfileCreateDto() # StudentProfileCreateDto |  (optional)

    try:
        api_instance.api_v2_learning_service_student_profiles_post(tenant_id, api_version=api_version, x_api_version=x_api_version, student_profile_create_dto=student_profile_create_dto)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **student_profile_create_dto** | [**StudentProfileCreateDto**](StudentProfileCreateDto.md)|  | [optional] 

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

# **api_v2_learning_service_student_profiles_student_profile_id_average_get**
> AverageDto api_v2_learning_service_student_profiles_student_profile_id_average_get(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.average_dto import AverageDto
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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    student_profile_id = 'student_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_student_profiles_student_profile_id_average_get(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_average_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_average_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **student_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AverageDto**](AverageDto.md)

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

# **api_v2_learning_service_student_profiles_student_profile_id_delete**
> api_v2_learning_service_student_profiles_student_profile_id_delete(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    student_profile_id = 'student_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_instance.api_v2_learning_service_student_profiles_student_profile_id_delete(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **student_profile_id** | **str**|  | 
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

# **api_v2_learning_service_student_profiles_student_profile_id_get**
> StudentProfileDto api_v2_learning_service_student_profiles_student_profile_id_get(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.student_profile_dto import StudentProfileDto
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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    student_profile_id = 'student_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_student_profiles_student_profile_id_get(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **student_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**StudentProfileDto**](StudentProfileDto.md)

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

# **api_v2_learning_service_student_profiles_student_profile_id_hours_completed_get**
> CountDto api_v2_learning_service_student_profiles_student_profile_id_hours_completed_get(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.count_dto import CountDto
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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    student_profile_id = 'student_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_student_profiles_student_profile_id_hours_completed_get(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_hours_completed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_hours_completed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **student_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountDto**](CountDto.md)

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

# **api_v2_learning_service_student_profiles_student_profile_id_put**
> api_v2_learning_service_student_profiles_student_profile_id_put(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version, student_profile_update_dto=student_profile_update_dto)



### Example


```python
import openapi_client
from openapi_client.models.student_profile_update_dto import StudentProfileUpdateDto
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
    api_instance = openapi_client.StudentProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    student_profile_id = 'student_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    student_profile_update_dto = openapi_client.StudentProfileUpdateDto() # StudentProfileUpdateDto |  (optional)

    try:
        api_instance.api_v2_learning_service_student_profiles_student_profile_id_put(tenant_id, student_profile_id, api_version=api_version, x_api_version=x_api_version, student_profile_update_dto=student_profile_update_dto)
    except Exception as e:
        print("Exception when calling StudentProfilesApi->api_v2_learning_service_student_profiles_student_profile_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **student_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **student_profile_update_dto** | [**StudentProfileUpdateDto**](StudentProfileUpdateDto.md)|  | [optional] 

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

