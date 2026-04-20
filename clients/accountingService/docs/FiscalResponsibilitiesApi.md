# openapi_client.FiscalResponsibilitiesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_responsibility**](FiscalResponsibilitiesApi.md#create_fiscal_responsibility) | **POST** /api/v2/AccountingService/Fiscals/Authorities/FiscalResponsibilities | Create a fiscal responsibility
[**delete_fiscal_responsibility**](FiscalResponsibilitiesApi.md#delete_fiscal_responsibility) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/FiscalResponsibilities/{fiscalResponsibilityId} | Delete a fiscal responsibility
[**get_fiscal_responsibilities**](FiscalResponsibilitiesApi.md#get_fiscal_responsibilities) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId}/FiscalResponsibilities | Get fiscal responsibilities for an authority
[**get_fiscal_responsibilities_count**](FiscalResponsibilitiesApi.md#get_fiscal_responsibilities_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalResponsibilities/Count | Get fiscal responsibilities count
[**get_fiscal_responsibility**](FiscalResponsibilitiesApi.md#get_fiscal_responsibility) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/FiscalResponsibilities/{fiscalResponsibilityId} | Get fiscal responsibility by ID
[**update_fiscal_responsibility**](FiscalResponsibilitiesApi.md#update_fiscal_responsibility) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/FiscalResponsibilities/{fiscalResponsibilityId} | Update a fiscal responsibility


# **create_fiscal_responsibility**
> EmptyEnvelope create_fiscal_responsibility(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_create_dto=fiscal_responsibility_create_dto)

Create a fiscal responsibility

Creates a new fiscal responsibility for a fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_responsibility_create_dto import FiscalResponsibilityCreateDto
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
    api_instance = openapi_client.FiscalResponsibilitiesApi(api_client)
    tenant_id = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_responsibility_create_dto = openapi_client.FiscalResponsibilityCreateDto() # FiscalResponsibilityCreateDto |  (optional)

    try:
        # Create a fiscal responsibility
        api_response = api_instance.create_fiscal_responsibility(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_create_dto=fiscal_responsibility_create_dto)
        print("The response of FiscalResponsibilitiesApi->create_fiscal_responsibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilitiesApi->create_fiscal_responsibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_responsibility_create_dto** | [**FiscalResponsibilityCreateDto**](FiscalResponsibilityCreateDto.md)|  | [optional] 

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

# **delete_fiscal_responsibility**
> EmptyEnvelope delete_fiscal_responsibility(tenant_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)

Delete a fiscal responsibility

Deletes a fiscal responsibility identified by its unique identifier.

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
    api_instance = openapi_client.FiscalResponsibilitiesApi(api_client)
    tenant_id = None # object | 
    fiscal_responsibility_id = 'fiscal_responsibility_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a fiscal responsibility
        api_response = api_instance.delete_fiscal_responsibility(tenant_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilitiesApi->delete_fiscal_responsibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilitiesApi->delete_fiscal_responsibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_responsibility_id** | **str**|  | 
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

# **get_fiscal_responsibilities**
> FiscalResponsibilityDtoListEnvelope get_fiscal_responsibilities(fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal responsibilities for an authority

Retrieves all fiscal responsibilities for the specified fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_responsibility_dto_list_envelope import FiscalResponsibilityDtoListEnvelope
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
    api_instance = openapi_client.FiscalResponsibilitiesApi(api_client)
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal responsibilities for an authority
        api_response = api_instance.get_fiscal_responsibilities(fiscal_authority_id, authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilitiesApi->get_fiscal_responsibilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilitiesApi->get_fiscal_responsibilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fiscal_authority_id** | **str**|  | 
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalResponsibilityDtoListEnvelope**](FiscalResponsibilityDtoListEnvelope.md)

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

# **get_fiscal_responsibilities_count**
> Int32Envelope get_fiscal_responsibilities_count(fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal responsibilities count

Returns the total count of fiscal responsibilities for the specified fiscal authority.

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
    api_instance = openapi_client.FiscalResponsibilitiesApi(api_client)
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal responsibilities count
        api_response = api_instance.get_fiscal_responsibilities_count(fiscal_authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilitiesApi->get_fiscal_responsibilities_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilitiesApi->get_fiscal_responsibilities_count: %s\n" % e)
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

# **get_fiscal_responsibility**
> FiscalResponsibilityDtoEnvelope get_fiscal_responsibility(tenant_id, fiscal_authority_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal responsibility by ID

Retrieves a specific fiscal responsibility by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_responsibility_dto_envelope import FiscalResponsibilityDtoEnvelope
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
    api_instance = openapi_client.FiscalResponsibilitiesApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    fiscal_responsibility_id = 'fiscal_responsibility_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal responsibility by ID
        api_response = api_instance.get_fiscal_responsibility(tenant_id, fiscal_authority_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalResponsibilitiesApi->get_fiscal_responsibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilitiesApi->get_fiscal_responsibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **fiscal_responsibility_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalResponsibilityDtoEnvelope**](FiscalResponsibilityDtoEnvelope.md)

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

# **update_fiscal_responsibility**
> EmptyEnvelope update_fiscal_responsibility(tenant_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_update_dto=fiscal_responsibility_update_dto)

Update a fiscal responsibility

Updates an existing fiscal responsibility identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_responsibility_update_dto import FiscalResponsibilityUpdateDto
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
    api_instance = openapi_client.FiscalResponsibilitiesApi(api_client)
    tenant_id = None # object | 
    fiscal_responsibility_id = 'fiscal_responsibility_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_responsibility_update_dto = openapi_client.FiscalResponsibilityUpdateDto() # FiscalResponsibilityUpdateDto |  (optional)

    try:
        # Update a fiscal responsibility
        api_response = api_instance.update_fiscal_responsibility(tenant_id, fiscal_responsibility_id, api_version=api_version, x_api_version=x_api_version, fiscal_responsibility_update_dto=fiscal_responsibility_update_dto)
        print("The response of FiscalResponsibilitiesApi->update_fiscal_responsibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalResponsibilitiesApi->update_fiscal_responsibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_responsibility_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_responsibility_update_dto** | [**FiscalResponsibilityUpdateDto**](FiscalResponsibilityUpdateDto.md)|  | [optional] 

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

