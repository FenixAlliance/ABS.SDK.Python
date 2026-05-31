# openapi_client.LedgerTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ledger_type_async**](LedgerTypesApi.md#create_ledger_type_async) | **POST** /api/v2/AccountingService/LedgerTypes | Creates a new ledger type
[**delete_ledger_type_async**](LedgerTypesApi.md#delete_ledger_type_async) | **DELETE** /api/v2/AccountingService/LedgerTypes/{ledgerTypeId} | Deletes a ledger type
[**get_ledger_type_details_async**](LedgerTypesApi.md#get_ledger_type_details_async) | **GET** /api/v2/AccountingService/LedgerTypes/{ledgerTypeId} | Gets a ledger type by ID
[**get_ledger_types_async**](LedgerTypesApi.md#get_ledger_types_async) | **GET** /api/v2/AccountingService/LedgerTypes | Retrieves all ledger types
[**get_ledger_types_count_async**](LedgerTypesApi.md#get_ledger_types_count_async) | **GET** /api/v2/AccountingService/LedgerTypes/Count | Counts ledger types
[**update_ledger_type_async**](LedgerTypesApi.md#update_ledger_type_async) | **PUT** /api/v2/AccountingService/LedgerTypes/{ledgerTypeId} | Updates a ledger type


# **create_ledger_type_async**
> EmptyEnvelope create_ledger_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, ledger_type_create_dto=ledger_type_create_dto)

Creates a new ledger type

Creates a new ledger type for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.ledger_type_create_dto import LedgerTypeCreateDto
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
    api_instance = openapi_client.LedgerTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    ledger_type_create_dto = openapi_client.LedgerTypeCreateDto() # LedgerTypeCreateDto |  (optional)

    try:
        # Creates a new ledger type
        api_response = api_instance.create_ledger_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, ledger_type_create_dto=ledger_type_create_dto)
        print("The response of LedgerTypesApi->create_ledger_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTypesApi->create_ledger_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **ledger_type_create_dto** | [**LedgerTypeCreateDto**](LedgerTypeCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ledger_type_async**
> EmptyEnvelope delete_ledger_type_async(tenant_id, ledger_type_id, api_version=api_version, x_api_version=x_api_version)

Deletes a ledger type

Deletes the specified ledger type.

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
    api_instance = openapi_client.LedgerTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ledger_type_id = 'ledger_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a ledger type
        api_response = api_instance.delete_ledger_type_async(tenant_id, ledger_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgerTypesApi->delete_ledger_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTypesApi->delete_ledger_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ledger_type_id** | **str**|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_type_details_async**
> LedgerTypeDtoEnvelope get_ledger_type_details_async(tenant_id, ledger_type_id, api_version=api_version, x_api_version=x_api_version)

Gets a ledger type by ID

Retrieves the details of a ledger type using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.ledger_type_dto_envelope import LedgerTypeDtoEnvelope
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
    api_instance = openapi_client.LedgerTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ledger_type_id = 'ledger_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a ledger type by ID
        api_response = api_instance.get_ledger_type_details_async(tenant_id, ledger_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgerTypesApi->get_ledger_type_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTypesApi->get_ledger_type_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ledger_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LedgerTypeDtoEnvelope**](LedgerTypeDtoEnvelope.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_types_async**
> LedgerTypeDtoIReadOnlyListEnvelope get_ledger_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieves all ledger types

Gets all ledger types for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.ledger_type_dto_i_read_only_list_envelope import LedgerTypeDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.LedgerTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieves all ledger types
        api_response = api_instance.get_ledger_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgerTypesApi->get_ledger_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTypesApi->get_ledger_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LedgerTypeDtoIReadOnlyListEnvelope**](LedgerTypeDtoIReadOnlyListEnvelope.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_types_count_async**
> Int32Envelope get_ledger_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts ledger types

Gets the count of ledger types for the current tenant.

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
    api_instance = openapi_client.LedgerTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts ledger types
        api_response = api_instance.get_ledger_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgerTypesApi->get_ledger_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTypesApi->get_ledger_types_count_async: %s\n" % e)
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ledger_type_async**
> EmptyEnvelope update_ledger_type_async(tenant_id, ledger_type_id, api_version=api_version, x_api_version=x_api_version, ledger_type_update_dto=ledger_type_update_dto)

Updates a ledger type

Updates the specified ledger type.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.ledger_type_update_dto import LedgerTypeUpdateDto
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
    api_instance = openapi_client.LedgerTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ledger_type_id = 'ledger_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    ledger_type_update_dto = openapi_client.LedgerTypeUpdateDto() # LedgerTypeUpdateDto |  (optional)

    try:
        # Updates a ledger type
        api_response = api_instance.update_ledger_type_async(tenant_id, ledger_type_id, api_version=api_version, x_api_version=x_api_version, ledger_type_update_dto=ledger_type_update_dto)
        print("The response of LedgerTypesApi->update_ledger_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTypesApi->update_ledger_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ledger_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **ledger_type_update_dto** | [**LedgerTypeUpdateDto**](LedgerTypeUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

