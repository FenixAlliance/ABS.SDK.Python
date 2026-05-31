# openapi_client.SharesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_share_class**](SharesApi.md#create_share_class) | **POST** /api/v2/AccountingService/Shares/Classes | Creates a new share class
[**create_share_issuance**](SharesApi.md#create_share_issuance) | **POST** /api/v2/AccountingService/Shares/Issuances | Creates a new share issuance
[**create_share_transfer**](SharesApi.md#create_share_transfer) | **POST** /api/v2/AccountingService/Shares/Transfers | Creates a new share transfer
[**create_share_transfer_reason**](SharesApi.md#create_share_transfer_reason) | **POST** /api/v2/AccountingService/Shares/TransferReasons | Creates a new share transfer reason
[**delete_share_class**](SharesApi.md#delete_share_class) | **DELETE** /api/v2/AccountingService/Shares/Classes/{shareClassId} | Deletes an existing share class
[**delete_share_issuance**](SharesApi.md#delete_share_issuance) | **DELETE** /api/v2/AccountingService/Shares/Issuances/{issuanceId} | Deletes an existing share issuance
[**delete_share_transfer**](SharesApi.md#delete_share_transfer) | **DELETE** /api/v2/AccountingService/Shares/Transfers/{transferId} | Deletes an existing share transfer
[**delete_share_transfer_reason**](SharesApi.md#delete_share_transfer_reason) | **DELETE** /api/v2/AccountingService/Shares/TransferReasons/{reasonId} | Deletes an existing share transfer reason
[**get_share_class**](SharesApi.md#get_share_class) | **GET** /api/v2/AccountingService/Shares/Classes/{shareClassId} | Gets a share class by id
[**get_share_classes**](SharesApi.md#get_share_classes) | **GET** /api/v2/AccountingService/Shares/Classes | Gets the current tenant share classes
[**get_share_classes_count**](SharesApi.md#get_share_classes_count) | **GET** /api/v2/AccountingService/Shares/Classes/Count | Gets the current tenant share classes count
[**get_share_issuance**](SharesApi.md#get_share_issuance) | **GET** /api/v2/AccountingService/Shares/Issuances/{issuanceId} | Gets a share issuance by id
[**get_share_issuances**](SharesApi.md#get_share_issuances) | **GET** /api/v2/AccountingService/Shares/Issuances | Gets the current tenant share issuances
[**get_share_issuances_count**](SharesApi.md#get_share_issuances_count) | **GET** /api/v2/AccountingService/Shares/Issuances/Count | Gets the current tenant share issuances count
[**get_share_transfer**](SharesApi.md#get_share_transfer) | **GET** /api/v2/AccountingService/Shares/Transfers/{transferId} | Gets a share transfer by id
[**get_share_transfer_reason**](SharesApi.md#get_share_transfer_reason) | **GET** /api/v2/AccountingService/Shares/TransferReasons/{reasonId} | Gets a share transfer reason by id
[**get_share_transfer_reasons**](SharesApi.md#get_share_transfer_reasons) | **GET** /api/v2/AccountingService/Shares/TransferReasons | Gets the current tenant share transfer reasons
[**get_share_transfer_reasons_count**](SharesApi.md#get_share_transfer_reasons_count) | **GET** /api/v2/AccountingService/Shares/TransferReasons/Count | Gets the current tenant share transfer reasons count
[**get_share_transfers**](SharesApi.md#get_share_transfers) | **GET** /api/v2/AccountingService/Shares/Transfers | Gets the current tenant share transfers
[**get_share_transfers_count**](SharesApi.md#get_share_transfers_count) | **GET** /api/v2/AccountingService/Shares/Transfers/Count | Gets the current tenant share transfers count
[**update_share_class**](SharesApi.md#update_share_class) | **PUT** /api/v2/AccountingService/Shares/Classes/{shareClassId} | Updates an existing share class
[**update_share_issuance**](SharesApi.md#update_share_issuance) | **PUT** /api/v2/AccountingService/Shares/Issuances/{issuanceId} | Updates an existing share issuance
[**update_share_transfer**](SharesApi.md#update_share_transfer) | **PUT** /api/v2/AccountingService/Shares/Transfers/{transferId} | Updates an existing share transfer
[**update_share_transfer_reason**](SharesApi.md#update_share_transfer_reason) | **PUT** /api/v2/AccountingService/Shares/TransferReasons/{reasonId} | Updates an existing share transfer reason


# **create_share_class**
> ShareClassDtoEnvelope create_share_class(tenant_id, api_version=api_version, x_api_version=x_api_version, share_class_create_dto=share_class_create_dto)

Creates a new share class

Creates a new share class.

### Example


```python
import openapi_client
from openapi_client.models.share_class_create_dto import ShareClassCreateDto
from openapi_client.models.share_class_dto_envelope import ShareClassDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_class_create_dto = openapi_client.ShareClassCreateDto() # ShareClassCreateDto |  (optional)

    try:
        # Creates a new share class
        api_response = api_instance.create_share_class(tenant_id, api_version=api_version, x_api_version=x_api_version, share_class_create_dto=share_class_create_dto)
        print("The response of SharesApi->create_share_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->create_share_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_class_create_dto** | [**ShareClassCreateDto**](ShareClassCreateDto.md)|  | [optional] 

### Return type

[**ShareClassDtoEnvelope**](ShareClassDtoEnvelope.md)

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

# **create_share_issuance**
> ShareIssuanceDtoEnvelope create_share_issuance(tenant_id, api_version=api_version, x_api_version=x_api_version, share_issuance_create_dto=share_issuance_create_dto)

Creates a new share issuance

Creates a new share issuance.

### Example


```python
import openapi_client
from openapi_client.models.share_issuance_create_dto import ShareIssuanceCreateDto
from openapi_client.models.share_issuance_dto_envelope import ShareIssuanceDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_issuance_create_dto = openapi_client.ShareIssuanceCreateDto() # ShareIssuanceCreateDto |  (optional)

    try:
        # Creates a new share issuance
        api_response = api_instance.create_share_issuance(tenant_id, api_version=api_version, x_api_version=x_api_version, share_issuance_create_dto=share_issuance_create_dto)
        print("The response of SharesApi->create_share_issuance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->create_share_issuance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_issuance_create_dto** | [**ShareIssuanceCreateDto**](ShareIssuanceCreateDto.md)|  | [optional] 

### Return type

[**ShareIssuanceDtoEnvelope**](ShareIssuanceDtoEnvelope.md)

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

# **create_share_transfer**
> ShareTransferDtoEnvelope create_share_transfer(tenant_id, api_version=api_version, x_api_version=x_api_version, share_transfer_create_dto=share_transfer_create_dto)

Creates a new share transfer

Creates a new share transfer.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_create_dto import ShareTransferCreateDto
from openapi_client.models.share_transfer_dto_envelope import ShareTransferDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_transfer_create_dto = openapi_client.ShareTransferCreateDto() # ShareTransferCreateDto |  (optional)

    try:
        # Creates a new share transfer
        api_response = api_instance.create_share_transfer(tenant_id, api_version=api_version, x_api_version=x_api_version, share_transfer_create_dto=share_transfer_create_dto)
        print("The response of SharesApi->create_share_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->create_share_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_transfer_create_dto** | [**ShareTransferCreateDto**](ShareTransferCreateDto.md)|  | [optional] 

### Return type

[**ShareTransferDtoEnvelope**](ShareTransferDtoEnvelope.md)

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

# **create_share_transfer_reason**
> ShareTransferReasonDtoEnvelope create_share_transfer_reason(tenant_id, api_version=api_version, x_api_version=x_api_version, share_transfer_reason_create_dto=share_transfer_reason_create_dto)

Creates a new share transfer reason

Creates a new share transfer reason.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_reason_create_dto import ShareTransferReasonCreateDto
from openapi_client.models.share_transfer_reason_dto_envelope import ShareTransferReasonDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_transfer_reason_create_dto = openapi_client.ShareTransferReasonCreateDto() # ShareTransferReasonCreateDto |  (optional)

    try:
        # Creates a new share transfer reason
        api_response = api_instance.create_share_transfer_reason(tenant_id, api_version=api_version, x_api_version=x_api_version, share_transfer_reason_create_dto=share_transfer_reason_create_dto)
        print("The response of SharesApi->create_share_transfer_reason:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->create_share_transfer_reason: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_transfer_reason_create_dto** | [**ShareTransferReasonCreateDto**](ShareTransferReasonCreateDto.md)|  | [optional] 

### Return type

[**ShareTransferReasonDtoEnvelope**](ShareTransferReasonDtoEnvelope.md)

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

# **delete_share_class**
> delete_share_class(tenant_id, share_class_id, api_version=api_version, x_api_version=x_api_version)

Deletes an existing share class

Deletes an existing share class.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    share_class_id = 'share_class_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes an existing share class
        api_instance.delete_share_class(tenant_id, share_class_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling SharesApi->delete_share_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **share_class_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_share_issuance**
> delete_share_issuance(tenant_id, issuance_id, api_version=api_version, x_api_version=x_api_version)

Deletes an existing share issuance

Deletes an existing share issuance.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    issuance_id = 'issuance_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes an existing share issuance
        api_instance.delete_share_issuance(tenant_id, issuance_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling SharesApi->delete_share_issuance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **issuance_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_share_transfer**
> delete_share_transfer(tenant_id, transfer_id, api_version=api_version, x_api_version=x_api_version)

Deletes an existing share transfer

Deletes an existing share transfer.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes an existing share transfer
        api_instance.delete_share_transfer(tenant_id, transfer_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling SharesApi->delete_share_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transfer_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_share_transfer_reason**
> delete_share_transfer_reason(tenant_id, reason_id, api_version=api_version, x_api_version=x_api_version)

Deletes an existing share transfer reason

Deletes an existing share transfer reason.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    reason_id = 'reason_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes an existing share transfer reason
        api_instance.delete_share_transfer_reason(tenant_id, reason_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling SharesApi->delete_share_transfer_reason: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **reason_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_class**
> ShareClassDtoEnvelope get_share_class(tenant_id, share_class_id, api_version=api_version, x_api_version=x_api_version)

Gets a share class by id

Get a specific share class by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.share_class_dto_envelope import ShareClassDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    share_class_id = 'share_class_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a share class by id
        api_response = api_instance.get_share_class(tenant_id, share_class_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **share_class_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareClassDtoEnvelope**](ShareClassDtoEnvelope.md)

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

# **get_share_classes**
> ShareClassDtoListEnvelope get_share_classes(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share classes

Get the currently acting tenant share classes.

### Example


```python
import openapi_client
from openapi_client.models.share_class_dto_list_envelope import ShareClassDtoListEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share classes
        api_response = api_instance.get_share_classes(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_classes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_classes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareClassDtoListEnvelope**](ShareClassDtoListEnvelope.md)

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

# **get_share_classes_count**
> Int32Envelope get_share_classes_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share classes count

Get the currently acting tenant share classes count.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share classes count
        api_response = api_instance.get_share_classes_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_classes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_classes_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_issuance**
> ShareIssuanceDtoEnvelope get_share_issuance(tenant_id, issuance_id, api_version=api_version, x_api_version=x_api_version)

Gets a share issuance by id

Get a specific share issuance by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.share_issuance_dto_envelope import ShareIssuanceDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    issuance_id = 'issuance_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a share issuance by id
        api_response = api_instance.get_share_issuance(tenant_id, issuance_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_issuance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_issuance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **issuance_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareIssuanceDtoEnvelope**](ShareIssuanceDtoEnvelope.md)

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

# **get_share_issuances**
> ShareIssuanceDtoListEnvelope get_share_issuances(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share issuances

Get the currently acting tenant share issuances.

### Example


```python
import openapi_client
from openapi_client.models.share_issuance_dto_list_envelope import ShareIssuanceDtoListEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share issuances
        api_response = api_instance.get_share_issuances(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_issuances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_issuances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareIssuanceDtoListEnvelope**](ShareIssuanceDtoListEnvelope.md)

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

# **get_share_issuances_count**
> Int32Envelope get_share_issuances_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share issuances count

Get the currently acting tenant share issuances count.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share issuances count
        api_response = api_instance.get_share_issuances_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_issuances_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_issuances_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_transfer**
> ShareTransferDtoEnvelope get_share_transfer(tenant_id, transfer_id, api_version=api_version, x_api_version=x_api_version)

Gets a share transfer by id

Get a specific share transfer by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_dto_envelope import ShareTransferDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a share transfer by id
        api_response = api_instance.get_share_transfer(tenant_id, transfer_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transfer_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareTransferDtoEnvelope**](ShareTransferDtoEnvelope.md)

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

# **get_share_transfer_reason**
> ShareTransferReasonDtoEnvelope get_share_transfer_reason(tenant_id, reason_id, api_version=api_version, x_api_version=x_api_version)

Gets a share transfer reason by id

Get a specific share transfer reason by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_reason_dto_envelope import ShareTransferReasonDtoEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    reason_id = 'reason_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a share transfer reason by id
        api_response = api_instance.get_share_transfer_reason(tenant_id, reason_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_transfer_reason:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_transfer_reason: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **reason_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareTransferReasonDtoEnvelope**](ShareTransferReasonDtoEnvelope.md)

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

# **get_share_transfer_reasons**
> ShareTransferReasonDtoListEnvelope get_share_transfer_reasons(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share transfer reasons

Get the currently acting tenant share transfer reasons.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_reason_dto_list_envelope import ShareTransferReasonDtoListEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share transfer reasons
        api_response = api_instance.get_share_transfer_reasons(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_transfer_reasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_transfer_reasons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareTransferReasonDtoListEnvelope**](ShareTransferReasonDtoListEnvelope.md)

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

# **get_share_transfer_reasons_count**
> Int32Envelope get_share_transfer_reasons_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share transfer reasons count

Get the currently acting tenant share transfer reasons count.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share transfer reasons count
        api_response = api_instance.get_share_transfer_reasons_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_transfer_reasons_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_transfer_reasons_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_transfers**
> ShareTransferDtoListEnvelope get_share_transfers(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share transfers

Get the currently acting tenant share transfers.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_dto_list_envelope import ShareTransferDtoListEnvelope
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share transfers
        api_response = api_instance.get_share_transfers(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ShareTransferDtoListEnvelope**](ShareTransferDtoListEnvelope.md)

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

# **get_share_transfers_count**
> Int32Envelope get_share_transfers_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the current tenant share transfers count

Get the currently acting tenant share transfers count.

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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the current tenant share transfers count
        api_response = api_instance.get_share_transfers_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SharesApi->get_share_transfers_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->get_share_transfers_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_share_class**
> ShareClassDtoEnvelope update_share_class(tenant_id, share_class_id, api_version=api_version, x_api_version=x_api_version, share_class_update_dto=share_class_update_dto)

Updates an existing share class

Updates an existing share class.

### Example


```python
import openapi_client
from openapi_client.models.share_class_dto_envelope import ShareClassDtoEnvelope
from openapi_client.models.share_class_update_dto import ShareClassUpdateDto
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    share_class_id = 'share_class_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_class_update_dto = openapi_client.ShareClassUpdateDto() # ShareClassUpdateDto |  (optional)

    try:
        # Updates an existing share class
        api_response = api_instance.update_share_class(tenant_id, share_class_id, api_version=api_version, x_api_version=x_api_version, share_class_update_dto=share_class_update_dto)
        print("The response of SharesApi->update_share_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->update_share_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **share_class_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_class_update_dto** | [**ShareClassUpdateDto**](ShareClassUpdateDto.md)|  | [optional] 

### Return type

[**ShareClassDtoEnvelope**](ShareClassDtoEnvelope.md)

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

# **update_share_issuance**
> ShareIssuanceDtoEnvelope update_share_issuance(tenant_id, issuance_id, api_version=api_version, x_api_version=x_api_version, share_issuance_update_dto=share_issuance_update_dto)

Updates an existing share issuance

Updates an existing share issuance.

### Example


```python
import openapi_client
from openapi_client.models.share_issuance_dto_envelope import ShareIssuanceDtoEnvelope
from openapi_client.models.share_issuance_update_dto import ShareIssuanceUpdateDto
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    issuance_id = 'issuance_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_issuance_update_dto = openapi_client.ShareIssuanceUpdateDto() # ShareIssuanceUpdateDto |  (optional)

    try:
        # Updates an existing share issuance
        api_response = api_instance.update_share_issuance(tenant_id, issuance_id, api_version=api_version, x_api_version=x_api_version, share_issuance_update_dto=share_issuance_update_dto)
        print("The response of SharesApi->update_share_issuance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->update_share_issuance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **issuance_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_issuance_update_dto** | [**ShareIssuanceUpdateDto**](ShareIssuanceUpdateDto.md)|  | [optional] 

### Return type

[**ShareIssuanceDtoEnvelope**](ShareIssuanceDtoEnvelope.md)

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

# **update_share_transfer**
> ShareTransferDtoEnvelope update_share_transfer(tenant_id, transfer_id, api_version=api_version, x_api_version=x_api_version, share_transfer_update_dto=share_transfer_update_dto)

Updates an existing share transfer

Updates an existing share transfer.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_dto_envelope import ShareTransferDtoEnvelope
from openapi_client.models.share_transfer_update_dto import ShareTransferUpdateDto
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    transfer_id = 'transfer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_transfer_update_dto = openapi_client.ShareTransferUpdateDto() # ShareTransferUpdateDto |  (optional)

    try:
        # Updates an existing share transfer
        api_response = api_instance.update_share_transfer(tenant_id, transfer_id, api_version=api_version, x_api_version=x_api_version, share_transfer_update_dto=share_transfer_update_dto)
        print("The response of SharesApi->update_share_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->update_share_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **transfer_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_transfer_update_dto** | [**ShareTransferUpdateDto**](ShareTransferUpdateDto.md)|  | [optional] 

### Return type

[**ShareTransferDtoEnvelope**](ShareTransferDtoEnvelope.md)

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

# **update_share_transfer_reason**
> ShareTransferReasonDtoEnvelope update_share_transfer_reason(tenant_id, reason_id, api_version=api_version, x_api_version=x_api_version, share_transfer_reason_update_dto=share_transfer_reason_update_dto)

Updates an existing share transfer reason

Updates an existing share transfer reason.

### Example


```python
import openapi_client
from openapi_client.models.share_transfer_reason_dto_envelope import ShareTransferReasonDtoEnvelope
from openapi_client.models.share_transfer_reason_update_dto import ShareTransferReasonUpdateDto
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
    api_instance = openapi_client.SharesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    reason_id = 'reason_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    share_transfer_reason_update_dto = openapi_client.ShareTransferReasonUpdateDto() # ShareTransferReasonUpdateDto |  (optional)

    try:
        # Updates an existing share transfer reason
        api_response = api_instance.update_share_transfer_reason(tenant_id, reason_id, api_version=api_version, x_api_version=x_api_version, share_transfer_reason_update_dto=share_transfer_reason_update_dto)
        print("The response of SharesApi->update_share_transfer_reason:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->update_share_transfer_reason: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **reason_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **share_transfer_reason_update_dto** | [**ShareTransferReasonUpdateDto**](ShareTransferReasonUpdateDto.md)|  | [optional] 

### Return type

[**ShareTransferReasonDtoEnvelope**](ShareTransferReasonDtoEnvelope.md)

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

