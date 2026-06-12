# openapi_client.SalariesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_salary_async**](SalariesApi.md#create_salary_async) | **POST** /api/v2/HrmsService/Salaries | Create a salary
[**delete_salary_async**](SalariesApi.md#delete_salary_async) | **DELETE** /api/v2/HrmsService/Salaries/{salaryId} | Delete a salary
[**get_salaries_async**](SalariesApi.md#get_salaries_async) | **GET** /api/v2/HrmsService/Salaries | Get salaries
[**get_salaries_count_async**](SalariesApi.md#get_salaries_count_async) | **GET** /api/v2/HrmsService/Salaries/Count | Count salaries
[**get_salary_by_id_async**](SalariesApi.md#get_salary_by_id_async) | **GET** /api/v2/HrmsService/Salaries/{salaryId} | Get salary by ID
[**patch_salary_async**](SalariesApi.md#patch_salary_async) | **PATCH** /api/v2/HrmsService/Salaries/{salaryId} | Patch a salary
[**update_salary_async**](SalariesApi.md#update_salary_async) | **PUT** /api/v2/HrmsService/Salaries/{salaryId} | Update a salary


# **create_salary_async**
> EmptyEnvelope create_salary_async(tenant_id, api_version=api_version, x_api_version=x_api_version, salary_create_dto=salary_create_dto)

Create a salary

Creates a new salary for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.salary_create_dto import SalaryCreateDto
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
    api_instance = openapi_client.SalariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    salary_create_dto = openapi_client.SalaryCreateDto() # SalaryCreateDto |  (optional)

    try:
        # Create a salary
        api_response = api_instance.create_salary_async(tenant_id, api_version=api_version, x_api_version=x_api_version, salary_create_dto=salary_create_dto)
        print("The response of SalariesApi->create_salary_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalariesApi->create_salary_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **salary_create_dto** | [**SalaryCreateDto**](SalaryCreateDto.md)|  | [optional] 

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

# **delete_salary_async**
> EmptyEnvelope delete_salary_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version)

Delete a salary

Deletes a salary for the specified tenant.

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
    api_instance = openapi_client.SalariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    salary_id = 'salary_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a salary
        api_response = api_instance.delete_salary_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalariesApi->delete_salary_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalariesApi->delete_salary_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **salary_id** | **str**|  | 
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

# **get_salaries_async**
> SalaryDtoListEnvelope get_salaries_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get salaries

Retrieves salaries for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.salary_dto_list_envelope import SalaryDtoListEnvelope
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
    api_instance = openapi_client.SalariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get salaries
        api_response = api_instance.get_salaries_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalariesApi->get_salaries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalariesApi->get_salaries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SalaryDtoListEnvelope**](SalaryDtoListEnvelope.md)

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

# **get_salaries_count_async**
> Int32Envelope get_salaries_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count salaries

Counts salaries for the specified tenant.

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
    api_instance = openapi_client.SalariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count salaries
        api_response = api_instance.get_salaries_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalariesApi->get_salaries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalariesApi->get_salaries_count_async: %s\n" % e)
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

# **get_salary_by_id_async**
> SalaryDtoEnvelope get_salary_by_id_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version)

Get salary by ID

Retrieves a specific salary by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.salary_dto_envelope import SalaryDtoEnvelope
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
    api_instance = openapi_client.SalariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    salary_id = 'salary_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get salary by ID
        api_response = api_instance.get_salary_by_id_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SalariesApi->get_salary_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalariesApi->get_salary_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **salary_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SalaryDtoEnvelope**](SalaryDtoEnvelope.md)

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

# **patch_salary_async**
> EmptyEnvelope patch_salary_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a salary

Partially updates an existing salary for the specified tenant.

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
    api_instance = openapi_client.SalariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    salary_id = 'salary_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a salary
        api_response = api_instance.patch_salary_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of SalariesApi->patch_salary_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalariesApi->patch_salary_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **salary_id** | **str**|  | 
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

# **update_salary_async**
> EmptyEnvelope update_salary_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version, salary_update_dto=salary_update_dto)

Update a salary

Updates an existing salary for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.salary_update_dto import SalaryUpdateDto
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
    api_instance = openapi_client.SalariesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    salary_id = 'salary_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    salary_update_dto = openapi_client.SalaryUpdateDto() # SalaryUpdateDto |  (optional)

    try:
        # Update a salary
        api_response = api_instance.update_salary_async(tenant_id, salary_id, api_version=api_version, x_api_version=x_api_version, salary_update_dto=salary_update_dto)
        print("The response of SalariesApi->update_salary_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalariesApi->update_salary_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **salary_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **salary_update_dto** | [**SalaryUpdateDto**](SalaryUpdateDto.md)|  | [optional] 

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

