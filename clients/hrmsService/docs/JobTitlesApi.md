# openapi_client.JobTitlesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_title_async**](JobTitlesApi.md#create_job_title_async) | **POST** /api/v2/HrmsService/JobTitles | Create a job title
[**delete_job_title_async**](JobTitlesApi.md#delete_job_title_async) | **DELETE** /api/v2/HrmsService/JobTitles/{jobTitleId} | Delete a job title
[**get_job_title_by_id_async**](JobTitlesApi.md#get_job_title_by_id_async) | **GET** /api/v2/HrmsService/JobTitles/{jobTitleId} | Get job title by ID
[**get_job_titles_async**](JobTitlesApi.md#get_job_titles_async) | **GET** /api/v2/HrmsService/JobTitles | Get job titles
[**get_job_titles_count_async**](JobTitlesApi.md#get_job_titles_count_async) | **GET** /api/v2/HrmsService/JobTitles/Count | Count job titles
[**patch_job_title_async**](JobTitlesApi.md#patch_job_title_async) | **PATCH** /api/v2/HrmsService/JobTitles/{jobTitleId} | Patch a job title
[**update_job_title_async**](JobTitlesApi.md#update_job_title_async) | **PUT** /api/v2/HrmsService/JobTitles/{jobTitleId} | Update a job title


# **create_job_title_async**
> EmptyEnvelope create_job_title_async(tenant_id, api_version=api_version, x_api_version=x_api_version, job_title_create_dto=job_title_create_dto)

Create a job title

Creates a new job title for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.job_title_create_dto import JobTitleCreateDto
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
    api_instance = openapi_client.JobTitlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    job_title_create_dto = openapi_client.JobTitleCreateDto() # JobTitleCreateDto |  (optional)

    try:
        # Create a job title
        api_response = api_instance.create_job_title_async(tenant_id, api_version=api_version, x_api_version=x_api_version, job_title_create_dto=job_title_create_dto)
        print("The response of JobTitlesApi->create_job_title_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTitlesApi->create_job_title_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **job_title_create_dto** | [**JobTitleCreateDto**](JobTitleCreateDto.md)|  | [optional] 

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

# **delete_job_title_async**
> EmptyEnvelope delete_job_title_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version)

Delete a job title

Deletes a job title for the specified tenant.

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
    api_instance = openapi_client.JobTitlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    job_title_id = 'job_title_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a job title
        api_response = api_instance.delete_job_title_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobTitlesApi->delete_job_title_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTitlesApi->delete_job_title_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **job_title_id** | **str**|  | 
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

# **get_job_title_by_id_async**
> JobTitleDtoEnvelope get_job_title_by_id_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version)

Get job title by ID

Retrieves a specific job title by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.job_title_dto_envelope import JobTitleDtoEnvelope
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
    api_instance = openapi_client.JobTitlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    job_title_id = 'job_title_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get job title by ID
        api_response = api_instance.get_job_title_by_id_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobTitlesApi->get_job_title_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTitlesApi->get_job_title_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **job_title_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JobTitleDtoEnvelope**](JobTitleDtoEnvelope.md)

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

# **get_job_titles_async**
> JobTitleDtoListEnvelope get_job_titles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get job titles

Retrieves job titles for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.job_title_dto_list_envelope import JobTitleDtoListEnvelope
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
    api_instance = openapi_client.JobTitlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get job titles
        api_response = api_instance.get_job_titles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobTitlesApi->get_job_titles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTitlesApi->get_job_titles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JobTitleDtoListEnvelope**](JobTitleDtoListEnvelope.md)

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

# **get_job_titles_count_async**
> Int32Envelope get_job_titles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count job titles

Counts job titles for the specified tenant.

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
    api_instance = openapi_client.JobTitlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count job titles
        api_response = api_instance.get_job_titles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobTitlesApi->get_job_titles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTitlesApi->get_job_titles_count_async: %s\n" % e)
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

# **patch_job_title_async**
> EmptyEnvelope patch_job_title_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a job title

Partially updates an existing job title for the specified tenant.

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
    api_instance = openapi_client.JobTitlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    job_title_id = 'job_title_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a job title
        api_response = api_instance.patch_job_title_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of JobTitlesApi->patch_job_title_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTitlesApi->patch_job_title_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **job_title_id** | **str**|  | 
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

# **update_job_title_async**
> EmptyEnvelope update_job_title_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version, job_title_update_dto=job_title_update_dto)

Update a job title

Updates an existing job title for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.job_title_update_dto import JobTitleUpdateDto
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
    api_instance = openapi_client.JobTitlesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    job_title_id = 'job_title_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    job_title_update_dto = openapi_client.JobTitleUpdateDto() # JobTitleUpdateDto |  (optional)

    try:
        # Update a job title
        api_response = api_instance.update_job_title_async(tenant_id, job_title_id, api_version=api_version, x_api_version=x_api_version, job_title_update_dto=job_title_update_dto)
        print("The response of JobTitlesApi->update_job_title_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTitlesApi->update_job_title_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **job_title_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **job_title_update_dto** | [**JobTitleUpdateDto**](JobTitleUpdateDto.md)|  | [optional] 

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

