# openapi_client.DiscountListsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_discount_list**](DiscountListsApi.md#create_discount_list) | **POST** /api/v2/PricingService/DiscountLists | Creates a new discount list
[**create_discount_list_entry**](DiscountListsApi.md#create_discount_list_entry) | **POST** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts | Creates a discount list entry
[**delete_discount_list**](DiscountListsApi.md#delete_discount_list) | **DELETE** /api/v2/PricingService/DiscountLists/{discountListId} | Deletes a discount list
[**delete_discount_list_entry**](DiscountListsApi.md#delete_discount_list_entry) | **DELETE** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | Deletes a discount list entry
[**get_discount_list**](DiscountListsApi.md#get_discount_list) | **GET** /api/v2/PricingService/DiscountLists/{discountListId} | Gets a discount list by ID
[**get_discount_list_entries**](DiscountListsApi.md#get_discount_list_entries) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts | Retrieves discounts in a discount list
[**get_discount_list_entries_count**](DiscountListsApi.md#get_discount_list_entries_count) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/Count | Counts discounts in a discount list
[**get_discount_list_entry**](DiscountListsApi.md#get_discount_list_entry) | **GET** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | Gets a discount list entry by ID
[**get_discount_lists**](DiscountListsApi.md#get_discount_lists) | **GET** /api/v2/PricingService/DiscountLists | Retrieves all discount lists
[**get_discount_lists_count**](DiscountListsApi.md#get_discount_lists_count) | **GET** /api/v2/PricingService/DiscountLists/Count | Counts discount lists
[**update_discount_list**](DiscountListsApi.md#update_discount_list) | **PUT** /api/v2/PricingService/DiscountLists/{discountListId} | Updates a discount list
[**update_discount_list_entry**](DiscountListsApi.md#update_discount_list_entry) | **PUT** /api/v2/PricingService/DiscountLists/{discountListId}/Discounts/{discountListEntryId} | Updates a discount list entry


# **create_discount_list**
> EmptyEnvelope create_discount_list(tenant_id, discount_list_create_dto=discount_list_create_dto)

Creates a new discount list

Creates a new discount list for the current tenant.

### Example


```python
import openapi_client
from openapi_client.models.discount_list_create_dto import DiscountListCreateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_create_dto = openapi_client.DiscountListCreateDto() # DiscountListCreateDto |  (optional)

    try:
        # Creates a new discount list
        api_response = api_instance.create_discount_list(tenant_id, discount_list_create_dto=discount_list_create_dto)
        print("The response of DiscountListsApi->create_discount_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->create_discount_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_create_dto** | [**DiscountListCreateDto**](DiscountListCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_discount_list_entry**
> EmptyEnvelope create_discount_list_entry(tenant_id, discount_list_id, discount_create_dto=discount_create_dto)

Creates a discount list entry

Creates a new discount entry in the specified discount list.

### Example


```python
import openapi_client
from openapi_client.models.discount_create_dto import DiscountCreateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_create_dto = openapi_client.DiscountCreateDto() # DiscountCreateDto |  (optional)

    try:
        # Creates a discount list entry
        api_response = api_instance.create_discount_list_entry(tenant_id, discount_list_id, discount_create_dto=discount_create_dto)
        print("The response of DiscountListsApi->create_discount_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->create_discount_list_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_create_dto** | [**DiscountCreateDto**](DiscountCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_discount_list**
> EmptyEnvelope delete_discount_list(tenant_id, discount_list_id)

Deletes a discount list

Deletes the specified discount list.

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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 

    try:
        # Deletes a discount list
        api_response = api_instance.delete_discount_list(tenant_id, discount_list_id)
        print("The response of DiscountListsApi->delete_discount_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->delete_discount_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_discount_list_entry**
> EmptyEnvelope delete_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id)

Deletes a discount list entry

Deletes the specified discount entry from a discount list.

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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_list_entry_id = 'discount_list_entry_id_example' # str | 

    try:
        # Deletes a discount list entry
        api_response = api_instance.delete_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id)
        print("The response of DiscountListsApi->delete_discount_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->delete_discount_list_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_list_entry_id** | **str**|  | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_list**
> DiscountListDtoEnvelope get_discount_list(tenant_id, discount_list_id)

Gets a discount list by ID

Retrieves the details of a discount list using its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.discount_list_dto_envelope import DiscountListDtoEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 

    try:
        # Gets a discount list by ID
        api_response = api_instance.get_discount_list(tenant_id, discount_list_id)
        print("The response of DiscountListsApi->get_discount_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->get_discount_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 

### Return type

[**DiscountListDtoEnvelope**](DiscountListDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_list_entries**
> DiscountDtoListEnvelope get_discount_list_entries(tenant_id, discount_list_id)

Retrieves discounts in a discount list

Gets all discount entries for a specific discount list with OData support.

### Example


```python
import openapi_client
from openapi_client.models.discount_dto_list_envelope import DiscountDtoListEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 

    try:
        # Retrieves discounts in a discount list
        api_response = api_instance.get_discount_list_entries(tenant_id, discount_list_id)
        print("The response of DiscountListsApi->get_discount_list_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->get_discount_list_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 

### Return type

[**DiscountDtoListEnvelope**](DiscountDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_list_entries_count**
> Int32Envelope get_discount_list_entries_count(tenant_id, discount_list_id)

Counts discounts in a discount list

Gets the count of discount entries for a specific discount list.

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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 

    try:
        # Counts discounts in a discount list
        api_response = api_instance.get_discount_list_entries_count(tenant_id, discount_list_id)
        print("The response of DiscountListsApi->get_discount_list_entries_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->get_discount_list_entries_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_list_entry**
> DiscountDtoEnvelope get_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id)

Gets a discount list entry by ID

Retrieves a specific discount entry from a discount list.

### Example


```python
import openapi_client
from openapi_client.models.discount_dto_envelope import DiscountDtoEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_list_entry_id = 'discount_list_entry_id_example' # str | 

    try:
        # Gets a discount list entry by ID
        api_response = api_instance.get_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id)
        print("The response of DiscountListsApi->get_discount_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->get_discount_list_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_list_entry_id** | **str**|  | 

### Return type

[**DiscountDtoEnvelope**](DiscountDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_lists**
> DiscountListDtoListEnvelope get_discount_lists(tenant_id)

Retrieves all discount lists

Gets all discount lists for the current tenant with OData support.

### Example


```python
import openapi_client
from openapi_client.models.discount_list_dto_list_envelope import DiscountListDtoListEnvelope
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Retrieves all discount lists
        api_response = api_instance.get_discount_lists(tenant_id)
        print("The response of DiscountListsApi->get_discount_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->get_discount_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**DiscountListDtoListEnvelope**](DiscountListDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_lists_count**
> Int32Envelope get_discount_lists_count(tenant_id)

Counts discount lists

Gets the count of discount lists for the current tenant.

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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Counts discount lists
        api_response = api_instance.get_discount_lists_count(tenant_id)
        print("The response of DiscountListsApi->get_discount_lists_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->get_discount_lists_count: %s\n" % e)
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_discount_list**
> EmptyEnvelope update_discount_list(tenant_id, discount_list_id, discount_list_update_dto=discount_list_update_dto)

Updates a discount list

Updates the specified discount list.

### Example


```python
import openapi_client
from openapi_client.models.discount_list_update_dto import DiscountListUpdateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_list_update_dto = openapi_client.DiscountListUpdateDto() # DiscountListUpdateDto |  (optional)

    try:
        # Updates a discount list
        api_response = api_instance.update_discount_list(tenant_id, discount_list_id, discount_list_update_dto=discount_list_update_dto)
        print("The response of DiscountListsApi->update_discount_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->update_discount_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_list_update_dto** | [**DiscountListUpdateDto**](DiscountListUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_discount_list_entry**
> EmptyEnvelope update_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id, discount_update_dto=discount_update_dto)

Updates a discount list entry

Updates the specified discount entry in a discount list.

### Example


```python
import openapi_client
from openapi_client.models.discount_update_dto import DiscountUpdateDto
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
    api_instance = openapi_client.DiscountListsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    discount_list_id = 'discount_list_id_example' # str | 
    discount_list_entry_id = 'discount_list_entry_id_example' # str | 
    discount_update_dto = openapi_client.DiscountUpdateDto() # DiscountUpdateDto |  (optional)

    try:
        # Updates a discount list entry
        api_response = api_instance.update_discount_list_entry(tenant_id, discount_list_id, discount_list_entry_id, discount_update_dto=discount_update_dto)
        print("The response of DiscountListsApi->update_discount_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountListsApi->update_discount_list_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **discount_list_id** | **str**|  | 
 **discount_list_entry_id** | **str**|  | 
 **discount_update_dto** | [**DiscountUpdateDto**](DiscountUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

