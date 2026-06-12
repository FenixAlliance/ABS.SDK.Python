# openapi_client.PayrollsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payroll_async**](PayrollsApi.md#create_payroll_async) | **POST** /api/v2/HrmsService/Payrolls | Create a payroll
[**delete_payroll_async**](PayrollsApi.md#delete_payroll_async) | **DELETE** /api/v2/HrmsService/Payrolls/{payrollId} | Delete a payroll
[**get_payroll_by_id_async**](PayrollsApi.md#get_payroll_by_id_async) | **GET** /api/v2/HrmsService/Payrolls/{payrollId} | Get payroll by ID
[**get_payrolls_async**](PayrollsApi.md#get_payrolls_async) | **GET** /api/v2/HrmsService/Payrolls | Get payrolls
[**get_payrolls_count_async**](PayrollsApi.md#get_payrolls_count_async) | **GET** /api/v2/HrmsService/Payrolls/Count | Count payrolls
[**patch_payroll_async**](PayrollsApi.md#patch_payroll_async) | **PATCH** /api/v2/HrmsService/Payrolls/{payrollId} | Patch a payroll
[**update_payroll_async**](PayrollsApi.md#update_payroll_async) | **PUT** /api/v2/HrmsService/Payrolls/{payrollId} | Update a payroll


# **create_payroll_async**
> EmptyEnvelope create_payroll_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payroll_create_dto=payroll_create_dto)

Create a payroll

Creates a new payroll for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payroll_create_dto import PayrollCreateDto
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
    api_instance = openapi_client.PayrollsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payroll_create_dto = openapi_client.PayrollCreateDto() # PayrollCreateDto |  (optional)

    try:
        # Create a payroll
        api_response = api_instance.create_payroll_async(tenant_id, api_version=api_version, x_api_version=x_api_version, payroll_create_dto=payroll_create_dto)
        print("The response of PayrollsApi->create_payroll_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollsApi->create_payroll_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payroll_create_dto** | [**PayrollCreateDto**](PayrollCreateDto.md)|  | [optional] 

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

# **delete_payroll_async**
> EmptyEnvelope delete_payroll_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version)

Delete a payroll

Deletes a payroll for the specified tenant.

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
    api_instance = openapi_client.PayrollsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payroll_id = 'payroll_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a payroll
        api_response = api_instance.delete_payroll_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollsApi->delete_payroll_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollsApi->delete_payroll_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payroll_id** | **str**|  | 
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

# **get_payroll_by_id_async**
> PayrollDtoEnvelope get_payroll_by_id_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version)

Get payroll by ID

Retrieves a specific payroll by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.payroll_dto_envelope import PayrollDtoEnvelope
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
    api_instance = openapi_client.PayrollsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payroll_id = 'payroll_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get payroll by ID
        api_response = api_instance.get_payroll_by_id_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollsApi->get_payroll_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollsApi->get_payroll_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payroll_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PayrollDtoEnvelope**](PayrollDtoEnvelope.md)

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

# **get_payrolls_async**
> PayrollDtoListEnvelope get_payrolls_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get payrolls

Retrieves payrolls for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.payroll_dto_list_envelope import PayrollDtoListEnvelope
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
    api_instance = openapi_client.PayrollsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get payrolls
        api_response = api_instance.get_payrolls_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollsApi->get_payrolls_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollsApi->get_payrolls_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PayrollDtoListEnvelope**](PayrollDtoListEnvelope.md)

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

# **get_payrolls_count_async**
> Int32Envelope get_payrolls_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count payrolls

Counts payrolls for the specified tenant.

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
    api_instance = openapi_client.PayrollsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count payrolls
        api_response = api_instance.get_payrolls_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of PayrollsApi->get_payrolls_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollsApi->get_payrolls_count_async: %s\n" % e)
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

# **patch_payroll_async**
> EmptyEnvelope patch_payroll_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a payroll

Partially updates an existing payroll for the specified tenant.

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
    api_instance = openapi_client.PayrollsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payroll_id = 'payroll_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a payroll
        api_response = api_instance.patch_payroll_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of PayrollsApi->patch_payroll_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollsApi->patch_payroll_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payroll_id** | **str**|  | 
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

# **update_payroll_async**
> EmptyEnvelope update_payroll_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version, payroll_update_dto=payroll_update_dto)

Update a payroll

Updates an existing payroll for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payroll_update_dto import PayrollUpdateDto
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
    api_instance = openapi_client.PayrollsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    payroll_id = 'payroll_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payroll_update_dto = openapi_client.PayrollUpdateDto() # PayrollUpdateDto |  (optional)

    try:
        # Update a payroll
        api_response = api_instance.update_payroll_async(tenant_id, payroll_id, api_version=api_version, x_api_version=x_api_version, payroll_update_dto=payroll_update_dto)
        print("The response of PayrollsApi->update_payroll_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayrollsApi->update_payroll_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **payroll_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payroll_update_dto** | [**PayrollUpdateDto**](PayrollUpdateDto.md)|  | [optional] 

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

