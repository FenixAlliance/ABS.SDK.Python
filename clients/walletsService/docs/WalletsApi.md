# openapi_client.WalletsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wallet_bank_account_async**](WalletsApi.md#create_wallet_bank_account_async) | **POST** /api/v2/WalletsService/Wallets/{walletId}/BankAccounts | Create Wallet Bank Account
[**create_wallet_location_async**](WalletsApi.md#create_wallet_location_async) | **POST** /api/v2/WalletsService/Wallets/{walletId}/Locations | Create Wallet Location
[**create_wallet_payment_async**](WalletsApi.md#create_wallet_payment_async) | **POST** /api/v2/WalletsService/Wallets/{walletId}/Payments | Create Wallet Payment
[**create_wallet_token_async**](WalletsApi.md#create_wallet_token_async) | **POST** /api/v2/WalletsService/Wallets/{walletId}/Tokens | Create Wallet Token
[**create_wallet_withdraw_request_async**](WalletsApi.md#create_wallet_withdraw_request_async) | **POST** /api/v2/WalletsService/Wallets/{walletId}/Withdraws | Create Wallet Withdraw Request
[**delete_wallet_bank_account_async**](WalletsApi.md#delete_wallet_bank_account_async) | **DELETE** /api/v2/WalletsService/Wallets/{walletId}/BankAccounts/{bankAccountId} | Delete Wallet Bank Account
[**delete_wallet_location_async**](WalletsApi.md#delete_wallet_location_async) | **DELETE** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Delete Wallet Location
[**delete_wallet_token_async**](WalletsApi.md#delete_wallet_token_async) | **DELETE** /api/v2/WalletsService/Wallets/{walletId}/Tokens/{tokenId} | Delete Wallet Token
[**get_incoming_payments_async**](WalletsApi.md#get_incoming_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Incoming | Get Incoming Payments
[**get_incoming_payments_count_async**](WalletsApi.md#get_incoming_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Incoming/Count | Get Incoming Payments Count
[**get_incoming_wallet_invoices_async**](WalletsApi.md#get_incoming_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Incoming | Get Incoming Wallet Invoices
[**get_incoming_wallet_invoices_count_async**](WalletsApi.md#get_incoming_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Incoming/Count | Get Incoming Wallet Invoices Count
[**get_outgoing_payments_async**](WalletsApi.md#get_outgoing_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Outgoing | Get Outgoing Payments
[**get_outgoing_payments_count_async**](WalletsApi.md#get_outgoing_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Outgoing/Count | Get Outgoing Payments Count
[**get_outgoing_wallet_invoices_async**](WalletsApi.md#get_outgoing_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Outgoing | Get Outgoing Wallet Invoices
[**get_outgoing_wallet_invoices_count_async**](WalletsApi.md#get_outgoing_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Outgoing/Count | Get Outgoing Wallet Invoices Count
[**get_wallet_bank_account_async**](WalletsApi.md#get_wallet_bank_account_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/BankAccounts/{bankAccountId} | Get Wallet Bank Account
[**get_wallet_bank_accounts_async**](WalletsApi.md#get_wallet_bank_accounts_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/BankAccounts | Get Wallet Bank Accounts
[**get_wallet_bank_accounts_count_async**](WalletsApi.md#get_wallet_bank_accounts_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/BankAccounts/Count | Get Wallet Bank Accounts Count
[**get_wallet_chargebacks_async**](WalletsApi.md#get_wallet_chargebacks_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Chargebacks | Get Wallet Chargebacks
[**get_wallet_chargebacks_count_async**](WalletsApi.md#get_wallet_chargebacks_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Chargebacks/Count | Get Wallet Chargebacks Count
[**get_wallet_details_async**](WalletsApi.md#get_wallet_details_async) | **GET** /api/v2/WalletsService/Wallets/{walletId} | Get Wallet Details
[**get_wallet_extended_orders_async**](WalletsApi.md#get_wallet_extended_orders_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Orders/Extended | Get Wallet Extended Orders
[**get_wallet_invoices_async**](WalletsApi.md#get_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices | Get Wallet Invoices
[**get_wallet_invoices_count_async**](WalletsApi.md#get_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Count | Get Wallet Invoices Count
[**get_wallet_location_async**](WalletsApi.md#get_wallet_location_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Get Wallet Location
[**get_wallet_locations_async**](WalletsApi.md#get_wallet_locations_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Locations | Get Wallet Locations
[**get_wallet_locations_count_async**](WalletsApi.md#get_wallet_locations_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Locations/Count | Get Wallet Locations Count
[**get_wallet_orders_async**](WalletsApi.md#get_wallet_orders_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Orders | Get Wallet Orders
[**get_wallet_orders_count_async**](WalletsApi.md#get_wallet_orders_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Orders/Count | Get Wallet Orders Count
[**get_wallet_payments_async**](WalletsApi.md#get_wallet_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments | Get Wallet Payments
[**get_wallet_payments_count_async**](WalletsApi.md#get_wallet_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Count | Get Wallet Payments Count
[**get_wallet_quotes_async**](WalletsApi.md#get_wallet_quotes_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Quotes | Get Wallet Quotes
[**get_wallet_quotes_count_async**](WalletsApi.md#get_wallet_quotes_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Quotes/Count | Get Wallet Quotes Count
[**get_wallet_refunds_async**](WalletsApi.md#get_wallet_refunds_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Refunds | Get Wallet Refunds
[**get_wallet_refunds_count_async**](WalletsApi.md#get_wallet_refunds_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Refunds/Count | Get Wallet Refunds Count
[**get_wallet_token_async**](WalletsApi.md#get_wallet_token_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Tokens/{tokenId} | Get Wallet Token
[**get_wallet_tokens_async**](WalletsApi.md#get_wallet_tokens_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Tokens | Get Wallet Tokens
[**get_wallet_tokens_count_async**](WalletsApi.md#get_wallet_tokens_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Tokens/Count | Get Wallet Tokens Count
[**get_wallet_withdraw_requests_async**](WalletsApi.md#get_wallet_withdraw_requests_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/WithdrawRequests | Get Wallet Withdraw Requests
[**get_wallet_withdraw_requests_count_async**](WalletsApi.md#get_wallet_withdraw_requests_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/WithdrawRequests/Count | Get Wallet Withdraw Requests Count
[**get_wallet_withdraws_async**](WalletsApi.md#get_wallet_withdraws_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Withdraws | Get Wallet Withdraws
[**get_wallet_withdraws_count_async**](WalletsApi.md#get_wallet_withdraws_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Withdraws/Count | Get Wallet Withdraws Count
[**patch_wallet_bank_account_async**](WalletsApi.md#patch_wallet_bank_account_async) | **PATCH** /api/v2/WalletsService/Wallets/{walletId}/BankAccounts/{bankAccountId} | Patch Wallet Bank Account
[**patch_wallet_token_async**](WalletsApi.md#patch_wallet_token_async) | **PATCH** /api/v2/WalletsService/Wallets/{walletId}/Tokens/{tokenId} | Patch Wallet Token
[**update_wallet_bank_account_async**](WalletsApi.md#update_wallet_bank_account_async) | **PUT** /api/v2/WalletsService/Wallets/{walletId}/BankAccounts/{bankAccountId} | Update Wallet Bank Account
[**update_wallet_location_async**](WalletsApi.md#update_wallet_location_async) | **PUT** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Update Wallet Location
[**update_wallet_token_async**](WalletsApi.md#update_wallet_token_async) | **PUT** /api/v2/WalletsService/Wallets/{walletId}/Tokens/{tokenId} | Update Wallet Token


# **create_wallet_bank_account_async**
> EmptyEnvelope create_wallet_bank_account_async(wallet_id, api_version=api_version, x_api_version=x_api_version, bank_account_create_dto=bank_account_create_dto)

Create Wallet Bank Account

Create a new bank account for a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.bank_account_create_dto import BankAccountCreateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_account_create_dto = openapi_client.BankAccountCreateDto() # BankAccountCreateDto |  (optional)

    try:
        # Create Wallet Bank Account
        api_response = api_instance.create_wallet_bank_account_async(wallet_id, api_version=api_version, x_api_version=x_api_version, bank_account_create_dto=bank_account_create_dto)
        print("The response of WalletsApi->create_wallet_bank_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_wallet_bank_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_account_create_dto** | [**BankAccountCreateDto**](BankAccountCreateDto.md)|  | [optional] 

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

# **create_wallet_location_async**
> EmptyEnvelope create_wallet_location_async(wallet_id, api_version=api_version, x_api_version=x_api_version, location_create_dto=location_create_dto)

Create Wallet Location

Create a new location for a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.location_create_dto import LocationCreateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    location_create_dto = openapi_client.LocationCreateDto() # LocationCreateDto |  (optional)

    try:
        # Create Wallet Location
        api_response = api_instance.create_wallet_location_async(wallet_id, api_version=api_version, x_api_version=x_api_version, location_create_dto=location_create_dto)
        print("The response of WalletsApi->create_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **location_create_dto** | [**LocationCreateDto**](LocationCreateDto.md)|  | [optional] 

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

# **create_wallet_payment_async**
> EmptyEnvelope create_wallet_payment_async(wallet_id, api_version=api_version, x_api_version=x_api_version, payment_create_dto=payment_create_dto)

Create Wallet Payment

Create a new payment for a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_create_dto import PaymentCreateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_create_dto = openapi_client.PaymentCreateDto() # PaymentCreateDto |  (optional)

    try:
        # Create Wallet Payment
        api_response = api_instance.create_wallet_payment_async(wallet_id, api_version=api_version, x_api_version=x_api_version, payment_create_dto=payment_create_dto)
        print("The response of WalletsApi->create_wallet_payment_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_wallet_payment_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_create_dto** | [**PaymentCreateDto**](PaymentCreateDto.md)|  | [optional] 

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

# **create_wallet_token_async**
> EmptyEnvelope create_wallet_token_async(wallet_id, api_version=api_version, x_api_version=x_api_version, payment_token_create_dto=payment_token_create_dto)

Create Wallet Token

Create a new payment token for a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_token_create_dto import PaymentTokenCreateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_token_create_dto = openapi_client.PaymentTokenCreateDto() # PaymentTokenCreateDto |  (optional)

    try:
        # Create Wallet Token
        api_response = api_instance.create_wallet_token_async(wallet_id, api_version=api_version, x_api_version=x_api_version, payment_token_create_dto=payment_token_create_dto)
        print("The response of WalletsApi->create_wallet_token_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_wallet_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_token_create_dto** | [**PaymentTokenCreateDto**](PaymentTokenCreateDto.md)|  | [optional] 

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

# **create_wallet_withdraw_request_async**
> EmptyEnvelope create_wallet_withdraw_request_async(wallet_id, api_version=api_version, x_api_version=x_api_version, wallet_withdraw_request_create_dto=wallet_withdraw_request_create_dto)

Create Wallet Withdraw Request

Create a new withdraw request for a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.wallet_withdraw_request_create_dto import WalletWithdrawRequestCreateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    wallet_withdraw_request_create_dto = openapi_client.WalletWithdrawRequestCreateDto() # WalletWithdrawRequestCreateDto |  (optional)

    try:
        # Create Wallet Withdraw Request
        api_response = api_instance.create_wallet_withdraw_request_async(wallet_id, api_version=api_version, x_api_version=x_api_version, wallet_withdraw_request_create_dto=wallet_withdraw_request_create_dto)
        print("The response of WalletsApi->create_wallet_withdraw_request_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_wallet_withdraw_request_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **wallet_withdraw_request_create_dto** | [**WalletWithdrawRequestCreateDto**](WalletWithdrawRequestCreateDto.md)|  | [optional] 

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

# **delete_wallet_bank_account_async**
> EmptyEnvelope delete_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version)

Delete Wallet Bank Account

Delete a specific bank account of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete Wallet Bank Account
        api_response = api_instance.delete_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->delete_wallet_bank_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->delete_wallet_bank_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **bank_account_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wallet_location_async**
> EmptyEnvelope delete_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version)

Delete Wallet Location

Delete a specific location of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    location_id = 'location_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete Wallet Location
        api_response = api_instance.delete_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->delete_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->delete_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **location_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wallet_token_async**
> EmptyEnvelope delete_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version)

Delete Wallet Token

Delete a specific payment token of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    token_id = 'token_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete Wallet Token
        api_response = api_instance.delete_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->delete_wallet_token_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->delete_wallet_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **token_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incoming_payments_async**
> PaymentDtoListEnvelope get_incoming_payments_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Incoming Payments

Get incoming payments of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_dto_list_envelope import PaymentDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Incoming Payments
        api_response = api_instance.get_incoming_payments_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_incoming_payments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_incoming_payments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

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

# **get_incoming_payments_count_async**
> Int32Envelope get_incoming_payments_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Incoming Payments Count

Get incoming payments count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Incoming Payments Count
        api_response = api_instance.get_incoming_payments_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_incoming_payments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_incoming_payments_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_incoming_wallet_invoices_async**
> InvoiceDtoListEnvelope get_incoming_wallet_invoices_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Incoming Wallet Invoices

Get incoming invoices of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_dto_list_envelope import InvoiceDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Incoming Wallet Invoices
        api_response = api_instance.get_incoming_wallet_invoices_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_incoming_wallet_invoices_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_incoming_wallet_invoices_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InvoiceDtoListEnvelope**](InvoiceDtoListEnvelope.md)

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

# **get_incoming_wallet_invoices_count_async**
> Int32Envelope get_incoming_wallet_invoices_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Incoming Wallet Invoices Count

Get incoming invoices count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Incoming Wallet Invoices Count
        api_response = api_instance.get_incoming_wallet_invoices_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_incoming_wallet_invoices_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_incoming_wallet_invoices_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_outgoing_payments_async**
> PaymentDtoListEnvelope get_outgoing_payments_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Outgoing Payments

Get outgoing payments of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_dto_list_envelope import PaymentDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Outgoing Payments
        api_response = api_instance.get_outgoing_payments_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_outgoing_payments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_outgoing_payments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

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

# **get_outgoing_payments_count_async**
> Int32Envelope get_outgoing_payments_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Outgoing Payments Count

Get outgoing payments count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Outgoing Payments Count
        api_response = api_instance.get_outgoing_payments_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_outgoing_payments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_outgoing_payments_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_outgoing_wallet_invoices_async**
> InvoiceDtoListEnvelope get_outgoing_wallet_invoices_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Outgoing Wallet Invoices

Get outgoing invoices of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_dto_list_envelope import InvoiceDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Outgoing Wallet Invoices
        api_response = api_instance.get_outgoing_wallet_invoices_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_outgoing_wallet_invoices_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_outgoing_wallet_invoices_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InvoiceDtoListEnvelope**](InvoiceDtoListEnvelope.md)

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

# **get_outgoing_wallet_invoices_count_async**
> Int32Envelope get_outgoing_wallet_invoices_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Outgoing Wallet Invoices Count

Get outgoing invoices count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Outgoing Wallet Invoices Count
        api_response = api_instance.get_outgoing_wallet_invoices_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_outgoing_wallet_invoices_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_outgoing_wallet_invoices_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_bank_account_async**
> BankAccountDtoEnvelope get_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Bank Account

Get a specific bank account of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Bank Account
        api_response = api_instance.get_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_bank_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_bank_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **bank_account_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_bank_accounts_async**
> BankAccountDtoListEnvelope get_wallet_bank_accounts_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Bank Accounts

Get bank accounts of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Bank Accounts
        api_response = api_instance.get_wallet_bank_accounts_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_bank_accounts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_bank_accounts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_bank_accounts_count_async**
> Int32Envelope get_wallet_bank_accounts_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Bank Accounts Count

Get bank accounts count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Bank Accounts Count
        api_response = api_instance.get_wallet_bank_accounts_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_bank_accounts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_bank_accounts_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_chargebacks_async**
> PaymentChargebackDtoListEnvelope get_wallet_chargebacks_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Chargebacks

Get chargebacks of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_chargeback_dto_list_envelope import PaymentChargebackDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Chargebacks
        api_response = api_instance.get_wallet_chargebacks_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_chargebacks_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_chargebacks_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentChargebackDtoListEnvelope**](PaymentChargebackDtoListEnvelope.md)

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

# **get_wallet_chargebacks_count_async**
> Int32Envelope get_wallet_chargebacks_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Chargebacks Count

Get chargebacks count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Chargebacks Count
        api_response = api_instance.get_wallet_chargebacks_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_chargebacks_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_chargebacks_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_details_async**
> WalletDtoEnvelope get_wallet_details_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Details

Get details of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.wallet_dto_envelope import WalletDtoEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Details
        api_response = api_instance.get_wallet_details_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WalletDtoEnvelope**](WalletDtoEnvelope.md)

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

# **get_wallet_extended_orders_async**
> ExtendedOrderDtoListEnvelope get_wallet_extended_orders_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Extended Orders

Get extended orders of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.extended_order_dto_list_envelope import ExtendedOrderDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Extended Orders
        api_response = api_instance.get_wallet_extended_orders_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_extended_orders_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_extended_orders_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ExtendedOrderDtoListEnvelope**](ExtendedOrderDtoListEnvelope.md)

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

# **get_wallet_invoices_async**
> InvoiceDtoListEnvelope get_wallet_invoices_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Invoices

Get invoices of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_dto_list_envelope import InvoiceDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Invoices
        api_response = api_instance.get_wallet_invoices_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_invoices_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_invoices_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**InvoiceDtoListEnvelope**](InvoiceDtoListEnvelope.md)

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

# **get_wallet_invoices_count_async**
> Int32Envelope get_wallet_invoices_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Invoices Count

Get invoices count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Invoices Count
        api_response = api_instance.get_wallet_invoices_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_invoices_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_invoices_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_location_async**
> LocationDtoEnvelope get_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Location

Get a specific location of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.location_dto_envelope import LocationDtoEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    location_id = 'location_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Location
        api_response = api_instance.get_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **location_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LocationDtoEnvelope**](LocationDtoEnvelope.md)

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

# **get_wallet_locations_async**
> LocationDtoListEnvelope get_wallet_locations_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Locations

Get locations of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.location_dto_list_envelope import LocationDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Locations
        api_response = api_instance.get_wallet_locations_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_locations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_locations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**LocationDtoListEnvelope**](LocationDtoListEnvelope.md)

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

# **get_wallet_locations_count_async**
> Int32Envelope get_wallet_locations_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Locations Count

Get locations count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Locations Count
        api_response = api_instance.get_wallet_locations_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_locations_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_locations_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_orders_async**
> OrderDtoListEnvelope get_wallet_orders_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Orders

Get orders of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.order_dto_list_envelope import OrderDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Orders
        api_response = api_instance.get_wallet_orders_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_orders_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_orders_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OrderDtoListEnvelope**](OrderDtoListEnvelope.md)

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

# **get_wallet_orders_count_async**
> Int32Envelope get_wallet_orders_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Orders Count

Get orders count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Orders Count
        api_response = api_instance.get_wallet_orders_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_orders_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_orders_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_payments_async**
> PaymentDtoListEnvelope get_wallet_payments_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Payments

Get payments of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_dto_list_envelope import PaymentDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Payments
        api_response = api_instance.get_wallet_payments_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_payments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_payments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentDtoListEnvelope**](PaymentDtoListEnvelope.md)

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

# **get_wallet_payments_count_async**
> Int32Envelope get_wallet_payments_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Payments Count

Get payments count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Payments Count
        api_response = api_instance.get_wallet_payments_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_payments_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_payments_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_quotes_async**
> QuoteDtoListEnvelope get_wallet_quotes_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Quotes

Get quotes of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.quote_dto_list_envelope import QuoteDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Quotes
        api_response = api_instance.get_wallet_quotes_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_quotes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_quotes_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**QuoteDtoListEnvelope**](QuoteDtoListEnvelope.md)

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

# **get_wallet_quotes_count_async**
> Int32Envelope get_wallet_quotes_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Quotes Count

Get quotes count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Quotes Count
        api_response = api_instance.get_wallet_quotes_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_quotes_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_quotes_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_refunds_async**
> PaymentRefundDtoListEnvelope get_wallet_refunds_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Refunds

Get refunds of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_refund_dto_list_envelope import PaymentRefundDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Refunds
        api_response = api_instance.get_wallet_refunds_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_refunds_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_refunds_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentRefundDtoListEnvelope**](PaymentRefundDtoListEnvelope.md)

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

# **get_wallet_refunds_count_async**
> Int32Envelope get_wallet_refunds_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Refunds Count

Get refunds count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Refunds Count
        api_response = api_instance.get_wallet_refunds_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_refunds_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_refunds_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_token_async**
> PaymentTokenDtoEnvelope get_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Token

Get a specific payment token of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_token_dto_envelope import PaymentTokenDtoEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    token_id = 'token_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Token
        api_response = api_instance.get_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_token_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **token_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentTokenDtoEnvelope**](PaymentTokenDtoEnvelope.md)

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

# **get_wallet_tokens_async**
> PaymentTokenDtoListEnvelope get_wallet_tokens_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Tokens

Get payment tokens of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.payment_token_dto_list_envelope import PaymentTokenDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Tokens
        api_response = api_instance.get_wallet_tokens_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_tokens_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_tokens_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**PaymentTokenDtoListEnvelope**](PaymentTokenDtoListEnvelope.md)

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

# **get_wallet_tokens_count_async**
> Int32Envelope get_wallet_tokens_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Tokens Count

Get payment tokens count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Tokens Count
        api_response = api_instance.get_wallet_tokens_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_tokens_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_tokens_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_withdraw_requests_async**
> WalletWithdrawRequestDtoListEnvelope get_wallet_withdraw_requests_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Withdraw Requests

Get withdraw requests of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.wallet_withdraw_request_dto_list_envelope import WalletWithdrawRequestDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Withdraw Requests
        api_response = api_instance.get_wallet_withdraw_requests_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_withdraw_requests_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_withdraw_requests_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WalletWithdrawRequestDtoListEnvelope**](WalletWithdrawRequestDtoListEnvelope.md)

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

# **get_wallet_withdraw_requests_count_async**
> Int32Envelope get_wallet_withdraw_requests_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Withdraw Requests Count

Get withdraw requests count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Withdraw Requests Count
        api_response = api_instance.get_wallet_withdraw_requests_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_withdraw_requests_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_withdraw_requests_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **get_wallet_withdraws_async**
> WalletWithdrawDtoListEnvelope get_wallet_withdraws_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Withdraws

Get withdraws of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.wallet_withdraw_dto_list_envelope import WalletWithdrawDtoListEnvelope
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Withdraws
        api_response = api_instance.get_wallet_withdraws_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_withdraws_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_withdraws_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WalletWithdrawDtoListEnvelope**](WalletWithdrawDtoListEnvelope.md)

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

# **get_wallet_withdraws_count_async**
> Int32Envelope get_wallet_withdraws_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)

Get Wallet Withdraws Count

Get withdraws count of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Wallet Withdraws Count
        api_response = api_instance.get_wallet_withdraws_count_async(wallet_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WalletsApi->get_wallet_withdraws_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_withdraws_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
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

# **patch_wallet_bank_account_async**
> EmptyEnvelope patch_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch Wallet Bank Account

Partially update a specific bank account of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch Wallet Bank Account
        api_response = api_instance.patch_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of WalletsApi->patch_wallet_bank_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->patch_wallet_bank_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **bank_account_id** | **str**|  | 
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

# **patch_wallet_token_async**
> EmptyEnvelope patch_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch Wallet Token

Partially update a specific payment token of a specific wallet by ID.

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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    token_id = 'token_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch Wallet Token
        api_response = api_instance.patch_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of WalletsApi->patch_wallet_token_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->patch_wallet_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **token_id** | **str**|  | 
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

# **update_wallet_bank_account_async**
> EmptyEnvelope update_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version, bank_account_update_dto=bank_account_update_dto)

Update Wallet Bank Account

Update a specific bank account of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.bank_account_update_dto import BankAccountUpdateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    bank_account_id = 'bank_account_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bank_account_update_dto = openapi_client.BankAccountUpdateDto() # BankAccountUpdateDto |  (optional)

    try:
        # Update Wallet Bank Account
        api_response = api_instance.update_wallet_bank_account_async(wallet_id, bank_account_id, api_version=api_version, x_api_version=x_api_version, bank_account_update_dto=bank_account_update_dto)
        print("The response of WalletsApi->update_wallet_bank_account_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->update_wallet_bank_account_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **bank_account_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bank_account_update_dto** | [**BankAccountUpdateDto**](BankAccountUpdateDto.md)|  | [optional] 

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

# **update_wallet_location_async**
> EmptyEnvelope update_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version, location_update_dto=location_update_dto)

Update Wallet Location

Update a specific location of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.location_update_dto import LocationUpdateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    location_id = 'location_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    location_update_dto = openapi_client.LocationUpdateDto() # LocationUpdateDto |  (optional)

    try:
        # Update Wallet Location
        api_response = api_instance.update_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version, location_update_dto=location_update_dto)
        print("The response of WalletsApi->update_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->update_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **location_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **location_update_dto** | [**LocationUpdateDto**](LocationUpdateDto.md)|  | [optional] 

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

# **update_wallet_token_async**
> EmptyEnvelope update_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version, payment_token_update_dto=payment_token_update_dto)

Update Wallet Token

Update a specific payment token of a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.payment_token_update_dto import PaymentTokenUpdateDto
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
    api_instance = openapi_client.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    token_id = 'token_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    payment_token_update_dto = openapi_client.PaymentTokenUpdateDto() # PaymentTokenUpdateDto |  (optional)

    try:
        # Update Wallet Token
        api_response = api_instance.update_wallet_token_async(wallet_id, token_id, api_version=api_version, x_api_version=x_api_version, payment_token_update_dto=payment_token_update_dto)
        print("The response of WalletsApi->update_wallet_token_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->update_wallet_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **token_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **payment_token_update_dto** | [**PaymentTokenUpdateDto**](PaymentTokenUpdateDto.md)|  | [optional] 

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

