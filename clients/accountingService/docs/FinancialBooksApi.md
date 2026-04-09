# openapi_client.FinancialBooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_financial_book_async**](FinancialBooksApi.md#create_financial_book_async) | **POST** /api/v2/AccountingService/FinancialBooks | Creates a new financial book
[**delete_financial_book_async**](FinancialBooksApi.md#delete_financial_book_async) | **DELETE** /api/v2/AccountingService/FinancialBooks/{financialBookId} | Deletes an existing financial book
[**get_financial_book_details_async**](FinancialBooksApi.md#get_financial_book_details_async) | **GET** /api/v2/AccountingService/FinancialBooks/{financialBookId} | Gets the details of a specific financial book
[**get_financial_books_async**](FinancialBooksApi.md#get_financial_books_async) | **GET** /api/v2/AccountingService/FinancialBooks | Get all financial books for a tenant
[**get_financial_books_count_async**](FinancialBooksApi.md#get_financial_books_count_async) | **GET** /api/v2/AccountingService/FinancialBooks/Count | Get the count of financial books
[**update_financial_book_async**](FinancialBooksApi.md#update_financial_book_async) | **PUT** /api/v2/AccountingService/FinancialBooks/{financialBookId} | Updates an existing financial book


# **create_financial_book_async**
> EmptyEnvelope create_financial_book_async(tenant_id, financial_book_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a new financial book

Creates a new financial book.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.financial_book_create_dto import FinancialBookCreateDto
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
    api_instance = openapi_client.FinancialBooksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    financial_book_create_dto = openapi_client.FinancialBookCreateDto() # FinancialBookCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a new financial book
        api_response = api_instance.create_financial_book_async(tenant_id, financial_book_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of FinancialBooksApi->create_financial_book_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialBooksApi->create_financial_book_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **financial_book_create_dto** | [**FinancialBookCreateDto**](FinancialBookCreateDto.md)|  | 
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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_financial_book_async**
> EmptyEnvelope delete_financial_book_async(tenant_id, financial_book_id, api_version=api_version, x_api_version=x_api_version)

Deletes an existing financial book

Deletes an existing financial book.

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
    api_instance = openapi_client.FinancialBooksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    financial_book_id = 'financial_book_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes an existing financial book
        api_response = api_instance.delete_financial_book_async(tenant_id, financial_book_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FinancialBooksApi->delete_financial_book_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialBooksApi->delete_financial_book_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **financial_book_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_book_details_async**
> FinancialBookDtoEnvelope get_financial_book_details_async(tenant_id, financial_book_id, api_version=api_version, x_api_version=x_api_version)

Gets the details of a specific financial book

Gets the details of a specific financial book.

### Example


```python
import openapi_client
from openapi_client.models.financial_book_dto_envelope import FinancialBookDtoEnvelope
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
    api_instance = openapi_client.FinancialBooksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    financial_book_id = 'financial_book_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the details of a specific financial book
        api_response = api_instance.get_financial_book_details_async(tenant_id, financial_book_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FinancialBooksApi->get_financial_book_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialBooksApi->get_financial_book_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **financial_book_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FinancialBookDtoEnvelope**](FinancialBookDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_books_async**
> FinancialBookDtoListEnvelope get_financial_books_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all financial books for a tenant

Retrieves all financial books for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.financial_book_dto_list_envelope import FinancialBookDtoListEnvelope
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
    api_instance = openapi_client.FinancialBooksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all financial books for a tenant
        api_response = api_instance.get_financial_books_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FinancialBooksApi->get_financial_books_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialBooksApi->get_financial_books_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FinancialBookDtoListEnvelope**](FinancialBookDtoListEnvelope.md)

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_books_count_async**
> Int32Envelope get_financial_books_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of financial books

Get the count of financial books.

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
    api_instance = openapi_client.FinancialBooksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of financial books
        api_response = api_instance.get_financial_books_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FinancialBooksApi->get_financial_books_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialBooksApi->get_financial_books_count_async: %s\n" % e)
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_financial_book_async**
> EmptyEnvelope update_financial_book_async(tenant_id, financial_book_id, financial_book_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates an existing financial book

Updates an existing financial book.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.financial_book_update_dto import FinancialBookUpdateDto
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
    api_instance = openapi_client.FinancialBooksApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    financial_book_id = 'financial_book_id_example' # str | 
    financial_book_update_dto = openapi_client.FinancialBookUpdateDto() # FinancialBookUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates an existing financial book
        api_response = api_instance.update_financial_book_async(tenant_id, financial_book_id, financial_book_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of FinancialBooksApi->update_financial_book_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialBooksApi->update_financial_book_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **financial_book_id** | **str**|  | 
 **financial_book_update_dto** | [**FinancialBookUpdateDto**](FinancialBookUpdateDto.md)|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

