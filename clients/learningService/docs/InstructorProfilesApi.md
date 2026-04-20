# openapi_client.InstructorProfilesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_learning_service_instructor_profiles_count_get**](InstructorProfilesApi.md#api_v2_learning_service_instructor_profiles_count_get) | **GET** /api/v2/LearningService/InstructorProfiles/Count | 
[**api_v2_learning_service_instructor_profiles_get**](InstructorProfilesApi.md#api_v2_learning_service_instructor_profiles_get) | **GET** /api/v2/LearningService/InstructorProfiles | 
[**api_v2_learning_service_instructor_profiles_instructor_profile_id_delete**](InstructorProfilesApi.md#api_v2_learning_service_instructor_profiles_instructor_profile_id_delete) | **DELETE** /api/v2/LearningService/InstructorProfiles/{instructorProfileId} | 
[**api_v2_learning_service_instructor_profiles_instructor_profile_id_get**](InstructorProfilesApi.md#api_v2_learning_service_instructor_profiles_instructor_profile_id_get) | **GET** /api/v2/LearningService/InstructorProfiles/{instructorProfileId} | 
[**api_v2_learning_service_instructor_profiles_instructor_profile_id_put**](InstructorProfilesApi.md#api_v2_learning_service_instructor_profiles_instructor_profile_id_put) | **PUT** /api/v2/LearningService/InstructorProfiles/{instructorProfileId} | 
[**api_v2_learning_service_instructor_profiles_post**](InstructorProfilesApi.md#api_v2_learning_service_instructor_profiles_post) | **POST** /api/v2/LearningService/InstructorProfiles | 


# **api_v2_learning_service_instructor_profiles_count_get**
> int api_v2_learning_service_instructor_profiles_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.InstructorProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_instructor_profiles_count_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InstructorProfilesApi->api_v2_learning_service_instructor_profiles_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstructorProfilesApi->api_v2_learning_service_instructor_profiles_count_get: %s\n" % e)
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

# **api_v2_learning_service_instructor_profiles_get**
> List[InstructorProfileDto] api_v2_learning_service_instructor_profiles_get(tenant_id, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.instructor_profile_dto import InstructorProfileDto
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
    api_instance = openapi_client.InstructorProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_instructor_profiles_get(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InstructorProfilesApi->api_v2_learning_service_instructor_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstructorProfilesApi->api_v2_learning_service_instructor_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[InstructorProfileDto]**](InstructorProfileDto.md)

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

# **api_v2_learning_service_instructor_profiles_instructor_profile_id_delete**
> api_v2_learning_service_instructor_profiles_instructor_profile_id_delete(tenant_id, instructor_profile_id, api_version=api_version, x_api_version=x_api_version)



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
    api_instance = openapi_client.InstructorProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    instructor_profile_id = 'instructor_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_instance.api_v2_learning_service_instructor_profiles_instructor_profile_id_delete(tenant_id, instructor_profile_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling InstructorProfilesApi->api_v2_learning_service_instructor_profiles_instructor_profile_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **instructor_profile_id** | **str**|  | 
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

# **api_v2_learning_service_instructor_profiles_instructor_profile_id_get**
> InstructorProfileDto api_v2_learning_service_instructor_profiles_instructor_profile_id_get(tenant_id, instructor_profile_id, api_version=api_version, x_api_version=x_api_version)



### Example


```python
import openapi_client
from openapi_client.models.instructor_profile_dto import InstructorProfileDto
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
    api_instance = openapi_client.InstructorProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    instructor_profile_id = 'instructor_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_learning_service_instructor_profiles_instructor_profile_id_get(tenant_id, instructor_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of InstructorProfilesApi->api_v2_learning_service_instructor_profiles_instructor_profile_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstructorProfilesApi->api_v2_learning_service_instructor_profiles_instructor_profile_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **instructor_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InstructorProfileDto**](InstructorProfileDto.md)

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

# **api_v2_learning_service_instructor_profiles_instructor_profile_id_put**
> api_v2_learning_service_instructor_profiles_instructor_profile_id_put(tenant_id, instructor_profile_id, api_version=api_version, x_api_version=x_api_version, instructor_profile_update_dto=instructor_profile_update_dto)



### Example


```python
import openapi_client
from openapi_client.models.instructor_profile_update_dto import InstructorProfileUpdateDto
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
    api_instance = openapi_client.InstructorProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    instructor_profile_id = 'instructor_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    instructor_profile_update_dto = openapi_client.InstructorProfileUpdateDto() # InstructorProfileUpdateDto |  (optional)

    try:
        api_instance.api_v2_learning_service_instructor_profiles_instructor_profile_id_put(tenant_id, instructor_profile_id, api_version=api_version, x_api_version=x_api_version, instructor_profile_update_dto=instructor_profile_update_dto)
    except Exception as e:
        print("Exception when calling InstructorProfilesApi->api_v2_learning_service_instructor_profiles_instructor_profile_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **instructor_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **instructor_profile_update_dto** | [**InstructorProfileUpdateDto**](InstructorProfileUpdateDto.md)|  | [optional] 

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

# **api_v2_learning_service_instructor_profiles_post**
> api_v2_learning_service_instructor_profiles_post(tenant_id, api_version=api_version, x_api_version=x_api_version, instructor_profile_create_dto=instructor_profile_create_dto)



### Example


```python
import openapi_client
from openapi_client.models.instructor_profile_create_dto import InstructorProfileCreateDto
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
    api_instance = openapi_client.InstructorProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    instructor_profile_create_dto = openapi_client.InstructorProfileCreateDto() # InstructorProfileCreateDto |  (optional)

    try:
        api_instance.api_v2_learning_service_instructor_profiles_post(tenant_id, api_version=api_version, x_api_version=x_api_version, instructor_profile_create_dto=instructor_profile_create_dto)
    except Exception as e:
        print("Exception when calling InstructorProfilesApi->api_v2_learning_service_instructor_profiles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **instructor_profile_create_dto** | [**InstructorProfileCreateDto**](InstructorProfileCreateDto.md)|  | [optional] 

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

