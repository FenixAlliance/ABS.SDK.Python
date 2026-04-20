# openapi_client.QuotesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_quote**](QuotesApi.md#calculate_quote) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Calculate | Calculate a quote.
[**calculate_quote_line**](QuotesApi.md#calculate_quote_line) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId}/Calculate | Calculate a quote line.
[**close_quote**](QuotesApi.md#close_quote) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Close | Close a quote.
[**create_order_from_quote**](QuotesApi.md#create_order_from_quote) | **POST** /api/v2/QuotesService/Quotes/{quoteId}/Orders | Create an order from a quote.
[**create_quote**](QuotesApi.md#create_quote) | **POST** /api/v2/QuotesService/Quotes | Create a new quote.
[**create_quote_line**](QuotesApi.md#create_quote_line) | **POST** /api/v2/QuotesService/Quotes/{quoteId}/Lines | Create a new quote line.
[**delete_quote**](QuotesApi.md#delete_quote) | **DELETE** /api/v2/QuotesService/Quotes/{quoteId} | Delete a quote.
[**delete_quote_line**](QuotesApi.md#delete_quote_line) | **DELETE** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId} | Delete a quote line.
[**get_extended_quotes**](QuotesApi.md#get_extended_quotes) | **GET** /api/v2/QuotesService/Quotes/Extended | Get a list of extended quotes.
[**get_quote**](QuotesApi.md#get_quote) | **GET** /api/v2/QuotesService/Quotes/{quoteId} | Get a quote by ID.
[**get_quote_line**](QuotesApi.md#get_quote_line) | **GET** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId} | Get a quote line by ID.
[**get_quote_lines**](QuotesApi.md#get_quote_lines) | **GET** /api/v2/QuotesService/Quotes/{quoteId}/Lines | Get quote lines for a quote.
[**get_quote_lines_count**](QuotesApi.md#get_quote_lines_count) | **GET** /api/v2/QuotesService/Quotes/{quoteId}/Lines/Count | Get the count of quote lines.
[**get_quotes**](QuotesApi.md#get_quotes) | **GET** /api/v2/QuotesService/Quotes | Get a list of quotes.
[**get_quotes_count**](QuotesApi.md#get_quotes_count) | **GET** /api/v2/QuotesService/Quotes/Count | Get the count of quotes.
[**preview_quote_email_template**](QuotesApi.md#preview_quote_email_template) | **POST** /api/v2/QuotesService/Quotes/{quoteId}/Emails/Preview | Preview the rendered email for an invoice.
[**quote_line_exists**](QuotesApi.md#quote_line_exists) | **GET** /api/v2/QuotesService/Quotes/{quoteId}/Lines/Exists | Check if a quote line exists.
[**reopen_quote**](QuotesApi.md#reopen_quote) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Reopen | Reopen a closed quote.
[**send_quote_email**](QuotesApi.md#send_quote_email) | **POST** /api/v2/QuotesService/Quotes/{quoteId}/Emails/Send | Send a quote transactional email to recipients.
[**update_quote**](QuotesApi.md#update_quote) | **PUT** /api/v2/QuotesService/Quotes/{quoteId} | Update an existing quote.
[**update_quote_line**](QuotesApi.md#update_quote_line) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId} | Update a quote line.
[**upsert_quote_line**](QuotesApi.md#upsert_quote_line) | **PUT** /api/v2/QuotesService/Quotes/{quoteId}/Lines/{quoteLineId}/Upsert | Upsert a quote line.


# **calculate_quote**
> EmptyEnvelope calculate_quote(tenant_id, quote_id)

Calculate a quote.

Performs calculation logic for the specified quote.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Calculate a quote.
        api_response = api_instance.calculate_quote(tenant_id, quote_id)
        print("The response of QuotesApi->calculate_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->calculate_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_quote_line**
> EmptyEnvelope calculate_quote_line(tenant_id, quote_id, quote_line_id)

Calculate a quote line.

Performs calculation logic for the specified quote line.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 

    try:
        # Calculate a quote line.
        api_response = api_instance.calculate_quote_line(tenant_id, quote_id, quote_line_id)
        print("The response of QuotesApi->calculate_quote_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->calculate_quote_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_quote**
> EmptyEnvelope close_quote(tenant_id, quote_id)

Close a quote.

Closes the specified quote for the tenant.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Close a quote.
        api_response = api_instance.close_quote(tenant_id, quote_id)
        print("The response of QuotesApi->close_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->close_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order_from_quote**
> EmptyEnvelope create_order_from_quote(tenant_id, quote_id)

Create an order from a quote.

Creates an order based on the specified quote for the tenant.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Create an order from a quote.
        api_response = api_instance.create_order_from_quote(tenant_id, quote_id)
        print("The response of QuotesApi->create_order_from_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->create_order_from_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quote**
> EmptyEnvelope create_quote(tenant_id, quote_create_dto=quote_create_dto)

Create a new quote.

Creates a new quote for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_create_dto import QuoteCreateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_create_dto = openapi_client.QuoteCreateDto() # QuoteCreateDto |  (optional)

    try:
        # Create a new quote.
        api_response = api_instance.create_quote(tenant_id, quote_create_dto=quote_create_dto)
        print("The response of QuotesApi->create_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->create_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_create_dto** | [**QuoteCreateDto**](QuoteCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quote_line**
> EmptyEnvelope create_quote_line(tenant_id, quote_id, quote_line_create_dto=quote_line_create_dto)

Create a new quote line.

Creates a new quote line for the specified quote and tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_line_create_dto import QuoteLineCreateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_create_dto = openapi_client.QuoteLineCreateDto() # QuoteLineCreateDto |  (optional)

    try:
        # Create a new quote line.
        api_response = api_instance.create_quote_line(tenant_id, quote_id, quote_line_create_dto=quote_line_create_dto)
        print("The response of QuotesApi->create_quote_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->create_quote_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_create_dto** | [**QuoteLineCreateDto**](QuoteLineCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quote**
> EmptyEnvelope delete_quote(quote_id, tenant_id)

Delete a quote.

Deletes the specified quote for the tenant.

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
    api_instance = openapi_client.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Delete a quote.
        api_response = api_instance.delete_quote(quote_id, tenant_id)
        print("The response of QuotesApi->delete_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->delete_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quote_line**
> EmptyEnvelope delete_quote_line(tenant_id, quote_id, quote_line_id)

Delete a quote line.

Deletes the specified quote line for the quote and tenant.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 

    try:
        # Delete a quote line.
        api_response = api_instance.delete_quote_line(tenant_id, quote_id, quote_line_id)
        print("The response of QuotesApi->delete_quote_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->delete_quote_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_quotes**
> ExtendedQuoteDtoListEnvelope get_extended_quotes(tenant_id)

Get a list of extended quotes.

Retrieves a list of extended quotes for the specified tenant, supporting OData query options.

### Example


```python
import openapi_client
from openapi_client.models.extended_quote_dto_list_envelope import ExtendedQuoteDtoListEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get a list of extended quotes.
        api_response = api_instance.get_extended_quotes(tenant_id)
        print("The response of QuotesApi->get_extended_quotes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_extended_quotes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedQuoteDtoListEnvelope**](ExtendedQuoteDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote**
> QuoteDtoEnvelope get_quote(tenant_id, quote_id)

Get a quote by ID.

Retrieves a single quote by its unique identifier for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.quote_dto_envelope import QuoteDtoEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Get a quote by ID.
        api_response = api_instance.get_quote(tenant_id, quote_id)
        print("The response of QuotesApi->get_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

### Return type

[**QuoteDtoEnvelope**](QuoteDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_line**
> QuoteLineDtoEnvelope get_quote_line(tenant_id, quote_id, quote_line_id)

Get a quote line by ID.

Retrieves a single quote line by its unique identifier for the specified quote and tenant.

### Example


```python
import openapi_client
from openapi_client.models.quote_line_dto_envelope import QuoteLineDtoEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 

    try:
        # Get a quote line by ID.
        api_response = api_instance.get_quote_line(tenant_id, quote_id, quote_line_id)
        print("The response of QuotesApi->get_quote_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 

### Return type

[**QuoteLineDtoEnvelope**](QuoteLineDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_lines**
> QuoteLineDtoListEnvelope get_quote_lines(tenant_id, quote_id, item_id=item_id)

Get quote lines for a quote.

Retrieves all quote lines for the specified quote and tenant.

### Example


```python
import openapi_client
from openapi_client.models.quote_line_dto_list_envelope import QuoteLineDtoListEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        # Get quote lines for a quote.
        api_response = api_instance.get_quote_lines(tenant_id, quote_id, item_id=item_id)
        print("The response of QuotesApi->get_quote_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 

### Return type

[**QuoteLineDtoListEnvelope**](QuoteLineDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_lines_count**
> Int32Envelope get_quote_lines_count(tenant_id, quote_id)

Get the count of quote lines.

Retrieves the total count of quote lines for the specified quote and tenant.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Get the count of quote lines.
        api_response = api_instance.get_quote_lines_count(tenant_id, quote_id)
        print("The response of QuotesApi->get_quote_lines_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_lines_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes**
> QuoteDtoListEnvelope get_quotes(tenant_id)

Get a list of quotes.

Retrieves a list of quotes for the specified tenant, supporting OData query options.

### Example


```python
import openapi_client
from openapi_client.models.quote_dto_list_envelope import QuoteDtoListEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get a list of quotes.
        api_response = api_instance.get_quotes(tenant_id)
        print("The response of QuotesApi->get_quotes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quotes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes_count**
> Int32Envelope get_quotes_count(tenant_id)

Get the count of quotes.

Retrieves the total count of quotes for the specified tenant, supporting OData query options.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get the count of quotes.
        api_response = api_instance.get_quotes_count(tenant_id)
        print("The response of QuotesApi->get_quotes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quotes_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_quote_email_template**
> preview_quote_email_template(quote_id, tenant_id, email_dispatch_request=email_dispatch_request)

Preview the rendered email for an invoice.

This action is only available for users with the 'send_email' permission.

### Example


```python
import openapi_client
from openapi_client.models.email_dispatch_request import EmailDispatchRequest
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
    api_instance = openapi_client.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    email_dispatch_request = openapi_client.EmailDispatchRequest() # EmailDispatchRequest |  (optional)

    try:
        # Preview the rendered email for an invoice.
        api_instance.preview_quote_email_template(quote_id, tenant_id, email_dispatch_request=email_dispatch_request)
    except Exception as e:
        print("Exception when calling QuotesApi->preview_quote_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **email_dispatch_request** | [**EmailDispatchRequest**](EmailDispatchRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_line_exists**
> BooleanEnvelope quote_line_exists(tenant_id, quote_id, quote_line_id=quote_line_id, item_id=item_id)

Check if a quote line exists.

Checks if a quote line exists for the specified quote and tenant, by quote line ID or item ID.

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str |  (optional)
    item_id = 'item_id_example' # str |  (optional)

    try:
        # Check if a quote line exists.
        api_response = api_instance.quote_line_exists(tenant_id, quote_id, quote_line_id=quote_line_id, item_id=item_id)
        print("The response of QuotesApi->quote_line_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->quote_line_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | [optional] 
 **item_id** | **str**|  | [optional] 

### Return type

[**BooleanEnvelope**](BooleanEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopen_quote**
> EmptyEnvelope reopen_quote(tenant_id, quote_id)

Reopen a closed quote.

Reopens a previously closed quote for the tenant.

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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 

    try:
        # Reopen a closed quote.
        api_response = api_instance.reopen_quote(tenant_id, quote_id)
        print("The response of QuotesApi->reopen_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->reopen_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_quote_email**
> EmptyEnvelope send_quote_email(tenant_id, quote_id, email_dispatch_request=email_dispatch_request)

Send a quote transactional email to recipients.

This action is only available for users with the 'send_email' permission.

### Example


```python
import openapi_client
from openapi_client.models.email_dispatch_request import EmailDispatchRequest
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    email_dispatch_request = openapi_client.EmailDispatchRequest() # EmailDispatchRequest |  (optional)

    try:
        # Send a quote transactional email to recipients.
        api_response = api_instance.send_quote_email(tenant_id, quote_id, email_dispatch_request=email_dispatch_request)
        print("The response of QuotesApi->send_quote_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->send_quote_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **email_dispatch_request** | [**EmailDispatchRequest**](EmailDispatchRequest.md)|  | [optional] 

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

# **update_quote**
> EmptyEnvelope update_quote(tenant_id, quote_id, quote_update_dto=quote_update_dto)

Update an existing quote.

Updates an existing quote for the specified tenant and quote ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_update_dto import QuoteUpdateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_update_dto = openapi_client.QuoteUpdateDto() # QuoteUpdateDto |  (optional)

    try:
        # Update an existing quote.
        api_response = api_instance.update_quote(tenant_id, quote_id, quote_update_dto=quote_update_dto)
        print("The response of QuotesApi->update_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->update_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_update_dto** | [**QuoteUpdateDto**](QuoteUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quote_line**
> EmptyEnvelope update_quote_line(tenant_id, quote_id, quote_line_id, quote_line_update_dto=quote_line_update_dto)

Update a quote line.

Updates an existing quote line for the specified quote and tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_line_update_dto import QuoteLineUpdateDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 
    quote_line_update_dto = openapi_client.QuoteLineUpdateDto() # QuoteLineUpdateDto |  (optional)

    try:
        # Update a quote line.
        api_response = api_instance.update_quote_line(tenant_id, quote_id, quote_line_id, quote_line_update_dto=quote_line_update_dto)
        print("The response of QuotesApi->update_quote_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->update_quote_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 
 **quote_line_update_dto** | [**QuoteLineUpdateDto**](QuoteLineUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_quote_line**
> EmptyEnvelope upsert_quote_line(tenant_id, quote_id, quote_line_id, quote_line_upsert_dto=quote_line_upsert_dto)

Upsert a quote line.

Creates or updates a quote line for the specified quote and tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.quote_line_upsert_dto import QuoteLineUpsertDto
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
    api_instance = openapi_client.QuotesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_line_id = 'quote_line_id_example' # str | 
    quote_line_upsert_dto = openapi_client.QuoteLineUpsertDto() # QuoteLineUpsertDto |  (optional)

    try:
        # Upsert a quote line.
        api_response = api_instance.upsert_quote_line(tenant_id, quote_id, quote_line_id, quote_line_upsert_dto=quote_line_upsert_dto)
        print("The response of QuotesApi->upsert_quote_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->upsert_quote_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_line_id** | **str**|  | 
 **quote_line_upsert_dto** | [**QuoteLineUpsertDto**](QuoteLineUpsertDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

