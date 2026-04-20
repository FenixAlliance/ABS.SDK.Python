# openapi_client.WishListsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_to_wish_list**](WishListsApi.md#add_product_to_wish_list) | **POST** /api/v2/CartService/WishLists/Records | Add a product to a wish list
[**create_wish_list**](WishListsApi.md#create_wish_list) | **POST** /api/v2/CartService/WishLists | Create a wish list
[**delete_wish_list**](WishListsApi.md#delete_wish_list) | **DELETE** /api/v2/CartService/WishLists/{wishListId} | Delete a wish list
[**delete_wish_list_record**](WishListsApi.md#delete_wish_list_record) | **DELETE** /api/v2/CartService/WishLists/Records/{recordId} | Delete a wish list record
[**get_cart_wish_list_details_async**](WishListsApi.md#get_cart_wish_list_details_async) | **GET** /api/v2/CartService/WishLists/{wishListId}/Details | Get wish list details
[**get_cart_wish_list_items_async**](WishListsApi.md#get_cart_wish_list_items_async) | **GET** /api/v2/CartService/WishLists/{wishListId}/Records | Get wish list item records
[**get_wish_list_async**](WishListsApi.md#get_wish_list_async) | **GET** /api/v2/CartService/WishLists/{cartId} | Get wish lists for a cart
[**is_product_in_wish_lists**](WishListsApi.md#is_product_in_wish_lists) | **GET** /api/v2/CartService/WishLists/Contains | Check if a product is in any wish list
[**update_product_to_wish_list**](WishListsApi.md#update_product_to_wish_list) | **PUT** /api/v2/CartService/WishLists/{wishListId} | Update a wish list
[**wish_list_exists**](WishListsApi.md#wish_list_exists) | **GET** /api/v2/CartService/WishLists/Exists | Check if a wish list exists
[**wish_list_exists_head_async**](WishListsApi.md#wish_list_exists_head_async) | **HEAD** /api/v2/CartService/WishLists/Exists | Check if a wish list exists (HEAD)


# **add_product_to_wish_list**
> EmptyEnvelope add_product_to_wish_list(api_version=api_version, x_api_version=x_api_version, product_to_wish_list_request=product_to_wish_list_request)

Add a product to a wish list

Adds the specified product to the given wish list.

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
    api_instance = openapi_client.WishListsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    product_to_wish_list_request = openapi_client.ProductToWishListRequest() # ProductToWishListRequest |  (optional)

    try:
        # Add a product to a wish list
        api_response = api_instance.add_product_to_wish_list(api_version=api_version, x_api_version=x_api_version, product_to_wish_list_request=product_to_wish_list_request)
        print("The response of WishListsApi->add_product_to_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->add_product_to_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wish_list**
> EmptyEnvelope create_wish_list(api_version=api_version, x_api_version=x_api_version, new_wish_list_request=new_wish_list_request)

Create a wish list

Creates a new wish list from the provided request data.

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
    api_instance = openapi_client.WishListsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    new_wish_list_request = openapi_client.NewWishListRequest() # NewWishListRequest |  (optional)

    try:
        # Create a wish list
        api_response = api_instance.create_wish_list(api_version=api_version, x_api_version=x_api_version, new_wish_list_request=new_wish_list_request)
        print("The response of WishListsApi->create_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->create_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wish_list**
> EmptyEnvelope delete_wish_list(wish_list_id, api_version=api_version, x_api_version=x_api_version)

Delete a wish list

Deletes the specified wish list.

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
    api_instance = openapi_client.WishListsApi(api_client)
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a wish list
        api_response = api_instance.delete_wish_list(wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WishListsApi->delete_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->delete_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wish_list_record**
> delete_wish_list_record(record_id, api_version=api_version, x_api_version=x_api_version)

Delete a wish list record

Removes a specific item record from a wish list by its record ID.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WishListsApi(api_client)
    record_id = 'record_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a wish list record
        api_instance.delete_wish_list_record(record_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling WishListsApi->delete_wish_list_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_wish_list_details_async**
> WishListDto get_cart_wish_list_details_async(wish_list_id, api_version=api_version, x_api_version=x_api_version)

Get wish list details

Retrieves the full details of the specified wish list.

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
    api_instance = openapi_client.WishListsApi(api_client)
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get wish list details
        api_response = api_instance.get_cart_wish_list_details_async(wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WishListsApi->get_cart_wish_list_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->get_cart_wish_list_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wish_list_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WishListDto**](WishListDto.md)

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

# **get_cart_wish_list_items_async**
> List[WishListItemRecordDto] get_cart_wish_list_items_async(wish_list_id, api_version=api_version, x_api_version=x_api_version)

Get wish list item records

Retrieves all item records in the specified wish list.

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
    api_instance = openapi_client.WishListsApi(api_client)
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get wish list item records
        api_response = api_instance.get_cart_wish_list_items_async(wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WishListsApi->get_cart_wish_list_items_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->get_cart_wish_list_items_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wish_list_async**
> List[WishListDto] get_wish_list_async(cart_id, api_version=api_version, x_api_version=x_api_version)

Get wish lists for a cart

Retrieves all wish lists associated with the specified cart.

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
    api_instance = openapi_client.WishListsApi(api_client)
    cart_id = 'cart_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get wish lists for a cart
        api_response = api_instance.get_wish_list_async(cart_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WishListsApi->get_wish_list_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->get_wish_list_async: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_product_in_wish_lists**
> BooleanEnvelope is_product_in_wish_lists(cart_id=cart_id, product_id=product_id, api_version=api_version, x_api_version=x_api_version)

Check if a product is in any wish list

Returns a boolean indicating whether the specified product exists in any wish list of the given cart.

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
    api_instance = openapi_client.WishListsApi(api_client)
    cart_id = 'cart_id_example' # str |  (optional)
    product_id = 'product_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Check if a product is in any wish list
        api_response = api_instance.is_product_in_wish_lists(cart_id=cart_id, product_id=product_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WishListsApi->is_product_in_wish_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->is_product_in_wish_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | [optional] 
 **product_id** | **str**|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_to_wish_list**
> EmptyEnvelope update_product_to_wish_list(wish_list_id, api_version=api_version, x_api_version=x_api_version, wish_list_update_dto=wish_list_update_dto)

Update a wish list

Updates the specified wish list with the provided data.

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
    api_instance = openapi_client.WishListsApi(api_client)
    wish_list_id = 'wish_list_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    wish_list_update_dto = openapi_client.WishListUpdateDto() # WishListUpdateDto |  (optional)

    try:
        # Update a wish list
        api_response = api_instance.update_product_to_wish_list(wish_list_id, api_version=api_version, x_api_version=x_api_version, wish_list_update_dto=wish_list_update_dto)
        print("The response of WishListsApi->update_product_to_wish_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->update_product_to_wish_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wish_list_exists**
> BooleanEnvelope wish_list_exists(wish_list_id=wish_list_id, api_version=api_version, x_api_version=x_api_version)

Check if a wish list exists

Returns a boolean indicating whether the specified wish list exists.

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
    api_instance = openapi_client.WishListsApi(api_client)
    wish_list_id = 'wish_list_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Check if a wish list exists
        api_response = api_instance.wish_list_exists(wish_list_id=wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WishListsApi->wish_list_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->wish_list_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wish_list_id** | **str**|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wish_list_exists_head_async**
> EmptyEnvelope wish_list_exists_head_async(wish_list_id=wish_list_id, api_version=api_version, x_api_version=x_api_version)

Check if a wish list exists (HEAD)

HEAD request to check whether the specified wish list exists without returning a response body.

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
    api_instance = openapi_client.WishListsApi(api_client)
    wish_list_id = 'wish_list_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Check if a wish list exists (HEAD)
        api_response = api_instance.wish_list_exists_head_async(wish_list_id=wish_list_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of WishListsApi->wish_list_exists_head_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WishListsApi->wish_list_exists_head_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wish_list_id** | **str**|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

