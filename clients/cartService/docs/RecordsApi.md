# openapi_client.RecordsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_to_cart**](RecordsApi.md#add_item_to_cart) | **POST** /api/v2/CartService/Records/AddItem | Add an item to a cart
[**add_product_to_cart_async**](RecordsApi.md#add_product_to_cart_async) | **POST** /api/v2/CartService/Records | Add a product to a cart with tracking
[**clear_cart_async**](RecordsApi.md#clear_cart_async) | **POST** /api/v2/CartService/Records/ClearCart | Clear all items from a cart
[**decrease_item_cart_record**](RecordsApi.md#decrease_item_cart_record) | **PUT** /api/v2/CartService/Records/{recordId}/Decrease | Decrease cart record quantity
[**get_item_cart_record**](RecordsApi.md#get_item_cart_record) | **GET** /api/v2/CartService/Records/{recordId}/Details | Get a cart record by ID
[**get_items_in_cart_async**](RecordsApi.md#get_items_in_cart_async) | **GET** /api/v2/CartService/Records/{cartId} | Get all items in a cart
[**increase_item_cart_record**](RecordsApi.md#increase_item_cart_record) | **PUT** /api/v2/CartService/Records/{recordId}/Increase | Increase cart record quantity
[**is_item_already_in_cart**](RecordsApi.md#is_item_already_in_cart) | **GET** /api/v2/CartService/Records/IsInCart | Check if an item is in a cart
[**remove_product_from_cart_by_params**](RecordsApi.md#remove_product_from_cart_by_params) | **DELETE** /api/v2/CartService/Records | Remove a product from a cart
[**remove_product_from_cart_by_record_id**](RecordsApi.md#remove_product_from_cart_by_record_id) | **DELETE** /api/v2/CartService/Records/{recordId} | Remove a product from a cart by record ID
[**update_item_cart_record**](RecordsApi.md#update_item_cart_record) | **PUT** /api/v2/CartService/Records/{recordId} | Update a cart record


# **add_item_to_cart**
> EmptyEnvelope add_item_to_cart(cart_id=cart_id, item_id=item_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)

Add an item to a cart

Adds an item with the specified quantity to the given cart.

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
    api_instance = openapi_client.RecordsApi(api_client)
    cart_id = 'cart_id_example' # str |  (optional)
    item_id = 'item_id_example' # str |  (optional)
    quantity = 56 # int |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Add an item to a cart
        api_response = api_instance.add_item_to_cart(cart_id=cart_id, item_id=item_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->add_item_to_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->add_item_to_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | [optional] 
 **item_id** | **str**|  | [optional] 
 **quantity** | **int**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_product_to_cart_async**
> EmptyEnvelope add_product_to_cart_async(api_version=api_version, x_api_version=x_api_version, item_cart_record_create_dto=item_cart_record_create_dto)

Add a product to a cart with tracking

Adds a product to the cart using a request body with cart ID, product ID, and quantity.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_cart_record_create_dto import ItemCartRecordCreateDto
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
    api_instance = openapi_client.RecordsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_cart_record_create_dto = openapi_client.ItemCartRecordCreateDto() # ItemCartRecordCreateDto |  (optional)

    try:
        # Add a product to a cart with tracking
        api_response = api_instance.add_product_to_cart_async(api_version=api_version, x_api_version=x_api_version, item_cart_record_create_dto=item_cart_record_create_dto)
        print("The response of RecordsApi->add_product_to_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->add_product_to_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_cart_record_create_dto** | [**ItemCartRecordCreateDto**](ItemCartRecordCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_cart_async**
> EmptyEnvelope clear_cart_async(cart_id, api_version=api_version, x_api_version=x_api_version)

Clear all items from a cart

Removes all item records from the specified cart.

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
    api_instance = openapi_client.RecordsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Clear all items from a cart
        api_response = api_instance.clear_cart_async(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->clear_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->clear_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrease_item_cart_record**
> EmptyEnvelope decrease_item_cart_record(record_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)

Decrease cart record quantity

Decreases the quantity of the specified item cart record by the given amount.

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
    api_instance = openapi_client.RecordsApi(api_client)
    record_id = 'record_id_example' # str | 
    quantity = 1 # float |  (optional) (default to 1)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Decrease cart record quantity
        api_response = api_instance.decrease_item_cart_record(record_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->decrease_item_cart_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->decrease_item_cart_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **quantity** | **float**|  | [optional] [default to 1]
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_cart_record**
> EmptyEnvelope get_item_cart_record(record_id, api_version=api_version, x_api_version=x_api_version)

Get a cart record by ID

Retrieves the details of a specific item cart record.

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
    api_instance = openapi_client.RecordsApi(api_client)
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a cart record by ID
        api_response = api_instance.get_item_cart_record(record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->get_item_cart_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->get_item_cart_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_in_cart_async**
> ItemCartRecordDtoListEnvelope get_items_in_cart_async(cart_id, api_version=api_version, x_api_version=x_api_version)

Get all items in a cart

Retrieves all item cart records for the specified cart.

### Example


```python
import openapi_client
from openapi_client.models.item_cart_record_dto_list_envelope import ItemCartRecordDtoListEnvelope
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
    api_instance = openapi_client.RecordsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all items in a cart
        api_response = api_instance.get_items_in_cart_async(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->get_items_in_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->get_items_in_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCartRecordDtoListEnvelope**](ItemCartRecordDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increase_item_cart_record**
> EmptyEnvelope increase_item_cart_record(record_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)

Increase cart record quantity

Increases the quantity of the specified item cart record by the given amount.

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
    api_instance = openapi_client.RecordsApi(api_client)
    record_id = 'record_id_example' # str | 
    quantity = 1 # float |  (optional) (default to 1)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Increase cart record quantity
        api_response = api_instance.increase_item_cart_record(record_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->increase_item_cart_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->increase_item_cart_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **quantity** | **float**|  | [optional] [default to 1]
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_item_already_in_cart**
> BooleanEnvelope is_item_already_in_cart(item_id, cart_id, api_version=api_version, x_api_version=x_api_version)

Check if an item is in a cart

Returns a boolean indicating whether the specified item is already in the given cart.

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
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
    api_instance = openapi_client.RecordsApi(api_client)
    item_id = 'item_id_example' # str | 
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Check if an item is in a cart
        api_response = api_instance.is_item_already_in_cart(item_id, cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->is_item_already_in_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->is_item_already_in_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BooleanEnvelope**](BooleanEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_product_from_cart_by_params**
> EmptyEnvelope remove_product_from_cart_by_params(cart_id=cart_id, product_id=product_id, api_version=api_version, x_api_version=x_api_version)

Remove a product from a cart

Removes a product from the cart using cart ID and product ID query parameters.

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
    api_instance = openapi_client.RecordsApi(api_client)
    cart_id = 'cart_id_example' # str |  (optional)
    product_id = 'product_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a product from a cart
        api_response = api_instance.remove_product_from_cart_by_params(cart_id=cart_id, product_id=product_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->remove_product_from_cart_by_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->remove_product_from_cart_by_params: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | [optional] 
 **product_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_product_from_cart_by_record_id**
> EmptyEnvelope remove_product_from_cart_by_record_id(record_id, api_version=api_version, x_api_version=x_api_version)

Remove a product from a cart by record ID

Removes a specific item record from the cart by its record ID.

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
    api_instance = openapi_client.RecordsApi(api_client)
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a product from a cart by record ID
        api_response = api_instance.remove_product_from_cart_by_record_id(record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of RecordsApi->remove_product_from_cart_by_record_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->remove_product_from_cart_by_record_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_cart_record**
> EmptyEnvelope update_item_cart_record(record_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)

Update a cart record

Updates the specified item cart record with the provided data.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_cart_record_update_dto import ItemCartRecordUpdateDto
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
    api_instance = openapi_client.RecordsApi(api_client)
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_cart_record_update_dto = openapi_client.ItemCartRecordUpdateDto() # ItemCartRecordUpdateDto |  (optional)

    try:
        # Update a cart record
        api_response = api_instance.update_item_cart_record(record_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)
        print("The response of RecordsApi->update_item_cart_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->update_item_cart_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **item_cart_record_update_dto** | [**ItemCartRecordUpdateDto**](ItemCartRecordUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

