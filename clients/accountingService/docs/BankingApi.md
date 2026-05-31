# openapi_client.BankingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank**](BankingApi.md#create_bank) | **POST** /api/v2/AccountingService/Banking | Creates a new bank
[**create_bank_account**](BankingApi.md#create_bank_account) | **POST** /api/v2/AccountingService/Banking/{bankId}/Accounts | Creates a new bank account
[**create_bank_guarantee**](BankingApi.md#create_bank_guarantee) | **POST** /api/v2/AccountingService/Banking/{bankId}/Guarantees | Creates a new bank guarantee
[**create_bank_transaction**](BankingApi.md#create_bank_transaction) | **POST** /api/v2/AccountingService/Banking/{bankId}/Transactions | Creates a new bank transaction
[**delete_bank**](BankingApi.md#delete_bank) | **DELETE** /api/v2/AccountingService/Banking/{bankId} | Deletes a bank
[**delete_bank_account**](BankingApi.md#delete_bank_account) | **DELETE** /api/v2/AccountingService/Banking/{bankId}/Accounts/{accountId} | Deletes a bank account
[**delete_bank_guarantee**](BankingApi.md#delete_bank_guarantee) | **DELETE** /api/v2/AccountingService/Banking/{bankId}/Guarantees/{guaranteeId} | Deletes a bank guarantee
[**delete_bank_transaction**](BankingApi.md#delete_bank_transaction) | **DELETE** /api/v2/AccountingService/Banking/{bankId}/Transactions/{transactionId} | Deletes a bank transaction
[**get_bank**](BankingApi.md#get_bank) | **GET** /api/v2/AccountingService/Banking/{bankId} | Gets the current tenant bank
[**get_bank_account**](BankingApi.md#get_bank_account) | **GET** /api/v2/AccountingService/Banking/{bankId}/Accounts/{accountId} | Gets the current tenant bank account
[**get_bank_accounts**](BankingApi.md#get_bank_accounts) | **GET** /api/v2/AccountingService/Banking/{bankId}/Accounts | Gets the current tenant bank accounts
[**get_bank_accounts_count**](BankingApi.md#get_bank_accounts_count) | **GET** /api/v2/AccountingService/Banking/{bankId}/Accounts/Count | Gets the current tenant bank accounts count
[**get_bank_guarantee**](BankingApi.md#get_bank_guarantee) | **GET** /api/v2/AccountingService/Banking/{bankId}/Guarantees/{guaranteeId} | Gets the current tenant bank guarantee
[**get_bank_guarantees**](BankingApi.md#get_bank_guarantees) | **GET** /api/v2/AccountingService/Banking/{bankId}/Guarantees | Gets the current tenant bank guarantees
[**get_bank_guarantees_count**](BankingApi.md#get_bank_guarantees_count) | **GET** /api/v2/AccountingService/Banking/{bankId}/Guarantees/Count | Gets the current tenant bank guarantees count
[**get_bank_transaction**](BankingApi.md#get_bank_transaction) | **GET** /api/v2/AccountingService/Banking/{bankId}/Transactions/{transactionId} | Gets the current tenant bank transaction
[**get_bank_transactions**](BankingApi.md#get_bank_transactions) | **GET** /api/v2/AccountingService/Banking/{bankId}/Transactions | Gets the current tenant bank transactions
[**get_bank_transactions_count**](BankingApi.md#get_bank_transactions_count) | **GET** /api/v2/AccountingService/Banking/{bankId}/Transactions/Count | Gets the current tenant bank transactions count
[**get_banks**](BankingApi.md#get_banks) | **GET** /api/v2/AccountingService/Banking | Gets the current tenant banks
[**get_banks_count**](BankingApi.md#get_banks_count) | **GET** /api/v2/AccountingService/Banking/Count | Gets the current tenant banks count
[**update_bank**](BankingApi.md#update_bank) | **PUT** /api/v2/AccountingService/Banking/{bankId} | Updates a bank
[**update_bank_account**](BankingApi.md#update_bank_account) | **PUT** /api/v2/AccountingService/Banking/{bankId}/Accounts/{accountId} | Updates a bank account
[**update_bank_guarantee**](BankingApi.md#update_bank_guarantee) | **PUT** /api/v2/AccountingService/Banking/{bankId}/Guarantees/{guaranteeId} | Updates a bank guarantee
[**update_bank_transaction**](BankingApi.md#update_bank_transaction) | **PUT** /api/v2/AccountingService/Banking/{bankId}/Transactions/{transactionId} | Updates a bank transaction


# **create_bank**
> BankDtoEnvelope create_bank(tenant_id, api_version=api_version, x_api_version=x_api_version, bank_create_dto=bank_create_dto)

Creates a new bank

Create a new bank.

### Example


```python
import openapi_client
from openapi_client.models.bank_create_dto import BankCreateDto
from openapi_client.models.bank_dto_envelope import BankDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_create_dto = openapi_client.BankCreateDto() # BankCreateDto |  (optional)

    try:
        # Creates a new bank
        api_response = api_instance.create_bank(tenant_id, api_version=api_version, x_api_version=x_api_version, bank_create_dto=bank_create_dto)
        print("The response of BankingApi->create_bank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->create_bank: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_create_dto** | [**BankCreateDto**](BankCreateDto.md)|  | [optional] 

### Return type

[**BankDtoEnvelope**](BankDtoEnvelope.md)

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

# **create_bank_account**
> BankAccountDtoEnvelope create_bank_account(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_account_create_dto=bank_account_create_dto)

Creates a new bank account

Create a new bank account.

### Example


```python
import openapi_client
from openapi_client.models.bank_account_create_dto import BankAccountCreateDto
from openapi_client.models.bank_account_dto_envelope import BankAccountDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_account_create_dto = openapi_client.BankAccountCreateDto() # BankAccountCreateDto |  (optional)

    try:
        # Creates a new bank account
        api_response = api_instance.create_bank_account(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_account_create_dto=bank_account_create_dto)
        print("The response of BankingApi->create_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->create_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_account_create_dto** | [**BankAccountCreateDto**](BankAccountCreateDto.md)|  | [optional] 

### Return type

[**BankAccountDtoEnvelope**](BankAccountDtoEnvelope.md)

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

# **create_bank_guarantee**
> BankGuaranteeDtoEnvelope create_bank_guarantee(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_guarantee_create_dto=bank_guarantee_create_dto)

Creates a new bank guarantee

Create a new bank guarantee.

### Example


```python
import openapi_client
from openapi_client.models.bank_guarantee_create_dto import BankGuaranteeCreateDto
from openapi_client.models.bank_guarantee_dto_envelope import BankGuaranteeDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_guarantee_create_dto = openapi_client.BankGuaranteeCreateDto() # BankGuaranteeCreateDto |  (optional)

    try:
        # Creates a new bank guarantee
        api_response = api_instance.create_bank_guarantee(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_guarantee_create_dto=bank_guarantee_create_dto)
        print("The response of BankingApi->create_bank_guarantee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->create_bank_guarantee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_guarantee_create_dto** | [**BankGuaranteeCreateDto**](BankGuaranteeCreateDto.md)|  | [optional] 

### Return type

[**BankGuaranteeDtoEnvelope**](BankGuaranteeDtoEnvelope.md)

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

# **create_bank_transaction**
> BankTransactionDtoEnvelope create_bank_transaction(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_transaction_create_dto=bank_transaction_create_dto)

Creates a new bank transaction

Create a new bank transaction.

### Example


```python
import openapi_client
from openapi_client.models.bank_transaction_create_dto import BankTransactionCreateDto
from openapi_client.models.bank_transaction_dto_envelope import BankTransactionDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_transaction_create_dto = openapi_client.BankTransactionCreateDto() # BankTransactionCreateDto |  (optional)

    try:
        # Creates a new bank transaction
        api_response = api_instance.create_bank_transaction(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_transaction_create_dto=bank_transaction_create_dto)
        print("The response of BankingApi->create_bank_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->create_bank_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_transaction_create_dto** | [**BankTransactionCreateDto**](BankTransactionCreateDto.md)|  | [optional] 

### Return type

[**BankTransactionDtoEnvelope**](BankTransactionDtoEnvelope.md)

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

# **delete_bank**
> delete_bank(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Deletes a bank

Delete a bank.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a bank
        api_instance.delete_bank(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BankingApi->delete_bank: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bank_account**
> delete_bank_account(tenant_id, bank_id, account_id, api_version=api_version, x_api_version=x_api_version)

Deletes a bank account

Delete a bank account.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a bank account
        api_instance.delete_bank_account(tenant_id, bank_id, account_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BankingApi->delete_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bank_guarantee**
> delete_bank_guarantee(tenant_id, bank_id, guarantee_id, api_version=api_version, x_api_version=x_api_version)

Deletes a bank guarantee

Delete a bank guarantee.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    guarantee_id = 'guarantee_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a bank guarantee
        api_instance.delete_bank_guarantee(tenant_id, bank_id, guarantee_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BankingApi->delete_bank_guarantee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **guarantee_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bank_transaction**
> delete_bank_transaction(tenant_id, bank_id, transaction_id, api_version=api_version, x_api_version=x_api_version)

Deletes a bank transaction

Delete a bank transaction.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a bank transaction
        api_instance.delete_bank_transaction(tenant_id, bank_id, transaction_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BankingApi->delete_bank_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank**
> BankDtoEnvelope get_bank(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank

Get the currently acting tenant bank.

### Example


```python
import openapi_client
from openapi_client.models.bank_dto_envelope import BankDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank
        api_response = api_instance.get_bank(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankDtoEnvelope**](BankDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_account**
> BankAccountDtoEnvelope get_bank_account(tenant_id, bank_id, account_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank account

Get the currently acting tenant bank account.

### Example


```python
import openapi_client
from openapi_client.models.bank_account_dto_envelope import BankAccountDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank account
        api_response = api_instance.get_bank_account(tenant_id, bank_id, account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankAccountDtoEnvelope**](BankAccountDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_accounts**
> BankAccountDtoListEnvelope get_bank_accounts(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank accounts

Get the currently acting tenant bank accounts.

### Example


```python
import openapi_client
from openapi_client.models.bank_account_dto_list_envelope import BankAccountDtoListEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank accounts
        api_response = api_instance.get_bank_accounts(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankAccountDtoListEnvelope**](BankAccountDtoListEnvelope.md)

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

# **get_bank_accounts_count**
> Int32Envelope get_bank_accounts_count(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank accounts count

Get the currently acting tenant bank accounts count.

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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank accounts count
        api_response = api_instance.get_bank_accounts_count(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_accounts_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_accounts_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
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

# **get_bank_guarantee**
> BankGuaranteeDtoEnvelope get_bank_guarantee(tenant_id, bank_id, guarantee_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank guarantee

Get the currently acting tenant bank guarantee.

### Example


```python
import openapi_client
from openapi_client.models.bank_guarantee_dto_envelope import BankGuaranteeDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    guarantee_id = 'guarantee_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank guarantee
        api_response = api_instance.get_bank_guarantee(tenant_id, bank_id, guarantee_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_guarantee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_guarantee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **guarantee_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankGuaranteeDtoEnvelope**](BankGuaranteeDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_guarantees**
> BankGuaranteeDtoListEnvelope get_bank_guarantees(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank guarantees

Get the currently acting tenant bank guarantees.

### Example


```python
import openapi_client
from openapi_client.models.bank_guarantee_dto_list_envelope import BankGuaranteeDtoListEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank guarantees
        api_response = api_instance.get_bank_guarantees(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_guarantees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_guarantees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankGuaranteeDtoListEnvelope**](BankGuaranteeDtoListEnvelope.md)

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

# **get_bank_guarantees_count**
> Int32Envelope get_bank_guarantees_count(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank guarantees count

Get the currently acting tenant bank guarantees count.

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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank guarantees count
        api_response = api_instance.get_bank_guarantees_count(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_guarantees_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_guarantees_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
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

# **get_bank_transaction**
> BankTransactionDtoEnvelope get_bank_transaction(tenant_id, bank_id, transaction_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank transaction

Get the currently acting tenant bank transaction.

### Example


```python
import openapi_client
from openapi_client.models.bank_transaction_dto_envelope import BankTransactionDtoEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank transaction
        api_response = api_instance.get_bank_transaction(tenant_id, bank_id, transaction_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankTransactionDtoEnvelope**](BankTransactionDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transactions**
> BankTransactionDtoListEnvelope get_bank_transactions(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank transactions

Get the currently acting tenant bank transactions.

### Example


```python
import openapi_client
from openapi_client.models.bank_transaction_dto_list_envelope import BankTransactionDtoListEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank transactions
        api_response = api_instance.get_bank_transactions(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankTransactionDtoListEnvelope**](BankTransactionDtoListEnvelope.md)

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

# **get_bank_transactions_count**
> Int32Envelope get_bank_transactions_count(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant bank transactions count

Get the currently acting tenant bank transactions count.

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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant bank transactions count
        api_response = api_instance.get_bank_transactions_count(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_bank_transactions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_bank_transactions_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
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

# **get_banks**
> BankDtoListEnvelope get_banks(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant banks

Get the currently acting tenant banks.

### Example


```python
import openapi_client
from openapi_client.models.bank_dto_list_envelope import BankDtoListEnvelope
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant banks
        api_response = api_instance.get_banks(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_banks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_banks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankDtoListEnvelope**](BankDtoListEnvelope.md)

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

# **get_banks_count**
> Int32Envelope get_banks_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant banks count

Get the currently acting tenant banks count.

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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant banks count
        api_response = api_instance.get_banks_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankingApi->get_banks_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->get_banks_count: %s\n" % e)
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

# **update_bank**
> BankDtoEnvelope update_bank(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_update_dto=bank_update_dto)

Updates a bank

Update a bank.

### Example


```python
import openapi_client
from openapi_client.models.bank_dto_envelope import BankDtoEnvelope
from openapi_client.models.bank_update_dto import BankUpdateDto
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_update_dto = openapi_client.BankUpdateDto() # BankUpdateDto |  (optional)

    try:
        # Updates a bank
        api_response = api_instance.update_bank(tenant_id, bank_id, api_version=api_version, x_api_version=x_api_version, bank_update_dto=bank_update_dto)
        print("The response of BankingApi->update_bank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->update_bank: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_update_dto** | [**BankUpdateDto**](BankUpdateDto.md)|  | [optional] 

### Return type

[**BankDtoEnvelope**](BankDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_account**
> BankAccountDtoEnvelope update_bank_account(tenant_id, bank_id, account_id, api_version=api_version, x_api_version=x_api_version, bank_account_update_dto=bank_account_update_dto)

Updates a bank account

Update a bank account.

### Example


```python
import openapi_client
from openapi_client.models.bank_account_dto_envelope import BankAccountDtoEnvelope
from openapi_client.models.bank_account_update_dto import BankAccountUpdateDto
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    account_id = 'account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_account_update_dto = openapi_client.BankAccountUpdateDto() # BankAccountUpdateDto |  (optional)

    try:
        # Updates a bank account
        api_response = api_instance.update_bank_account(tenant_id, bank_id, account_id, api_version=api_version, x_api_version=x_api_version, bank_account_update_dto=bank_account_update_dto)
        print("The response of BankingApi->update_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->update_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_account_update_dto** | [**BankAccountUpdateDto**](BankAccountUpdateDto.md)|  | [optional] 

### Return type

[**BankAccountDtoEnvelope**](BankAccountDtoEnvelope.md)

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

# **update_bank_guarantee**
> BankGuaranteeDtoEnvelope update_bank_guarantee(tenant_id, bank_id, guarantee_id, api_version=api_version, x_api_version=x_api_version, bank_guarantee_update_dto=bank_guarantee_update_dto)

Updates a bank guarantee

Update a bank guarantee.

### Example


```python
import openapi_client
from openapi_client.models.bank_guarantee_dto_envelope import BankGuaranteeDtoEnvelope
from openapi_client.models.bank_guarantee_update_dto import BankGuaranteeUpdateDto
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    guarantee_id = 'guarantee_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_guarantee_update_dto = openapi_client.BankGuaranteeUpdateDto() # BankGuaranteeUpdateDto |  (optional)

    try:
        # Updates a bank guarantee
        api_response = api_instance.update_bank_guarantee(tenant_id, bank_id, guarantee_id, api_version=api_version, x_api_version=x_api_version, bank_guarantee_update_dto=bank_guarantee_update_dto)
        print("The response of BankingApi->update_bank_guarantee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->update_bank_guarantee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **guarantee_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_guarantee_update_dto** | [**BankGuaranteeUpdateDto**](BankGuaranteeUpdateDto.md)|  | [optional] 

### Return type

[**BankGuaranteeDtoEnvelope**](BankGuaranteeDtoEnvelope.md)

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

# **update_bank_transaction**
> BankTransactionDtoEnvelope update_bank_transaction(tenant_id, bank_id, transaction_id, api_version=api_version, x_api_version=x_api_version, bank_transaction_update_dto=bank_transaction_update_dto)

Updates a bank transaction

Update a bank transaction.

### Example


```python
import openapi_client
from openapi_client.models.bank_transaction_dto_envelope import BankTransactionDtoEnvelope
from openapi_client.models.bank_transaction_update_dto import BankTransactionUpdateDto
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
    api_instance = openapi_client.BankingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bank_id = 'bank_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_transaction_update_dto = openapi_client.BankTransactionUpdateDto() # BankTransactionUpdateDto |  (optional)

    try:
        # Updates a bank transaction
        api_response = api_instance.update_bank_transaction(tenant_id, bank_id, transaction_id, api_version=api_version, x_api_version=x_api_version, bank_transaction_update_dto=bank_transaction_update_dto)
        print("The response of BankingApi->update_bank_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankingApi->update_bank_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bank_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_transaction_update_dto** | [**BankTransactionUpdateDto**](BankTransactionUpdateDto.md)|  | [optional] 

### Return type

[**BankTransactionDtoEnvelope**](BankTransactionDtoEnvelope.md)

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

