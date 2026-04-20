# openapi_client.SalesLiteraturesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_sales_literatures_async**](SalesLiteraturesApi.md#count_sales_literatures_async) | **GET** /api/v2/DealsService/SalesLiteratures/Count | Get sales literatures count
[**create_sales_literature_async**](SalesLiteraturesApi.md#create_sales_literature_async) | **POST** /api/v2/DealsService/SalesLiteratures | Create a sales literature
[**delete_sales_literature_async**](SalesLiteraturesApi.md#delete_sales_literature_async) | **DELETE** /api/v2/DealsService/SalesLiteratures/{salesLiteratureId} | Delete a sales literature
[**get_extended_sales_literatures_async**](SalesLiteraturesApi.md#get_extended_sales_literatures_async) | **GET** /api/v2/DealsService/SalesLiteratures/Extended | Get extended sales literatures
[**get_sales_literature_async**](SalesLiteraturesApi.md#get_sales_literature_async) | **GET** /api/v2/DealsService/SalesLiteratures/{salesLiteratureId} | Get sales literature by ID
[**get_sales_literatures_async**](SalesLiteraturesApi.md#get_sales_literatures_async) | **GET** /api/v2/DealsService/SalesLiteratures | Get sales literatures
[**update_sales_literature_async**](SalesLiteraturesApi.md#update_sales_literature_async) | **PUT** /api/v2/DealsService/SalesLiteratures/{salesLiteratureId} | Update a sales literature


# **count_sales_literatures_async**
> Int32Envelope count_sales_literatures_async(tenant_id)

Get sales literatures count

Returns the total count of sales literatures for the specified tenant with OData filter support.

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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get sales literatures count
        api_response = api_instance.count_sales_literatures_async(tenant_id)
        print("The response of SalesLiteraturesApi->count_sales_literatures_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->count_sales_literatures_async: %s\n" % e)
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

# **create_sales_literature_async**
> EmptyEnvelope create_sales_literature_async(tenant_id, sales_literature_create_dto=sales_literature_create_dto)

Create a sales literature

Creates a new sales literature for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.sales_literature_create_dto import SalesLiteratureCreateDto
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sales_literature_create_dto = openapi_client.SalesLiteratureCreateDto() # SalesLiteratureCreateDto |  (optional)

    try:
        # Create a sales literature
        api_response = api_instance.create_sales_literature_async(tenant_id, sales_literature_create_dto=sales_literature_create_dto)
        print("The response of SalesLiteraturesApi->create_sales_literature_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->create_sales_literature_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sales_literature_create_dto** | [**SalesLiteratureCreateDto**](SalesLiteratureCreateDto.md)|  | [optional] 

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

# **delete_sales_literature_async**
> EmptyEnvelope delete_sales_literature_async(tenant_id, sales_literature_id)

Delete a sales literature

Deletes an existing sales literature by its unique identifier.

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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sales_literature_id = 'sales_literature_id_example' # str | 

    try:
        # Delete a sales literature
        api_response = api_instance.delete_sales_literature_async(tenant_id, sales_literature_id)
        print("The response of SalesLiteraturesApi->delete_sales_literature_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->delete_sales_literature_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sales_literature_id** | **str**|  | 

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

# **get_extended_sales_literatures_async**
> ExtendedSalesLiteratureDtoListEnvelope get_extended_sales_literatures_async(tenant_id)

Get extended sales literatures

Retrieves a list of sales literatures with extended details for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.extended_sales_literature_dto_list_envelope import ExtendedSalesLiteratureDtoListEnvelope
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get extended sales literatures
        api_response = api_instance.get_extended_sales_literatures_async(tenant_id)
        print("The response of SalesLiteraturesApi->get_extended_sales_literatures_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->get_extended_sales_literatures_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ExtendedSalesLiteratureDtoListEnvelope**](ExtendedSalesLiteratureDtoListEnvelope.md)

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

# **get_sales_literature_async**
> SalesLiteratureDtoEnvelope get_sales_literature_async(tenant_id, sales_literature_id)

Get sales literature by ID

Retrieves a single sales literature by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.sales_literature_dto_envelope import SalesLiteratureDtoEnvelope
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sales_literature_id = 'sales_literature_id_example' # str | 

    try:
        # Get sales literature by ID
        api_response = api_instance.get_sales_literature_async(tenant_id, sales_literature_id)
        print("The response of SalesLiteraturesApi->get_sales_literature_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->get_sales_literature_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sales_literature_id** | **str**|  | 

### Return type

[**SalesLiteratureDtoEnvelope**](SalesLiteratureDtoEnvelope.md)

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

# **get_sales_literatures_async**
> SalesLiteratureDtoListEnvelope get_sales_literatures_async(tenant_id)

Get sales literatures

Retrieves a list of sales literatures for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.sales_literature_dto_list_envelope import SalesLiteratureDtoListEnvelope
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get sales literatures
        api_response = api_instance.get_sales_literatures_async(tenant_id)
        print("The response of SalesLiteraturesApi->get_sales_literatures_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->get_sales_literatures_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**SalesLiteratureDtoListEnvelope**](SalesLiteratureDtoListEnvelope.md)

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

# **update_sales_literature_async**
> EmptyEnvelope update_sales_literature_async(tenant_id, sales_literature_id, sales_literature_update_dto=sales_literature_update_dto)

Update a sales literature

Updates an existing sales literature by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.sales_literature_update_dto import SalesLiteratureUpdateDto
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
    api_instance = openapi_client.SalesLiteraturesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sales_literature_id = 'sales_literature_id_example' # str | 
    sales_literature_update_dto = openapi_client.SalesLiteratureUpdateDto() # SalesLiteratureUpdateDto |  (optional)

    try:
        # Update a sales literature
        api_response = api_instance.update_sales_literature_async(tenant_id, sales_literature_id, sales_literature_update_dto=sales_literature_update_dto)
        print("The response of SalesLiteraturesApi->update_sales_literature_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesLiteraturesApi->update_sales_literature_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sales_literature_id** | **str**|  | 
 **sales_literature_update_dto** | [**SalesLiteratureUpdateDto**](SalesLiteratureUpdateDto.md)|  | [optional] 

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

