# openapi_client.JournalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_journals_async**](JournalsApi.md#count_journals_async) | **GET** /api/v2/AccountingService/Journals/Count | Count journals
[**create_journal_async**](JournalsApi.md#create_journal_async) | **POST** /api/v2/AccountingService/Journals | Create journal
[**create_journal_entry_async**](JournalsApi.md#create_journal_entry_async) | **POST** /api/v2/AccountingService/Journals/{journalId}/Entries | Create journal entry
[**delete_journal_async**](JournalsApi.md#delete_journal_async) | **DELETE** /api/v2/AccountingService/Journals/{journalId} | Delete journal
[**delete_journal_entry_async**](JournalsApi.md#delete_journal_entry_async) | **DELETE** /api/v2/AccountingService/Journals/{journalId}/Entries/{entryId} | Delete journal entry
[**get_journal_details_async**](JournalsApi.md#get_journal_details_async) | **GET** /api/v2/AccountingService/Journals/{journalId} | Get journal by ID
[**get_journal_entries_async**](JournalsApi.md#get_journal_entries_async) | **GET** /api/v2/AccountingService/Journals/{journalId}/Entries | Get journal entries
[**get_journal_entries_count_async**](JournalsApi.md#get_journal_entries_count_async) | **GET** /api/v2/AccountingService/Journals/{journalId}/Entries/Count | Count journal entries
[**get_journals_async**](JournalsApi.md#get_journals_async) | **GET** /api/v2/AccountingService/Journals | Get all journals
[**update_journal_async**](JournalsApi.md#update_journal_async) | **PUT** /api/v2/AccountingService/Journals/{journalId} | Update journal
[**update_journal_entry_async**](JournalsApi.md#update_journal_entry_async) | **PUT** /api/v2/AccountingService/Journals/{journalId}/Entries/{entryId} | Update journal entry


# **count_journals_async**
> Int32Envelope count_journals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count journals

Returns the count of journals for the tenant.

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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count journals
        api_response = api_instance.count_journals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalsApi->count_journals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->count_journals_async: %s\n" % e)
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

# **create_journal_async**
> EmptyEnvelope create_journal_async(tenant_id, api_version=api_version, x_api_version=x_api_version, journal_create_dto=journal_create_dto)

Create journal

Creates a new journal for the tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.journal_create_dto import JournalCreateDto
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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    journal_create_dto = openapi_client.JournalCreateDto() # JournalCreateDto |  (optional)

    try:
        # Create journal
        api_response = api_instance.create_journal_async(tenant_id, api_version=api_version, x_api_version=x_api_version, journal_create_dto=journal_create_dto)
        print("The response of JournalsApi->create_journal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->create_journal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **journal_create_dto** | [**JournalCreateDto**](JournalCreateDto.md)|  | [optional] 

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

# **create_journal_entry_async**
> EmptyEnvelope create_journal_entry_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version, journal_entry_create_dto=journal_entry_create_dto)

Create journal entry

Creates a new journal entry for a given journal.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.journal_entry_create_dto import JournalEntryCreateDto
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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    journal_entry_create_dto = openapi_client.JournalEntryCreateDto() # JournalEntryCreateDto |  (optional)

    try:
        # Create journal entry
        api_response = api_instance.create_journal_entry_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version, journal_entry_create_dto=journal_entry_create_dto)
        print("The response of JournalsApi->create_journal_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->create_journal_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **journal_entry_create_dto** | [**JournalEntryCreateDto**](JournalEntryCreateDto.md)|  | [optional] 

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

# **delete_journal_async**
> EmptyEnvelope delete_journal_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)

Delete journal

Deletes a journal by ID.

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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete journal
        api_response = api_instance.delete_journal_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalsApi->delete_journal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->delete_journal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
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

# **delete_journal_entry_async**
> EmptyEnvelope delete_journal_entry_async(tenant_id, journal_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Delete journal entry

Deletes a specific journal entry.

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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete journal entry
        api_response = api_instance.delete_journal_entry_async(tenant_id, journal_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalsApi->delete_journal_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->delete_journal_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
 **entry_id** | **str**|  | 
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

# **get_journal_details_async**
> JournalDtoEnvelope get_journal_details_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)

Get journal by ID

Retrieves the details of a journal.

### Example


```python
import openapi_client
from openapi_client.models.journal_dto_envelope import JournalDtoEnvelope
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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get journal by ID
        api_response = api_instance.get_journal_details_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalsApi->get_journal_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->get_journal_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JournalDtoEnvelope**](JournalDtoEnvelope.md)

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

# **get_journal_entries_async**
> JournalEntryDtoIReadOnlyListEnvelope get_journal_entries_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)

Get journal entries

Gets entries for the specified journal.

### Example


```python
import openapi_client
from openapi_client.models.journal_entry_dto_i_read_only_list_envelope import JournalEntryDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get journal entries
        api_response = api_instance.get_journal_entries_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalsApi->get_journal_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->get_journal_entries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JournalEntryDtoIReadOnlyListEnvelope**](JournalEntryDtoIReadOnlyListEnvelope.md)

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

# **get_journal_entries_count_async**
> Int32Envelope get_journal_entries_count_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)

Count journal entries

Returns the number of entries in the specified journal.

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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count journal entries
        api_response = api_instance.get_journal_entries_count_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalsApi->get_journal_entries_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->get_journal_entries_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
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

# **get_journals_async**
> JournalDtoIReadOnlyListEnvelope get_journals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all journals

Retrieves all journals for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.journal_dto_i_read_only_list_envelope import JournalDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all journals
        api_response = api_instance.get_journals_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JournalsApi->get_journals_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->get_journals_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JournalDtoIReadOnlyListEnvelope**](JournalDtoIReadOnlyListEnvelope.md)

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

# **update_journal_async**
> EmptyEnvelope update_journal_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version, journal_update_dto=journal_update_dto)

Update journal

Updates an existing journal.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.journal_update_dto import JournalUpdateDto
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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    journal_update_dto = openapi_client.JournalUpdateDto() # JournalUpdateDto |  (optional)

    try:
        # Update journal
        api_response = api_instance.update_journal_async(tenant_id, journal_id, api_version=api_version, x_api_version=x_api_version, journal_update_dto=journal_update_dto)
        print("The response of JournalsApi->update_journal_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->update_journal_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **journal_update_dto** | [**JournalUpdateDto**](JournalUpdateDto.md)|  | [optional] 

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

# **update_journal_entry_async**
> EmptyEnvelope update_journal_entry_async(tenant_id, journal_id, entry_id, api_version=api_version, x_api_version=x_api_version, journal_entry_update_dto=journal_entry_update_dto)

Update journal entry

Updates a specific journal entry.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.journal_entry_update_dto import JournalEntryUpdateDto
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
    api_instance = openapi_client.JournalsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    journal_id = 'journal_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    journal_entry_update_dto = openapi_client.JournalEntryUpdateDto() # JournalEntryUpdateDto |  (optional)

    try:
        # Update journal entry
        api_response = api_instance.update_journal_entry_async(tenant_id, journal_id, entry_id, api_version=api_version, x_api_version=x_api_version, journal_entry_update_dto=journal_entry_update_dto)
        print("The response of JournalsApi->update_journal_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->update_journal_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **journal_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **journal_entry_update_dto** | [**JournalEntryUpdateDto**](JournalEntryUpdateDto.md)|  | [optional] 

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

