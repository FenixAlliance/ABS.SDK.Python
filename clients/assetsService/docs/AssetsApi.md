# openapi_client.AssetsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetsApi.md#create_asset) | **POST** /api/v2/AssetsService/Assets | Creates a new asset
[**create_asset_asset_category**](AssetsApi.md#create_asset_asset_category) | **POST** /api/v2/AssetsService/Assets/Categories | Creates a new asset category
[**create_asset_depreciation_record**](AssetsApi.md#create_asset_depreciation_record) | **POST** /api/v2/AssetsService/Assets/{assetId}/DepreciationRecords | Creates a new depreciation record for an asset
[**create_asset_repair**](AssetsApi.md#create_asset_repair) | **POST** /api/v2/AssetsService/Assets/{assetId}/Repairs | Creates a new repair for an asset
[**create_asset_transfer**](AssetsApi.md#create_asset_transfer) | **POST** /api/v2/AssetsService/Assets/{assetId}/Transfers | Creates a new transfer for an asset
[**create_asset_value_amend**](AssetsApi.md#create_asset_value_amend) | **POST** /api/v2/AssetsService/Assets/{assetId}/ValueAmends | Creates a new value amendment for an asset
[**delete_asset**](AssetsApi.md#delete_asset) | **DELETE** /api/v2/AssetsService/Assets/{assetId} | Deletes an existing asset
[**delete_asset_asset_category**](AssetsApi.md#delete_asset_asset_category) | **DELETE** /api/v2/AssetsService/Assets/Categories/{categoryId} | Deletes an existing asset category
[**delete_asset_depreciation_record**](AssetsApi.md#delete_asset_depreciation_record) | **DELETE** /api/v2/AssetsService/Assets/{assetId}/DepreciationRecords/{recordId} | Deletes a depreciation record for an asset
[**delete_asset_repair**](AssetsApi.md#delete_asset_repair) | **DELETE** /api/v2/AssetsService/Assets/{assetId}/Repairs/{repairId} | Deletes a repair for an asset
[**delete_asset_transfer**](AssetsApi.md#delete_asset_transfer) | **DELETE** /api/v2/AssetsService/Assets/{assetId}/Transfers/{transferId} | Deletes a transfer for an asset
[**delete_asset_value_amend**](AssetsApi.md#delete_asset_value_amend) | **DELETE** /api/v2/AssetsService/Assets/{assetId}/ValueAmends/{amendId} | Deletes a value amendment for an asset
[**get_asset**](AssetsApi.md#get_asset) | **GET** /api/v2/AssetsService/Assets/{assetId} | Gets a specific asset by ID
[**get_asset_asset_categories**](AssetsApi.md#get_asset_asset_categories) | **GET** /api/v2/AssetsService/Assets/Categories | Gets all asset categories
[**get_asset_asset_categories_count**](AssetsApi.md#get_asset_asset_categories_count) | **GET** /api/v2/AssetsService/Assets/Categories/count | Gets the count of asset categories
[**get_asset_asset_category**](AssetsApi.md#get_asset_asset_category) | **GET** /api/v2/AssetsService/Assets/Categories/{categoryId} | Gets a specific asset category
[**get_asset_depreciation_record**](AssetsApi.md#get_asset_depreciation_record) | **GET** /api/v2/AssetsService/Assets/{assetId}/DepreciationRecords/{recordId} | Gets a specific depreciation record for an asset
[**get_asset_depreciation_records**](AssetsApi.md#get_asset_depreciation_records) | **GET** /api/v2/AssetsService/Assets/{assetId}/DepreciationRecords | Gets depreciation records for a specific asset
[**get_asset_depreciation_records_count**](AssetsApi.md#get_asset_depreciation_records_count) | **GET** /api/v2/AssetsService/Assets/{assetId}/DepreciationRecords/Count | Gets count of depreciation records for a specific asset
[**get_asset_repair**](AssetsApi.md#get_asset_repair) | **GET** /api/v2/AssetsService/Assets/{assetId}/Repairs/{repairId} | Gets a specific repair for an asset
[**get_asset_repairs**](AssetsApi.md#get_asset_repairs) | **GET** /api/v2/AssetsService/Assets/{assetId}/Repairs | Gets repairs for a specific asset
[**get_asset_repairs_count**](AssetsApi.md#get_asset_repairs_count) | **GET** /api/v2/AssetsService/Assets/{assetId}/Repairs/Count | Gets count of repairs for a specific asset
[**get_asset_transfer**](AssetsApi.md#get_asset_transfer) | **GET** /api/v2/AssetsService/Assets/{assetId}/Transfers/{transferId} | Gets a specific transfer for an asset
[**get_asset_transfers**](AssetsApi.md#get_asset_transfers) | **GET** /api/v2/AssetsService/Assets/{assetId}/Transfers | Gets transfers for a specific asset
[**get_asset_transfers_count**](AssetsApi.md#get_asset_transfers_count) | **GET** /api/v2/AssetsService/Assets/{assetId}/Transfers/Count | Gets count of transfers for a specific asset
[**get_asset_value_amend**](AssetsApi.md#get_asset_value_amend) | **GET** /api/v2/AssetsService/Assets/{assetId}/ValueAmends/{amendId} | Gets a specific value amendment for an asset
[**get_asset_value_amends**](AssetsApi.md#get_asset_value_amends) | **GET** /api/v2/AssetsService/Assets/{assetId}/ValueAmends | Gets value amendments for a specific asset
[**get_asset_value_amends_count**](AssetsApi.md#get_asset_value_amends_count) | **GET** /api/v2/AssetsService/Assets/{assetId}/ValueAmends/Count | Gets count of value amendments for a specific asset
[**get_assets**](AssetsApi.md#get_assets) | **GET** /api/v2/AssetsService/Assets | Gets all assets for the current tenant
[**get_assets_count**](AssetsApi.md#get_assets_count) | **GET** /api/v2/AssetsService/Assets/count | Gets the count of assets
[**update_asset**](AssetsApi.md#update_asset) | **PUT** /api/v2/AssetsService/Assets/{assetId} | Updates an existing asset
[**update_asset_asset_category**](AssetsApi.md#update_asset_asset_category) | **PUT** /api/v2/AssetsService/Assets/Categories/{categoryId} | Updates an existing asset category
[**update_asset_depreciation_record**](AssetsApi.md#update_asset_depreciation_record) | **PUT** /api/v2/AssetsService/Assets/{assetId}/DepreciationRecords/{recordId} | Updates a depreciation record for an asset
[**update_asset_repair**](AssetsApi.md#update_asset_repair) | **PUT** /api/v2/AssetsService/Assets/{assetId}/Repairs/{repairId} | Updates a repair for an asset
[**update_asset_transfer**](AssetsApi.md#update_asset_transfer) | **PUT** /api/v2/AssetsService/Assets/{assetId}/Transfers/{transferId} | Updates a transfer for an asset
[**update_asset_value_amend**](AssetsApi.md#update_asset_value_amend) | **PUT** /api/v2/AssetsService/Assets/{assetId}/ValueAmends/{amendId} | Updates a value amendment for an asset


# **create_asset**
> AssetDtoEnvelope create_asset(tenant_id, asset_create_dto=asset_create_dto)

Creates a new asset

Creates a new asset for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_create_dto import AssetCreateDto
from openapi_client.models.asset_dto_envelope import AssetDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_create_dto = openapi_client.AssetCreateDto() # AssetCreateDto |  (optional)

    try:
        # Creates a new asset
        api_response = api_instance.create_asset(tenant_id, asset_create_dto=asset_create_dto)
        print("The response of AssetsApi->create_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_create_dto** | [**AssetCreateDto**](AssetCreateDto.md)|  | [optional] 

### Return type

[**AssetDtoEnvelope**](AssetDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_asset_category**
> AssetCategoryDtoEnvelope create_asset_asset_category(tenant_id, asset_category_create_dto=asset_category_create_dto)

Creates a new asset category

Creates a new asset category for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_create_dto import AssetCategoryCreateDto
from openapi_client.models.asset_category_dto_envelope import AssetCategoryDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_category_create_dto = openapi_client.AssetCategoryCreateDto() # AssetCategoryCreateDto |  (optional)

    try:
        # Creates a new asset category
        api_response = api_instance.create_asset_asset_category(tenant_id, asset_category_create_dto=asset_category_create_dto)
        print("The response of AssetsApi->create_asset_asset_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_category_create_dto** | [**AssetCategoryCreateDto**](AssetCategoryCreateDto.md)|  | [optional] 

### Return type

[**AssetCategoryDtoEnvelope**](AssetCategoryDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_depreciation_record**
> EmptyEnvelope create_asset_depreciation_record(tenant_id, asset_id, asset_depreciation_record_create_dto=asset_depreciation_record_create_dto)

Creates a new depreciation record for an asset

Creates a new depreciation record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_depreciation_record_create_dto import AssetDepreciationRecordCreateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_depreciation_record_create_dto = openapi_client.AssetDepreciationRecordCreateDto() # AssetDepreciationRecordCreateDto |  (optional)

    try:
        # Creates a new depreciation record for an asset
        api_response = api_instance.create_asset_depreciation_record(tenant_id, asset_id, asset_depreciation_record_create_dto=asset_depreciation_record_create_dto)
        print("The response of AssetsApi->create_asset_depreciation_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset_depreciation_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **asset_depreciation_record_create_dto** | [**AssetDepreciationRecordCreateDto**](AssetDepreciationRecordCreateDto.md)|  | [optional] 

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

# **create_asset_repair**
> EmptyEnvelope create_asset_repair(tenant_id, asset_id, asset_repair_create_dto=asset_repair_create_dto)

Creates a new repair for an asset

Creates a new repair record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_repair_create_dto import AssetRepairCreateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_repair_create_dto = openapi_client.AssetRepairCreateDto() # AssetRepairCreateDto |  (optional)

    try:
        # Creates a new repair for an asset
        api_response = api_instance.create_asset_repair(tenant_id, asset_id, asset_repair_create_dto=asset_repair_create_dto)
        print("The response of AssetsApi->create_asset_repair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset_repair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **asset_repair_create_dto** | [**AssetRepairCreateDto**](AssetRepairCreateDto.md)|  | [optional] 

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

# **create_asset_transfer**
> EmptyEnvelope create_asset_transfer(tenant_id, asset_id, asset_transfer_create_dto=asset_transfer_create_dto)

Creates a new transfer for an asset

Creates a new transfer record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_create_dto import AssetTransferCreateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_transfer_create_dto = openapi_client.AssetTransferCreateDto() # AssetTransferCreateDto |  (optional)

    try:
        # Creates a new transfer for an asset
        api_response = api_instance.create_asset_transfer(tenant_id, asset_id, asset_transfer_create_dto=asset_transfer_create_dto)
        print("The response of AssetsApi->create_asset_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **asset_transfer_create_dto** | [**AssetTransferCreateDto**](AssetTransferCreateDto.md)|  | [optional] 

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

# **create_asset_value_amend**
> EmptyEnvelope create_asset_value_amend(tenant_id, asset_id, asset_value_amend_create_dto=asset_value_amend_create_dto)

Creates a new value amendment for an asset

Creates a new value amendment record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_value_amend_create_dto import AssetValueAmendCreateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_value_amend_create_dto = openapi_client.AssetValueAmendCreateDto() # AssetValueAmendCreateDto |  (optional)

    try:
        # Creates a new value amendment for an asset
        api_response = api_instance.create_asset_value_amend(tenant_id, asset_id, asset_value_amend_create_dto=asset_value_amend_create_dto)
        print("The response of AssetsApi->create_asset_value_amend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset_value_amend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **asset_value_amend_create_dto** | [**AssetValueAmendCreateDto**](AssetValueAmendCreateDto.md)|  | [optional] 

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

# **delete_asset**
> delete_asset(tenant_id, asset_id)

Deletes an existing asset

Deletes an existing asset for the authenticated tenant.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Deletes an existing asset
        api_instance.delete_asset(tenant_id, asset_id)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_asset_category**
> delete_asset_asset_category(tenant_id, category_id)

Deletes an existing asset category

Deletes an existing asset category for the authenticated tenant.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 

    try:
        # Deletes an existing asset category
        api_instance.delete_asset_asset_category(tenant_id, category_id)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_depreciation_record**
> EmptyEnvelope delete_asset_depreciation_record(tenant_id, asset_id, record_id)

Deletes a depreciation record for an asset

Deletes a depreciation record for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    record_id = 'record_id_example' # str | 

    try:
        # Deletes a depreciation record for an asset
        api_response = api_instance.delete_asset_depreciation_record(tenant_id, asset_id, record_id)
        print("The response of AssetsApi->delete_asset_depreciation_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset_depreciation_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **record_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_repair**
> EmptyEnvelope delete_asset_repair(tenant_id, asset_id, repair_id)

Deletes a repair for an asset

Deletes a repair record for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    repair_id = 'repair_id_example' # str | 

    try:
        # Deletes a repair for an asset
        api_response = api_instance.delete_asset_repair(tenant_id, asset_id, repair_id)
        print("The response of AssetsApi->delete_asset_repair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset_repair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **repair_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_transfer**
> EmptyEnvelope delete_asset_transfer(tenant_id, asset_id, transfer_id)

Deletes a transfer for an asset

Deletes a transfer record for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 

    try:
        # Deletes a transfer for an asset
        api_response = api_instance.delete_asset_transfer(tenant_id, asset_id, transfer_id)
        print("The response of AssetsApi->delete_asset_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **transfer_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_value_amend**
> EmptyEnvelope delete_asset_value_amend(tenant_id, asset_id, amend_id)

Deletes a value amendment for an asset

Deletes a value amendment record for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    amend_id = 'amend_id_example' # str | 

    try:
        # Deletes a value amendment for an asset
        api_response = api_instance.delete_asset_value_amend(tenant_id, asset_id, amend_id)
        print("The response of AssetsApi->delete_asset_value_amend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset_value_amend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **amend_id** | **str**|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetDtoEnvelope get_asset(tenant_id, asset_id)

Gets a specific asset by ID

Retrieves a specific asset for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_dto_envelope import AssetDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets a specific asset by ID
        api_response = api_instance.get_asset(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**AssetDtoEnvelope**](AssetDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_asset_categories**
> AssetCategoryDtoListEnvelope get_asset_asset_categories(tenant_id)

Gets all asset categories

Retrieves all asset categories for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_dto_list_envelope import AssetCategoryDtoListEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets all asset categories
        api_response = api_instance.get_asset_asset_categories(tenant_id)
        print("The response of AssetsApi->get_asset_asset_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_asset_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**AssetCategoryDtoListEnvelope**](AssetCategoryDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_asset_categories_count**
> Int32Envelope get_asset_asset_categories_count(tenant_id)

Gets the count of asset categories

Returns the total number of asset categories for the authenticated tenant.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets the count of asset categories
        api_response = api_instance.get_asset_asset_categories_count(tenant_id)
        print("The response of AssetsApi->get_asset_asset_categories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_asset_categories_count: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_asset_category**
> AssetCategoryDtoEnvelope get_asset_asset_category(tenant_id, category_id)

Gets a specific asset category

Retrieves a specific asset category for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_dto_envelope import AssetCategoryDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 

    try:
        # Gets a specific asset category
        api_response = api_instance.get_asset_asset_category(tenant_id, category_id)
        print("The response of AssetsApi->get_asset_asset_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 

### Return type

[**AssetCategoryDtoEnvelope**](AssetCategoryDtoEnvelope.md)

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_depreciation_record**
> AssetDepreciationRecordDtoEnvelope get_asset_depreciation_record(tenant_id, asset_id, record_id)

Gets a specific depreciation record for an asset

Retrieves a specific depreciation record by ID for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_depreciation_record_dto_envelope import AssetDepreciationRecordDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    record_id = 'record_id_example' # str | 

    try:
        # Gets a specific depreciation record for an asset
        api_response = api_instance.get_asset_depreciation_record(tenant_id, asset_id, record_id)
        print("The response of AssetsApi->get_asset_depreciation_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_depreciation_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **record_id** | **str**|  | 

### Return type

[**AssetDepreciationRecordDtoEnvelope**](AssetDepreciationRecordDtoEnvelope.md)

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

# **get_asset_depreciation_records**
> AssetDepreciationRecordDtoListEnvelope get_asset_depreciation_records(tenant_id, asset_id)

Gets depreciation records for a specific asset

Retrieves all depreciation records for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_depreciation_record_dto_list_envelope import AssetDepreciationRecordDtoListEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets depreciation records for a specific asset
        api_response = api_instance.get_asset_depreciation_records(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_depreciation_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_depreciation_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**AssetDepreciationRecordDtoListEnvelope**](AssetDepreciationRecordDtoListEnvelope.md)

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

# **get_asset_depreciation_records_count**
> Int32Envelope get_asset_depreciation_records_count(tenant_id, asset_id)

Gets count of depreciation records for a specific asset

Returns the total number of depreciation records for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets count of depreciation records for a specific asset
        api_response = api_instance.get_asset_depreciation_records_count(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_depreciation_records_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_depreciation_records_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

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

# **get_asset_repair**
> AssetRepairDtoEnvelope get_asset_repair(tenant_id, asset_id, repair_id)

Gets a specific repair for an asset

Retrieves a specific repair record by ID for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_repair_dto_envelope import AssetRepairDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    repair_id = 'repair_id_example' # str | 

    try:
        # Gets a specific repair for an asset
        api_response = api_instance.get_asset_repair(tenant_id, asset_id, repair_id)
        print("The response of AssetsApi->get_asset_repair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_repair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **repair_id** | **str**|  | 

### Return type

[**AssetRepairDtoEnvelope**](AssetRepairDtoEnvelope.md)

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

# **get_asset_repairs**
> AssetRepairDtoListEnvelope get_asset_repairs(tenant_id, asset_id)

Gets repairs for a specific asset

Retrieves all repair records for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_repair_dto_list_envelope import AssetRepairDtoListEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets repairs for a specific asset
        api_response = api_instance.get_asset_repairs(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_repairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_repairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**AssetRepairDtoListEnvelope**](AssetRepairDtoListEnvelope.md)

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

# **get_asset_repairs_count**
> Int32Envelope get_asset_repairs_count(tenant_id, asset_id)

Gets count of repairs for a specific asset

Returns the total number of repair records for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets count of repairs for a specific asset
        api_response = api_instance.get_asset_repairs_count(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_repairs_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_repairs_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

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

# **get_asset_transfer**
> AssetTransferDtoEnvelope get_asset_transfer(tenant_id, asset_id, transfer_id)

Gets a specific transfer for an asset

Retrieves a specific transfer record by ID for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_dto_envelope import AssetTransferDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 

    try:
        # Gets a specific transfer for an asset
        api_response = api_instance.get_asset_transfer(tenant_id, asset_id, transfer_id)
        print("The response of AssetsApi->get_asset_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **transfer_id** | **str**|  | 

### Return type

[**AssetTransferDtoEnvelope**](AssetTransferDtoEnvelope.md)

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

# **get_asset_transfers**
> AssetTransferDtoListEnvelope get_asset_transfers(tenant_id, asset_id)

Gets transfers for a specific asset

Retrieves all transfer records for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_dto_list_envelope import AssetTransferDtoListEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets transfers for a specific asset
        api_response = api_instance.get_asset_transfers(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**AssetTransferDtoListEnvelope**](AssetTransferDtoListEnvelope.md)

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

# **get_asset_transfers_count**
> Int32Envelope get_asset_transfers_count(tenant_id, asset_id)

Gets count of transfers for a specific asset

Returns the total number of transfer records for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets count of transfers for a specific asset
        api_response = api_instance.get_asset_transfers_count(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_transfers_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_transfers_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

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

# **get_asset_value_amend**
> AssetValueAmendDtoEnvelope get_asset_value_amend(tenant_id, asset_id, amend_id)

Gets a specific value amendment for an asset

Retrieves a specific value amendment record by ID for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_value_amend_dto_envelope import AssetValueAmendDtoEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    amend_id = 'amend_id_example' # str | 

    try:
        # Gets a specific value amendment for an asset
        api_response = api_instance.get_asset_value_amend(tenant_id, asset_id, amend_id)
        print("The response of AssetsApi->get_asset_value_amend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_value_amend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **amend_id** | **str**|  | 

### Return type

[**AssetValueAmendDtoEnvelope**](AssetValueAmendDtoEnvelope.md)

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

# **get_asset_value_amends**
> AssetValueAmendDtoListEnvelope get_asset_value_amends(tenant_id, asset_id)

Gets value amendments for a specific asset

Retrieves all value amendment records for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_value_amend_dto_list_envelope import AssetValueAmendDtoListEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets value amendments for a specific asset
        api_response = api_instance.get_asset_value_amends(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_value_amends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_value_amends: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

### Return type

[**AssetValueAmendDtoListEnvelope**](AssetValueAmendDtoListEnvelope.md)

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

# **get_asset_value_amends_count**
> Int32Envelope get_asset_value_amends_count(tenant_id, asset_id)

Gets count of value amendments for a specific asset

Returns the total number of value amendment records for the specified asset.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 

    try:
        # Gets count of value amendments for a specific asset
        api_response = api_instance.get_asset_value_amends_count(tenant_id, asset_id)
        print("The response of AssetsApi->get_asset_value_amends_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_value_amends_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 

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

# **get_assets**
> AssetDtoListEnvelope get_assets(tenant_id)

Gets all assets for the current tenant

Retrieves all assets for the authenticated tenant with optional filtering.

### Example


```python
import openapi_client
from openapi_client.models.asset_dto_list_envelope import AssetDtoListEnvelope
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets all assets for the current tenant
        api_response = api_instance.get_assets(tenant_id)
        print("The response of AssetsApi->get_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**AssetDtoListEnvelope**](AssetDtoListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_count**
> Int32Envelope get_assets_count(tenant_id)

Gets the count of assets

Returns the total number of assets for the authenticated tenant.

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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Gets the count of assets
        api_response = api_instance.get_assets_count(tenant_id)
        print("The response of AssetsApi->get_assets_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_count: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> AssetDtoEnvelope update_asset(tenant_id, asset_id, asset_update_dto=asset_update_dto)

Updates an existing asset

Updates an existing asset for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_dto_envelope import AssetDtoEnvelope
from openapi_client.models.asset_update_dto import AssetUpdateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    asset_update_dto = openapi_client.AssetUpdateDto() # AssetUpdateDto |  (optional)

    try:
        # Updates an existing asset
        api_response = api_instance.update_asset(tenant_id, asset_id, asset_update_dto=asset_update_dto)
        print("The response of AssetsApi->update_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **asset_update_dto** | [**AssetUpdateDto**](AssetUpdateDto.md)|  | [optional] 

### Return type

[**AssetDtoEnvelope**](AssetDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_asset_category**
> AssetCategoryDtoEnvelope update_asset_asset_category(tenant_id, category_id, asset_category_update_dto=asset_category_update_dto)

Updates an existing asset category

Updates an existing asset category for the authenticated tenant.

### Example


```python
import openapi_client
from openapi_client.models.asset_category_dto_envelope import AssetCategoryDtoEnvelope
from openapi_client.models.asset_category_update_dto import AssetCategoryUpdateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    category_id = 'category_id_example' # str | 
    asset_category_update_dto = openapi_client.AssetCategoryUpdateDto() # AssetCategoryUpdateDto |  (optional)

    try:
        # Updates an existing asset category
        api_response = api_instance.update_asset_asset_category(tenant_id, category_id, asset_category_update_dto=asset_category_update_dto)
        print("The response of AssetsApi->update_asset_asset_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_asset_asset_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **category_id** | **str**|  | 
 **asset_category_update_dto** | [**AssetCategoryUpdateDto**](AssetCategoryUpdateDto.md)|  | [optional] 

### Return type

[**AssetCategoryDtoEnvelope**](AssetCategoryDtoEnvelope.md)

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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_depreciation_record**
> EmptyEnvelope update_asset_depreciation_record(tenant_id, asset_id, record_id, asset_depreciation_record_update_dto=asset_depreciation_record_update_dto)

Updates a depreciation record for an asset

Updates an existing depreciation record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_depreciation_record_update_dto import AssetDepreciationRecordUpdateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    record_id = 'record_id_example' # str | 
    asset_depreciation_record_update_dto = openapi_client.AssetDepreciationRecordUpdateDto() # AssetDepreciationRecordUpdateDto |  (optional)

    try:
        # Updates a depreciation record for an asset
        api_response = api_instance.update_asset_depreciation_record(tenant_id, asset_id, record_id, asset_depreciation_record_update_dto=asset_depreciation_record_update_dto)
        print("The response of AssetsApi->update_asset_depreciation_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_asset_depreciation_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **record_id** | **str**|  | 
 **asset_depreciation_record_update_dto** | [**AssetDepreciationRecordUpdateDto**](AssetDepreciationRecordUpdateDto.md)|  | [optional] 

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

# **update_asset_repair**
> EmptyEnvelope update_asset_repair(tenant_id, asset_id, repair_id, asset_repair_update_dto=asset_repair_update_dto)

Updates a repair for an asset

Updates an existing repair record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_repair_update_dto import AssetRepairUpdateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    repair_id = 'repair_id_example' # str | 
    asset_repair_update_dto = openapi_client.AssetRepairUpdateDto() # AssetRepairUpdateDto |  (optional)

    try:
        # Updates a repair for an asset
        api_response = api_instance.update_asset_repair(tenant_id, asset_id, repair_id, asset_repair_update_dto=asset_repair_update_dto)
        print("The response of AssetsApi->update_asset_repair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_asset_repair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **repair_id** | **str**|  | 
 **asset_repair_update_dto** | [**AssetRepairUpdateDto**](AssetRepairUpdateDto.md)|  | [optional] 

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

# **update_asset_transfer**
> EmptyEnvelope update_asset_transfer(tenant_id, asset_id, transfer_id, asset_transfer_update_dto=asset_transfer_update_dto)

Updates a transfer for an asset

Updates an existing transfer record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_transfer_update_dto import AssetTransferUpdateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 
    asset_transfer_update_dto = openapi_client.AssetTransferUpdateDto() # AssetTransferUpdateDto |  (optional)

    try:
        # Updates a transfer for an asset
        api_response = api_instance.update_asset_transfer(tenant_id, asset_id, transfer_id, asset_transfer_update_dto=asset_transfer_update_dto)
        print("The response of AssetsApi->update_asset_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_asset_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **transfer_id** | **str**|  | 
 **asset_transfer_update_dto** | [**AssetTransferUpdateDto**](AssetTransferUpdateDto.md)|  | [optional] 

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

# **update_asset_value_amend**
> EmptyEnvelope update_asset_value_amend(tenant_id, asset_id, amend_id, asset_value_amend_update_dto=asset_value_amend_update_dto)

Updates a value amendment for an asset

Updates an existing value amendment record for the specified asset.

### Example


```python
import openapi_client
from openapi_client.models.asset_value_amend_update_dto import AssetValueAmendUpdateDto
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
    api_instance = openapi_client.AssetsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    amend_id = 'amend_id_example' # str | 
    asset_value_amend_update_dto = openapi_client.AssetValueAmendUpdateDto() # AssetValueAmendUpdateDto |  (optional)

    try:
        # Updates a value amendment for an asset
        api_response = api_instance.update_asset_value_amend(tenant_id, asset_id, amend_id, asset_value_amend_update_dto=asset_value_amend_update_dto)
        print("The response of AssetsApi->update_asset_value_amend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_asset_value_amend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **amend_id** | **str**|  | 
 **asset_value_amend_update_dto** | [**AssetValueAmendUpdateDto**](AssetValueAmendUpdateDto.md)|  | [optional] 

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

