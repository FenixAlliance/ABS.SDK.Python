# openapi_client.LedgersApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ledger_async**](LedgersApi.md#create_ledger_async) | **POST** /api/v2/AccountingService/Ledgers | Creates a new ledger
[**delete_ledger_async**](LedgersApi.md#delete_ledger_async) | **DELETE** /api/v2/AccountingService/Ledgers/{ledgerId} | Deletes a ledger
[**get_ledger_details_async**](LedgersApi.md#get_ledger_details_async) | **GET** /api/v2/AccountingService/Ledgers/{ledgerId} | Gets a ledger by ID
[**get_ledgers_async**](LedgersApi.md#get_ledgers_async) | **GET** /api/v2/AccountingService/Ledgers | Retrieves all ledgers
[**get_ledgers_count_async**](LedgersApi.md#get_ledgers_count_async) | **GET** /api/v2/AccountingService/Ledgers/Count | Counts ledgers
[**update_ledger_async**](LedgersApi.md#update_ledger_async) | **PUT** /api/v2/AccountingService/Ledgers/{ledgerId} | Updates a ledger


# **create_ledger_async**
> EmptyEnvelope create_ledger_async(tenant_id, api_version=api_version, x_api_version=x_api_version, create_ledger_dto=create_ledger_dto)

Creates a new ledger

Creates a new ledger for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.create_ledger_dto import CreateLedgerDto
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.LedgersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    create_ledger_dto = openapi_client.CreateLedgerDto() # CreateLedgerDto |  (optional)

    try:
        # Creates a new ledger
        api_response = api_instance.create_ledger_async(tenant_id, api_version=api_version, x_api_version=x_api_version, create_ledger_dto=create_ledger_dto)
        print("The response of LedgersApi->create_ledger_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgersApi->create_ledger_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **create_ledger_dto** | [**CreateLedgerDto**](CreateLedgerDto.md)|  | [optional] 

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

# **delete_ledger_async**
> EmptyEnvelope delete_ledger_async(tenant_id, ledger_id, api_version=api_version, x_api_version=x_api_version)

Deletes a ledger

Deletes the specified ledger.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
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
    api_instance = openapi_client.LedgersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ledger_id = 'ledger_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a ledger
        api_response = api_instance.delete_ledger_async(tenant_id, ledger_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgersApi->delete_ledger_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgersApi->delete_ledger_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ledger_id** | **str**|  | 
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

# **get_ledger_details_async**
> LedgerDtoEnvelope get_ledger_details_async(tenant_id, ledger_id, api_version=api_version, x_api_version=x_api_version)

Gets a ledger by ID

Retrieves the details of a ledger using its unique ID.

### Example


```python
import openapi_client
from openapi_client.models.ledger_dto_envelope import LedgerDtoEnvelope
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
    api_instance = openapi_client.LedgersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ledger_id = 'ledger_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a ledger by ID
        api_response = api_instance.get_ledger_details_async(tenant_id, ledger_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgersApi->get_ledger_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgersApi->get_ledger_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ledger_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LedgerDtoEnvelope**](LedgerDtoEnvelope.md)

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

# **get_ledgers_async**
> LedgerDtoIReadOnlyListEnvelope get_ledgers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieves all ledgers

Gets all ledgers for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.ledger_dto_i_read_only_list_envelope import LedgerDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.LedgersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieves all ledgers
        api_response = api_instance.get_ledgers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgersApi->get_ledgers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgersApi->get_ledgers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LedgerDtoIReadOnlyListEnvelope**](LedgerDtoIReadOnlyListEnvelope.md)

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

# **get_ledgers_count_async**
> Int32Envelope get_ledgers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts ledgers

Gets the count of ledgers for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
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
    api_instance = openapi_client.LedgersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts ledgers
        api_response = api_instance.get_ledgers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of LedgersApi->get_ledgers_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgersApi->get_ledgers_count_async: %s\n" % e)
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

# **update_ledger_async**
> EmptyEnvelope update_ledger_async(tenant_id, ledger_id, api_version=api_version, x_api_version=x_api_version, update_ledger_dto=update_ledger_dto)

Updates a ledger

Updates the specified ledger.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.update_ledger_dto import UpdateLedgerDto
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
    api_instance = openapi_client.LedgersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ledger_id = 'ledger_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    update_ledger_dto = openapi_client.UpdateLedgerDto() # UpdateLedgerDto |  (optional)

    try:
        # Updates a ledger
        api_response = api_instance.update_ledger_async(tenant_id, ledger_id, api_version=api_version, x_api_version=x_api_version, update_ledger_dto=update_ledger_dto)
        print("The response of LedgersApi->update_ledger_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgersApi->update_ledger_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ledger_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **update_ledger_dto** | [**UpdateLedgerDto**](UpdateLedgerDto.md)|  | [optional] 

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

