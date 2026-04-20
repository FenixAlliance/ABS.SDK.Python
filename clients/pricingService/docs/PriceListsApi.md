# openapi_client.PriceListsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_price_list_async**](PriceListsApi.md#create_price_list_async) | **POST** /api/v2/PricingService/PriceLists | Creates a new price list
[**create_price_list_prices_async**](PriceListsApi.md#create_price_list_prices_async) | **POST** /api/v2/PricingService/PriceLists/{priceListId}/Prices | Creates a price list entry
[**delete_price_list_async**](PriceListsApi.md#delete_price_list_async) | **DELETE** /api/v2/PricingService/PriceLists/{priceListId} | Deletes a price list
[**delete_price_list_price_async**](PriceListsApi.md#delete_price_list_price_async) | **DELETE** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | Deletes a price list entry
[**get_price_list_async**](PriceListsApi.md#get_price_list_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId} | Gets a price list by ID
[**get_price_list_price_async**](PriceListsApi.md#get_price_list_price_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | Gets a price list entry by ID
[**get_price_list_prices_async**](PriceListsApi.md#get_price_list_prices_async) | **GET** /api/v2/PricingService/PriceLists/{priceListId}/Prices | Retrieves prices in a price list
[**get_price_lists_async**](PriceListsApi.md#get_price_lists_async) | **GET** /api/v2/PricingService/PriceLists | Retrieves all price lists
[**get_price_lists_count_async**](PriceListsApi.md#get_price_lists_count_async) | **GET** /api/v2/PricingService/PriceLists/Count | Counts price lists
[**update_price_list_async**](PriceListsApi.md#update_price_list_async) | **PUT** /api/v2/PricingService/PriceLists/{priceListId} | Updates a price list
[**update_price_list_price_async**](PriceListsApi.md#update_price_list_price_async) | **PUT** /api/v2/PricingService/PriceLists/{priceListId}/Prices/{priceId} | Updates a price list entry


# **create_price_list_async**
> EmptyEnvelope create_price_list_async(tenant_id, price_list_create_dto=price_list_create_dto)

Creates a new price list

Creates a new price list for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.price_list_create_dto import PriceListCreateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_create_dto = openapi_client.PriceListCreateDto() # PriceListCreateDto |  (optional)

    try:
        # Creates a new price list
        api_response = api_instance.create_price_list_async(tenant_id, price_list_create_dto=price_list_create_dto)
        print("The response of PriceListsApi->create_price_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->create_price_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_create_dto** | [**PriceListCreateDto**](PriceListCreateDto.md)|  | [optional] 

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

# **create_price_list_prices_async**
> EmptyEnvelope create_price_list_prices_async(tenant_id, price_list_id, item_price_create_dto=item_price_create_dto)

Creates a price list entry

Creates a new price entry in the specified price list.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_price_create_dto import ItemPriceCreateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    item_price_create_dto = openapi_client.ItemPriceCreateDto() # ItemPriceCreateDto |  (optional)

    try:
        # Creates a price list entry
        api_response = api_instance.create_price_list_prices_async(tenant_id, price_list_id, item_price_create_dto=item_price_create_dto)
        print("The response of PriceListsApi->create_price_list_prices_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->create_price_list_prices_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **item_price_create_dto** | [**ItemPriceCreateDto**](ItemPriceCreateDto.md)|  | [optional] 

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

# **delete_price_list_async**
> EmptyEnvelope delete_price_list_async(tenant_id, price_list_id)

Deletes a price list

Deletes the specified price list.

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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 

    try:
        # Deletes a price list
        api_response = api_instance.delete_price_list_async(tenant_id, price_list_id)
        print("The response of PriceListsApi->delete_price_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->delete_price_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 

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

# **delete_price_list_price_async**
> EmptyEnvelope delete_price_list_price_async(tenant_id, price_list_id, price_id)

Deletes a price list entry

Deletes the specified price entry from a price list.

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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    price_id = 'price_id_example' # str | 

    try:
        # Deletes a price list entry
        api_response = api_instance.delete_price_list_price_async(tenant_id, price_list_id, price_id)
        print("The response of PriceListsApi->delete_price_list_price_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->delete_price_list_price_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **price_id** | **str**|  | 

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

# **get_price_list_async**
> PriceListDtoEnvelope get_price_list_async(tenant_id, price_list_id)

Gets a price list by ID

Retrieves the details of a price list using its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.price_list_dto_envelope import PriceListDtoEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 

    try:
        # Gets a price list by ID
        api_response = api_instance.get_price_list_async(tenant_id, price_list_id)
        print("The response of PriceListsApi->get_price_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 

### Return type

[**PriceListDtoEnvelope**](PriceListDtoEnvelope.md)

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

# **get_price_list_price_async**
> ItemPriceDtoEnvelope get_price_list_price_async(tenant_id, price_list_id, price_id)

Gets a price list entry by ID

Retrieves a specific price entry from a price list.

### Example


```python
import openapi_client
from openapi_client.models.item_price_dto_envelope import ItemPriceDtoEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    price_id = 'price_id_example' # str | 

    try:
        # Gets a price list entry by ID
        api_response = api_instance.get_price_list_price_async(tenant_id, price_list_id, price_id)
        print("The response of PriceListsApi->get_price_list_price_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_list_price_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **price_id** | **str**|  | 

### Return type

[**ItemPriceDtoEnvelope**](ItemPriceDtoEnvelope.md)

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

# **get_price_list_prices_async**
> ItemPriceDtoListEnvelope get_price_list_prices_async(tenant_id, price_list_id, item_id=item_id)

Retrieves prices in a price list

Gets all price entries for a specific price list with OData support.

### Example


```python
import openapi_client
from openapi_client.models.item_price_dto_list_envelope import ItemPriceDtoListEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        # Retrieves prices in a price list
        api_response = api_instance.get_price_list_prices_async(tenant_id, price_list_id, item_id=item_id)
        print("The response of PriceListsApi->get_price_list_prices_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_list_prices_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 

### Return type

[**ItemPriceDtoListEnvelope**](ItemPriceDtoListEnvelope.md)

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

# **get_price_lists_async**
> PriceListDtoListEnvelope get_price_lists_async(tenant_id)

Retrieves all price lists

Gets all price lists for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.price_list_dto_list_envelope import PriceListDtoListEnvelope
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves all price lists
        api_response = api_instance.get_price_lists_async(tenant_id)
        print("The response of PriceListsApi->get_price_lists_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_lists_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**PriceListDtoListEnvelope**](PriceListDtoListEnvelope.md)

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

# **get_price_lists_count_async**
> Int32Envelope get_price_lists_count_async(tenant_id)

Counts price lists

Gets the count of price lists for the current tenant.

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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Counts price lists
        api_response = api_instance.get_price_lists_count_async(tenant_id)
        print("The response of PriceListsApi->get_price_lists_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->get_price_lists_count_async: %s\n" % e)
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

# **update_price_list_async**
> EmptyEnvelope update_price_list_async(tenant_id, price_list_id, price_list_update_dto=price_list_update_dto)

Updates a price list

Updates the specified price list.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.price_list_update_dto import PriceListUpdateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    price_list_update_dto = openapi_client.PriceListUpdateDto() # PriceListUpdateDto |  (optional)

    try:
        # Updates a price list
        api_response = api_instance.update_price_list_async(tenant_id, price_list_id, price_list_update_dto=price_list_update_dto)
        print("The response of PriceListsApi->update_price_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->update_price_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **price_list_update_dto** | [**PriceListUpdateDto**](PriceListUpdateDto.md)|  | [optional] 

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

# **update_price_list_price_async**
> EmptyEnvelope update_price_list_price_async(tenant_id, price_list_id, price_id, item_price_update_dto=item_price_update_dto)

Updates a price list entry

Updates the specified price entry in a price list.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_price_update_dto import ItemPriceUpdateDto
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
    api_instance = openapi_client.PriceListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    price_list_id = 'price_list_id_example' # str | 
    price_id = 'price_id_example' # str | 
    item_price_update_dto = openapi_client.ItemPriceUpdateDto() # ItemPriceUpdateDto |  (optional)

    try:
        # Updates a price list entry
        api_response = api_instance.update_price_list_price_async(tenant_id, price_list_id, price_id, item_price_update_dto=item_price_update_dto)
        print("The response of PriceListsApi->update_price_list_price_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListsApi->update_price_list_price_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **price_list_id** | **str**|  | 
 **price_id** | **str**|  | 
 **item_price_update_dto** | [**ItemPriceUpdateDto**](ItemPriceUpdateDto.md)|  | [optional] 

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

