# openapi_client.AssetTransfersApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_transfer_async**](AssetTransfersApi.md#create_asset_transfer_async) | **POST** /api/v2/AssetsService/AssetTransfers | Creates a new asset transfer
[**delete_asset_transfer_async**](AssetTransfersApi.md#delete_asset_transfer_async) | **DELETE** /api/v2/AssetsService/AssetTransfers/{transferId} | Deletes an asset transfer
[**get_asset_transfer_async**](AssetTransfersApi.md#get_asset_transfer_async) | **GET** /api/v2/AssetsService/AssetTransfers/{transferId} | Gets a single asset transfer by ID
[**get_asset_transfers_async**](AssetTransfersApi.md#get_asset_transfers_async) | **GET** /api/v2/AssetsService/AssetTransfers | Gets a list of asset transfers
[**get_asset_transfers_count_async**](AssetTransfersApi.md#get_asset_transfers_count_async) | **GET** /api/v2/AssetsService/AssetTransfers/Count | Gets the count of asset transfers
[**update_asset_transfer_async**](AssetTransfersApi.md#update_asset_transfer_async) | **PUT** /api/v2/AssetsService/AssetTransfers/{transferId} | Updates an existing asset transfer


# **create_asset_transfer_async**
> EmptyEnvelope create_asset_transfer_async(tenant_id, asset_transfer_create_dto=asset_transfer_create_dto)

Creates a new asset transfer

Creates a new asset transfer for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_create_dto import AssetTransferCreateDto
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
    api_instance = openapi_client.AssetTransfersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_transfer_create_dto = openapi_client.AssetTransferCreateDto() # AssetTransferCreateDto |  (optional)

    try:
        # Creates a new asset transfer
        api_response = api_instance.create_asset_transfer_async(tenant_id, asset_transfer_create_dto=asset_transfer_create_dto)
        print("The response of AssetTransfersApi->create_asset_transfer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTransfersApi->create_asset_transfer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_transfer_create_dto** | [**AssetTransferCreateDto**](AssetTransferCreateDto.md)|  | [optional] 

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

# **delete_asset_transfer_async**
> EmptyEnvelope delete_asset_transfer_async(tenant_id, transfer_id)

Deletes an asset transfer

Deletes an asset transfer for the authenticated tenant.

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
    api_instance = openapi_client.AssetTransfersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 

    try:
        # Deletes an asset transfer
        api_response = api_instance.delete_asset_transfer_async(tenant_id, transfer_id)
        print("The response of AssetTransfersApi->delete_asset_transfer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTransfersApi->delete_asset_transfer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transfer_id** | **str**|  | 

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

# **get_asset_transfer_async**
> AssetTransferDtoEnvelope get_asset_transfer_async(tenant_id, transfer_id)

Gets a single asset transfer by ID

Retrieves a specific asset transfer by its ID for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_dto_envelope import AssetTransferDtoEnvelope
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
    api_instance = openapi_client.AssetTransfersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 

    try:
        # Gets a single asset transfer by ID
        api_response = api_instance.get_asset_transfer_async(tenant_id, transfer_id)
        print("The response of AssetTransfersApi->get_asset_transfer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTransfersApi->get_asset_transfer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transfer_id** | **str**|  | 

### Return type

[**AssetTransferDtoEnvelope**](AssetTransferDtoEnvelope.md)

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

# **get_asset_transfers_async**
> AssetTransferDtoListEnvelope get_asset_transfers_async(tenant_id)

Gets a list of asset transfers

Retrieves all asset transfers for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_dto_list_envelope import AssetTransferDtoListEnvelope
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
    api_instance = openapi_client.AssetTransfersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets a list of asset transfers
        api_response = api_instance.get_asset_transfers_async(tenant_id)
        print("The response of AssetTransfersApi->get_asset_transfers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTransfersApi->get_asset_transfers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**AssetTransferDtoListEnvelope**](AssetTransferDtoListEnvelope.md)

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

# **get_asset_transfers_count_async**
> Int32Envelope get_asset_transfers_count_async(tenant_id)

Gets the count of asset transfers

Returns the total number of asset transfers for the authenticated tenant.

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
    api_instance = openapi_client.AssetTransfersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets the count of asset transfers
        api_response = api_instance.get_asset_transfers_count_async(tenant_id)
        print("The response of AssetTransfersApi->get_asset_transfers_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTransfersApi->get_asset_transfers_count_async: %s\n" % e)
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_transfer_async**
> EmptyEnvelope update_asset_transfer_async(tenant_id, transfer_id, asset_transfer_update_dto=asset_transfer_update_dto)

Updates an existing asset transfer

Updates an existing asset transfer for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_update_dto import AssetTransferUpdateDto
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
    api_instance = openapi_client.AssetTransfersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 
    asset_transfer_update_dto = openapi_client.AssetTransferUpdateDto() # AssetTransferUpdateDto |  (optional)

    try:
        # Updates an existing asset transfer
        api_response = api_instance.update_asset_transfer_async(tenant_id, transfer_id, asset_transfer_update_dto=asset_transfer_update_dto)
        print("The response of AssetTransfersApi->update_asset_transfer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTransfersApi->update_asset_transfer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transfer_id** | **str**|  | 
 **asset_transfer_update_dto** | [**AssetTransferUpdateDto**](AssetTransferUpdateDto.md)|  | [optional] 

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

