# openapi_client.WalletsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wallet_location_async**](WalletsApi.md#create_wallet_location_async) | **POST** /api/v2/WalletsService/Wallets/{walletId}/Locations | Create Wallet Location
[**delete_wallet_location_async**](WalletsApi.md#delete_wallet_location_async) | **DELETE** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Delete Wallet Location
[**get_incoming_payments_async**](WalletsApi.md#get_incoming_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Incoming | Get Incoming Payments
[**get_incoming_payments_count_async**](WalletsApi.md#get_incoming_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Incoming/Count | Get Incoming Payments Count
[**get_incoming_wallet_invoices_async**](WalletsApi.md#get_incoming_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Incoming | Get Incoming Wallet Invoices
[**get_incoming_wallet_invoices_count_async**](WalletsApi.md#get_incoming_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Incoming/Count | Get Incoming Wallet Invoices Count
[**get_outgoing_payments_async**](WalletsApi.md#get_outgoing_payments_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Outgoing | Get Outgoing Payments
[**get_outgoing_payments_count_async**](WalletsApi.md#get_outgoing_payments_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Payments/Outgoing/Count | Get Outgoing Payments Count
[**get_outgoing_wallet_invoices_async**](WalletsApi.md#get_outgoing_wallet_invoices_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Outgoing | Get Outgoing Wallet Invoices
[**get_outgoing_wallet_invoices_count_async**](WalletsApi.md#get_outgoing_wallet_invoices_count_async) | **GET** /api/v2/WalletsService/Wallets/{walletId}/Invoices/Outgoing/Count | Get Outgoing Wallet Invoices Count
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
[**update_wallet_location_async**](WalletsApi.md#update_wallet_location_async) | **PUT** /api/v2/WalletsService/Wallets/{walletId}/Locations/{locationId} | Update Wallet Location


# **create_wallet_location_async**
> EmptyEnvelope create_wallet_location_async(wallet_id, api_version=api_version, x_api_version=x_api_version, location_create_dto=location_create_dto)

Create Wallet Location

Create a new location for a specific wallet by ID.

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

# **delete_wallet_location_async**
> EmptyEnvelope delete_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version)

Delete Wallet Location

Delete a specific location of a specific wallet by ID.

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

# **update_wallet_location_async**
> EmptyEnvelope update_wallet_location_async(wallet_id, location_id, api_version=api_version, x_api_version=x_api_version, location_update_dto=location_update_dto)

Update Wallet Location

Update a specific location of a specific wallet by ID.

### Example

* Api Key Authentication (Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

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

[Bearer](../README.md#Bearer)

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

