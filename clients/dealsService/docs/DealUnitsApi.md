# openapi_client.DealUnitsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_deal_unit_async**](DealUnitsApi.md#calculate_deal_unit_async) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId}/Calculate | Calculate a deal unit
[**calculate_deal_unit_line_async**](DealUnitsApi.md#calculate_deal_unit_line_async) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId}/Calculate | Calculate a deal unit line
[**create_deal_unit_async**](DealUnitsApi.md#create_deal_unit_async) | **POST** /api/v2/DealsService/DealUnits | Create a deal unit
[**create_get_deal_unit_lines_async**](DealUnitsApi.md#create_get_deal_unit_lines_async) | **POST** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines | Create a deal unit line
[**delete_deal_unit_async**](DealUnitsApi.md#delete_deal_unit_async) | **DELETE** /api/v2/DealsService/DealUnits/{dealUnitId} | Delete a deal unit
[**delete_deal_unit_price_async**](DealUnitsApi.md#delete_deal_unit_price_async) | **DELETE** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId} | Delete a deal unit line
[**get_deal_unit_async**](DealUnitsApi.md#get_deal_unit_async) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId} | Get deal unit by ID
[**get_deal_unit_lines_async**](DealUnitsApi.md#get_deal_unit_lines_async) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines | Get deal unit lines
[**get_deal_unit_lines_count_async**](DealUnitsApi.md#get_deal_unit_lines_count_async) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/Count | Get deal unit lines count
[**get_deal_unit_price_async**](DealUnitsApi.md#get_deal_unit_price_async) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId} | Get a deal unit line by ID
[**get_deal_units_async**](DealUnitsApi.md#get_deal_units_async) | **GET** /api/v2/DealsService/DealUnits | Get deal units
[**get_deal_units_count_async**](DealUnitsApi.md#get_deal_units_count_async) | **GET** /api/v2/DealsService/DealUnits/Count | Get deal units count
[**get_extended_deal_unit_async**](DealUnitsApi.md#get_extended_deal_unit_async) | **GET** /api/v2/DealsService/DealUnits/{dealUnitId}/Extended | Get extended deal unit by ID
[**get_extended_deal_units_async**](DealUnitsApi.md#get_extended_deal_units_async) | **GET** /api/v2/DealsService/DealUnits/Extended | Get extended deal units
[**update_deal_unit_async**](DealUnitsApi.md#update_deal_unit_async) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId} | Update a deal unit
[**update_deal_unit_price_async**](DealUnitsApi.md#update_deal_unit_price_async) | **PUT** /api/v2/DealsService/DealUnits/{dealUnitId}/Lines/{dealUnitLineId} | Update a deal unit line


# **calculate_deal_unit_async**
> EmptyEnvelope calculate_deal_unit_async(tenant_id, deal_unit_id)

Calculate a deal unit

Triggers recalculation of totals and derived values for a specific deal unit.

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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        # Calculate a deal unit
        api_response = api_instance.calculate_deal_unit_async(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->calculate_deal_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->calculate_deal_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

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

# **calculate_deal_unit_line_async**
> EmptyEnvelope calculate_deal_unit_line_async(tenant_id, deal_unit_id, deal_unit_line_id)

Calculate a deal unit line

Triggers recalculation of totals and derived values for a specific deal unit line.

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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 

    try:
        # Calculate a deal unit line
        api_response = api_instance.calculate_deal_unit_line_async(tenant_id, deal_unit_id, deal_unit_line_id)
        print("The response of DealUnitsApi->calculate_deal_unit_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->calculate_deal_unit_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 

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

# **create_deal_unit_async**
> EmptyEnvelope create_deal_unit_async(tenant_id, deal_unit_create_dto=deal_unit_create_dto)

Create a deal unit

Creates a new deal unit for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_create_dto import DealUnitCreateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_create_dto = openapi_client.DealUnitCreateDto() # DealUnitCreateDto |  (optional)

    try:
        # Create a deal unit
        api_response = api_instance.create_deal_unit_async(tenant_id, deal_unit_create_dto=deal_unit_create_dto)
        print("The response of DealUnitsApi->create_deal_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->create_deal_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_create_dto** | [**DealUnitCreateDto**](DealUnitCreateDto.md)|  | [optional] 

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

# **create_get_deal_unit_lines_async**
> EmptyEnvelope create_get_deal_unit_lines_async(tenant_id, deal_unit_id, deal_unit_line_create_dto=deal_unit_line_create_dto)

Create a deal unit line

Creates a new line within a specific deal unit.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_line_create_dto import DealUnitLineCreateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_create_dto = openapi_client.DealUnitLineCreateDto() # DealUnitLineCreateDto |  (optional)

    try:
        # Create a deal unit line
        api_response = api_instance.create_get_deal_unit_lines_async(tenant_id, deal_unit_id, deal_unit_line_create_dto=deal_unit_line_create_dto)
        print("The response of DealUnitsApi->create_get_deal_unit_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->create_get_deal_unit_lines_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_create_dto** | [**DealUnitLineCreateDto**](DealUnitLineCreateDto.md)|  | [optional] 

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

# **delete_deal_unit_async**
> EmptyEnvelope delete_deal_unit_async(tenant_id, deal_unit_id)

Delete a deal unit

Deletes an existing deal unit by its unique identifier.

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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        # Delete a deal unit
        api_response = api_instance.delete_deal_unit_async(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->delete_deal_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->delete_deal_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

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

# **delete_deal_unit_price_async**
> EmptyEnvelope delete_deal_unit_price_async(tenant_id, deal_unit_id, deal_unit_line_id)

Delete a deal unit line

Deletes an existing line from a specific deal unit.

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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 

    try:
        # Delete a deal unit line
        api_response = api_instance.delete_deal_unit_price_async(tenant_id, deal_unit_id, deal_unit_line_id)
        print("The response of DealUnitsApi->delete_deal_unit_price_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->delete_deal_unit_price_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 

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

# **get_deal_unit_async**
> DealUnitDtoEnvelope get_deal_unit_async(tenant_id, deal_unit_id)

Get deal unit by ID

Retrieves a single deal unit by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_dto_envelope import DealUnitDtoEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        # Get deal unit by ID
        api_response = api_instance.get_deal_unit_async(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->get_deal_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_deal_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

### Return type

[**DealUnitDtoEnvelope**](DealUnitDtoEnvelope.md)

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

# **get_deal_unit_lines_async**
> DealUnitLineDtoListEnvelope get_deal_unit_lines_async(tenant_id, deal_unit_id, item_id=item_id)

Get deal unit lines

Retrieves a list of lines for a specific deal unit with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_line_dto_list_envelope import DealUnitLineDtoListEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    item_id = 'item_id_example' # str |  (optional)

    try:
        # Get deal unit lines
        api_response = api_instance.get_deal_unit_lines_async(tenant_id, deal_unit_id, item_id=item_id)
        print("The response of DealUnitsApi->get_deal_unit_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_deal_unit_lines_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **item_id** | **str**|  | [optional] 

### Return type

[**DealUnitLineDtoListEnvelope**](DealUnitLineDtoListEnvelope.md)

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

# **get_deal_unit_lines_count_async**
> Int32Envelope get_deal_unit_lines_count_async(tenant_id, deal_unit_id)

Get deal unit lines count

Returns the total count of lines for a specific deal unit with OData filter support.

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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        # Get deal unit lines count
        api_response = api_instance.get_deal_unit_lines_count_async(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->get_deal_unit_lines_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_deal_unit_lines_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

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

# **get_deal_unit_price_async**
> DealUnitLineDtoEnvelope get_deal_unit_price_async(tenant_id, deal_unit_id, deal_unit_line_id)

Get a deal unit line by ID

Retrieves a single deal unit line by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_line_dto_envelope import DealUnitLineDtoEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 

    try:
        # Get a deal unit line by ID
        api_response = api_instance.get_deal_unit_price_async(tenant_id, deal_unit_id, deal_unit_line_id)
        print("The response of DealUnitsApi->get_deal_unit_price_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_deal_unit_price_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 

### Return type

[**DealUnitLineDtoEnvelope**](DealUnitLineDtoEnvelope.md)

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

# **get_deal_units_async**
> DealUnitDtoListEnvelope get_deal_units_async(tenant_id)

Get deal units

Retrieves a list of deal units for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_dto_list_envelope import DealUnitDtoListEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get deal units
        api_response = api_instance.get_deal_units_async(tenant_id)
        print("The response of DealUnitsApi->get_deal_units_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_deal_units_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**DealUnitDtoListEnvelope**](DealUnitDtoListEnvelope.md)

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

# **get_deal_units_count_async**
> Int32Envelope get_deal_units_count_async(tenant_id)

Get deal units count

Returns the total count of deal units for the specified tenant with OData filter support.

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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get deal units count
        api_response = api_instance.get_deal_units_count_async(tenant_id)
        print("The response of DealUnitsApi->get_deal_units_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_deal_units_count_async: %s\n" % e)
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

# **get_extended_deal_unit_async**
> ExtendedDealUnitDtoEnvelope get_extended_deal_unit_async(tenant_id, deal_unit_id)

Get extended deal unit by ID

Retrieves a single deal unit with extended details by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.extended_deal_unit_dto_envelope import ExtendedDealUnitDtoEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 

    try:
        # Get extended deal unit by ID
        api_response = api_instance.get_extended_deal_unit_async(tenant_id, deal_unit_id)
        print("The response of DealUnitsApi->get_extended_deal_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_extended_deal_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 

### Return type

[**ExtendedDealUnitDtoEnvelope**](ExtendedDealUnitDtoEnvelope.md)

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

# **get_extended_deal_units_async**
> ExtendedDealUnitDtoListEnvelope get_extended_deal_units_async(tenant_id)

Get extended deal units

Retrieves a list of deal units with extended details for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.extended_deal_unit_dto_list_envelope import ExtendedDealUnitDtoListEnvelope
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get extended deal units
        api_response = api_instance.get_extended_deal_units_async(tenant_id)
        print("The response of DealUnitsApi->get_extended_deal_units_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->get_extended_deal_units_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedDealUnitDtoListEnvelope**](ExtendedDealUnitDtoListEnvelope.md)

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

# **update_deal_unit_async**
> EmptyEnvelope update_deal_unit_async(tenant_id, deal_unit_id, deal_unit_update_dto=deal_unit_update_dto)

Update a deal unit

Updates an existing deal unit by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_update_dto import DealUnitUpdateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_update_dto = openapi_client.DealUnitUpdateDto() # DealUnitUpdateDto |  (optional)

    try:
        # Update a deal unit
        api_response = api_instance.update_deal_unit_async(tenant_id, deal_unit_id, deal_unit_update_dto=deal_unit_update_dto)
        print("The response of DealUnitsApi->update_deal_unit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->update_deal_unit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_update_dto** | [**DealUnitUpdateDto**](DealUnitUpdateDto.md)|  | [optional] 

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

# **update_deal_unit_price_async**
> EmptyEnvelope update_deal_unit_price_async(tenant_id, deal_unit_id, deal_unit_line_id, deal_unit_line_update_dto=deal_unit_line_update_dto)

Update a deal unit line

Updates an existing line within a specific deal unit.

### Example


```python
import openapi_client
from openapi_client.models.deal_unit_line_update_dto import DealUnitLineUpdateDto
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
    api_instance = openapi_client.DealUnitsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    deal_unit_id = 'deal_unit_id_example' # str | 
    deal_unit_line_id = 'deal_unit_line_id_example' # str | 
    deal_unit_line_update_dto = openapi_client.DealUnitLineUpdateDto() # DealUnitLineUpdateDto |  (optional)

    try:
        # Update a deal unit line
        api_response = api_instance.update_deal_unit_price_async(tenant_id, deal_unit_id, deal_unit_line_id, deal_unit_line_update_dto=deal_unit_line_update_dto)
        print("The response of DealUnitsApi->update_deal_unit_price_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealUnitsApi->update_deal_unit_price_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **deal_unit_id** | **str**|  | 
 **deal_unit_line_id** | **str**|  | 
 **deal_unit_line_update_dto** | [**DealUnitLineUpdateDto**](DealUnitLineUpdateDto.md)|  | [optional] 

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

