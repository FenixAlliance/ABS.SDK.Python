# openapi_client.BlockchainsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_blockchain_async**](BlockchainsApi.md#create_blockchain_async) | **POST** /api/v2/BlockchainsService/Blockchains | Create a new blockchain
[**create_blockchain_block_async**](BlockchainsApi.md#create_blockchain_block_async) | **POST** /api/v2/BlockchainsService/Blockchains/{blockchainId}/Blocks | Add a block to a blockchain
[**delete_blockchain_async**](BlockchainsApi.md#delete_blockchain_async) | **DELETE** /api/v2/BlockchainsService/Blockchains/{id} | Delete a blockchain
[**delete_blockchain_block_async**](BlockchainsApi.md#delete_blockchain_block_async) | **DELETE** /api/v2/BlockchainsService/Blockchains/{blockchainId}/Blocks/{blockId} | Delete a blockchain block
[**get_blockchain_block_by_id_async**](BlockchainsApi.md#get_blockchain_block_by_id_async) | **GET** /api/v2/BlockchainsService/Blockchains/{blockchainId}/Blocks/{blockId} | Get a specific block
[**get_blockchain_blocks_async**](BlockchainsApi.md#get_blockchain_blocks_async) | **GET** /api/v2/BlockchainsService/Blockchains/{blockchainId}/Blocks | Get blocks for a blockchain
[**get_blockchain_blocks_count_async**](BlockchainsApi.md#get_blockchain_blocks_count_async) | **GET** /api/v2/BlockchainsService/Blockchains/{blockchainId}/Blocks/Count | Get block count for a blockchain
[**get_blockchain_by_id_async**](BlockchainsApi.md#get_blockchain_by_id_async) | **GET** /api/v2/BlockchainsService/Blockchains/{id} | Get blockchain by ID
[**get_blockchains_async**](BlockchainsApi.md#get_blockchains_async) | **GET** /api/v2/BlockchainsService/Blockchains | Get all blockchains
[**get_blockchains_count_async**](BlockchainsApi.md#get_blockchains_count_async) | **GET** /api/v2/BlockchainsService/Blockchains/Count | Get blockchains count
[**patch_blockchain_async**](BlockchainsApi.md#patch_blockchain_async) | **PATCH** /api/v2/BlockchainsService/Blockchains/{id} | Patch a blockchain
[**patch_blockchain_block_async**](BlockchainsApi.md#patch_blockchain_block_async) | **PATCH** /api/v2/BlockchainsService/Blockchains/{blockchainId}/Blocks/{blockId} | Patch a blockchain block
[**update_blockchain_async**](BlockchainsApi.md#update_blockchain_async) | **PUT** /api/v2/BlockchainsService/Blockchains/{id} | Update a blockchain
[**update_blockchain_block_async**](BlockchainsApi.md#update_blockchain_block_async) | **PUT** /api/v2/BlockchainsService/Blockchains/{blockchainId}/Blocks/{blockId} | Update a blockchain block


# **create_blockchain_async**
> create_blockchain_async(tenant_id, api_version=api_version, x_api_version=x_api_version, blockchain_create_dto=blockchain_create_dto)

Create a new blockchain

Creates a new blockchain for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blockchain_create_dto import BlockchainCreateDto
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blockchain_create_dto = openapi_client.BlockchainCreateDto() # BlockchainCreateDto |  (optional)

    try:
        # Create a new blockchain
        api_instance.create_blockchain_async(tenant_id, api_version=api_version, x_api_version=x_api_version, blockchain_create_dto=blockchain_create_dto)
    except Exception as e:
        print("Exception when calling BlockchainsApi->create_blockchain_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blockchain_create_dto** | [**BlockchainCreateDto**](BlockchainCreateDto.md)|  | [optional] 

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

# **create_blockchain_block_async**
> create_blockchain_block_async(tenant_id, blockchain_id, api_version=api_version, x_api_version=x_api_version, blockchain_block_create_dto=blockchain_block_create_dto)

Add a block to a blockchain

### Example


```python
import openapi_client
from openapi_client.models.blockchain_block_create_dto import BlockchainBlockCreateDto
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blockchain_id = 'blockchain_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blockchain_block_create_dto = openapi_client.BlockchainBlockCreateDto() # BlockchainBlockCreateDto |  (optional)

    try:
        # Add a block to a blockchain
        api_instance.create_blockchain_block_async(tenant_id, blockchain_id, api_version=api_version, x_api_version=x_api_version, blockchain_block_create_dto=blockchain_block_create_dto)
    except Exception as e:
        print("Exception when calling BlockchainsApi->create_blockchain_block_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blockchain_block_create_dto** | [**BlockchainBlockCreateDto**](BlockchainBlockCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blockchain_async**
> delete_blockchain_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Delete a blockchain

Deletes a blockchain for the specified tenant.

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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a blockchain
        api_instance.delete_blockchain_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BlockchainsApi->delete_blockchain_async: %s\n" % e)
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

# **delete_blockchain_block_async**
> delete_blockchain_block_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version)

Delete a blockchain block

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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blockchain_id = 'blockchain_id_example' # str | 
    block_id = 'block_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a blockchain block
        api_instance.delete_blockchain_block_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling BlockchainsApi->delete_blockchain_block_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **block_id** | **str**|  | 
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

# **get_blockchain_block_by_id_async**
> BlockchainBlockDto get_blockchain_block_by_id_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version)

Get a specific block

### Example


```python
import openapi_client
from openapi_client.models.blockchain_block_dto import BlockchainBlockDto
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blockchain_id = 'blockchain_id_example' # str | 
    block_id = 'block_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a specific block
        api_response = api_instance.get_blockchain_block_by_id_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlockchainsApi->get_blockchain_block_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->get_blockchain_block_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **block_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlockchainBlockDto**](BlockchainBlockDto.md)

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

# **get_blockchain_blocks_async**
> BlockchainBlockDtoListEnvelope get_blockchain_blocks_async(tenant_id, blockchain_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get blocks for a blockchain

### Example


```python
import openapi_client
from openapi_client.models.blockchain_block_dto_list_envelope import BlockchainBlockDtoListEnvelope
from openapi_client.models.blockchain_block_dto_o_data_query_options import BlockchainBlockDtoODataQueryOptions
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blockchain_id = 'blockchain_id_example' # str | 
    o_data_query_options = openapi_client.BlockchainBlockDtoODataQueryOptions() # BlockchainBlockDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blocks for a blockchain
        api_response = api_instance.get_blockchain_blocks_async(tenant_id, blockchain_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlockchainsApi->get_blockchain_blocks_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->get_blockchain_blocks_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **o_data_query_options** | [**BlockchainBlockDtoODataQueryOptions**](.md)|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlockchainBlockDtoListEnvelope**](BlockchainBlockDtoListEnvelope.md)

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

# **get_blockchain_blocks_count_async**
> Int32Envelope get_blockchain_blocks_count_async(tenant_id, blockchain_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get block count for a blockchain

### Example


```python
import openapi_client
from openapi_client.models.blockchain_block_dto_o_data_query_options import BlockchainBlockDtoODataQueryOptions
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blockchain_id = 'blockchain_id_example' # str | 
    o_data_query_options = openapi_client.BlockchainBlockDtoODataQueryOptions() # BlockchainBlockDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get block count for a blockchain
        api_response = api_instance.get_blockchain_blocks_count_async(tenant_id, blockchain_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlockchainsApi->get_blockchain_blocks_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->get_blockchain_blocks_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **o_data_query_options** | [**BlockchainBlockDtoODataQueryOptions**](.md)|  | [optional] 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_by_id_async**
> BlockchainDto get_blockchain_by_id_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)

Get blockchain by ID

Retrieves a specific blockchain by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.blockchain_dto import BlockchainDto
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blockchain by ID
        api_response = api_instance.get_blockchain_by_id_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlockchainsApi->get_blockchain_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->get_blockchain_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlockchainDto**](BlockchainDto.md)

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

# **get_blockchains_async**
> BlockchainDtoListEnvelope get_blockchains_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get all blockchains

Retrieves all blockchains for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blockchain_dto_list_envelope import BlockchainDtoListEnvelope
from openapi_client.models.blockchain_dto_o_data_query_options import BlockchainDtoODataQueryOptions
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    o_data_query_options = openapi_client.BlockchainDtoODataQueryOptions() # BlockchainDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all blockchains
        api_response = api_instance.get_blockchains_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlockchainsApi->get_blockchains_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->get_blockchains_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **o_data_query_options** | [**BlockchainDtoODataQueryOptions**](.md)|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BlockchainDtoListEnvelope**](BlockchainDtoListEnvelope.md)

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

# **get_blockchains_count_async**
> Int32Envelope get_blockchains_count_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)

Get blockchains count

Returns the count of blockchains for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blockchain_dto_o_data_query_options import BlockchainDtoODataQueryOptions
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    o_data_query_options = openapi_client.BlockchainDtoODataQueryOptions() # BlockchainDtoODataQueryOptions |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get blockchains count
        api_response = api_instance.get_blockchains_count_async(tenant_id, o_data_query_options=o_data_query_options, api_version=api_version, x_api_version=x_api_version)
        print("The response of BlockchainsApi->get_blockchains_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->get_blockchains_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **o_data_query_options** | [**BlockchainDtoODataQueryOptions**](.md)|  | [optional] 
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

# **patch_blockchain_async**
> EmptyEnvelope patch_blockchain_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a blockchain

Patch a blockchain

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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a blockchain
        api_response = api_instance.patch_blockchain_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of BlockchainsApi->patch_blockchain_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->patch_blockchain_async: %s\n" % e)
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

# **patch_blockchain_block_async**
> EmptyEnvelope patch_blockchain_block_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a blockchain block

Patch a blockchain block

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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blockchain_id = 'blockchain_id_example' # str | 
    block_id = 'block_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a blockchain block
        api_response = api_instance.patch_blockchain_block_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of BlockchainsApi->patch_blockchain_block_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsApi->patch_blockchain_block_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **block_id** | **str**|  | 
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

# **update_blockchain_async**
> update_blockchain_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, blockchain_update_dto=blockchain_update_dto)

Update a blockchain

Updates an existing blockchain for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.blockchain_update_dto import BlockchainUpdateDto
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    id = 'id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blockchain_update_dto = openapi_client.BlockchainUpdateDto() # BlockchainUpdateDto |  (optional)

    try:
        # Update a blockchain
        api_instance.update_blockchain_async(tenant_id, id, api_version=api_version, x_api_version=x_api_version, blockchain_update_dto=blockchain_update_dto)
    except Exception as e:
        print("Exception when calling BlockchainsApi->update_blockchain_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blockchain_update_dto** | [**BlockchainUpdateDto**](BlockchainUpdateDto.md)|  | [optional] 

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

# **update_blockchain_block_async**
> update_blockchain_block_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version, blockchain_block_update_dto=blockchain_block_update_dto)

Update a blockchain block

### Example


```python
import openapi_client
from openapi_client.models.blockchain_block_update_dto import BlockchainBlockUpdateDto
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
    api_instance = openapi_client.BlockchainsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    blockchain_id = 'blockchain_id_example' # str | 
    block_id = 'block_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    blockchain_block_update_dto = openapi_client.BlockchainBlockUpdateDto() # BlockchainBlockUpdateDto |  (optional)

    try:
        # Update a blockchain block
        api_instance.update_blockchain_block_async(tenant_id, blockchain_id, block_id, api_version=api_version, x_api_version=x_api_version, blockchain_block_update_dto=blockchain_block_update_dto)
    except Exception as e:
        print("Exception when calling BlockchainsApi->update_blockchain_block_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **block_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **blockchain_block_update_dto** | [**BlockchainBlockUpdateDto**](BlockchainBlockUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

