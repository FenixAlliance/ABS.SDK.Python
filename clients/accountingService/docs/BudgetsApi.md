# openapi_client.BudgetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_budget_account_entry_async**](BudgetsApi.md#create_budget_account_entry_async) | **POST** /api/v2/AccountingService/Budgets/{budgetId}/AccountEntries | Creates a budget account entry
[**create_budget_async**](BudgetsApi.md#create_budget_async) | **POST** /api/v2/AccountingService/Budgets | Creates a budget
[**delete_budget_account_entry_async**](BudgetsApi.md#delete_budget_account_entry_async) | **DELETE** /api/v2/AccountingService/Budgets/{budgetId}/AccountEntries/{entryId} | Deletes a budget account entry
[**delete_budget_async**](BudgetsApi.md#delete_budget_async) | **DELETE** /api/v2/AccountingService/Budgets/{budgetId} | Deletes a budget
[**get_budget_account_entries_collection_async**](BudgetsApi.md#get_budget_account_entries_collection_async) | **GET** /api/v2/AccountingService/Budgets/{budgetId}/AccountEntries | Gets all budget account entries
[**get_budget_account_entry_async**](BudgetsApi.md#get_budget_account_entry_async) | **GET** /api/v2/AccountingService/Budgets/{budgetId}/AccountEntries/{entryId} | Gets a budget account entry by id
[**get_budget_details_async**](BudgetsApi.md#get_budget_details_async) | **GET** /api/v2/AccountingService/Budgets/{budgetId} | Gets a budget by id
[**get_budgets_async**](BudgetsApi.md#get_budgets_async) | **GET** /api/v2/AccountingService/Budgets | Gets all budgets
[**update_budget_account_entry_async**](BudgetsApi.md#update_budget_account_entry_async) | **PUT** /api/v2/AccountingService/Budgets/{budgetId}/AccountEntries/{entryId} | Updates a budget account entry
[**update_budget_async**](BudgetsApi.md#update_budget_async) | **PUT** /api/v2/AccountingService/Budgets/{budgetId} | Updates a budget


# **create_budget_account_entry_async**
> EmptyEnvelope create_budget_account_entry_async(tenant_id, budget_id, budget_account_entry_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a budget account entry

Create a budget account entry

### Example


```python
import openapi_client
from openapi_client.models.budget_account_entry_create_dto import BudgetAccountEntryCreateDto
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    budget_account_entry_create_dto = openapi_client.BudgetAccountEntryCreateDto() # BudgetAccountEntryCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a budget account entry
        api_response = api_instance.create_budget_account_entry_async(tenant_id, budget_id, budget_account_entry_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->create_budget_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->create_budget_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **budget_account_entry_create_dto** | [**BudgetAccountEntryCreateDto**](BudgetAccountEntryCreateDto.md)|  | 
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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_budget_async**
> EmptyEnvelope create_budget_async(tenant_id, budget_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a budget

Create a budget

### Example


```python
import openapi_client
from openapi_client.models.budget_create_dto import BudgetCreateDto
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_create_dto = openapi_client.BudgetCreateDto() # BudgetCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a budget
        api_response = api_instance.create_budget_async(tenant_id, budget_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->create_budget_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->create_budget_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_create_dto** | [**BudgetCreateDto**](BudgetCreateDto.md)|  | 
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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget_account_entry_async**
> EmptyEnvelope delete_budget_account_entry_async(tenant_id, budget_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Deletes a budget account entry

Delete a budget account entry

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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a budget account entry
        api_response = api_instance.delete_budget_account_entry_async(tenant_id, budget_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->delete_budget_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->delete_budget_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
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

# **delete_budget_async**
> EmptyEnvelope delete_budget_async(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)

Deletes a budget

Delete a budget

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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a budget
        api_response = api_instance.delete_budget_async(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->delete_budget_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->delete_budget_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
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

# **get_budget_account_entries_collection_async**
> BudgetAccountEntryDtoIReadOnlyListEnvelope get_budget_account_entries_collection_async(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)

Gets all budget account entries

Get all budget account entries

### Example


```python
import openapi_client
from openapi_client.models.budget_account_entry_dto_i_read_only_list_envelope import BudgetAccountEntryDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets all budget account entries
        api_response = api_instance.get_budget_account_entries_collection_async(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->get_budget_account_entries_collection_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budget_account_entries_collection_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BudgetAccountEntryDtoIReadOnlyListEnvelope**](BudgetAccountEntryDtoIReadOnlyListEnvelope.md)

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

# **get_budget_account_entry_async**
> BudgetAccountEntryDtoEnvelope get_budget_account_entry_async(tenant_id, budget_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Gets a budget account entry by id

Get a budget account entry by id

### Example


```python
import openapi_client
from openapi_client.models.budget_account_entry_dto_envelope import BudgetAccountEntryDtoEnvelope
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a budget account entry by id
        api_response = api_instance.get_budget_account_entry_async(tenant_id, budget_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->get_budget_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budget_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BudgetAccountEntryDtoEnvelope**](BudgetAccountEntryDtoEnvelope.md)

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

# **get_budget_details_async**
> BudgetDtoEnvelope get_budget_details_async(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)

Gets a budget by id

Get a budget by id

### Example


```python
import openapi_client
from openapi_client.models.budget_dto_envelope import BudgetDtoEnvelope
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a budget by id
        api_response = api_instance.get_budget_details_async(tenant_id, budget_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->get_budget_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budget_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BudgetDtoEnvelope**](BudgetDtoEnvelope.md)

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

# **get_budgets_async**
> BudgetDtoIReadOnlyListEnvelope get_budgets_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets all budgets

Get all budgets

### Example


```python
import openapi_client
from openapi_client.models.budget_dto_i_read_only_list_envelope import BudgetDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets all budgets
        api_response = api_instance.get_budgets_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->get_budgets_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budgets_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BudgetDtoIReadOnlyListEnvelope**](BudgetDtoIReadOnlyListEnvelope.md)

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

# **update_budget_account_entry_async**
> EmptyEnvelope update_budget_account_entry_async(tenant_id, budget_id, entry_id, budget_account_entry_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates a budget account entry

Update a budget account entry

### Example


```python
import openapi_client
from openapi_client.models.budget_account_entry_update_dto import BudgetAccountEntryUpdateDto
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    budget_account_entry_update_dto = openapi_client.BudgetAccountEntryUpdateDto() # BudgetAccountEntryUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates a budget account entry
        api_response = api_instance.update_budget_account_entry_async(tenant_id, budget_id, entry_id, budget_account_entry_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->update_budget_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->update_budget_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **budget_account_entry_update_dto** | [**BudgetAccountEntryUpdateDto**](BudgetAccountEntryUpdateDto.md)|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget_async**
> EmptyEnvelope update_budget_async(tenant_id, budget_id, budget_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates a budget

Update a budget

### Example


```python
import openapi_client
from openapi_client.models.budget_update_dto import BudgetUpdateDto
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
    api_instance = openapi_client.BudgetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    budget_id = 'budget_id_example' # str | 
    budget_update_dto = openapi_client.BudgetUpdateDto() # BudgetUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates a budget
        api_response = api_instance.update_budget_async(tenant_id, budget_id, budget_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BudgetsApi->update_budget_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->update_budget_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **budget_id** | **str**|  | 
 **budget_update_dto** | [**BudgetUpdateDto**](BudgetUpdateDto.md)|  | 
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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

