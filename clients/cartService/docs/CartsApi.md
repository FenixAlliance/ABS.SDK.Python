# openapi_client.CartsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_to_cart_async**](CartsApi.md#add_item_to_cart_async) | **POST** /api/v2/CartService/Carts/{cartId}/Items/{itemId} | Add an Item to a cart
[**add_item_to_cart_compare_table**](CartsApi.md#add_item_to_cart_compare_table) | **POST** /api/v2/CartService/Carts/{cartId}/Compare/{itemId} | Add an item to the compare table
[**add_item_to_wish_list**](CartsApi.md#add_item_to_wish_list) | **POST** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId}/Records | Add a record to a wish list
[**cart_wish_list_exists_head**](CartsApi.md#cart_wish_list_exists_head) | **HEAD** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId}/Exists | Assesses if a WishList exists
[**clear_cart_records**](CartsApi.md#clear_cart_records) | **DELETE** /api/v2/CartService/Carts/{cartId}/Items | Clear all items from a cart
[**create_wish_list_async**](CartsApi.md#create_wish_list_async) | **POST** /api/v2/CartService/Carts/{cartId}/WishLists | Create a new wish list
[**decrease_cart_item_quantity**](CartsApi.md#decrease_cart_item_quantity) | **PUT** /api/v2/CartService/Carts/{cartId}/Items/{itemId}/Decrease | Decrease an Item in a cart
[**decrease_cart_line_async**](CartsApi.md#decrease_cart_line_async) | **PUT** /api/v2/CartService/Carts/{cartId}/Lines/{lineId}/Decrease | Decrease the quantity of a cart line
[**delete_cart_wish_list**](CartsApi.md#delete_cart_wish_list) | **DELETE** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId} | Delete a wish list
[**delete_cart_wish_list_record**](CartsApi.md#delete_cart_wish_list_record) | **DELETE** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId}/Records/{recordId} | Remove a record from a wish list
[**get_acting_cart**](CartsApi.md#get_acting_cart) | **GET** /api/v2/CartService/Carts/ActingCart | Get the acting cart
[**get_cart_by_id_async**](CartsApi.md#get_cart_by_id_async) | **GET** /api/v2/CartService/Carts/{cartId} | Get all business owned contacts
[**get_cart_compare_record**](CartsApi.md#get_cart_compare_record) | **GET** /api/v2/CartService/Carts/{cartId}/Compare/{itemId} | Get an item from the compare table
[**get_cart_compare_records**](CartsApi.md#get_cart_compare_records) | **GET** /api/v2/CartService/Carts/{cartId}/Compare | Get all items in the compare table
[**get_cart_country_async**](CartsApi.md#get_cart_country_async) | **GET** /api/v2/CartService/Carts/{cartId}/Country | Get the country of a cart
[**get_cart_currency_async**](CartsApi.md#get_cart_currency_async) | **GET** /api/v2/CartService/Carts/{cartId}/Currency | Get the currency of a cart
[**get_cart_items**](CartsApi.md#get_cart_items) | **GET** /api/v2/CartService/Carts/{cartId}/Items | Get all cart lines
[**get_cart_line_async**](CartsApi.md#get_cart_line_async) | **GET** /api/v2/CartService/Carts/{cartId}/Lines/{lineId} | Get a cart line by ID
[**get_cart_lines_async**](CartsApi.md#get_cart_lines_async) | **GET** /api/v2/CartService/Carts/{cartId}/Lines | Get all cart lines
[**get_cart_wish_list**](CartsApi.md#get_cart_wish_list) | **GET** /api/v2/CartService/Carts/{cartId}/WishLists | Get all wishlists in a cart
[**get_cart_wish_list_details**](CartsApi.md#get_cart_wish_list_details) | **GET** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId} | Get a wish list by ID
[**get_cart_wish_list_item_async**](CartsApi.md#get_cart_wish_list_item_async) | **GET** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId}/Records/{recordId} | Get a record in a wish list
[**get_cart_wish_list_items**](CartsApi.md#get_cart_wish_list_items) | **GET** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId}/Records | Get all records in a wish list
[**get_guest_cart_async**](CartsApi.md#get_guest_cart_async) | **GET** /api/v2/CartService/Carts/GuestCart | Get the guest cart
[**get_tenant_cart_async**](CartsApi.md#get_tenant_cart_async) | **GET** /api/v2/CartService/Carts/BusinessCart/{tenantId} | Get the business cart
[**get_user_cart**](CartsApi.md#get_user_cart) | **GET** /api/v2/CartService/Carts/UserCart | Get the current user&#39;s cart
[**increase_cart_line_async**](CartsApi.md#increase_cart_line_async) | **PUT** /api/v2/CartService/Carts/{cartId}/Lines/{lineId}/Increase | Increase the quantity of a cart line
[**increase_item_cart_record_quantity_async**](CartsApi.md#increase_item_cart_record_quantity_async) | **PUT** /api/v2/CartService/Carts/{cartId}/Items/{itemId}/Increase | Increase an Item in a cart
[**is_item_already_in_cart_async**](CartsApi.md#is_item_already_in_cart_async) | **GET** /api/v2/CartService/Carts/{cartId}/Contains/{itemId} | Assesses if an Item is already in a cart
[**is_item_in_compare_table_async**](CartsApi.md#is_item_in_compare_table_async) | **GET** /api/v2/CartService/Carts/{cartId}/Compare/Contains/{itemId} | Assesses if an Item is already in the compare table
[**is_item_in_wish_lists**](CartsApi.md#is_item_in_wish_lists) | **GET** /api/v2/CartService/Carts/{cartId}/WishLists/Contains/{itemId} | Assesses if an Item is already in any of the cart&#39;s wishlists
[**remove_cart_line_async**](CartsApi.md#remove_cart_line_async) | **DELETE** /api/v2/CartService/Carts/{cartId}/Lines/{lineId} | Remove a cart line
[**remove_item_from_cart_async**](CartsApi.md#remove_item_from_cart_async) | **DELETE** /api/v2/CartService/Carts/{cartId}/Items/{itemId} | Remove an Item from a cart
[**remove_item_from_compare_table_async**](CartsApi.md#remove_item_from_compare_table_async) | **DELETE** /api/v2/CartService/Carts/{cartId}/Compare/{itemId} | Remove an item from the compare table
[**set_cart_country_async**](CartsApi.md#set_cart_country_async) | **PUT** /api/v2/CartService/Carts/{cartId}/Country | Set the country of a cart
[**set_cart_currency_async**](CartsApi.md#set_cart_currency_async) | **PUT** /api/v2/CartService/Carts/{cartId}/Currency | Set the currency of a cart
[**submit_cart_async**](CartsApi.md#submit_cart_async) | **POST** /api/v2/CartService/Carts/{cartId}/Submit | Submit a cart for processing
[**update_cart_async**](CartsApi.md#update_cart_async) | **PUT** /api/v2/CartService/Carts/{cartId} | Update a cart
[**update_cart_line_async**](CartsApi.md#update_cart_line_async) | **PUT** /api/v2/CartService/Carts/{cartId}/Lines/{lineId} | Update a cart line
[**update_item_cart_record_async**](CartsApi.md#update_item_cart_record_async) | **PUT** /api/v2/CartService/Carts/{cartId}/Items/{itemId} | Update an Item in a cart
[**update_item_to_wish_list**](CartsApi.md#update_item_to_wish_list) | **PUT** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId} | Update a wish list
[**wish_list_exists_async**](CartsApi.md#wish_list_exists_async) | **GET** /api/v2/CartService/Carts/{cartId}/WishLists/{wishListId}/Exists | Assesses if a WishList exists


# **add_item_to_cart_async**
> EmptyEnvelope add_item_to_cart_async(cart_id, item_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)

Add an Item to a cart

Add an Item to a cart

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    quantity = 1 # int |  (optional) (default to 1)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Add an Item to a cart
        api_response = api_instance.add_item_to_cart_async(cart_id, item_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->add_item_to_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->add_item_to_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
 **quantity** | **int**|  | [optional] [default to 1]
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

# **add_item_to_cart_compare_table**
> ItemCartRecordDto add_item_to_cart_compare_table(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)

Add an item to the compare table

Add an item to the compare table

### Example


```python
import openapi_client
from openapi_client.models.item_cart_record_dto import ItemCartRecordDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Add an item to the compare table
        api_response = api_instance.add_item_to_cart_compare_table(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->add_item_to_cart_compare_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->add_item_to_cart_compare_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemCartRecordDto**](ItemCartRecordDto.md)

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

# **add_item_to_wish_list**
> EmptyEnvelope add_item_to_wish_list(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version, product_to_wish_list_request=product_to_wish_list_request)

Add a record to a wish list

Add a record to a wish list

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.product_to_wish_list_request import ProductToWishListRequest
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    product_to_wish_list_request = openapi_client.ProductToWishListRequest() # ProductToWishListRequest |  (optional)

    try:
        # Add a record to a wish list
        api_response = api_instance.add_item_to_wish_list(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version, product_to_wish_list_request=product_to_wish_list_request)
        print("The response of CartsApi->add_item_to_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->add_item_to_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **product_to_wish_list_request** | [**ProductToWishListRequest**](ProductToWishListRequest.md)|  | [optional] 

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

# **cart_wish_list_exists_head**
> EmptyEnvelope cart_wish_list_exists_head(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)

Assesses if a WishList exists

Assesses if a WishList exists but does not return the content

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assesses if a WishList exists
        api_response = api_instance.cart_wish_list_exists_head(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->cart_wish_list_exists_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->cart_wish_list_exists_head: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
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

# **clear_cart_records**
> EmptyEnvelope clear_cart_records(cart_id, api_version=api_version, x_api_version=x_api_version)

Clear all items from a cart

Clear all items from a cart

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Clear all items from a cart
        api_response = api_instance.clear_cart_records(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->clear_cart_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->clear_cart_records: %s\n" % e)
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

# **create_wish_list_async**
> EmptyEnvelope create_wish_list_async(cart_id, api_version=api_version, x_api_version=x_api_version, new_wish_list_request=new_wish_list_request)

Create a new wish list

Create a new wish list

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.new_wish_list_request import NewWishListRequest
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    new_wish_list_request = openapi_client.NewWishListRequest() # NewWishListRequest |  (optional)

    try:
        # Create a new wish list
        api_response = api_instance.create_wish_list_async(cart_id, api_version=api_version, x_api_version=x_api_version, new_wish_list_request=new_wish_list_request)
        print("The response of CartsApi->create_wish_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->create_wish_list_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **new_wish_list_request** | [**NewWishListRequest**](NewWishListRequest.md)|  | [optional] 

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

# **decrease_cart_item_quantity**
> EmptyEnvelope decrease_cart_item_quantity(cart_id, item_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)

Decrease an Item in a cart

Decrease an Item in a cart

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_cart_record_update_dto import ItemCartRecordUpdateDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_cart_record_update_dto = openapi_client.ItemCartRecordUpdateDto() # ItemCartRecordUpdateDto |  (optional)

    try:
        # Decrease an Item in a cart
        api_response = api_instance.decrease_cart_item_quantity(cart_id, item_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)
        print("The response of CartsApi->decrease_cart_item_quantity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->decrease_cart_item_quantity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **decrease_cart_line_async**
> EmptyEnvelope decrease_cart_line_async(cart_id, line_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)

Decrease the quantity of a cart line

Decrease the quantity of a cart line

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    line_id = 'line_id_example' # str | 
    quantity = 1 # float |  (optional) (default to 1)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Decrease the quantity of a cart line
        api_response = api_instance.decrease_cart_line_async(cart_id, line_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->decrease_cart_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->decrease_cart_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **line_id** | **str**|  | 
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

# **delete_cart_wish_list**
> EmptyEnvelope delete_cart_wish_list(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)

Delete a wish list

Delete a wish list

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a wish list
        api_response = api_instance.delete_cart_wish_list(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->delete_cart_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->delete_cart_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
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

# **delete_cart_wish_list_record**
> EmptyEnvelope delete_cart_wish_list_record(cart_id, wish_list_id, record_id, api_version=api_version, x_api_version=x_api_version)

Remove a record from a wish list

Remove a record from a wish list

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a record from a wish list
        api_response = api_instance.delete_cart_wish_list_record(cart_id, wish_list_id, record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->delete_cart_wish_list_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->delete_cart_wish_list_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
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

# **get_acting_cart**
> CartDtoEnvelope get_acting_cart(api_version=api_version, x_api_version=x_api_version)

Get the acting cart

Get the acting cart

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the acting cart
        api_response = api_instance.get_acting_cart(api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_acting_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_acting_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_by_id_async**
> CartDtoEnvelope get_cart_by_id_async(cart_id, api_version=api_version, x_api_version=x_api_version)

Get all business owned contacts

Get all business owned contacts

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all business owned contacts
        api_response = api_instance.get_cart_by_id_async(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_compare_record**
> ItemToCompareCartRecordDtoEnvelope get_cart_compare_record(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)

Get an item from the compare table

Get an item from the compare table

### Example


```python
import openapi_client
from openapi_client.models.item_to_compare_cart_record_dto_envelope import ItemToCompareCartRecordDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get an item from the compare table
        api_response = api_instance.get_cart_compare_record(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_compare_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_compare_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemToCompareCartRecordDtoEnvelope**](ItemToCompareCartRecordDtoEnvelope.md)

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

# **get_cart_compare_records**
> ItemToCompareCartRecordDtoListEnvelope get_cart_compare_records(cart_id, api_version=api_version, x_api_version=x_api_version)

Get all items in the compare table

Get all items in the compare table

### Example


```python
import openapi_client
from openapi_client.models.item_to_compare_cart_record_dto_list_envelope import ItemToCompareCartRecordDtoListEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all items in the compare table
        api_response = api_instance.get_cart_compare_records(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_compare_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_compare_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemToCompareCartRecordDtoListEnvelope**](ItemToCompareCartRecordDtoListEnvelope.md)

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

# **get_cart_country_async**
> CountryDtoEnvelope get_cart_country_async(cart_id, api_version=api_version, x_api_version=x_api_version)

Get the country of a cart

The country of a cart is used to calculate taxes and shipping costs

### Example


```python
import openapi_client
from openapi_client.models.country_dto_envelope import CountryDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the country of a cart
        api_response = api_instance.get_cart_country_async(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_country_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_country_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CountryDtoEnvelope**](CountryDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_currency_async**
> CurrencyDtoEnvelope get_cart_currency_async(cart_id, api_version=api_version, x_api_version=x_api_version)

Get the currency of a cart

The currency of a cart used for display purposes

### Example


```python
import openapi_client
from openapi_client.models.currency_dto_envelope import CurrencyDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the currency of a cart
        api_response = api_instance.get_cart_currency_async(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_currency_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_currency_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CurrencyDtoEnvelope**](CurrencyDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_items**
> ItemCartRecordDtoListEnvelope get_cart_items(cart_id, api_version=api_version, x_api_version=x_api_version)

Get all cart lines

Get all cart lines

### Example


```python
import openapi_client
from openapi_client.models.item_cart_record_dto_list_envelope import ItemCartRecordDtoListEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all cart lines
        api_response = api_instance.get_cart_items(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_items: %s\n" % e)
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

# **get_cart_line_async**
> EmptyEnvelope get_cart_line_async(cart_id, line_id, api_version=api_version, x_api_version=x_api_version)

Get a cart line by ID

Get a cart line by ID

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a cart line by ID
        api_response = api_instance.get_cart_line_async(cart_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **line_id** | **str**|  | 
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

# **get_cart_lines_async**
> ItemCartRecordDtoListEnvelope get_cart_lines_async(cart_id, api_version=api_version, x_api_version=x_api_version)

Get all cart lines

Get all cart lines

### Example


```python
import openapi_client
from openapi_client.models.item_cart_record_dto_list_envelope import ItemCartRecordDtoListEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all cart lines
        api_response = api_instance.get_cart_lines_async(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_lines_async: %s\n" % e)
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

# **get_cart_wish_list**
> List[WishListDto] get_cart_wish_list(cart_id, api_version=api_version, x_api_version=x_api_version)

Get all wishlists in a cart

Get all wishlists in a cart

### Example


```python
import openapi_client
from openapi_client.models.wish_list_dto import WishListDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all wishlists in a cart
        api_response = api_instance.get_cart_wish_list(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[WishListDto]**](WishListDto.md)

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

# **get_cart_wish_list_details**
> WishListDtoEnvelope get_cart_wish_list_details(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)

Get a wish list by ID

Get a wish list by ID

### Example


```python
import openapi_client
from openapi_client.models.wish_list_dto_envelope import WishListDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a wish list by ID
        api_response = api_instance.get_cart_wish_list_details(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_wish_list_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_wish_list_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WishListDtoEnvelope**](WishListDtoEnvelope.md)

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

# **get_cart_wish_list_item_async**
> List[WishListItemRecordDto] get_cart_wish_list_item_async(cart_id, wish_list_id, record_id, api_version=api_version, x_api_version=x_api_version)

Get a record in a wish list

Get a record in a wish list

### Example


```python
import openapi_client
from openapi_client.models.wish_list_item_record_dto import WishListItemRecordDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a record in a wish list
        api_response = api_instance.get_cart_wish_list_item_async(cart_id, wish_list_id, record_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_wish_list_item_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_wish_list_item_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
 **record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[WishListItemRecordDto]**](WishListItemRecordDto.md)

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

# **get_cart_wish_list_items**
> List[WishListItemRecordDto] get_cart_wish_list_items(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)

Get all records in a wish list

Get all records in a wish list

### Example


```python
import openapi_client
from openapi_client.models.wish_list_item_record_dto import WishListItemRecordDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all records in a wish list
        api_response = api_instance.get_cart_wish_list_items(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_cart_wish_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_cart_wish_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[WishListItemRecordDto]**](WishListItemRecordDto.md)

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

# **get_guest_cart_async**
> CartDtoEnvelope get_guest_cart_async(api_version=api_version, x_api_version=x_api_version)

Get the guest cart

Get the guest cart

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the guest cart
        api_response = api_instance.get_guest_cart_async(api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_guest_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_guest_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_cart_async**
> CartDtoEnvelope get_tenant_cart_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the business cart

Get the business cart

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the business cart
        api_response = api_instance.get_tenant_cart_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_tenant_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_tenant_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_cart**
> CartDtoEnvelope get_user_cart(api_version=api_version, x_api_version=x_api_version)

Get the current user's cart

Get the current user's cart

### Example


```python
import openapi_client
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the current user's cart
        api_response = api_instance.get_user_cart(api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->get_user_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->get_user_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CartDtoEnvelope**](CartDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increase_cart_line_async**
> EmptyEnvelope increase_cart_line_async(cart_id, line_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)

Increase the quantity of a cart line

Increase the quantity of a cart line

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    line_id = 'line_id_example' # str | 
    quantity = 1 # float |  (optional) (default to 1)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Increase the quantity of a cart line
        api_response = api_instance.increase_cart_line_async(cart_id, line_id, quantity=quantity, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->increase_cart_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->increase_cart_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **line_id** | **str**|  | 
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

# **increase_item_cart_record_quantity_async**
> EmptyEnvelope increase_item_cart_record_quantity_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)

Increase an Item in a cart

Increase an Item in a cart

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_cart_record_update_dto import ItemCartRecordUpdateDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_cart_record_update_dto = openapi_client.ItemCartRecordUpdateDto() # ItemCartRecordUpdateDto |  (optional)

    try:
        # Increase an Item in a cart
        api_response = api_instance.increase_item_cart_record_quantity_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)
        print("The response of CartsApi->increase_item_cart_record_quantity_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->increase_item_cart_record_quantity_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **is_item_already_in_cart_async**
> BooleanEnvelope is_item_already_in_cart_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)

Assesses if an Item is already in a cart

Assesses if an Item is already in a cart

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assesses if an Item is already in a cart
        api_response = api_instance.is_item_already_in_cart_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->is_item_already_in_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->is_item_already_in_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **is_item_in_compare_table_async**
> BooleanEnvelope is_item_in_compare_table_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)

Assesses if an Item is already in the compare table

Assesses if an Item is already in the compare table

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assesses if an Item is already in the compare table
        api_response = api_instance.is_item_in_compare_table_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->is_item_in_compare_table_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->is_item_in_compare_table_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **is_item_in_wish_lists**
> BooleanEnvelope is_item_in_wish_lists(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)

Assesses if an Item is already in any of the cart's wishlists

Assesses if an Item is already in any of the cart's wishlists

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assesses if an Item is already in any of the cart's wishlists
        api_response = api_instance.is_item_in_wish_lists(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->is_item_in_wish_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->is_item_in_wish_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
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
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cart_line_async**
> EmptyEnvelope remove_cart_line_async(cart_id, line_id, api_version=api_version, x_api_version=x_api_version)

Remove a cart line

Remove a cart line

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a cart line
        api_response = api_instance.remove_cart_line_async(cart_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->remove_cart_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->remove_cart_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **line_id** | **str**|  | 
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

# **remove_item_from_cart_async**
> EmptyEnvelope remove_item_from_cart_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)

Remove an Item from a cart

Remove an Item from a cart

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove an Item from a cart
        api_response = api_instance.remove_item_from_cart_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->remove_item_from_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->remove_item_from_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **remove_item_from_compare_table_async**
> ItemToCompareCartRecordDto remove_item_from_compare_table_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)

Remove an item from the compare table

Remove an item from the compare table

### Example


```python
import openapi_client
from openapi_client.models.item_to_compare_cart_record_dto import ItemToCompareCartRecordDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove an item from the compare table
        api_response = api_instance.remove_item_from_compare_table_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->remove_item_from_compare_table_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->remove_item_from_compare_table_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ItemToCompareCartRecordDto**](ItemToCompareCartRecordDto.md)

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

# **set_cart_country_async**
> EmptyEnvelope set_cart_country_async(cart_id, api_version=api_version, x_api_version=x_api_version, country_switch_request=country_switch_request)

Set the country of a cart

Set the country of a cart

### Example


```python
import openapi_client
from openapi_client.models.country_switch_request import CountrySwitchRequest
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    country_switch_request = openapi_client.CountrySwitchRequest() # CountrySwitchRequest |  (optional)

    try:
        # Set the country of a cart
        api_response = api_instance.set_cart_country_async(cart_id, api_version=api_version, x_api_version=x_api_version, country_switch_request=country_switch_request)
        print("The response of CartsApi->set_cart_country_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->set_cart_country_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **country_switch_request** | [**CountrySwitchRequest**](CountrySwitchRequest.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cart_currency_async**
> EmptyEnvelope set_cart_currency_async(cart_id, api_version=api_version, x_api_version=x_api_version, currency_switch_request=currency_switch_request)

Set the currency of a cart

Set the currency of a cart

### Example


```python
import openapi_client
from openapi_client.models.currency_switch_request import CurrencySwitchRequest
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    currency_switch_request = openapi_client.CurrencySwitchRequest() # CurrencySwitchRequest |  (optional)

    try:
        # Set the currency of a cart
        api_response = api_instance.set_cart_currency_async(cart_id, api_version=api_version, x_api_version=x_api_version, currency_switch_request=currency_switch_request)
        print("The response of CartsApi->set_cart_currency_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->set_cart_currency_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **currency_switch_request** | [**CurrencySwitchRequest**](CurrencySwitchRequest.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_cart_async**
> EmptyEnvelope submit_cart_async(cart_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)

Submit a cart for processing

Submit a cart for processing

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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    tenant_id = 'tenant_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Submit a cart for processing
        api_response = api_instance.submit_cart_async(cart_id, tenant_id=tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->submit_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->submit_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cart_async**
> EmptyEnvelope update_cart_async(cart_id, api_version=api_version, x_api_version=x_api_version, cart_update_request=cart_update_request)

Update a cart

Update a cart

### Example


```python
import openapi_client
from openapi_client.models.cart_update_request import CartUpdateRequest
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    cart_update_request = openapi_client.CartUpdateRequest() # CartUpdateRequest |  (optional)

    try:
        # Update a cart
        api_response = api_instance.update_cart_async(cart_id, api_version=api_version, x_api_version=x_api_version, cart_update_request=cart_update_request)
        print("The response of CartsApi->update_cart_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->update_cart_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **cart_update_request** | [**CartUpdateRequest**](CartUpdateRequest.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cart_line_async**
> EmptyEnvelope update_cart_line_async(cart_id, line_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)

Update a cart line

Update a cart line

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_cart_record_update_dto import ItemCartRecordUpdateDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_cart_record_update_dto = openapi_client.ItemCartRecordUpdateDto() # ItemCartRecordUpdateDto |  (optional)

    try:
        # Update a cart line
        api_response = api_instance.update_cart_line_async(cart_id, line_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)
        print("The response of CartsApi->update_cart_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->update_cart_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **line_id** | **str**|  | 
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

# **update_item_cart_record_async**
> EmptyEnvelope update_item_cart_record_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)

Update an Item in a cart

Update an Item in a cart

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.item_cart_record_update_dto import ItemCartRecordUpdateDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    item_id = 'item_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    item_cart_record_update_dto = openapi_client.ItemCartRecordUpdateDto() # ItemCartRecordUpdateDto |  (optional)

    try:
        # Update an Item in a cart
        api_response = api_instance.update_item_cart_record_async(cart_id, item_id, api_version=api_version, x_api_version=x_api_version, item_cart_record_update_dto=item_cart_record_update_dto)
        print("The response of CartsApi->update_item_cart_record_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->update_item_cart_record_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
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

# **update_item_to_wish_list**
> EmptyEnvelope update_item_to_wish_list(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version, wish_list_update_dto=wish_list_update_dto)

Update a wish list

Update a wish list

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.wish_list_update_dto import WishListUpdateDto
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    wish_list_update_dto = openapi_client.WishListUpdateDto() # WishListUpdateDto |  (optional)

    try:
        # Update a wish list
        api_response = api_instance.update_item_to_wish_list(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version, wish_list_update_dto=wish_list_update_dto)
        print("The response of CartsApi->update_item_to_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->update_item_to_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **wish_list_update_dto** | [**WishListUpdateDto**](WishListUpdateDto.md)|  | [optional] 

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

# **wish_list_exists_async**
> BooleanEnvelope wish_list_exists_async(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)

Assesses if a WishList exists

Assesses if a WishList exists

### Example


```python
import openapi_client
from openapi_client.models.boolean_envelope import BooleanEnvelope
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
    api_instance = openapi_client.CartsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Assesses if a WishList exists
        api_response = api_instance.wish_list_exists_async(cart_id, wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CartsApi->wish_list_exists_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartsApi->wish_list_exists_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **wish_list_id** | **str**|  | 
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
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

