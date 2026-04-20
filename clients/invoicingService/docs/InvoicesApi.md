# openapi_client.InvoicesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_invoice_discounts**](InvoicesApi.md#aggregate_invoice_discounts) | **POST** /api/v2/InvoicingService/Invoices/DiscountsAggregate | Aggregate invoice discounts.
[**aggregate_invoice_global_surcharges**](InvoicesApi.md#aggregate_invoice_global_surcharges) | **POST** /api/v2/InvoicingService/Invoices/GlobalSurchargesAggregate | Aggregate invoice global surcharges.
[**aggregate_invoice_tax_bases**](InvoicesApi.md#aggregate_invoice_tax_bases) | **POST** /api/v2/InvoicingService/Invoices/TaxBasesAggregate | Aggregate invoice tax bases.
[**aggregate_invoice_taxes**](InvoicesApi.md#aggregate_invoice_taxes) | **POST** /api/v2/InvoicingService/Invoices/TaxesAggregate | Aggregate invoice taxes.
[**aggregate_invoice_totals**](InvoicesApi.md#aggregate_invoice_totals) | **POST** /api/v2/InvoicingService/Invoices/TotalsAggregate | Aggregate invoice totals.
[**calculate_invoice**](InvoicesApi.md#calculate_invoice) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Calculate | Calculate an invoice.
[**calculate_invoice_line**](InvoicesApi.md#calculate_invoice_line) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Calculate | Calculate an invoice line.
[**create_invoice**](InvoicesApi.md#create_invoice) | **POST** /api/v2/InvoicingService/Invoices | Create a new invoice.
[**create_invoice_adjustment**](InvoicesApi.md#create_invoice_adjustment) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments | Create a new invoice adjustment.
[**create_invoice_line**](InvoicesApi.md#create_invoice_line) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines | Create a new invoice line.
[**create_invoice_line_tax**](InvoicesApi.md#create_invoice_line_tax) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes | Create a new tax for an invoice line.
[**create_invoice_reference**](InvoicesApi.md#create_invoice_reference) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/References | Create a new invoice reference.
[**delete_invoice**](InvoicesApi.md#delete_invoice) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId} | Delete an invoice.
[**delete_invoice_adjustment**](InvoicesApi.md#delete_invoice_adjustment) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/{invoiceAdjustmentId} | Delete an invoice adjustment.
[**delete_invoice_line**](InvoicesApi.md#delete_invoice_line) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId} | Delete an invoice line.
[**delete_invoice_line_tax**](InvoicesApi.md#delete_invoice_line_tax) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes/{invoiceLineTaxId} | Delete a tax from an invoice line.
[**delete_invoice_reference**](InvoicesApi.md#delete_invoice_reference) | **DELETE** /api/v2/InvoicingService/Invoices/{invoiceId}/References/{invoiceReferenceId} | Delete an invoice reference.
[**get_extended_invoice**](InvoicesApi.md#get_extended_invoice) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Extended | Get an extended invoice by ID.
[**get_extended_invoices**](InvoicesApi.md#get_extended_invoices) | **GET** /api/v2/InvoicingService/Invoices/Extended | Get a list of extended invoices.
[**get_extended_invoices_count**](InvoicesApi.md#get_extended_invoices_count) | **GET** /api/v2/InvoicingService/Invoices/Extended/Count | Get the count of extended invoices.
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId} | Get an invoice by ID.
[**get_invoice_adjustment**](InvoicesApi.md#get_invoice_adjustment) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/{invoiceAdjustmentId} | Get an invoice adjustment by ID.
[**get_invoice_adjustments**](InvoicesApi.md#get_invoice_adjustments) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments | Get invoice adjustments.
[**get_invoice_adjustments_count**](InvoicesApi.md#get_invoice_adjustments_count) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/Count | Get the count of invoice adjustments.
[**get_invoice_line**](InvoicesApi.md#get_invoice_line) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId} | Get an invoice line by ID.
[**get_invoice_line_taxes**](InvoicesApi.md#get_invoice_line_taxes) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes | Get taxes for an invoice line.
[**get_invoice_line_taxes_count**](InvoicesApi.md#get_invoice_line_taxes_count) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes/Count | Get the count of taxes for an invoice line.
[**get_invoice_lines**](InvoicesApi.md#get_invoice_lines) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines | Get invoice lines.
[**get_invoice_lines_count**](InvoicesApi.md#get_invoice_lines_count) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/Count | Get the count of invoice lines.
[**get_invoice_payments**](InvoicesApi.md#get_invoice_payments) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Payments | Get payments for an invoice.
[**get_invoice_payments_count**](InvoicesApi.md#get_invoice_payments_count) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/Payments/Count | Get the count of payments for an invoice.
[**get_invoice_reference**](InvoicesApi.md#get_invoice_reference) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/References/{invoiceReferenceId} | Get an invoice reference by ID.
[**get_invoice_references**](InvoicesApi.md#get_invoice_references) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/References | Get invoice references.
[**get_invoice_references_count**](InvoicesApi.md#get_invoice_references_count) | **GET** /api/v2/InvoicingService/Invoices/{invoiceId}/References/Count | Get the count of invoice references.
[**get_invoices**](InvoicesApi.md#get_invoices) | **GET** /api/v2/InvoicingService/Invoices | Get a list of invoices.
[**get_invoices_count**](InvoicesApi.md#get_invoices_count) | **GET** /api/v2/InvoicingService/Invoices/Count | Get the count of invoices.
[**preview_invoice_email**](InvoicesApi.md#preview_invoice_email) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Emails/Preview | Preview the rendered email for an invoice.
[**send_invoice_email**](InvoicesApi.md#send_invoice_email) | **POST** /api/v2/InvoicingService/Invoices/{invoiceId}/Emails/Send | Send an invoice transactional email to recipients.
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId} | Update an invoice.
[**update_invoice_adjustment**](InvoicesApi.md#update_invoice_adjustment) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Adjustments/{invoiceAdjustmentId} | Update an invoice adjustment.
[**update_invoice_line**](InvoicesApi.md#update_invoice_line) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId} | Update an invoice line.
[**update_invoice_line_tax**](InvoicesApi.md#update_invoice_line_tax) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/Lines/{invoiceLineId}/Taxes/{invoiceLineTaxId} | Update a tax for an invoice line.
[**update_invoice_reference**](InvoicesApi.md#update_invoice_reference) | **PUT** /api/v2/InvoicingService/Invoices/{invoiceId}/References/{invoiceReferenceId} | Update an invoice reference.


# **aggregate_invoice_discounts**
> MoneyEnvelope aggregate_invoice_discounts(request_body, currency_id=currency_id)

Aggregate invoice discounts.

Aggregates the discounts for the specified invoices.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        # Aggregate invoice discounts.
        api_response = api_instance.aggregate_invoice_discounts(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->aggregate_invoice_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->aggregate_invoice_discounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_invoice_global_surcharges**
> MoneyEnvelope aggregate_invoice_global_surcharges(request_body, currency_id=currency_id)

Aggregate invoice global surcharges.

Aggregates the global surcharges for the specified invoices.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        # Aggregate invoice global surcharges.
        api_response = api_instance.aggregate_invoice_global_surcharges(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->aggregate_invoice_global_surcharges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->aggregate_invoice_global_surcharges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_invoice_tax_bases**
> MoneyEnvelope aggregate_invoice_tax_bases(request_body, currency_id=currency_id)

Aggregate invoice tax bases.

Aggregates the tax bases for the specified invoices.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        # Aggregate invoice tax bases.
        api_response = api_instance.aggregate_invoice_tax_bases(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->aggregate_invoice_tax_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->aggregate_invoice_tax_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_invoice_taxes**
> MoneyEnvelope aggregate_invoice_taxes(request_body, currency_id=currency_id)

Aggregate invoice taxes.

Aggregates the taxes for the specified invoices.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        # Aggregate invoice taxes.
        api_response = api_instance.aggregate_invoice_taxes(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->aggregate_invoice_taxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->aggregate_invoice_taxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_invoice_totals**
> MoneyEnvelope aggregate_invoice_totals(request_body, currency_id=currency_id)

Aggregate invoice totals.

Aggregates the totals for the specified invoices.

### Example


```python
import openapi_client
from openapi_client.models.money_envelope import MoneyEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    currency_id = 'currency_id_example' # str |  (optional)

    try:
        # Aggregate invoice totals.
        api_response = api_instance.aggregate_invoice_totals(request_body, currency_id=currency_id)
        print("The response of InvoicesApi->aggregate_invoice_totals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->aggregate_invoice_totals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **currency_id** | **str**|  | [optional] 

### Return type

[**MoneyEnvelope**](MoneyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_invoice**
> EmptyEnvelope calculate_invoice(tenant_id, invoice_id)

Calculate an invoice.

Calculates the totals and taxes for the specified invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Calculate an invoice.
        api_response = api_instance.calculate_invoice(tenant_id, invoice_id)
        print("The response of InvoicesApi->calculate_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->calculate_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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

# **calculate_invoice_line**
> EmptyEnvelope calculate_invoice_line(tenant_id, invoice_id, invoice_line_id)

Calculate an invoice line.

Calculates the totals and taxes for the specified invoice line.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        # Calculate an invoice line.
        api_response = api_instance.calculate_invoice_line(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->calculate_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->calculate_invoice_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice**
> EmptyEnvelope create_invoice(tenant_id, invoice_create_dto=invoice_create_dto)

Create a new invoice.

Creates a new invoice for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_create_dto import InvoiceCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_create_dto = openapi_client.InvoiceCreateDto() # InvoiceCreateDto |  (optional)

    try:
        # Create a new invoice.
        api_response = api_instance.create_invoice(tenant_id, invoice_create_dto=invoice_create_dto)
        print("The response of InvoicesApi->create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_create_dto** | [**InvoiceCreateDto**](InvoiceCreateDto.md)|  | [optional] 

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

# **create_invoice_adjustment**
> EmptyEnvelope create_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_create_dto=invoice_adjustment_create_dto)

Create a new invoice adjustment.

Creates a new adjustment for the specified invoice.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_adjustment_create_dto import InvoiceAdjustmentCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_create_dto = openapi_client.InvoiceAdjustmentCreateDto() # InvoiceAdjustmentCreateDto |  (optional)

    try:
        # Create a new invoice adjustment.
        api_response = api_instance.create_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_create_dto=invoice_adjustment_create_dto)
        print("The response of InvoicesApi->create_invoice_adjustment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->create_invoice_adjustment: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_line**
> InvoiceLineDtoIReadOnlyListEnvelope create_invoice_line(tenant_id, invoice_id, invoice_line_create_dto=invoice_line_create_dto)

Create a new invoice line.

Creates a new invoice line for the specified invoice.

### Example


```python
import openapi_client
from openapi_client.models.invoice_line_create_dto import InvoiceLineCreateDto
from openapi_client.models.invoice_line_dto_i_read_only_list_envelope import InvoiceLineDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_create_dto = openapi_client.InvoiceLineCreateDto() # InvoiceLineCreateDto |  (optional)

    try:
        # Create a new invoice line.
        api_response = api_instance.create_invoice_line(tenant_id, invoice_id, invoice_line_create_dto=invoice_line_create_dto)
        print("The response of InvoicesApi->create_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->create_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_create_dto** | [**InvoiceLineCreateDto**](InvoiceLineCreateDto.md)|  | [optional] 

### Return type

[**InvoiceLineDtoIReadOnlyListEnvelope**](InvoiceLineDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_line_tax**
> EmptyEnvelope create_invoice_line_tax(tenant_id, invoice_id, invoice_line_id, invoice_line_applied_tax_create_dto=invoice_line_applied_tax_create_dto)

Create a new tax for an invoice line.

Creates a new tax entry for the specified invoice line.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_line_applied_tax_create_dto import InvoiceLineAppliedTaxCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_applied_tax_create_dto = openapi_client.InvoiceLineAppliedTaxCreateDto() # InvoiceLineAppliedTaxCreateDto |  (optional)

    try:
        # Create a new tax for an invoice line.
        api_response = api_instance.create_invoice_line_tax(tenant_id, invoice_id, invoice_line_id, invoice_line_applied_tax_create_dto=invoice_line_applied_tax_create_dto)
        print("The response of InvoicesApi->create_invoice_line_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->create_invoice_line_tax: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_reference**
> EmptyEnvelope create_invoice_reference(tenant_id, invoice_id, invoice_reference_create_dto=invoice_reference_create_dto)

Create a new invoice reference.

Creates a new reference for the specified invoice.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_reference_create_dto import InvoiceReferenceCreateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_create_dto = openapi_client.InvoiceReferenceCreateDto() # InvoiceReferenceCreateDto |  (optional)

    try:
        # Create a new invoice reference.
        api_response = api_instance.create_invoice_reference(tenant_id, invoice_id, invoice_reference_create_dto=invoice_reference_create_dto)
        print("The response of InvoicesApi->create_invoice_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->create_invoice_reference: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice**
> EmptyEnvelope delete_invoice(tenant_id, invoice_id)

Delete an invoice.

Deletes the specified invoice for the tenant.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Delete an invoice.
        api_response = api_instance.delete_invoice(tenant_id, invoice_id)
        print("The response of InvoicesApi->delete_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->delete_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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

# **delete_invoice_adjustment**
> EmptyEnvelope delete_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_id)

Delete an invoice adjustment.

Deletes the specified adjustment from the invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_id = 'invoice_adjustment_id_example' # str | 

    try:
        # Delete an invoice adjustment.
        api_response = api_instance.delete_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_id)
        print("The response of InvoicesApi->delete_invoice_adjustment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->delete_invoice_adjustment: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_line**
> EmptyEnvelope delete_invoice_line(tenant_id, invoice_id, invoice_line_id)

Delete an invoice line.

Deletes the specified invoice line.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        # Delete an invoice line.
        api_response = api_instance.delete_invoice_line(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->delete_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->delete_invoice_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_line_tax**
> EmptyEnvelope delete_invoice_line_tax(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id)

Delete a tax from an invoice line.

Deletes the specified tax entry from the invoice line.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_tax_id = 'invoice_line_tax_id_example' # str | 

    try:
        # Delete a tax from an invoice line.
        api_response = api_instance.delete_invoice_line_tax(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id)
        print("The response of InvoicesApi->delete_invoice_line_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->delete_invoice_line_tax: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_reference**
> EmptyEnvelope delete_invoice_reference(tenant_id, invoice_id, invoice_reference_id)

Delete an invoice reference.

Deletes the specified reference from the invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_id = 'invoice_reference_id_example' # str | 

    try:
        # Delete an invoice reference.
        api_response = api_instance.delete_invoice_reference(tenant_id, invoice_id, invoice_reference_id)
        print("The response of InvoicesApi->delete_invoice_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->delete_invoice_reference: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_invoice**
> InvoiceDtoEnvelope get_extended_invoice(tenant_id, invoice_id)

Get an extended invoice by ID.

Retrieves the extended invoice details for the specified invoice ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_dto_envelope import InvoiceDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get an extended invoice by ID.
        api_response = api_instance.get_extended_invoice(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_extended_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_extended_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceDtoEnvelope**](InvoiceDtoEnvelope.md)

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

# **get_extended_invoices**
> ExtendedInvoiceDtoListEnvelope get_extended_invoices(tenant_id)

Get a list of extended invoices.

Retrieves a list of extended invoice details for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.extended_invoice_dto_list_envelope import ExtendedInvoiceDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get a list of extended invoices.
        api_response = api_instance.get_extended_invoices(tenant_id)
        print("The response of InvoicesApi->get_extended_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_extended_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedInvoiceDtoListEnvelope**](ExtendedInvoiceDtoListEnvelope.md)

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

# **get_extended_invoices_count**
> Int32Envelope get_extended_invoices_count(tenant_id)

Get the count of extended invoices.

Retrieves the total count of extended invoices for the specified tenant.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get the count of extended invoices.
        api_response = api_instance.get_extended_invoices_count(tenant_id)
        print("The response of InvoicesApi->get_extended_invoices_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_extended_invoices_count: %s\n" % e)
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

# **get_invoice**
> InvoiceDtoEnvelope get_invoice(tenant_id, invoice_id)

Get an invoice by ID.

Retrieves the invoice details for the specified invoice ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_dto_envelope import InvoiceDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get an invoice by ID.
        api_response = api_instance.get_invoice(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceDtoEnvelope**](InvoiceDtoEnvelope.md)

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

# **get_invoice_adjustment**
> InvoiceAdjustmentDtoEnvelope get_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_id)

Get an invoice adjustment by ID.

Retrieves the adjustment details for the specified invoice adjustment ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_adjustment_dto_envelope import InvoiceAdjustmentDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_id = 'invoice_adjustment_id_example' # str | 

    try:
        # Get an invoice adjustment by ID.
        api_response = api_instance.get_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_id)
        print("The response of InvoicesApi->get_invoice_adjustment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_adjustment: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_adjustments**
> InvoiceAdjustmentDtoIReadOnlyListEnvelope get_invoice_adjustments(tenant_id, invoice_id)

Get invoice adjustments.

Retrieves the adjustments for the specified invoice.

### Example


```python
import openapi_client
from openapi_client.models.invoice_adjustment_dto_i_read_only_list_envelope import InvoiceAdjustmentDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get invoice adjustments.
        api_response = api_instance.get_invoice_adjustments(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_invoice_adjustments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_adjustments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceAdjustmentDtoIReadOnlyListEnvelope**](InvoiceAdjustmentDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_adjustments_count**
> Int32Envelope get_invoice_adjustments_count(tenant_id, invoice_id)

Get the count of invoice adjustments.

Retrieves the total count of adjustments for the specified invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get the count of invoice adjustments.
        api_response = api_instance.get_invoice_adjustments_count(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_invoice_adjustments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_adjustments_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_line**
> InvoiceLineDtoEnvelope get_invoice_line(tenant_id, invoice_id, invoice_line_id)

Get an invoice line by ID.

Retrieves the invoice line details for the specified invoice line ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_line_dto_envelope import InvoiceLineDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        # Get an invoice line by ID.
        api_response = api_instance.get_invoice_line(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->get_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_line: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_line_taxes**
> InvoiceLineAppliedTaxDtoIReadOnlyListEnvelope get_invoice_line_taxes(tenant_id, invoice_id, invoice_line_id)

Get taxes for an invoice line.

Retrieves the taxes applied to the specified invoice line.

### Example


```python
import openapi_client
from openapi_client.models.invoice_line_applied_tax_dto_i_read_only_list_envelope import InvoiceLineAppliedTaxDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        # Get taxes for an invoice line.
        api_response = api_instance.get_invoice_line_taxes(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->get_invoice_line_taxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_line_taxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 

### Return type

[**InvoiceLineAppliedTaxDtoIReadOnlyListEnvelope**](InvoiceLineAppliedTaxDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_line_taxes_count**
> Int32Envelope get_invoice_line_taxes_count(tenant_id, invoice_id, invoice_line_id)

Get the count of taxes for an invoice line.

Retrieves the total count of taxes applied to the specified invoice line.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 

    try:
        # Get the count of taxes for an invoice line.
        api_response = api_instance.get_invoice_line_taxes_count(tenant_id, invoice_id, invoice_line_id)
        print("The response of InvoicesApi->get_invoice_line_taxes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_line_taxes_count: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_lines**
> InvoiceLineDtoListEnvelope get_invoice_lines(tenant_id, invoice_id, item_id=item_id)

Get invoice lines.

Retrieves the invoice lines for the specified invoice.

### Example


```python
import openapi_client
from openapi_client.models.invoice_line_dto_list_envelope import InvoiceLineDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        # Get invoice lines.
        api_response = api_instance.get_invoice_lines(tenant_id, invoice_id, item_id=item_id)
        print("The response of InvoicesApi->get_invoice_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_lines: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_lines_count**
> Int32Envelope get_invoice_lines_count(tenant_id, invoice_id)

Get the count of invoice lines.

Retrieves the total count of invoice lines for the specified invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get the count of invoice lines.
        api_response = api_instance.get_invoice_lines_count(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_invoice_lines_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_lines_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payments**
> PaymentDtoIReadOnlyListEnvelope get_invoice_payments(invoice_id)

Get payments for an invoice.

Retrieves the list of payments related to the specified invoice.

### Example


```python
import openapi_client
from openapi_client.models.payment_dto_i_read_only_list_envelope import PaymentDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get payments for an invoice.
        api_response = api_instance.get_invoice_payments(invoice_id)
        print("The response of InvoicesApi->get_invoice_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**PaymentDtoIReadOnlyListEnvelope**](PaymentDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payments_count**
> Int32Envelope get_invoice_payments_count(invoice_id)

Get the count of payments for an invoice.

Retrieves the total count of payments for the specified invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get the count of payments for an invoice.
        api_response = api_instance.get_invoice_payments_count(invoice_id)
        print("The response of InvoicesApi->get_invoice_payments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_payments_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_reference**
> InvoiceReferenceDtoEnvelope get_invoice_reference(tenant_id, invoice_id, invoice_reference_id)

Get an invoice reference by ID.

Retrieves the reference details for the specified invoice reference ID.

### Example


```python
import openapi_client
from openapi_client.models.invoice_reference_dto_envelope import InvoiceReferenceDtoEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_id = 'invoice_reference_id_example' # str | 

    try:
        # Get an invoice reference by ID.
        api_response = api_instance.get_invoice_reference(tenant_id, invoice_id, invoice_reference_id)
        print("The response of InvoicesApi->get_invoice_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_reference: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_references**
> InvoiceReferenceDtoIReadOnlyListEnvelope get_invoice_references(tenant_id, invoice_id)

Get invoice references.

Retrieves the references for the specified invoice.

### Example


```python
import openapi_client
from openapi_client.models.invoice_reference_dto_i_read_only_list_envelope import InvoiceReferenceDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get invoice references.
        api_response = api_instance.get_invoice_references(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_invoice_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_references: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceReferenceDtoIReadOnlyListEnvelope**](InvoiceReferenceDtoIReadOnlyListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_references_count**
> Int32Envelope get_invoice_references_count(tenant_id, invoice_id)

Get the count of invoice references.

Retrieves the total count of references for the specified invoice.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get the count of invoice references.
        api_response = api_instance.get_invoice_references_count(tenant_id, invoice_id)
        print("The response of InvoicesApi->get_invoice_references_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_references_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> InvoiceDtoListEnvelope get_invoices(tenant_id)

Get a list of invoices.

Retrieves a list of invoices for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.invoice_dto_list_envelope import InvoiceDtoListEnvelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get a list of invoices.
        api_response = api_instance.get_invoices(tenant_id)
        print("The response of InvoicesApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices_count**
> Int32Envelope get_invoices_count(tenant_id)

Get the count of invoices.

Retrieves the total count of invoices for the specified tenant.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get the count of invoices.
        api_response = api_instance.get_invoices_count(tenant_id)
        print("The response of InvoicesApi->get_invoices_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoices_count: %s\n" % e)
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

# **preview_invoice_email**
> preview_invoice_email(invoice_id, tenant_id, email_dispatch_request=email_dispatch_request)

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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    email_dispatch_request = openapi_client.EmailDispatchRequest() # EmailDispatchRequest |  (optional)

    try:
        # Preview the rendered email for an invoice.
        api_instance.preview_invoice_email(invoice_id, tenant_id, email_dispatch_request=email_dispatch_request)
    except Exception as e:
        print("Exception when calling InvoicesApi->preview_invoice_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
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

# **send_invoice_email**
> Envelope send_invoice_email(tenant_id, invoice_id, email_dispatch_request=email_dispatch_request)

Send an invoice transactional email to recipients.

This action is only available for users with the 'send_email' permission.

### Example


```python
import openapi_client
from openapi_client.models.email_dispatch_request import EmailDispatchRequest
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    email_dispatch_request = openapi_client.EmailDispatchRequest() # EmailDispatchRequest |  (optional)

    try:
        # Send an invoice transactional email to recipients.
        api_response = api_instance.send_invoice_email(tenant_id, invoice_id, email_dispatch_request=email_dispatch_request)
        print("The response of InvoicesApi->send_invoice_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->send_invoice_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **email_dispatch_request** | [**EmailDispatchRequest**](EmailDispatchRequest.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> EmptyEnvelope update_invoice(tenant_id, invoice_id, invoice_update_dto=invoice_update_dto)

Update an invoice.

Updates the specified invoice for the tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_update_dto import InvoiceUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_update_dto = openapi_client.InvoiceUpdateDto() # InvoiceUpdateDto |  (optional)

    try:
        # Update an invoice.
        api_response = api_instance.update_invoice(tenant_id, invoice_id, invoice_update_dto=invoice_update_dto)
        print("The response of InvoicesApi->update_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)
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

# **update_invoice_adjustment**
> EmptyEnvelope update_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_id, invoice_adjustment_update_dto=invoice_adjustment_update_dto)

Update an invoice adjustment.

Updates the specified adjustment for the invoice.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_adjustment_update_dto import InvoiceAdjustmentUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_adjustment_id = 'invoice_adjustment_id_example' # str | 
    invoice_adjustment_update_dto = openapi_client.InvoiceAdjustmentUpdateDto() # InvoiceAdjustmentUpdateDto |  (optional)

    try:
        # Update an invoice adjustment.
        api_response = api_instance.update_invoice_adjustment(tenant_id, invoice_id, invoice_adjustment_id, invoice_adjustment_update_dto=invoice_adjustment_update_dto)
        print("The response of InvoicesApi->update_invoice_adjustment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice_adjustment: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_line**
> InvoiceLineDtoEnvelope update_invoice_line(tenant_id, invoice_id, invoice_line_id, invoice_line_update_dto=invoice_line_update_dto)

Update an invoice line.

Updates the specified invoice line.

### Example


```python
import openapi_client
from openapi_client.models.invoice_line_dto_envelope import InvoiceLineDtoEnvelope
from openapi_client.models.invoice_line_update_dto import InvoiceLineUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_update_dto = openapi_client.InvoiceLineUpdateDto() # InvoiceLineUpdateDto |  (optional)

    try:
        # Update an invoice line.
        api_response = api_instance.update_invoice_line(tenant_id, invoice_id, invoice_line_id, invoice_line_update_dto=invoice_line_update_dto)
        print("The response of InvoicesApi->update_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **invoice_line_id** | **str**|  | 
 **invoice_line_update_dto** | [**InvoiceLineUpdateDto**](InvoiceLineUpdateDto.md)|  | [optional] 

### Return type

[**InvoiceLineDtoEnvelope**](InvoiceLineDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_line_tax**
> EmptyEnvelope update_invoice_line_tax(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id, invoice_line_applied_tax_update_dto=invoice_line_applied_tax_update_dto)

Update a tax for an invoice line.

Updates the specified tax entry for the invoice line.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_line_applied_tax_update_dto import InvoiceLineAppliedTaxUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_line_id = 'invoice_line_id_example' # str | 
    invoice_line_tax_id = 'invoice_line_tax_id_example' # str | 
    invoice_line_applied_tax_update_dto = openapi_client.InvoiceLineAppliedTaxUpdateDto() # InvoiceLineAppliedTaxUpdateDto |  (optional)

    try:
        # Update a tax for an invoice line.
        api_response = api_instance.update_invoice_line_tax(tenant_id, invoice_id, invoice_line_id, invoice_line_tax_id, invoice_line_applied_tax_update_dto=invoice_line_applied_tax_update_dto)
        print("The response of InvoicesApi->update_invoice_line_tax:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice_line_tax: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_reference**
> EmptyEnvelope update_invoice_reference(tenant_id, invoice_id, invoice_reference_id, invoice_reference_update_dto=invoice_reference_update_dto)

Update an invoice reference.

Updates the specified reference for the invoice.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.invoice_reference_update_dto import InvoiceReferenceUpdateDto
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
    api_instance = openapi_client.InvoicesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    invoice_reference_id = 'invoice_reference_id_example' # str | 
    invoice_reference_update_dto = openapi_client.InvoiceReferenceUpdateDto() # InvoiceReferenceUpdateDto |  (optional)

    try:
        # Update an invoice reference.
        api_response = api_instance.update_invoice_reference(tenant_id, invoice_id, invoice_reference_id, invoice_reference_update_dto=invoice_reference_update_dto)
        print("The response of InvoicesApi->update_invoice_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice_reference: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

