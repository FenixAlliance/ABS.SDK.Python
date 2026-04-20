# openapi_client.JournalTypesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_journal_type_async**](JournalTypesApi.md#create_journal_type_async) | **POST** /api/v2/AccountingService/JournalTypes | Creates a new journal type
[**delete_journal_type_async**](JournalTypesApi.md#delete_journal_type_async) | **DELETE** /api/v2/AccountingService/JournalTypes/{journalTypeId} | Deletes a journal type
[**get_journal_type_details_async**](JournalTypesApi.md#get_journal_type_details_async) | **GET** /api/v2/AccountingService/JournalTypes/{journalTypeId} | Retrieves a journal type by ID
[**get_journal_types_async**](JournalTypesApi.md#get_journal_types_async) | **GET** /api/v2/AccountingService/JournalTypes | Retrieves all journal types
[**get_journal_types_count_async**](JournalTypesApi.md#get_journal_types_count_async) | **GET** /api/v2/AccountingService/JournalTypes/Count | Counts journal types
[**update_journal_type_async**](JournalTypesApi.md#update_journal_type_async) | **PUT** /api/v2/AccountingService/JournalTypes/{journalTypeId} | Updates an existing journal type


# **create_journal_type_async**
> EmptyEnvelope create_journal_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, journal_type_create_dto=journal_type_create_dto)

Creates a new journal type

Adds a new journal type to the tenant's catalog.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.journal_type_create_dto import JournalTypeCreateDto
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
    api_instance = openapi_client.JournalTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    journal_type_create_dto = openapi_client.JournalTypeCreateDto() # JournalTypeCreateDto |  (optional)

    try:
        # Creates a new journal type
        api_response = api_instance.create_journal_type_async(tenant_id, api_version=api_version, x_api_version=x_api_version, journal_type_create_dto=journal_type_create_dto)
        print("The response of JournalTypesApi->create_journal_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalTypesApi->create_journal_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **journal_type_create_dto** | [**JournalTypeCreateDto**](JournalTypeCreateDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_journal_type_async**
> EmptyEnvelope delete_journal_type_async(tenant_id, journal_type_id, api_version=api_version, x_api_version=x_api_version)

Deletes a journal type

Removes a journal type from the tenant's configuration.

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
    api_instance = openapi_client.JournalTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_type_id = 'journal_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a journal type
        api_response = api_instance.delete_journal_type_async(tenant_id, journal_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalTypesApi->delete_journal_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalTypesApi->delete_journal_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_type_id** | **str**|  | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_type_details_async**
> JournalTypeDtoEnvelope get_journal_type_details_async(tenant_id, journal_type_id, api_version=api_version, x_api_version=x_api_version)

Retrieves a journal type by ID

Fetches the journal type matching the specified ID.

### Example


```python
import openapi_client
from openapi_client.models.journal_type_dto_envelope import JournalTypeDtoEnvelope
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
    api_instance = openapi_client.JournalTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_type_id = 'journal_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieves a journal type by ID
        api_response = api_instance.get_journal_type_details_async(tenant_id, journal_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalTypesApi->get_journal_type_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalTypesApi->get_journal_type_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JournalTypeDtoEnvelope**](JournalTypeDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_types_async**
> JournalTypeDtoIReadOnlyListEnvelope get_journal_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieves all journal types

Fetches all journal types for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.journal_type_dto_i_read_only_list_envelope import JournalTypeDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.JournalTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieves all journal types
        api_response = api_instance.get_journal_types_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalTypesApi->get_journal_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalTypesApi->get_journal_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JournalTypeDtoIReadOnlyListEnvelope**](JournalTypeDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_types_count_async**
> Int32Envelope get_journal_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Counts journal types

Returns the total number of journal types available for the tenant.

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
    api_instance = openapi_client.JournalTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Counts journal types
        api_response = api_instance.get_journal_types_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalTypesApi->get_journal_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalTypesApi->get_journal_types_count_async: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_journal_type_async**
> EmptyEnvelope update_journal_type_async(tenant_id, journal_type_id, api_version=api_version, x_api_version=x_api_version, journal_type_update_dto=journal_type_update_dto)

Updates an existing journal type

Modifies the details of a specific journal type.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.journal_type_update_dto import JournalTypeUpdateDto
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
    api_instance = openapi_client.JournalTypesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_type_id = 'journal_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    journal_type_update_dto = openapi_client.JournalTypeUpdateDto() # JournalTypeUpdateDto |  (optional)

    try:
        # Updates an existing journal type
        api_response = api_instance.update_journal_type_async(tenant_id, journal_type_id, api_version=api_version, x_api_version=x_api_version, journal_type_update_dto=journal_type_update_dto)
        print("The response of JournalTypesApi->update_journal_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalTypesApi->update_journal_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **journal_type_update_dto** | [**JournalTypeUpdateDto**](JournalTypeUpdateDto.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

