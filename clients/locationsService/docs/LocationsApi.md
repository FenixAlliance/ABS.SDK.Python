# openapi_client.LocationsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_location_async**](LocationsApi.md#create_location_async) | **POST** /api/v2/LocationsService/Locations | Create Location
[**create_wallet_location_async**](LocationsApi.md#create_wallet_location_async) | **POST** /api/v2/LocationsService/Locations/wallet/{walletId} | Create Wallet Location
[**delete_location_async**](LocationsApi.md#delete_location_async) | **DELETE** /api/v2/LocationsService/Locations/{locationId} | Delete Location
[**delete_wallet_location_async**](LocationsApi.md#delete_wallet_location_async) | **DELETE** /api/v2/LocationsService/Locations/wallet/{walletId}/{locationId} | Delete Wallet Location
[**get_location_async**](LocationsApi.md#get_location_async) | **GET** /api/v2/LocationsService/Locations/{locationId} | Get Location
[**get_locations_async**](LocationsApi.md#get_locations_async) | **GET** /api/v2/LocationsService/Locations | Get Locations
[**get_locations_count_async**](LocationsApi.md#get_locations_count_async) | **GET** /api/v2/LocationsService/Locations/count | Get Locations Count
[**get_wallet_location_async**](LocationsApi.md#get_wallet_location_async) | **GET** /api/v2/LocationsService/Locations/wallet/{walletId}/{locationId} | Get Wallet Location
[**get_wallet_locations_async**](LocationsApi.md#get_wallet_locations_async) | **GET** /api/v2/LocationsService/Locations/wallet/{walletId} | Get Wallet Locations
[**get_wallet_locations_count_async**](LocationsApi.md#get_wallet_locations_count_async) | **GET** /api/v2/LocationsService/Locations/wallet/{walletId}/count | Get Wallet Locations Count
[**update_location_async**](LocationsApi.md#update_location_async) | **PUT** /api/v2/LocationsService/Locations/{locationId} | Update Location
[**update_wallet_location_async**](LocationsApi.md#update_wallet_location_async) | **PUT** /api/v2/LocationsService/Locations/wallet/{walletId}/{locationId} | Update Wallet Location


# **create_location_async**
> EmptyEnvelope create_location_async(tenant_id, location_create_dto=location_create_dto)

Create Location

Create a new location.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.location_create_dto import LocationCreateDto
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
    api_instance = openapi_client.LocationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    location_create_dto = openapi_client.LocationCreateDto() # LocationCreateDto |  (optional)

    try:
        # Create Location
        api_response = api_instance.create_location_async(tenant_id, location_create_dto=location_create_dto)
        print("The response of LocationsApi->create_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->create_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **location_create_dto** | [**LocationCreateDto**](LocationCreateDto.md)|  | [optional] 

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

# **create_wallet_location_async**
> EmptyEnvelope create_wallet_location_async(wallet_id, location_create_dto=location_create_dto)

Create Wallet Location

Create a new location for a specific wallet.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.location_create_dto import LocationCreateDto
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
    api_instance = openapi_client.LocationsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    location_create_dto = openapi_client.LocationCreateDto() # LocationCreateDto |  (optional)

    try:
        # Create Wallet Location
        api_response = api_instance.create_wallet_location_async(wallet_id, location_create_dto=location_create_dto)
        print("The response of LocationsApi->create_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->create_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **location_create_dto** | [**LocationCreateDto**](LocationCreateDto.md)|  | [optional] 

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

# **delete_location_async**
> EmptyEnvelope delete_location_async(tenant_id, location_id)

Delete Location

Delete a specific location by ID.

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
    api_instance = openapi_client.LocationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    location_id = 'location_id_example' # str | 

    try:
        # Delete Location
        api_response = api_instance.delete_location_async(tenant_id, location_id)
        print("The response of LocationsApi->delete_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->delete_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **location_id** | **str**|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wallet_location_async**
> EmptyEnvelope delete_wallet_location_async(wallet_id, location_id)

Delete Wallet Location

Delete a specific location of a wallet.

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
    api_instance = openapi_client.LocationsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    location_id = 'location_id_example' # str | 

    try:
        # Delete Wallet Location
        api_response = api_instance.delete_wallet_location_async(wallet_id, location_id)
        print("The response of LocationsApi->delete_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->delete_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **location_id** | **str**|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_async**
> LocationDtoEnvelope get_location_async(tenant_id, location_id)

Get Location

Get details of a specific location by ID.

### Example


```python
import openapi_client
from openapi_client.models.location_dto_envelope import LocationDtoEnvelope
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
    api_instance = openapi_client.LocationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    location_id = 'location_id_example' # str | 

    try:
        # Get Location
        api_response = api_instance.get_location_async(tenant_id, location_id)
        print("The response of LocationsApi->get_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **location_id** | **str**|  | 

### Return type

[**LocationDtoEnvelope**](LocationDtoEnvelope.md)

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

# **get_locations_async**
> LocationDtoIReadOnlyListEnvelope get_locations_async(tenant_id)

Get Locations

Get all locations with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.location_dto_i_read_only_list_envelope import LocationDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.LocationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get Locations
        api_response = api_instance.get_locations_async(tenant_id)
        print("The response of LocationsApi->get_locations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**LocationDtoIReadOnlyListEnvelope**](LocationDtoIReadOnlyListEnvelope.md)

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

# **get_locations_count_async**
> Int32Envelope get_locations_count_async(tenant_id)

Get Locations Count

Get the count of locations with OData query support.

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
    api_instance = openapi_client.LocationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get Locations Count
        api_response = api_instance.get_locations_count_async(tenant_id)
        print("The response of LocationsApi->get_locations_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations_count_async: %s\n" % e)
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

# **get_wallet_location_async**
> LocationDtoEnvelope get_wallet_location_async(wallet_id, location_id)

Get Wallet Location

Get a specific location of a wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.location_dto_envelope import LocationDtoEnvelope
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
    api_instance = openapi_client.LocationsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    location_id = 'location_id_example' # str | 

    try:
        # Get Wallet Location
        api_response = api_instance.get_wallet_location_async(wallet_id, location_id)
        print("The response of LocationsApi->get_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **location_id** | **str**|  | 

### Return type

[**LocationDtoEnvelope**](LocationDtoEnvelope.md)

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

# **get_wallet_locations_async**
> LocationDtoIReadOnlyListEnvelope get_wallet_locations_async(wallet_id)

Get Wallet Locations

Get locations for a specific wallet by ID.

### Example


```python
import openapi_client
from openapi_client.models.location_dto_i_read_only_list_envelope import LocationDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.LocationsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Get Wallet Locations
        api_response = api_instance.get_wallet_locations_async(wallet_id)
        print("The response of LocationsApi->get_wallet_locations_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_wallet_locations_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 

### Return type

[**LocationDtoIReadOnlyListEnvelope**](LocationDtoIReadOnlyListEnvelope.md)

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

# **get_wallet_locations_count_async**
> Int32Envelope get_wallet_locations_count_async(wallet_id)

Get Wallet Locations Count

Get the count of locations for a specific wallet by ID.

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
    api_instance = openapi_client.LocationsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Get Wallet Locations Count
        api_response = api_instance.get_wallet_locations_count_async(wallet_id)
        print("The response of LocationsApi->get_wallet_locations_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_wallet_locations_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 

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

# **update_location_async**
> EmptyEnvelope update_location_async(tenant_id, location_id, location_update_dto=location_update_dto)

Update Location

Update a specific location by ID.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.location_update_dto import LocationUpdateDto
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
    api_instance = openapi_client.LocationsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    location_id = 'location_id_example' # str | 
    location_update_dto = openapi_client.LocationUpdateDto() # LocationUpdateDto |  (optional)

    try:
        # Update Location
        api_response = api_instance.update_location_async(tenant_id, location_id, location_update_dto=location_update_dto)
        print("The response of LocationsApi->update_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->update_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **location_id** | **str**|  | 
 **location_update_dto** | [**LocationUpdateDto**](LocationUpdateDto.md)|  | [optional] 

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

# **update_wallet_location_async**
> EmptyEnvelope update_wallet_location_async(wallet_id, location_id, location_update_dto=location_update_dto)

Update Wallet Location

Update a specific location of a wallet.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.location_update_dto import LocationUpdateDto
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
    api_instance = openapi_client.LocationsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    location_id = 'location_id_example' # str | 
    location_update_dto = openapi_client.LocationUpdateDto() # LocationUpdateDto |  (optional)

    try:
        # Update Wallet Location
        api_response = api_instance.update_wallet_location_async(wallet_id, location_id, location_update_dto=location_update_dto)
        print("The response of LocationsApi->update_wallet_location_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->update_wallet_location_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **location_id** | **str**|  | 
 **location_update_dto** | [**LocationUpdateDto**](LocationUpdateDto.md)|  | [optional] 

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

