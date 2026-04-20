# openapi_client.FiscalRegimesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_regime**](FiscalRegimesApi.md#create_fiscal_regime) | **POST** /api/v2/AccountingService/Fiscals/Authorities/FiscalRegimes | Create a fiscal regime
[**delete_fiscal_regime**](FiscalRegimesApi.md#delete_fiscal_regime) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/FiscalRegimes/{regimeId} | Delete a fiscal regime
[**get_fiscal_regime**](FiscalRegimesApi.md#get_fiscal_regime) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalRegimes/{regimeId} | Get fiscal regime by ID
[**get_fiscal_regimes**](FiscalRegimesApi.md#get_fiscal_regimes) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId}/FiscalRegimes | Get fiscal regimes for an authority
[**get_fiscal_regimes_count**](FiscalRegimesApi.md#get_fiscal_regimes_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalRegimes/Count | Get fiscal regimes count
[**update_fiscal_regime**](FiscalRegimesApi.md#update_fiscal_regime) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/FiscalRegimes/{regimeId} | Update a fiscal regime


# **create_fiscal_regime**
> EmptyEnvelope create_fiscal_regime(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_regime_create_dto=fiscal_regime_create_dto)

Create a fiscal regime

Creates a new fiscal regime for a fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_regime_create_dto import FiscalRegimeCreateDto
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
    api_instance = openapi_client.FiscalRegimesApi(api_client)
    tenant_id = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_regime_create_dto = openapi_client.FiscalRegimeCreateDto() # FiscalRegimeCreateDto |  (optional)

    try:
        # Create a fiscal regime
        api_response = api_instance.create_fiscal_regime(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_regime_create_dto=fiscal_regime_create_dto)
        print("The response of FiscalRegimesApi->create_fiscal_regime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalRegimesApi->create_fiscal_regime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_regime_create_dto** | [**FiscalRegimeCreateDto**](FiscalRegimeCreateDto.md)|  | [optional] 

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

# **delete_fiscal_regime**
> EmptyEnvelope delete_fiscal_regime(tenant_id, regime_id, api_version=api_version, x_api_version=x_api_version)

Delete a fiscal regime

Deletes a fiscal regime identified by its unique identifier.

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
    api_instance = openapi_client.FiscalRegimesApi(api_client)
    tenant_id = None # object | 
    regime_id = 'regime_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a fiscal regime
        api_response = api_instance.delete_fiscal_regime(tenant_id, regime_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalRegimesApi->delete_fiscal_regime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalRegimesApi->delete_fiscal_regime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **regime_id** | **str**|  | 
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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiscal_regime**
> FiscalRegimeDtoEnvelope get_fiscal_regime(tenant_id, fiscal_authority_id, regime_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal regime by ID

Retrieves a specific fiscal regime by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_regime_dto_envelope import FiscalRegimeDtoEnvelope
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
    api_instance = openapi_client.FiscalRegimesApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    regime_id = 'regime_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal regime by ID
        api_response = api_instance.get_fiscal_regime(tenant_id, fiscal_authority_id, regime_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalRegimesApi->get_fiscal_regime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalRegimesApi->get_fiscal_regime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **regime_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalRegimeDtoEnvelope**](FiscalRegimeDtoEnvelope.md)

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

# **get_fiscal_regimes**
> FiscalRegimeDtoListEnvelope get_fiscal_regimes(fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal regimes for an authority

Retrieves all fiscal regimes for the specified fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_regime_dto_list_envelope import FiscalRegimeDtoListEnvelope
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
    api_instance = openapi_client.FiscalRegimesApi(api_client)
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal regimes for an authority
        api_response = api_instance.get_fiscal_regimes(fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalRegimesApi->get_fiscal_regimes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalRegimesApi->get_fiscal_regimes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fiscal_authority_id** | **str**|  | 
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalRegimeDtoListEnvelope**](FiscalRegimeDtoListEnvelope.md)

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

# **get_fiscal_regimes_count**
> Int32Envelope get_fiscal_regimes_count(fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal regimes count

Returns the total count of fiscal regimes for the specified fiscal authority.

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
    api_instance = openapi_client.FiscalRegimesApi(api_client)
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal regimes count
        api_response = api_instance.get_fiscal_regimes_count(fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalRegimesApi->get_fiscal_regimes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalRegimesApi->get_fiscal_regimes_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fiscal_authority_id** | **str**|  | 
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

# **update_fiscal_regime**
> EmptyEnvelope update_fiscal_regime(tenant_id, regime_id, api_version=api_version, x_api_version=x_api_version, fiscal_regime_update_dto=fiscal_regime_update_dto)

Update a fiscal regime

Updates an existing fiscal regime identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_regime_update_dto import FiscalRegimeUpdateDto
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
    api_instance = openapi_client.FiscalRegimesApi(api_client)
    tenant_id = None # object | 
    regime_id = 'regime_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_regime_update_dto = openapi_client.FiscalRegimeUpdateDto() # FiscalRegimeUpdateDto |  (optional)

    try:
        # Update a fiscal regime
        api_response = api_instance.update_fiscal_regime(tenant_id, regime_id, api_version=api_version, x_api_version=x_api_version, fiscal_regime_update_dto=fiscal_regime_update_dto)
        print("The response of FiscalRegimesApi->update_fiscal_regime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalRegimesApi->update_fiscal_regime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **regime_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_regime_update_dto** | [**FiscalRegimeUpdateDto**](FiscalRegimeUpdateDto.md)|  | [optional] 

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

