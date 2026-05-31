# openapi_client.CourseUnitComponentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_unit_component_async**](CourseUnitComponentsApi.md#create_course_unit_component_async) | **POST** /api/v2/LearningService/CourseUnitComponents | Create a new course unit component
[**delete_course_unit_component_async**](CourseUnitComponentsApi.md#delete_course_unit_component_async) | **DELETE** /api/v2/LearningService/CourseUnitComponents/{componentId} | Delete a course unit component
[**get_course_unit_component_by_id_async**](CourseUnitComponentsApi.md#get_course_unit_component_by_id_async) | **GET** /api/v2/LearningService/CourseUnitComponents/{componentId} | Get course unit component by ID
[**get_course_unit_components_async**](CourseUnitComponentsApi.md#get_course_unit_components_async) | **GET** /api/v2/LearningService/CourseUnitComponents | Get all course unit components
[**get_course_unit_components_count_async**](CourseUnitComponentsApi.md#get_course_unit_components_count_async) | **GET** /api/v2/LearningService/CourseUnitComponents/Count | Get course unit components count
[**update_course_unit_component_async**](CourseUnitComponentsApi.md#update_course_unit_component_async) | **PUT** /api/v2/LearningService/CourseUnitComponents/{componentId} | Update a course unit component


# **create_course_unit_component_async**
> create_course_unit_component_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_unit_component_create_dto=course_unit_component_create_dto)

Create a new course unit component

Creates a new course unit component for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_component_create_dto import CourseUnitComponentCreateDto
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
    api_instance = openapi_client.CourseUnitComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_unit_component_create_dto = openapi_client.CourseUnitComponentCreateDto() # CourseUnitComponentCreateDto |  (optional)

    try:
        # Create a new course unit component
        api_instance.create_course_unit_component_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_unit_component_create_dto=course_unit_component_create_dto)
    except Exception as e:
        print("Exception when calling CourseUnitComponentsApi->create_course_unit_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_unit_component_create_dto** | [**CourseUnitComponentCreateDto**](CourseUnitComponentCreateDto.md)|  | [optional] 

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

# **delete_course_unit_component_async**
> delete_course_unit_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version)

Delete a course unit component

Deletes a course unit component for the specified tenant.

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
    api_instance = openapi_client.CourseUnitComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    component_id = 'component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course unit component
        api_instance.delete_course_unit_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseUnitComponentsApi->delete_course_unit_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **component_id** | **str**|  | 
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

# **get_course_unit_component_by_id_async**
> CourseUnitComponentDto get_course_unit_component_by_id_async(component_id, api_version=api_version, x_api_version=x_api_version)

Get course unit component by ID

Retrieves a specific course unit component by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_component_dto import CourseUnitComponentDto
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
    api_instance = openapi_client.CourseUnitComponentsApi(api_client)
    component_id = 'component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course unit component by ID
        api_response = api_instance.get_course_unit_component_by_id_async(component_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUnitComponentsApi->get_course_unit_component_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUnitComponentsApi->get_course_unit_component_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseUnitComponentDto**](CourseUnitComponentDto.md)

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

# **get_course_unit_components_async**
> List[CourseUnitComponentDto] get_course_unit_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course unit components

Retrieves all course unit components for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_component_dto import CourseUnitComponentDto
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
    api_instance = openapi_client.CourseUnitComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course unit components
        api_response = api_instance.get_course_unit_components_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUnitComponentsApi->get_course_unit_components_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUnitComponentsApi->get_course_unit_components_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseUnitComponentDto]**](CourseUnitComponentDto.md)

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

# **get_course_unit_components_count_async**
> int get_course_unit_components_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course unit components count

Returns the count of course unit components for the specified tenant.

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
    api_instance = openapi_client.CourseUnitComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course unit components count
        api_response = api_instance.get_course_unit_components_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUnitComponentsApi->get_course_unit_components_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUnitComponentsApi->get_course_unit_components_count_async: %s\n" % e)
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

# **update_course_unit_component_async**
> update_course_unit_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version, course_unit_component_update_dto=course_unit_component_update_dto)

Update a course unit component

Updates an existing course unit component for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_component_update_dto import CourseUnitComponentUpdateDto
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
    api_instance = openapi_client.CourseUnitComponentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    component_id = 'component_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_unit_component_update_dto = openapi_client.CourseUnitComponentUpdateDto() # CourseUnitComponentUpdateDto |  (optional)

    try:
        # Update a course unit component
        api_instance.update_course_unit_component_async(tenant_id, component_id, api_version=api_version, x_api_version=x_api_version, course_unit_component_update_dto=course_unit_component_update_dto)
    except Exception as e:
        print("Exception when calling CourseUnitComponentsApi->update_course_unit_component_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **component_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_unit_component_update_dto** | [**CourseUnitComponentUpdateDto**](CourseUnitComponentUpdateDto.md)|  | [optional] 

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

