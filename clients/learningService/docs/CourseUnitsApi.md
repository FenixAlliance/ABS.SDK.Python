# openapi_client.CourseUnitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_unit_async**](CourseUnitsApi.md#create_course_unit_async) | **POST** /api/v2/LearningService/CourseUnits | Create a new course unit
[**delete_course_unit_async**](CourseUnitsApi.md#delete_course_unit_async) | **DELETE** /api/v2/LearningService/CourseUnits/{unitId} | Delete a course unit
[**get_course_unit_by_id_async**](CourseUnitsApi.md#get_course_unit_by_id_async) | **GET** /api/v2/LearningService/CourseUnits/{unitId} | Get course unit by ID
[**get_course_units_async**](CourseUnitsApi.md#get_course_units_async) | **GET** /api/v2/LearningService/CourseUnits | Get all course units
[**get_course_units_count_async**](CourseUnitsApi.md#get_course_units_count_async) | **GET** /api/v2/LearningService/CourseUnits/Count | Get course units count
[**update_course_unit_async**](CourseUnitsApi.md#update_course_unit_async) | **PUT** /api/v2/LearningService/CourseUnits/{unitId} | Update a course unit


# **create_course_unit_async**
> create_course_unit_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_unit_create_dto=course_unit_create_dto)

Create a new course unit

Creates a new course unit for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_create_dto import CourseUnitCreateDto
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
    api_instance = openapi_client.CourseUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_unit_create_dto = openapi_client.CourseUnitCreateDto() # CourseUnitCreateDto |  (optional)

    try:
        # Create a new course unit
        api_instance.create_course_unit_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_unit_create_dto=course_unit_create_dto)
    except Exception as e:
        print("Exception when calling CourseUnitsApi->create_course_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_unit_create_dto** | [**CourseUnitCreateDto**](CourseUnitCreateDto.md)|  | [optional] 

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

# **delete_course_unit_async**
> delete_course_unit_async(tenant_id, unit_id, api_version=api_version, x_api_version=x_api_version)

Delete a course unit

Deletes a course unit for the specified tenant.

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
    api_instance = openapi_client.CourseUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course unit
        api_instance.delete_course_unit_async(tenant_id, unit_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseUnitsApi->delete_course_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_id** | **str**|  | 
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

# **get_course_unit_by_id_async**
> CourseUnitDto get_course_unit_by_id_async(unit_id, api_version=api_version, x_api_version=x_api_version)

Get course unit by ID

Retrieves a specific course unit by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_dto import CourseUnitDto
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
    api_instance = openapi_client.CourseUnitsApi(api_client)
    unit_id = 'unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course unit by ID
        api_response = api_instance.get_course_unit_by_id_async(unit_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUnitsApi->get_course_unit_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUnitsApi->get_course_unit_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseUnitDto**](CourseUnitDto.md)

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

# **get_course_units_async**
> List[CourseUnitDto] get_course_units_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course units

Retrieves all course units for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_dto import CourseUnitDto
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
    api_instance = openapi_client.CourseUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course units
        api_response = api_instance.get_course_units_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUnitsApi->get_course_units_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUnitsApi->get_course_units_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseUnitDto]**](CourseUnitDto.md)

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

# **get_course_units_count_async**
> int get_course_units_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course units count

Returns the count of course units for the specified tenant.

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
    api_instance = openapi_client.CourseUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course units count
        api_response = api_instance.get_course_units_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseUnitsApi->get_course_units_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseUnitsApi->get_course_units_count_async: %s\n" % e)
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

# **update_course_unit_async**
> update_course_unit_async(tenant_id, unit_id, api_version=api_version, x_api_version=x_api_version, course_unit_update_dto=course_unit_update_dto)

Update a course unit

Updates an existing course unit for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_unit_update_dto import CourseUnitUpdateDto
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
    api_instance = openapi_client.CourseUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    unit_id = 'unit_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_unit_update_dto = openapi_client.CourseUnitUpdateDto() # CourseUnitUpdateDto |  (optional)

    try:
        # Update a course unit
        api_instance.update_course_unit_async(tenant_id, unit_id, api_version=api_version, x_api_version=x_api_version, course_unit_update_dto=course_unit_update_dto)
    except Exception as e:
        print("Exception when calling CourseUnitsApi->update_course_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **unit_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_unit_update_dto** | [**CourseUnitUpdateDto**](CourseUnitUpdateDto.md)|  | [optional] 

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

