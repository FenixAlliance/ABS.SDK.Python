# openapi_client.TransactionsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /api/v2/AccountingService/Transactions | Create a transaction
[**create_transaction_category**](TransactionsApi.md#create_transaction_category) | **POST** /api/v2/AccountingService/Transactions/Categories | Create a transaction category
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /api/v2/AccountingService/Transactions/{transactionId} | Delete a transaction
[**delete_transaction_category**](TransactionsApi.md#delete_transaction_category) | **DELETE** /api/v2/AccountingService/Transactions/Categories/{categoryId} | Delete a transaction category
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /api/v2/AccountingService/Transactions/{transactionId} | Get transaction by ID
[**get_transaction_categories**](TransactionsApi.md#get_transaction_categories) | **GET** /api/v2/AccountingService/Transactions/Categories | Get all transaction categories
[**get_transaction_categories_count**](TransactionsApi.md#get_transaction_categories_count) | **GET** /api/v2/AccountingService/Transactions/Categories/Count | Get transaction categories count
[**get_transaction_category**](TransactionsApi.md#get_transaction_category) | **GET** /api/v2/AccountingService/Transactions/Categories/{categoryId} | Get transaction category by ID
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /api/v2/AccountingService/Transactions | Get all transactions for a tenant
[**get_transactions_count**](TransactionsApi.md#get_transactions_count) | **GET** /api/v2/AccountingService/Transactions/Count | Get transactions count
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /api/v2/AccountingService/Transactions/{transactionId} | Update a transaction
[**update_transaction_category**](TransactionsApi.md#update_transaction_category) | **PUT** /api/v2/AccountingService/Transactions/Categories/{categoryId} | Update a transaction category


# **create_transaction**
> TransactionDtoEnvelope create_transaction(tenant_id, api_version=api_version, x_api_version=x_api_version, transaction_create_dto=transaction_create_dto)

Create a transaction

Creates a new transaction for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.transaction_create_dto import TransactionCreateDto
from openapi_client.models.transaction_dto_envelope import TransactionDtoEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    transaction_create_dto = openapi_client.TransactionCreateDto() # TransactionCreateDto |  (optional)

    try:
        # Create a transaction
        api_response = api_instance.create_transaction(tenant_id, api_version=api_version, x_api_version=x_api_version, transaction_create_dto=transaction_create_dto)
        print("The response of TransactionsApi->create_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **transaction_create_dto** | [**TransactionCreateDto**](TransactionCreateDto.md)|  | [optional] 

### Return type

[**TransactionDtoEnvelope**](TransactionDtoEnvelope.md)

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

# **create_transaction_category**
> TransactionCategoryDtoEnvelope create_transaction_category(tenant_id, api_version=api_version, x_api_version=x_api_version, transaction_category_create_dto=transaction_category_create_dto)

Create a transaction category

Creates a new transaction category for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.transaction_category_create_dto import TransactionCategoryCreateDto
from openapi_client.models.transaction_category_dto_envelope import TransactionCategoryDtoEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    transaction_category_create_dto = openapi_client.TransactionCategoryCreateDto() # TransactionCategoryCreateDto |  (optional)

    try:
        # Create a transaction category
        api_response = api_instance.create_transaction_category(tenant_id, api_version=api_version, x_api_version=x_api_version, transaction_category_create_dto=transaction_category_create_dto)
        print("The response of TransactionsApi->create_transaction_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transaction_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **transaction_category_create_dto** | [**TransactionCategoryCreateDto**](TransactionCategoryCreateDto.md)|  | [optional] 

### Return type

[**TransactionCategoryDtoEnvelope**](TransactionCategoryDtoEnvelope.md)

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

# **delete_transaction**
> TransactionDtoEnvelope delete_transaction(tenant_id, transaction_id, api_version=api_version, x_api_version=x_api_version)

Delete a transaction

Deletes a transaction by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.transaction_dto_envelope import TransactionDtoEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a transaction
        api_response = api_instance.delete_transaction(tenant_id, transaction_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->delete_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TransactionDtoEnvelope**](TransactionDtoEnvelope.md)

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_category**
> TransactionCategoryDtoEnvelope delete_transaction_category(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version)

Delete a transaction category

Deletes a transaction category by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.transaction_category_dto_envelope import TransactionCategoryDtoEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a transaction category
        api_response = api_instance.delete_transaction_category(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->delete_transaction_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_transaction_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TransactionCategoryDtoEnvelope**](TransactionCategoryDtoEnvelope.md)

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionDtoEnvelope get_transaction(tenant_id, transaction_id, api_version=api_version, x_api_version=x_api_version)

Get transaction by ID

Retrieves a specific transaction by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.transaction_dto_envelope import TransactionDtoEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get transaction by ID
        api_response = api_instance.get_transaction(tenant_id, transaction_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TransactionDtoEnvelope**](TransactionDtoEnvelope.md)

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

# **get_transaction_categories**
> TransactionCategoryDtoListEnvelope get_transaction_categories(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all transaction categories

Retrieves all transaction categories for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.transaction_category_dto_list_envelope import TransactionCategoryDtoListEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all transaction categories
        api_response = api_instance.get_transaction_categories(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->get_transaction_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TransactionCategoryDtoListEnvelope**](TransactionCategoryDtoListEnvelope.md)

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

# **get_transaction_categories_count**
> Int32Envelope get_transaction_categories_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get transaction categories count

Returns total number of transaction categories for the tenant.

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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get transaction categories count
        api_response = api_instance.get_transaction_categories_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->get_transaction_categories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_categories_count: %s\n" % e)
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

# **get_transaction_category**
> TransactionCategoryDtoEnvelope get_transaction_category(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version)

Get transaction category by ID

Retrieves a specific transaction category by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.transaction_category_dto_envelope import TransactionCategoryDtoEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get transaction category by ID
        api_response = api_instance.get_transaction_category(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->get_transaction_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TransactionCategoryDtoEnvelope**](TransactionCategoryDtoEnvelope.md)

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

# **get_transactions**
> TransactionDtoListEnvelope get_transactions(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all transactions for a tenant

Retrieves all transactions for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.transaction_dto_list_envelope import TransactionDtoListEnvelope
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all transactions for a tenant
        api_response = api_instance.get_transactions(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TransactionDtoListEnvelope**](TransactionDtoListEnvelope.md)

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

# **get_transactions_count**
> Int32Envelope get_transactions_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get transactions count

Returns total number of transactions for the tenant with OData filter support.

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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get transactions count
        api_response = api_instance.get_transactions_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TransactionsApi->get_transactions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions_count: %s\n" % e)
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

# **update_transaction**
> TransactionDtoEnvelope update_transaction(tenant_id, transaction_id, api_version=api_version, x_api_version=x_api_version, transaction_update_dto=transaction_update_dto)

Update a transaction

Updates an existing transaction with the provided data.

### Example


```python
import openapi_client
from openapi_client.models.transaction_dto_envelope import TransactionDtoEnvelope
from openapi_client.models.transaction_update_dto import TransactionUpdateDto
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    transaction_update_dto = openapi_client.TransactionUpdateDto() # TransactionUpdateDto |  (optional)

    try:
        # Update a transaction
        api_response = api_instance.update_transaction(tenant_id, transaction_id, api_version=api_version, x_api_version=x_api_version, transaction_update_dto=transaction_update_dto)
        print("The response of TransactionsApi->update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **transaction_update_dto** | [**TransactionUpdateDto**](TransactionUpdateDto.md)|  | [optional] 

### Return type

[**TransactionDtoEnvelope**](TransactionDtoEnvelope.md)

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

# **update_transaction_category**
> TransactionCategoryDtoEnvelope update_transaction_category(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version, transaction_category_update_dto=transaction_category_update_dto)

Update a transaction category

Updates an existing transaction category with the provided data.

### Example


```python
import openapi_client
from openapi_client.models.transaction_category_dto_envelope import TransactionCategoryDtoEnvelope
from openapi_client.models.transaction_category_update_dto import TransactionCategoryUpdateDto
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
    api_instance = openapi_client.TransactionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    transaction_category_update_dto = openapi_client.TransactionCategoryUpdateDto() # TransactionCategoryUpdateDto |  (optional)

    try:
        # Update a transaction category
        api_response = api_instance.update_transaction_category(tenant_id, category_id, api_version=api_version, x_api_version=x_api_version, transaction_category_update_dto=transaction_category_update_dto)
        print("The response of TransactionsApi->update_transaction_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transaction_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **transaction_category_update_dto** | [**TransactionCategoryUpdateDto**](TransactionCategoryUpdateDto.md)|  | [optional] 

### Return type

[**TransactionCategoryDtoEnvelope**](TransactionCategoryDtoEnvelope.md)

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

