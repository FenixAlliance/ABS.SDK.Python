# openapi_client.ReceiptsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_receipt_async**](ReceiptsApi.md#create_receipt_async) | **POST** /api/v2/AccountingService/Receipts | Creates a new receipt
[**delete_receipt_async**](ReceiptsApi.md#delete_receipt_async) | **DELETE** /api/v2/AccountingService/Receipts/{receiptId} | Deletes a receipt
[**get_receipt_details_async**](ReceiptsApi.md#get_receipt_details_async) | **GET** /api/v2/AccountingService/Receipts/{receiptId} | Gets details of a receipt
[**get_receipts_async**](ReceiptsApi.md#get_receipts_async) | **GET** /api/v2/AccountingService/Receipts | Retrieves tenant receipts
[**get_receipts_count_async**](ReceiptsApi.md#get_receipts_count_async) | **GET** /api/v2/AccountingService/Receipts/Count | Gets count of tenant receipts
[**update_receipt_async**](ReceiptsApi.md#update_receipt_async) | **PUT** /api/v2/AccountingService/Receipts/{receiptId} | Updates a receipt


# **create_receipt_async**
> EmptyEnvelope create_receipt_async(tenant_id, receipt_create_dto)

Creates a new receipt

Adds a new receipt record under the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.receipt_create_dto import ReceiptCreateDto
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
    api_instance = openapi_client.ReceiptsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    receipt_create_dto = openapi_client.ReceiptCreateDto() # ReceiptCreateDto | 

    try:
        # Creates a new receipt
        api_response = api_instance.create_receipt_async(tenant_id, receipt_create_dto)
        print("The response of ReceiptsApi->create_receipt_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiptsApi->create_receipt_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **receipt_create_dto** | [**ReceiptCreateDto**](ReceiptCreateDto.md)|  | 

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

# **delete_receipt_async**
> EmptyEnvelope delete_receipt_async(tenant_id, receipt_id)

Deletes a receipt

Removes an existing receipt from the tenant’s records.

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
    api_instance = openapi_client.ReceiptsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    receipt_id = 'receipt_id_example' # str | 

    try:
        # Deletes a receipt
        api_response = api_instance.delete_receipt_async(tenant_id, receipt_id)
        print("The response of ReceiptsApi->delete_receipt_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiptsApi->delete_receipt_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **receipt_id** | **str**|  | 

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

# **get_receipt_details_async**
> ReceiptDtoEnvelope get_receipt_details_async(tenant_id, receipt_id)

Gets details of a receipt

Retrieves a specific receipt by its ID for the given tenant.

### Example


```python
import openapi_client
from openapi_client.models.receipt_dto_envelope import ReceiptDtoEnvelope
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
    api_instance = openapi_client.ReceiptsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    receipt_id = 'receipt_id_example' # str | 

    try:
        # Gets details of a receipt
        api_response = api_instance.get_receipt_details_async(tenant_id, receipt_id)
        print("The response of ReceiptsApi->get_receipt_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiptsApi->get_receipt_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **receipt_id** | **str**|  | 

### Return type

[**ReceiptDtoEnvelope**](ReceiptDtoEnvelope.md)

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

# **get_receipts_async**
> ReceiptDtoIReadOnlyListEnvelope get_receipts_async(tenant_id)

Retrieves tenant receipts

Fetches all receipts for a given tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.receipt_dto_i_read_only_list_envelope import ReceiptDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ReceiptsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves tenant receipts
        api_response = api_instance.get_receipts_async(tenant_id)
        print("The response of ReceiptsApi->get_receipts_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiptsApi->get_receipts_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ReceiptDtoIReadOnlyListEnvelope**](ReceiptDtoIReadOnlyListEnvelope.md)

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

# **get_receipts_count_async**
> Int32Envelope get_receipts_count_async(tenant_id)

Gets count of tenant receipts

Returns total number of receipts for the tenant with OData filter support.

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
    api_instance = openapi_client.ReceiptsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets count of tenant receipts
        api_response = api_instance.get_receipts_count_async(tenant_id)
        print("The response of ReceiptsApi->get_receipts_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiptsApi->get_receipts_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receipt_async**
> EmptyEnvelope update_receipt_async(tenant_id, receipt_id, receipt_update_dto)

Updates a receipt

Modifies the data of an existing receipt for the given tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.receipt_update_dto import ReceiptUpdateDto
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
    api_instance = openapi_client.ReceiptsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    receipt_id = 'receipt_id_example' # str | 
    receipt_update_dto = openapi_client.ReceiptUpdateDto() # ReceiptUpdateDto | 

    try:
        # Updates a receipt
        api_response = api_instance.update_receipt_async(tenant_id, receipt_id, receipt_update_dto)
        print("The response of ReceiptsApi->update_receipt_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReceiptsApi->update_receipt_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **receipt_id** | **str**|  | 
 **receipt_update_dto** | [**ReceiptUpdateDto**](ReceiptUpdateDto.md)|  | 

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

