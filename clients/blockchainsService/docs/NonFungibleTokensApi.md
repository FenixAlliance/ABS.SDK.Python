# openapi_client.NonFungibleTokensApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_non_fungible_token_async**](NonFungibleTokensApi.md#create_non_fungible_token_async) | **POST** /api/v2/BlockchainsService/NonFungibleTokens | Create a new NFT
[**delete_non_fungible_token_async**](NonFungibleTokensApi.md#delete_non_fungible_token_async) | **DELETE** /api/v2/BlockchainsService/NonFungibleTokens/{id} | Delete an NFT
[**get_non_fungible_token_by_id_async**](NonFungibleTokensApi.md#get_non_fungible_token_by_id_async) | **GET** /api/v2/BlockchainsService/NonFungibleTokens/{id} | Get NFT by ID
[**get_non_fungible_tokens_async**](NonFungibleTokensApi.md#get_non_fungible_tokens_async) | **GET** /api/v2/BlockchainsService/NonFungibleTokens | Get all non-fungible tokens
[**get_non_fungible_tokens_count_async**](NonFungibleTokensApi.md#get_non_fungible_tokens_count_async) | **GET** /api/v2/BlockchainsService/NonFungibleTokens/Count | Get NFTs count
[**patch_non_fungible_token_async**](NonFungibleTokensApi.md#patch_non_fungible_token_async) | **PATCH** /api/v2/BlockchainsService/NonFungibleTokens/{id} | Patch a non-fungible token
[**update_non_fungible_token_async**](NonFungibleTokensApi.md#update_non_fungible_token_async) | **PUT** /api/v2/BlockchainsService/NonFungibleTokens/{id} | Update an NFT


# **create_non_fungible_token_async**
> create_non_fungible_token_async(tenant_id, api_version=api_version, x_api_version=x_api_version, non_fungible_token_create_dto=non_fungible_token_create_dto)

Create a new NFT

Creates a new non-fungible token for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.non_fungible_token_create_dto import NonFungibleTokenCreateDto
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
    api_instance = openapi_client.NonFungibleTokensApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    non_fungible_token_create_dto = openapi_client.NonFungibleTokenCreateDto() # NonFungibleTokenCreateDto |  (optional)

    try:
        # Create a new NFT
        api_instance.create_non_fungible_token_async(tenant_id, api_version=api_version, x_api_version=x_api_version, non_fungible_token_create_dto=non_fungible_token_create_dto)
    except Exception as e:
        print("Exception when calling NonFungibleTokensApi->create_non_fungible_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **non_fungible_token_create_dto** | [**NonFungibleTokenCreateDto**](NonFungibleTokenCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_non_fungible_token_async**
> delete_non_fungible_token_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Delete an NFT

Deletes a non-fungible token for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.NonFungibleTokensApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete an NFT
        api_instance.delete_non_fungible_token_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling NonFungibleTokensApi->delete_non_fungible_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_fungible_token_by_id_async**
> NonFungibleTokenDto get_non_fungible_token_by_id_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Get NFT by ID

Retrieves a specific non-fungible token by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.non_fungible_token_dto import NonFungibleTokenDto
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
    api_instance = openapi_client.NonFungibleTokensApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get NFT by ID
        api_response = api_instance.get_non_fungible_token_by_id_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of NonFungibleTokensApi->get_non_fungible_token_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonFungibleTokensApi->get_non_fungible_token_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**NonFungibleTokenDto**](NonFungibleTokenDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_fungible_tokens_async**
> NonFungibleTokenDtoListEnvelope get_non_fungible_tokens_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get all non-fungible tokens

Retrieves all NFTs for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.non_fungible_token_dto_list_envelope import NonFungibleTokenDtoListEnvelope
from openapi_client.models.non_fungible_token_dto_o_data_query_options import NonFungibleTokenDtoODataQueryOptions
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
    api_instance = openapi_client.NonFungibleTokensApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    o_data_query_options = openapi_client.NonFungibleTokenDtoODataQueryOptions() # NonFungibleTokenDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all non-fungible tokens
        api_response = api_instance.get_non_fungible_tokens_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of NonFungibleTokensApi->get_non_fungible_tokens_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonFungibleTokensApi->get_non_fungible_tokens_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **o_data_query_options** | [**NonFungibleTokenDtoODataQueryOptions**](.md)|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**NonFungibleTokenDtoListEnvelope**](NonFungibleTokenDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_fungible_tokens_count_async**
> Int32Envelope get_non_fungible_tokens_count_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get NFTs count

Returns the count of NFTs for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.int32_envelope import Int32Envelope
from openapi_client.models.non_fungible_token_dto_o_data_query_options import NonFungibleTokenDtoODataQueryOptions
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
    api_instance = openapi_client.NonFungibleTokensApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    o_data_query_options = openapi_client.NonFungibleTokenDtoODataQueryOptions() # NonFungibleTokenDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get NFTs count
        api_response = api_instance.get_non_fungible_tokens_count_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of NonFungibleTokensApi->get_non_fungible_tokens_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonFungibleTokensApi->get_non_fungible_tokens_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **o_data_query_options** | [**NonFungibleTokenDtoODataQueryOptions**](.md)|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_non_fungible_token_async**
> EmptyEnvelope patch_non_fungible_token_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a non-fungible token

Patch a non-fungible token

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
    api_instance = openapi_client.NonFungibleTokensApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a non-fungible token
        api_response = api_instance.patch_non_fungible_token_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of NonFungibleTokensApi->patch_non_fungible_token_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NonFungibleTokensApi->patch_non_fungible_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_non_fungible_token_async**
> update_non_fungible_token_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, non_fungible_token_update_dto=non_fungible_token_update_dto)

Update an NFT

Updates an existing non-fungible token for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.non_fungible_token_update_dto import NonFungibleTokenUpdateDto
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
    api_instance = openapi_client.NonFungibleTokensApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    non_fungible_token_update_dto = openapi_client.NonFungibleTokenUpdateDto() # NonFungibleTokenUpdateDto |  (optional)

    try:
        # Update an NFT
        api_instance.update_non_fungible_token_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, non_fungible_token_update_dto=non_fungible_token_update_dto)
    except Exception as e:
        print("Exception when calling NonFungibleTokensApi->update_non_fungible_token_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **non_fungible_token_update_dto** | [**NonFungibleTokenUpdateDto**](NonFungibleTokenUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

