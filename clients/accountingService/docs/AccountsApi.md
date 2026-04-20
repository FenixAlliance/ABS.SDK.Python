# openapi_client.AccountsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_account_async**](AccountsApi.md#balance_account_async) | **POST** /api/v2/AccountingService/Accounts/{accountId}/Balance | Balance account
[**balance_root_account_async**](AccountsApi.md#balance_root_account_async) | **POST** /api/v2/AccountingService/Accounts/Root/Balance | Balance root account
[**create_account_async**](AccountsApi.md#create_account_async) | **POST** /api/v2/AccountingService/Accounts | Get root accounts
[**create_account_credit_async**](AccountsApi.md#create_account_credit_async) | **POST** /api/v2/AccountingService/Accounts/{accountId}/Credits | Create account credit
[**create_account_debit_async**](AccountsApi.md#create_account_debit_async) | **POST** /api/v2/AccountingService/Accounts/{accountId}/Debits | Create account debit
[**create_account_entry_async**](AccountsApi.md#create_account_entry_async) | **POST** /api/v2/AccountingService/Accounts/{accountId}/Entries | Create account entry
[**create_account_relation_async**](AccountsApi.md#create_account_relation_async) | **POST** /api/v2/AccountingService/Accounts/Relations | Create account relation
[**create_account_type_async**](AccountsApi.md#create_account_type_async) | **POST** /api/v2/AccountingService/Accounts/Types | Create account type
[**delete_account_async**](AccountsApi.md#delete_account_async) | **DELETE** /api/v2/AccountingService/Accounts/{accountId} | Delete an account
[**delete_account_entry_async**](AccountsApi.md#delete_account_entry_async) | **DELETE** /api/v2/AccountingService/Accounts/{accountId}/Entries/{entryId} | Delete account entry
[**delete_account_relation_async**](AccountsApi.md#delete_account_relation_async) | **DELETE** /api/v2/AccountingService/Accounts/Relations/{accountRelationId} | Delete account relation
[**delete_account_type_async**](AccountsApi.md#delete_account_type_async) | **DELETE** /api/v2/AccountingService/Accounts/Types/{accountTypeId} | Delete account type
[**get_account_aggregate_async**](AccountsApi.md#get_account_aggregate_async) | **POST** /api/v2/AccountingService/Accounts/Aggregate | Get account aggregate
[**get_account_credits_async**](AccountsApi.md#get_account_credits_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Credits | Get account credits
[**get_account_credits_count_async**](AccountsApi.md#get_account_credits_count_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Credits/Count | Get account credits count
[**get_account_debits_async**](AccountsApi.md#get_account_debits_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Debits | Get account debits
[**get_account_debits_count_async**](AccountsApi.md#get_account_debits_count_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Debits/Count | Get account debits count
[**get_account_details_async**](AccountsApi.md#get_account_details_async) | **GET** /api/v2/AccountingService/Accounts/{accountId} | Get account details
[**get_account_entries_async**](AccountsApi.md#get_account_entries_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Entries | Get account entries
[**get_account_entry_async**](AccountsApi.md#get_account_entry_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Entries/{entryId} | Get account entry
[**get_account_relations_async**](AccountsApi.md#get_account_relations_async) | **GET** /api/v2/AccountingService/Accounts/Relations | Get account relations
[**get_account_relations_count_async**](AccountsApi.md#get_account_relations_count_async) | **GET** /api/v2/AccountingService/Accounts/Relations/Count | Get account relations count
[**get_account_types_async**](AccountsApi.md#get_account_types_async) | **GET** /api/v2/AccountingService/Accounts/Types | Get account types
[**get_account_types_count_async**](AccountsApi.md#get_account_types_count_async) | **GET** /api/v2/AccountingService/Accounts/Types/Count | Get account types count
[**get_accounts_async**](AccountsApi.md#get_accounts_async) | **GET** /api/v2/AccountingService/Accounts | Creates a new account
[**get_accounts_count_async**](AccountsApi.md#get_accounts_count_async) | **GET** /api/v2/AccountingService/Accounts/Count | Get the number of accounts
[**get_child_accounts_async**](AccountsApi.md#get_child_accounts_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Children | Get child accounts
[**get_credit_account_entries_async**](AccountsApi.md#get_credit_account_entries_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Entries/Credit | Get credit account entries
[**get_debit_account_entries_async**](AccountsApi.md#get_debit_account_entries_async) | **GET** /api/v2/AccountingService/Accounts/{accountId}/Entries/Debit | Get debit account entries
[**get_root_accounts_async**](AccountsApi.md#get_root_accounts_async) | **GET** /api/v2/AccountingService/Accounts/Root | Get root accounts
[**patch_account_async**](AccountsApi.md#patch_account_async) | **PATCH** /api/v2/AccountingService/Accounts/{accountId} | Patch an account
[**update_account_async**](AccountsApi.md#update_account_async) | **PUT** /api/v2/AccountingService/Accounts/{accountId} | Update an account
[**update_account_entry_async**](AccountsApi.md#update_account_entry_async) | **PUT** /api/v2/AccountingService/Accounts/{accountId}/Entries/{entryId} | Update account entry
[**update_account_relation_async**](AccountsApi.md#update_account_relation_async) | **PUT** /api/v2/AccountingService/Accounts/Relations/{accountRelationId} | Update account relation
[**update_account_type_async**](AccountsApi.md#update_account_type_async) | **PUT** /api/v2/AccountingService/Accounts/Types/{accountTypeId} | Update account type


# **balance_account_async**
> AccountDtoEnvelope balance_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Balance account

Balance account.

### Example


```python
import openapi_client
from openapi_client.models.account_dto_envelope import AccountDtoEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Balance account
        api_response = api_instance.balance_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->balance_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->balance_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountDtoEnvelope**](AccountDtoEnvelope.md)

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

# **balance_root_account_async**
> AccountDtoListEnvelope balance_root_account_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Balance root account

Balance root account.

### Example


```python
import openapi_client
from openapi_client.models.account_dto_list_envelope import AccountDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Balance root account
        api_response = api_instance.balance_root_account_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->balance_root_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->balance_root_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountDtoListEnvelope**](AccountDtoListEnvelope.md)

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

# **create_account_async**
> AccountDtoListEnvelope create_account_async(tenant_id, api_version=api_version, x_api_version=x_api_version, account_create_dto=account_create_dto)

Get root accounts

Get root accounts.

### Example


```python
import openapi_client
from openapi_client.models.account_create_dto import AccountCreateDto
from openapi_client.models.account_dto_list_envelope import AccountDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_create_dto = openapi_client.AccountCreateDto() # AccountCreateDto |  (optional)

    try:
        # Get root accounts
        api_response = api_instance.create_account_async(tenant_id, api_version=api_version, x_api_version=x_api_version, account_create_dto=account_create_dto)
        print("The response of AccountsApi->create_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_create_dto** | [**AccountCreateDto**](AccountCreateDto.md)|  | [optional] 

### Return type

[**AccountDtoListEnvelope**](AccountDtoListEnvelope.md)

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

# **create_account_credit_async**
> AccountingEntryDtoListEnvelope create_account_credit_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_create_dto=accounting_entry_create_dto)

Create account credit

Create account credit.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_create_dto import AccountingEntryCreateDto
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    accounting_entry_create_dto = openapi_client.AccountingEntryCreateDto() # AccountingEntryCreateDto |  (optional)

    try:
        # Create account credit
        api_response = api_instance.create_account_credit_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_create_dto=accounting_entry_create_dto)
        print("The response of AccountsApi->create_account_credit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account_credit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **accounting_entry_create_dto** | [**AccountingEntryCreateDto**](AccountingEntryCreateDto.md)|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **create_account_debit_async**
> AccountingEntryDtoListEnvelope create_account_debit_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_create_dto=accounting_entry_create_dto)

Create account debit

Create account debit.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_create_dto import AccountingEntryCreateDto
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    accounting_entry_create_dto = openapi_client.AccountingEntryCreateDto() # AccountingEntryCreateDto |  (optional)

    try:
        # Create account debit
        api_response = api_instance.create_account_debit_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_create_dto=accounting_entry_create_dto)
        print("The response of AccountsApi->create_account_debit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account_debit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **accounting_entry_create_dto** | [**AccountingEntryCreateDto**](AccountingEntryCreateDto.md)|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **create_account_entry_async**
> AccountingEntryDtoEnvelope create_account_entry_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_create_dto=accounting_entry_create_dto)

Create account entry

Create account entry.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_create_dto import AccountingEntryCreateDto
from openapi_client.models.accounting_entry_dto_envelope import AccountingEntryDtoEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    accounting_entry_create_dto = openapi_client.AccountingEntryCreateDto() # AccountingEntryCreateDto |  (optional)

    try:
        # Create account entry
        api_response = api_instance.create_account_entry_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_create_dto=accounting_entry_create_dto)
        print("The response of AccountsApi->create_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **accounting_entry_create_dto** | [**AccountingEntryCreateDto**](AccountingEntryCreateDto.md)|  | [optional] 

### Return type

[**AccountingEntryDtoEnvelope**](AccountingEntryDtoEnvelope.md)

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_relation_async**
> EmptyEnvelope create_account_relation_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, account_relation_create_dto=account_relation_create_dto)

Create account relation

Create account relation.

### Example


```python
import openapi_client
from openapi_client.models.account_relation_create_dto import AccountRelationCreateDto
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_relation_create_dto = openapi_client.AccountRelationCreateDto() # AccountRelationCreateDto |  (optional)

    try:
        # Create account relation
        api_response = api_instance.create_account_relation_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, account_relation_create_dto=account_relation_create_dto)
        print("The response of AccountsApi->create_account_relation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account_relation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_relation_create_dto** | [**AccountRelationCreateDto**](AccountRelationCreateDto.md)|  | [optional] 

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

# **create_account_type_async**
> EmptyEnvelope create_account_type_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, account_type_create_dto=account_type_create_dto)

Create account type

Create account type.

### Example


```python
import openapi_client
from openapi_client.models.account_type_create_dto import AccountTypeCreateDto
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_type_create_dto = openapi_client.AccountTypeCreateDto() # AccountTypeCreateDto |  (optional)

    try:
        # Create account type
        api_response = api_instance.create_account_type_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, account_type_create_dto=account_type_create_dto)
        print("The response of AccountsApi->create_account_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_type_create_dto** | [**AccountTypeCreateDto**](AccountTypeCreateDto.md)|  | [optional] 

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

# **delete_account_async**
> EmptyEnvelope delete_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Delete an account

Delete an account.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an account
        api_response = api_instance.delete_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->delete_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
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

# **delete_account_entry_async**
> EmptyEnvelope delete_account_entry_async(tenant_id, account_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Delete account entry

Delete account entry.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete account entry
        api_response = api_instance.delete_account_entry_async(tenant_id, account_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->delete_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_relation_async**
> EmptyEnvelope delete_account_relation_async(tenant_id, account_relation_id, account_id, api_version=api_version, x_api_version=x_api_version)

Delete account relation

Delete account relation.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_relation_id = 'account_relation_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete account relation
        api_response = api_instance.delete_account_relation_async(tenant_id, account_relation_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->delete_account_relation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_account_relation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_relation_id** | **str**|  | 
 **account_id** | **str**|  | 
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

# **delete_account_type_async**
> EmptyEnvelope delete_account_type_async(tenant_id, account_type_id, account_id, api_version=api_version, x_api_version=x_api_version)

Delete account type

Delete account type.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_type_id = 'account_type_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete account type
        api_response = api_instance.delete_account_type_async(tenant_id, account_type_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->delete_account_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_account_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_type_id** | **str**|  | 
 **account_id** | **str**|  | 
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

# **get_account_aggregate_async**
> AccountingEntryDtoListEnvelope get_account_aggregate_async(tenant_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version, account_dto=account_dto)

Get account aggregate

Get account aggregate.

### Example


```python
import openapi_client
from openapi_client.models.account_dto import AccountDto
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    currency_id = 'currency_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_dto = [openapi_client.AccountDto()] # List[AccountDto] |  (optional)

    try:
        # Get account aggregate
        api_response = api_instance.get_account_aggregate_async(tenant_id, currency_id=currency_id, api_version=api_version, x_api_version=x_api_version, account_dto=account_dto)
        print("The response of AccountsApi->get_account_aggregate_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_aggregate_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **currency_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_dto** | [**List[AccountDto]**](AccountDto.md)|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **get_account_credits_async**
> AccountingEntryDtoListEnvelope get_account_credits_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account credits

Get account credits.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account credits
        api_response = api_instance.get_account_credits_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_credits_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_credits_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **get_account_credits_count_async**
> Int32Envelope get_account_credits_count_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account credits count

Get account credits count.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account credits count
        api_response = api_instance.get_account_credits_count_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_credits_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_credits_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
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

# **get_account_debits_async**
> AccountingEntryDtoListEnvelope get_account_debits_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account debits

Get account debits.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account debits
        api_response = api_instance.get_account_debits_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_debits_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_debits_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **get_account_debits_count_async**
> Int32Envelope get_account_debits_count_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account debits count

Get account debits count.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account debits count
        api_response = api_instance.get_account_debits_count_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_debits_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_debits_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
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

# **get_account_details_async**
> AccountDtoEnvelope get_account_details_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account details

Get account details.

### Example


```python
import openapi_client
from openapi_client.models.account_dto_envelope import AccountDtoEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account details
        api_response = api_instance.get_account_details_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountDtoEnvelope**](AccountDtoEnvelope.md)

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

# **get_account_entries_async**
> AccountingEntryDtoListEnvelope get_account_entries_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account entries

Get account entries.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account entries
        api_response = api_instance.get_account_entries_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_entries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **get_account_entry_async**
> AccountingEntryDtoEnvelope get_account_entry_async(tenant_id, account_id, entry_id, api_version=api_version, x_api_version=x_api_version)

Get account entry

Get account entry.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_dto_envelope import AccountingEntryDtoEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account entry
        api_response = api_instance.get_account_entry_async(tenant_id, account_id, entry_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingEntryDtoEnvelope**](AccountingEntryDtoEnvelope.md)

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

# **get_account_relations_async**
> AccountRelationDtoListEnvelope get_account_relations_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account relations

Get account relations.

### Example


```python
import openapi_client
from openapi_client.models.account_relation_dto_list_envelope import AccountRelationDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account relations
        api_response = api_instance.get_account_relations_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_relations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_relations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountRelationDtoListEnvelope**](AccountRelationDtoListEnvelope.md)

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

# **get_account_relations_count_async**
> Int32Envelope get_account_relations_count_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get account relations count

Get account relations count.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account relations count
        api_response = api_instance.get_account_relations_count_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_relations_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_relations_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
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

# **get_account_types_async**
> AccountTypeDtoListEnvelope get_account_types_async(tenant_id, account_type_id, api_version=api_version, x_api_version=x_api_version)

Get account types

Get account types.

### Example


```python
import openapi_client
from openapi_client.models.account_type_dto_list_envelope import AccountTypeDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_type_id = 'account_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account types
        api_response = api_instance.get_account_types_async(tenant_id, account_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_types_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_types_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountTypeDtoListEnvelope**](AccountTypeDtoListEnvelope.md)

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

# **get_account_types_count_async**
> Int32Envelope get_account_types_count_async(tenant_id, account_type_id, api_version=api_version, x_api_version=x_api_version)

Get account types count

Get account types count.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_type_id = 'account_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get account types count
        api_response = api_instance.get_account_types_count_async(tenant_id, account_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_account_types_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_types_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_type_id** | **str**|  | 
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

# **get_accounts_async**
> AccountDtoListEnvelope get_accounts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Creates a new account

Creates a new account.

### Example


```python
import openapi_client
from openapi_client.models.account_dto_list_envelope import AccountDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a new account
        api_response = api_instance.get_accounts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_accounts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_accounts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountDtoListEnvelope**](AccountDtoListEnvelope.md)

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

# **get_accounts_count_async**
> Int32Envelope get_accounts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the number of accounts

Get the number of accounts.

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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the number of accounts
        api_response = api_instance.get_accounts_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_accounts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_accounts_count_async: %s\n" % e)
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

# **get_child_accounts_async**
> AccountDtoListEnvelope get_child_accounts_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get child accounts

Get child accounts.

### Example


```python
import openapi_client
from openapi_client.models.account_dto_list_envelope import AccountDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get child accounts
        api_response = api_instance.get_child_accounts_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_child_accounts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_child_accounts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountDtoListEnvelope**](AccountDtoListEnvelope.md)

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

# **get_credit_account_entries_async**
> AccountingEntryDtoListEnvelope get_credit_account_entries_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get credit account entries

Get credit account entries.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get credit account entries
        api_response = api_instance.get_credit_account_entries_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_credit_account_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_credit_account_entries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **get_debit_account_entries_async**
> AccountingEntryDtoListEnvelope get_debit_account_entries_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)

Get debit account entries

Get debit account entries.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_dto_list_envelope import AccountingEntryDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get debit account entries
        api_response = api_instance.get_debit_account_entries_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_debit_account_entries_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_debit_account_entries_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountingEntryDtoListEnvelope**](AccountingEntryDtoListEnvelope.md)

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

# **get_root_accounts_async**
> AccountDtoListEnvelope get_root_accounts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get root accounts

Get root accounts.

### Example


```python
import openapi_client
from openapi_client.models.account_dto_list_envelope import AccountDtoListEnvelope
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get root accounts
        api_response = api_instance.get_root_accounts_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of AccountsApi->get_root_accounts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_root_accounts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AccountDtoListEnvelope**](AccountDtoListEnvelope.md)

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

# **patch_account_async**
> EmptyEnvelope patch_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch an account

Patch an account.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch an account
        api_response = api_instance.patch_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of AccountsApi->patch_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->patch_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_async**
> AccountDtoEnvelope update_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, account_update_dto=account_update_dto)

Update an account

Update an account.

### Example


```python
import openapi_client
from openapi_client.models.account_dto_envelope import AccountDtoEnvelope
from openapi_client.models.account_update_dto import AccountUpdateDto
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_update_dto = openapi_client.AccountUpdateDto() # AccountUpdateDto |  (optional)

    try:
        # Update an account
        api_response = api_instance.update_account_async(tenant_id, account_id, api_version=api_version, x_api_version=x_api_version, account_update_dto=account_update_dto)
        print("The response of AccountsApi->update_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_update_dto** | [**AccountUpdateDto**](AccountUpdateDto.md)|  | [optional] 

### Return type

[**AccountDtoEnvelope**](AccountDtoEnvelope.md)

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

# **update_account_entry_async**
> EmptyEnvelope update_account_entry_async(tenant_id, account_id, entry_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_update_dto=accounting_entry_update_dto)

Update account entry

Update account entry.

### Example


```python
import openapi_client
from openapi_client.models.accounting_entry_update_dto import AccountingEntryUpdateDto
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_id = 'account_id_example' # str | 
    entry_id = 'entry_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    accounting_entry_update_dto = openapi_client.AccountingEntryUpdateDto() # AccountingEntryUpdateDto |  (optional)

    try:
        # Update account entry
        api_response = api_instance.update_account_entry_async(tenant_id, account_id, entry_id, api_version=api_version, x_api_version=x_api_version, accounting_entry_update_dto=accounting_entry_update_dto)
        print("The response of AccountsApi->update_account_entry_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account_entry_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_id** | **str**|  | 
 **entry_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **accounting_entry_update_dto** | [**AccountingEntryUpdateDto**](AccountingEntryUpdateDto.md)|  | [optional] 

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

# **update_account_relation_async**
> EmptyEnvelope update_account_relation_async(tenant_id, account_relation_id, account_id, api_version=api_version, x_api_version=x_api_version, account_relation_update_dto=account_relation_update_dto)

Update account relation

Update account relation.

### Example


```python
import openapi_client
from openapi_client.models.account_relation_update_dto import AccountRelationUpdateDto
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_relation_id = 'account_relation_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_relation_update_dto = openapi_client.AccountRelationUpdateDto() # AccountRelationUpdateDto |  (optional)

    try:
        # Update account relation
        api_response = api_instance.update_account_relation_async(tenant_id, account_relation_id, account_id, api_version=api_version, x_api_version=x_api_version, account_relation_update_dto=account_relation_update_dto)
        print("The response of AccountsApi->update_account_relation_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account_relation_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_relation_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_relation_update_dto** | [**AccountRelationUpdateDto**](AccountRelationUpdateDto.md)|  | [optional] 

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

# **update_account_type_async**
> EmptyEnvelope update_account_type_async(tenant_id, account_type_id, account_id, api_version=api_version, x_api_version=x_api_version, account_type_update_dto=account_type_update_dto)

Update account type

Update account type.

### Example


```python
import openapi_client
from openapi_client.models.account_type_update_dto import AccountTypeUpdateDto
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
    api_instance = openapi_client.AccountsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    account_type_id = 'account_type_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    account_type_update_dto = openapi_client.AccountTypeUpdateDto() # AccountTypeUpdateDto |  (optional)

    try:
        # Update account type
        api_response = api_instance.update_account_type_async(tenant_id, account_type_id, account_id, api_version=api_version, x_api_version=x_api_version, account_type_update_dto=account_type_update_dto)
        print("The response of AccountsApi->update_account_type_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account_type_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **account_type_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **account_type_update_dto** | [**AccountTypeUpdateDto**](AccountTypeUpdateDto.md)|  | [optional] 

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

