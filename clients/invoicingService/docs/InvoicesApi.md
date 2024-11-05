# openapi_client.InvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_invoicing_service_invoices_count_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_count_get) | **GET** /api/v2/InvoicingService/Invoices/Count | 
[**api_v2_invoicing_service_invoices_discounts_aggregate_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_discounts_aggregate_post) | **POST** /api/v2/InvoicingService/Invoices/DiscountsAggregate | 
[**api_v2_invoicing_service_invoices_extended_count_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_extended_count_get) | **GET** /api/v2/InvoicingService/Invoices/Extended/Count | 
[**api_v2_invoicing_service_invoices_extended_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_extended_get) | **GET** /api/v2/InvoicingService/Invoices/Extended | 
[**api_v2_invoicing_service_invoices_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_get) | **GET** /api/v2/InvoicingService/Invoices | 
[**api_v2_invoicing_service_invoices_global_surcharges_aggregate_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_global_surcharges_aggregate_post) | **POST** /api/v2/InvoicingService/Invoices/GlobalSurchargesAggregate | 
[**api_v2_invoicing_service_invoices_invoice_id_adjustments_count_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_adjustments_count_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/Count | 
[**api_v2_invoicing_service_invoices_invoice_id_adjustments_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_adjustments_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments | 
[**api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_delete**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_delete) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/{invoiceAdjustmentId} | 
[**api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/{invoiceAdjustmentId} | 
[**api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_put**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_put) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/{invoiceAdjustmentId} | 
[**api_v2_invoicing_service_invoices_invoice_id_adjustments_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_adjustments_post) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments | 
[**api_v2_invoicing_service_invoices_invoice_id_calculate_put**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_calculate_put) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Calculate | 
[**api_v2_invoicing_service_invoices_invoice_id_delete**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_delete) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId} | 
[**api_v2_invoicing_service_invoices_invoice_id_extended_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_extended_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Extended | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_count_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_count_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/Count | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_calculate_put**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_calculate_put) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Calculate | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_delete**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_delete) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId} | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId} | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_put**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_put) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId} | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_count_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_count_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes/Count | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_delete**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_delete) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes/{invoiceLineTaxId} | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_put**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_put) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes/{invoiceLineTaxId} | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_post) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes | 
[**api_v2_invoicing_service_invoices_invoice_id_lines_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_lines_post) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines | 
[**api_v2_invoicing_service_invoices_invoice_id_payments_count_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_payments_count_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Payments/Count | 
[**api_v2_invoicing_service_invoices_invoice_id_payments_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_payments_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Payments | 
[**api_v2_invoicing_service_invoices_invoice_id_put**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_put) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId} | 
[**api_v2_invoicing_service_invoices_invoice_id_references_count_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_references_count_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/References/Count | 
[**api_v2_invoicing_service_invoices_invoice_id_references_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_references_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/References | 
[**api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_delete**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_delete) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/References/{invoiceReferenceId} | 
[**api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_get**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_get) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/References/{invoiceReferenceId} | 
[**api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_put**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_put) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/References/{invoiceReferenceId} | 
[**api_v2_invoicing_service_invoices_invoice_id_references_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_invoice_id_references_post) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/References | 
[**api_v2_invoicing_service_invoices_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_post) | **POST** /api/v2/InvoicingService/Invoices | 
[**api_v2_invoicing_service_invoices_tax_bases_aggregate_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_tax_bases_aggregate_post) | **POST** /api/v2/InvoicingService/Invoices/TaxBasesAggregate | 
[**api_v2_invoicing_service_invoices_taxes_aggregate_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_taxes_aggregate_post) | **POST** /api/v2/InvoicingService/Invoices/TaxesAggregate | 
[**api_v2_invoicing_service_invoices_totals_aggregate_post**](InvoicesApi.md#api_v2_invoicing_service_invoices_totals_aggregate_post) | **POST** /api/v2/InvoicingService/Invoices/TotalsAggregate | 
[**get_invoice_async**](InvoicesApi.md#get_invoice_async) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId} | 


# **api_v2_invoicing_service_invoices_count_get**
> Int32Envelope api_v2_invoicing_service_invoices_count_get(tenant_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_count_get(tenant_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_discounts_aggregate_post**
> MoneyEnvelope api_v2_invoicing_service_invoices_discounts_aggregate_post(request_body, currency_id=currency_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_discounts_aggregate_post(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_discounts_aggregate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_discounts_aggregate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **api_v2_invoicing_service_invoices_extended_count_get**
> Int32Envelope api_v2_invoicing_service_invoices_extended_count_get(tenant_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_extended_count_get(tenant_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_extended_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_extended_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_extended_get**
> ExtendedInvoiceDtoListEnvelope api_v2_invoicing_service_invoices_extended_get(tenant_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.extended_invoice_dto_list_envelope import ExtendedInvoiceDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_extended_get(tenant_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_extended_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_extended_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedInvoiceDtoListEnvelope**](ExtendedInvoiceDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_get**
> InvoiceDtoListEnvelope api_v2_invoicing_service_invoices_get(tenant_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_get(tenant_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_global_surcharges_aggregate_post**
> MoneyEnvelope api_v2_invoicing_service_invoices_global_surcharges_aggregate_post(request_body, currency_id=currency_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_global_surcharges_aggregate_post(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_global_surcharges_aggregate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_global_surcharges_aggregate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **api_v2_invoicing_service_invoices_invoice_id_adjustments_count_get**
> Int32Envelope api_v2_invoicing_service_invoices_invoice_id_adjustments_count_get(tenant_id, invoice_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_adjustments_count_get(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_adjustments_get**
> InvoiceAdjustmentDtoListEnvelope api_v2_invoicing_service_invoices_invoice_id_adjustments_get(tenant_id, invoice_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_adjustment_dto_list_envelope import InvoiceAdjustmentDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_adjustments_get(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceAdjustmentDtoListEnvelope**](InvoiceAdjustmentDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_delete**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_delete(tenant_id, invoice_id, invoice_adjustment_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_id = 'invoice_adjustment_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_delete(tenant_id, invoice_id, invoice_adjustment_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_adjustment_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_get**
> InvoiceAdjustmentDtoEnvelope api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_get(tenant_id, invoice_id, invoice_adjustment_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_adjustment_dto_envelope import InvoiceAdjustmentDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_id = 'invoice_adjustment_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_get(tenant_id, invoice_id, invoice_adjustment_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_adjustment_id** | **str**|  | 

### Return type

[**InvoiceAdjustmentDtoEnvelope**](InvoiceAdjustmentDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_put**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_put(tenant_id, invoice_id, invoice_adjustment_id, invoice_adjustment_update_dto=invoice_adjustment_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_adjustment_update_dto import InvoiceAdjustmentUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_id = 'invoice_adjustment_id_example' # str | 
    invoice_adjustment_update_dto = openapi_client.InvoiceAdjustmentUpdateDto() # InvoiceAdjustmentUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_put(tenant_id, invoice_id, invoice_adjustment_id, invoice_adjustment_update_dto=invoice_adjustment_update_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_invoice_adjustment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_adjustment_id** | **str**|  | 
 **invoice_adjustment_update_dto** | [**InvoiceAdjustmentUpdateDto**](InvoiceAdjustmentUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_adjustments_post**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_adjustments_post(tenant_id, invoice_id, invoice_adjustment_create_dto=invoice_adjustment_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_adjustment_create_dto import InvoiceAdjustmentCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_create_dto = openapi_client.InvoiceAdjustmentCreateDto() # InvoiceAdjustmentCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_adjustments_post(tenant_id, invoice_id, invoice_adjustment_create_dto=invoice_adjustment_create_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_adjustments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_adjustment_create_dto** | [**InvoiceAdjustmentCreateDto**](InvoiceAdjustmentCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_calculate_put**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_calculate_put(tenant_id, invoice_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_calculate_put(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_delete**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_delete(tenant_id, invoice_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_delete(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_extended_get**
> InvoiceDtoEnvelope api_v2_invoicing_service_invoices_invoice_id_extended_get(tenant_id, invoice_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_dto_envelope import InvoiceDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_extended_get(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_extended_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_extended_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceDtoEnvelope**](InvoiceDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_count_get**
> Int32Envelope api_v2_invoicing_service_invoices_invoice_id_lines_count_get(tenant_id, invoice_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_count_get(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_get**
> InvoiceLineDtoListEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_get(tenant_id, invoice_id, item_id=item_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_line_dto_list_envelope import InvoiceLineDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_get(tenant_id, invoice_id, item_id=item_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 

### Return type

[**InvoiceLineDtoListEnvelope**](InvoiceLineDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_calculate_put**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_calculate_put(tenant_id, invoice_id, invoice_line_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_calculate_put(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_calculate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_calculate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_delete**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_delete(tenant_id, invoice_id, invoice_line_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_delete(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_get**
> InvoiceLineDtoEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_get(tenant_id, invoice_id, invoice_line_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_line_dto_envelope import InvoiceLineDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_get(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 

### Return type

[**InvoiceLineDtoEnvelope**](InvoiceLineDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_put**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_put(tenant_id, invoice_id, invoice_line_id, invoice_line_update_dto=invoice_line_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_line_update_dto import InvoiceLineUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_update_dto = openapi_client.InvoiceLineUpdateDto() # InvoiceLineUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_put(tenant_id, invoice_id, invoice_line_id, invoice_line_update_dto=invoice_line_update_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 
 **invoice_line_update_dto** | [**InvoiceLineUpdateDto**](InvoiceLineUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_count_get**
> Int32Envelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_count_get(tenant_id, invoice_id, invoice_line_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_count_get(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_get**
> InvoiceLineAppliedTaxDtoListEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_get(tenant_id, invoice_id, invoice_line_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_line_applied_tax_dto_list_envelope import InvoiceLineAppliedTaxDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_get(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 

### Return type

[**InvoiceLineAppliedTaxDtoListEnvelope**](InvoiceLineAppliedTaxDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_delete**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_delete(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_tax_id = 'invoice_line_tax_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_delete(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 
 **invoice_line_tax_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_put**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_put(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id, invoice_line_applied_tax_update_dto=invoice_line_applied_tax_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_line_applied_tax_update_dto import InvoiceLineAppliedTaxUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_tax_id = 'invoice_line_tax_id_example' # str | 
    invoice_line_applied_tax_update_dto = openapi_client.InvoiceLineAppliedTaxUpdateDto() # InvoiceLineAppliedTaxUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_put(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id, invoice_line_applied_tax_update_dto=invoice_line_applied_tax_update_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_invoice_line_tax_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 
 **invoice_line_tax_id** | **str**|  | 
 **invoice_line_applied_tax_update_dto** | [**InvoiceLineAppliedTaxUpdateDto**](InvoiceLineAppliedTaxUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_post**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_post(tenant_id, invoice_id, invoice_line_id, invoice_line_applied_tax_create_dto=invoice_line_applied_tax_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_line_applied_tax_create_dto import InvoiceLineAppliedTaxCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_applied_tax_create_dto = openapi_client.InvoiceLineAppliedTaxCreateDto() # InvoiceLineAppliedTaxCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_post(tenant_id, invoice_id, invoice_line_id, invoice_line_applied_tax_create_dto=invoice_line_applied_tax_create_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_invoice_line_id_taxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 
 **invoice_line_applied_tax_create_dto** | [**InvoiceLineAppliedTaxCreateDto**](InvoiceLineAppliedTaxCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_lines_post**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_lines_post(tenant_id, invoice_id, invoice_line_create_dto=invoice_line_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_line_create_dto import InvoiceLineCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_create_dto = openapi_client.InvoiceLineCreateDto() # InvoiceLineCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_lines_post(tenant_id, invoice_id, invoice_line_create_dto=invoice_line_create_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_lines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_create_dto** | [**InvoiceLineCreateDto**](InvoiceLineCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_payments_count_get**
> Int32Envelope api_v2_invoicing_service_invoices_invoice_id_payments_count_get(invoice_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_payments_count_get(invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_payments_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_payments_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

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

# **api_v2_invoicing_service_invoices_invoice_id_payments_get**
> InvoiceDtoListEnvelope api_v2_invoicing_service_invoices_invoice_id_payments_get(invoice_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_payments_get(invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

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

# **api_v2_invoicing_service_invoices_invoice_id_put**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_put(tenant_id, invoice_id, invoice_update_dto=invoice_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_update_dto import InvoiceUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_update_dto = openapi_client.InvoiceUpdateDto() # InvoiceUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_put(tenant_id, invoice_id, invoice_update_dto=invoice_update_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_update_dto** | [**InvoiceUpdateDto**](InvoiceUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_references_count_get**
> Int32Envelope api_v2_invoicing_service_invoices_invoice_id_references_count_get(tenant_id, invoice_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_references_count_get(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_references_get**
> InvoiceReferenceDtoListEnvelope api_v2_invoicing_service_invoices_invoice_id_references_get(tenant_id, invoice_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_reference_dto_list_envelope import InvoiceReferenceDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_references_get(tenant_id, invoice_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceReferenceDtoListEnvelope**](InvoiceReferenceDtoListEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_delete**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_delete(tenant_id, invoice_id, invoice_reference_id)



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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_id = 'invoice_reference_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_delete(tenant_id, invoice_id, invoice_reference_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_reference_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_get**
> InvoiceReferenceDtoEnvelope api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_get(tenant_id, invoice_id, invoice_reference_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_reference_dto_envelope import InvoiceReferenceDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_id = 'invoice_reference_id_example' # str | 

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_get(tenant_id, invoice_id, invoice_reference_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_reference_id** | **str**|  | 

### Return type

[**InvoiceReferenceDtoEnvelope**](InvoiceReferenceDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_put**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_put(tenant_id, invoice_id, invoice_reference_id, invoice_reference_update_dto=invoice_reference_update_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_reference_update_dto import InvoiceReferenceUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_id = 'invoice_reference_id_example' # str | 
    invoice_reference_update_dto = openapi_client.InvoiceReferenceUpdateDto() # InvoiceReferenceUpdateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_put(tenant_id, invoice_id, invoice_reference_id, invoice_reference_update_dto=invoice_reference_update_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_invoice_reference_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_reference_id** | **str**|  | 
 **invoice_reference_update_dto** | [**InvoiceReferenceUpdateDto**](InvoiceReferenceUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_invoice_id_references_post**
> EmptyEnvelope api_v2_invoicing_service_invoices_invoice_id_references_post(tenant_id, invoice_id, invoice_reference_create_dto=invoice_reference_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_reference_create_dto import InvoiceReferenceCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_create_dto = openapi_client.InvoiceReferenceCreateDto() # InvoiceReferenceCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_invoice_id_references_post(tenant_id, invoice_id, invoice_reference_create_dto=invoice_reference_create_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_invoice_id_references_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_reference_create_dto** | [**InvoiceReferenceCreateDto**](InvoiceReferenceCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_post**
> EmptyEnvelope api_v2_invoicing_service_invoices_post(tenant_id, invoice_create_dto=invoice_create_dto)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_create_dto import InvoiceCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_create_dto = openapi_client.InvoiceCreateDto() # InvoiceCreateDto |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_post(tenant_id, invoice_create_dto=invoice_create_dto)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_create_dto** | [**InvoiceCreateDto**](InvoiceCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_invoicing_service_invoices_tax_bases_aggregate_post**
> MoneyEnvelope api_v2_invoicing_service_invoices_tax_bases_aggregate_post(request_body, currency_id=currency_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_tax_bases_aggregate_post(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_tax_bases_aggregate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_tax_bases_aggregate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **api_v2_invoicing_service_invoices_taxes_aggregate_post**
> MoneyEnvelope api_v2_invoicing_service_invoices_taxes_aggregate_post(request_body, currency_id=currency_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_taxes_aggregate_post(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_taxes_aggregate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_taxes_aggregate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **api_v2_invoicing_service_invoices_totals_aggregate_post**
> MoneyEnvelope api_v2_invoicing_service_invoices_totals_aggregate_post(request_body, currency_id=currency_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_invoicing_service_invoices_totals_aggregate_post(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->api_v2_invoicing_service_invoices_totals_aggregate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->api_v2_invoicing_service_invoices_totals_aggregate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

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

# **get_invoice_async**
> InvoiceDtoEnvelope get_invoice_async(tenant_id, invoice_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.invoice_dto_envelope import InvoiceDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        api_response = api_instance.get_invoice_async(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_invoice_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceDtoEnvelope**](InvoiceDtoEnvelope.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

