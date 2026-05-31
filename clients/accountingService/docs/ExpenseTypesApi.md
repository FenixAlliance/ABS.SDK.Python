# openapi_client.ExpenseTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_expense_type**](ExpenseTypesApi.md#create_expense_type) | **POST** /api/v2/AccountingService/ExpenseTypes | Create an expense type
[**delete_expense_type**](ExpenseTypesApi.md#delete_expense_type) | **DELETE** /api/v2/AccountingService/ExpenseTypes/{expenseTypeId} | Delete an expense type
[**get_expense_type**](ExpenseTypesApi.md#get_expense_type) | **GET** /api/v2/AccountingService/ExpenseTypes/{expenseTypeId} | Get an expense type by id
[**get_expense_types**](ExpenseTypesApi.md#get_expense_types) | **GET** /api/v2/AccountingService/ExpenseTypes | Get all expense types for a tenant
[**get_expense_types_count**](ExpenseTypesApi.md#get_expense_types_count) | **GET** /api/v2/AccountingService/ExpenseTypes/Count | Get the count of expense types for a tenant
[**update_expense_type**](ExpenseTypesApi.md#update_expense_type) | **PUT** /api/v2/AccountingService/ExpenseTypes/{expenseTypeId} | Update an expense type


# **create_expense_type**
> EmptyEnvelope create_expense_type(tenant_id, expense_type_create_dto, api_version=api_version, x_api_version=x_api_version)

Create an expense type

Creates a new expense type.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.expense_type_create_dto import ExpenseTypeCreateDto
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
    api_instance = openapi_client.ExpenseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_type_create_dto = openapi_client.ExpenseTypeCreateDto() # ExpenseTypeCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Create an expense type
        api_response = api_instance.create_expense_type(tenant_id, expense_type_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseTypesApi->create_expense_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseTypesApi->create_expense_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_type_create_dto** | [**ExpenseTypeCreateDto**](ExpenseTypeCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_expense_type**
> EmptyEnvelope delete_expense_type(tenant_id, expense_type_id, api_version=api_version, x_api_version=x_api_version)

Delete an expense type

Deletes an expense type.

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
    api_instance = openapi_client.ExpenseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_type_id = 'expense_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an expense type
        api_response = api_instance.delete_expense_type(tenant_id, expense_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseTypesApi->delete_expense_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseTypesApi->delete_expense_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_type_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_type**
> ExpenseTypeDtoEnvelope get_expense_type(tenant_id, expense_type_id, api_version=api_version, x_api_version=x_api_version)

Get an expense type by id

Retrieves an expense type by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.expense_type_dto_envelope import ExpenseTypeDtoEnvelope
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
    api_instance = openapi_client.ExpenseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_type_id = 'expense_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get an expense type by id
        api_response = api_instance.get_expense_type(tenant_id, expense_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseTypesApi->get_expense_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseTypesApi->get_expense_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExpenseTypeDtoEnvelope**](ExpenseTypeDtoEnvelope.md)

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

# **get_expense_types**
> ExpenseTypeDtoListEnvelope get_expense_types(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all expense types for a tenant

Retrieves all expense types for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.expense_type_dto_list_envelope import ExpenseTypeDtoListEnvelope
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
    api_instance = openapi_client.ExpenseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all expense types for a tenant
        api_response = api_instance.get_expense_types(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseTypesApi->get_expense_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseTypesApi->get_expense_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExpenseTypeDtoListEnvelope**](ExpenseTypeDtoListEnvelope.md)

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

# **get_expense_types_count**
> Int32Envelope get_expense_types_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of expense types for a tenant

Retrieves the count of expense types for the specified tenant using OData query options.

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
    api_instance = openapi_client.ExpenseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of expense types for a tenant
        api_response = api_instance.get_expense_types_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseTypesApi->get_expense_types_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseTypesApi->get_expense_types_count: %s\n" % e)
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

# **update_expense_type**
> EmptyEnvelope update_expense_type(tenant_id, expense_type_id, expense_type_update_dto, api_version=api_version, x_api_version=x_api_version)

Update an expense type

Updates an existing expense type.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.expense_type_update_dto import ExpenseTypeUpdateDto
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
    api_instance = openapi_client.ExpenseTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    expense_type_id = 'expense_type_id_example' # str | 
    expense_type_update_dto = openapi_client.ExpenseTypeUpdateDto() # ExpenseTypeUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update an expense type
        api_response = api_instance.update_expense_type(tenant_id, expense_type_id, expense_type_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of ExpenseTypesApi->update_expense_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseTypesApi->update_expense_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **expense_type_id** | **str**|  | 
 **expense_type_update_dto** | [**ExpenseTypeUpdateDto**](ExpenseTypeUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

