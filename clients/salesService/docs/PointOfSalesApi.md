# openapi_client.PointOfSalesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_point_of_sales_async**](PointOfSalesApi.md#count_point_of_sales_async) | **GET** /api/v2/SalesService/PointOfSales/Count | Get point of sales count
[**create_point_of_sale_async**](PointOfSalesApi.md#create_point_of_sale_async) | **POST** /api/v2/SalesService/PointOfSales | Create a point of sale
[**delete_point_of_sale_async**](PointOfSalesApi.md#delete_point_of_sale_async) | **DELETE** /api/v2/SalesService/PointOfSales/{pointOfSaleId} | Delete a point of sale
[**get_point_of_sale_async**](PointOfSalesApi.md#get_point_of_sale_async) | **GET** /api/v2/SalesService/PointOfSales/{pointOfSaleId} | Get point of sale by ID
[**get_point_of_sales_async**](PointOfSalesApi.md#get_point_of_sales_async) | **GET** /api/v2/SalesService/PointOfSales | Get point of sales
[**patch_point_of_sale_async**](PointOfSalesApi.md#patch_point_of_sale_async) | **PATCH** /api/v2/SalesService/PointOfSales/{pointOfSaleId} | Patch a point of sale
[**update_point_of_sale_async**](PointOfSalesApi.md#update_point_of_sale_async) | **PUT** /api/v2/SalesService/PointOfSales/{pointOfSaleId} | Update a point of sale


# **count_point_of_sales_async**
> Int32Envelope count_point_of_sales_async(tenant_id)

Get point of sales count

Returns the total count of point of sales for the specified tenant with OData filter support.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PointOfSalesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get point of sales count
        api_response = api_instance.count_point_of_sales_async(tenant_id)
        print("The response of PointOfSalesApi->count_point_of_sales_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSalesApi->count_point_of_sales_async: %s\n" % e)
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

# **create_point_of_sale_async**
> EmptyEnvelope create_point_of_sale_async(tenant_id, point_of_sale_create_dto=point_of_sale_create_dto)

Create a point of sale

Creates a new point of sale for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.point_of_sale_create_dto import PointOfSaleCreateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PointOfSalesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    point_of_sale_create_dto = openapi_client.PointOfSaleCreateDto() # PointOfSaleCreateDto |  (optional)

    try:
        # Create a point of sale
        api_response = api_instance.create_point_of_sale_async(tenant_id, point_of_sale_create_dto=point_of_sale_create_dto)
        print("The response of PointOfSalesApi->create_point_of_sale_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSalesApi->create_point_of_sale_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **point_of_sale_create_dto** | [**PointOfSaleCreateDto**](PointOfSaleCreateDto.md)|  | [optional] 

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

# **delete_point_of_sale_async**
> EmptyEnvelope delete_point_of_sale_async(tenant_id, point_of_sale_id)

Delete a point of sale

Deletes an existing point of sale by its unique identifier.

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PointOfSalesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    point_of_sale_id = 'point_of_sale_id_example' # str | 

    try:
        # Delete a point of sale
        api_response = api_instance.delete_point_of_sale_async(tenant_id, point_of_sale_id)
        print("The response of PointOfSalesApi->delete_point_of_sale_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSalesApi->delete_point_of_sale_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **point_of_sale_id** | **str**|  | 

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

# **get_point_of_sale_async**
> PointOfSaleDtoEnvelope get_point_of_sale_async(tenant_id, point_of_sale_id)

Get point of sale by ID

Retrieves a single point of sale by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.point_of_sale_dto_envelope import PointOfSaleDtoEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PointOfSalesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    point_of_sale_id = 'point_of_sale_id_example' # str | 

    try:
        # Get point of sale by ID
        api_response = api_instance.get_point_of_sale_async(tenant_id, point_of_sale_id)
        print("The response of PointOfSalesApi->get_point_of_sale_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSalesApi->get_point_of_sale_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **point_of_sale_id** | **str**|  | 

### Return type

[**PointOfSaleDtoEnvelope**](PointOfSaleDtoEnvelope.md)

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

# **get_point_of_sales_async**
> PointOfSaleDtoListEnvelope get_point_of_sales_async(tenant_id)

Get point of sales

Retrieves a list of point of sales for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.point_of_sale_dto_list_envelope import PointOfSaleDtoListEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PointOfSalesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get point of sales
        api_response = api_instance.get_point_of_sales_async(tenant_id)
        print("The response of PointOfSalesApi->get_point_of_sales_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSalesApi->get_point_of_sales_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**PointOfSaleDtoListEnvelope**](PointOfSaleDtoListEnvelope.md)

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

# **patch_point_of_sale_async**
> EmptyEnvelope patch_point_of_sale_async(tenant_id, point_of_sale_id, operation=operation)

Patch a point of sale

Partially updates an existing point of sale using a JSON Patch document.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PointOfSalesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    point_of_sale_id = 'point_of_sale_id_example' # str | 
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a point of sale
        api_response = api_instance.patch_point_of_sale_async(tenant_id, point_of_sale_id, operation=operation)
        print("The response of PointOfSalesApi->patch_point_of_sale_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSalesApi->patch_point_of_sale_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **point_of_sale_id** | **str**|  | 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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

# **update_point_of_sale_async**
> EmptyEnvelope update_point_of_sale_async(tenant_id, point_of_sale_id, point_of_sale_update_dto=point_of_sale_update_dto)

Update a point of sale

Updates an existing point of sale by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.point_of_sale_update_dto import PointOfSaleUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PointOfSalesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    point_of_sale_id = 'point_of_sale_id_example' # str | 
    point_of_sale_update_dto = openapi_client.PointOfSaleUpdateDto() # PointOfSaleUpdateDto |  (optional)

    try:
        # Update a point of sale
        api_response = api_instance.update_point_of_sale_async(tenant_id, point_of_sale_id, point_of_sale_update_dto=point_of_sale_update_dto)
        print("The response of PointOfSalesApi->update_point_of_sale_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointOfSalesApi->update_point_of_sale_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **point_of_sale_id** | **str**|  | 
 **point_of_sale_update_dto** | [**PointOfSaleUpdateDto**](PointOfSaleUpdateDto.md)|  | [optional] 

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

