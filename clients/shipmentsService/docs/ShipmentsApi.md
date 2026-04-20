# openapi_client.ShipmentsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shipments_async**](ShipmentsApi.md#get_shipments_async) | **GET** /api/v2/ShipmentsService/Shipments | Retrieve a list of shipments


# **get_shipments_async**
> ShipmentDtoListEnvelope get_shipments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of shipments

Retrieves a list of shipments for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.shipment_dto_list_envelope import ShipmentDtoListEnvelope
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of shipments
        api_response = api_instance.get_shipments_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ShipmentsApi->get_shipments_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->get_shipments_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShipmentDtoListEnvelope**](ShipmentDtoListEnvelope.md)

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

