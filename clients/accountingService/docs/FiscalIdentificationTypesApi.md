# openapi_client.FiscalIdentificationTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fiscal_identification_type**](FiscalIdentificationTypesApi.md#create_fiscal_identification_type) | **POST** /api/v2/AccountingService/Fiscals/Authorities/IdentificationTypes | Create a fiscal identification type
[**delete_fiscal_identification_type**](FiscalIdentificationTypesApi.md#delete_fiscal_identification_type) | **DELETE** /api/v2/AccountingService/Fiscals/Authorities/IdentificationTypes/{identificationTypeId} | Delete a fiscal identification type
[**get_fiscal_identification_type**](FiscalIdentificationTypesApi.md#get_fiscal_identification_type) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{fiscalAuthorityId}/IdentificationTypes/{identificationTypeId} | Get fiscal identification type by ID
[**get_fiscal_identification_types**](FiscalIdentificationTypesApi.md#get_fiscal_identification_types) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId}/IdentificationTypes | Get fiscal identification types for an authority
[**get_fiscal_identification_types_count**](FiscalIdentificationTypesApi.md#get_fiscal_identification_types_count) | **GET** /api/v2/AccountingService/Fiscals/Authorities/{authorityId}/IdentificationTypes/Count | Get fiscal identification types count
[**update_fiscal_identification_type**](FiscalIdentificationTypesApi.md#update_fiscal_identification_type) | **PUT** /api/v2/AccountingService/Fiscals/Authorities/IdentificationTypes/{identificationTypeId} | Update a fiscal identification type


# **create_fiscal_identification_type**
> EmptyEnvelope create_fiscal_identification_type(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_identification_type_create_dto=fiscal_identification_type_create_dto)

Create a fiscal identification type

Creates a new fiscal identification type for a fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_identification_type_create_dto import FiscalIdentificationTypeCreateDto
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
    api_instance = openapi_client.FiscalIdentificationTypesApi(api_client)
    tenant_id = None # object | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_identification_type_create_dto = openapi_client.FiscalIdentificationTypeCreateDto() # FiscalIdentificationTypeCreateDto |  (optional)

    try:
        # Create a fiscal identification type
        api_response = api_instance.create_fiscal_identification_type(tenant_id, api_version=api_version, x_api_version=x_api_version, fiscal_identification_type_create_dto=fiscal_identification_type_create_dto)
        print("The response of FiscalIdentificationTypesApi->create_fiscal_identification_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalIdentificationTypesApi->create_fiscal_identification_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_identification_type_create_dto** | [**FiscalIdentificationTypeCreateDto**](FiscalIdentificationTypeCreateDto.md)|  | [optional] 

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

# **delete_fiscal_identification_type**
> EmptyEnvelope delete_fiscal_identification_type(tenant_id, identification_type_id, api_version=api_version, x_api_version=x_api_version)

Delete a fiscal identification type

Deletes a fiscal identification type identified by its unique identifier.

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
    api_instance = openapi_client.FiscalIdentificationTypesApi(api_client)
    tenant_id = None # object | 
    identification_type_id = 'identification_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a fiscal identification type
        api_response = api_instance.delete_fiscal_identification_type(tenant_id, identification_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalIdentificationTypesApi->delete_fiscal_identification_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalIdentificationTypesApi->delete_fiscal_identification_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **identification_type_id** | **str**|  | 
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

# **get_fiscal_identification_type**
> FiscalIdentificationTypeDtoEnvelope get_fiscal_identification_type(tenant_id, fiscal_authority_id, identification_type_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal identification type by ID

Retrieves a specific fiscal identification type by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_identification_type_dto_envelope import FiscalIdentificationTypeDtoEnvelope
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
    api_instance = openapi_client.FiscalIdentificationTypesApi(api_client)
    tenant_id = None # object | 
    fiscal_authority_id = 'fiscal_authority_id_example' # str | 
    identification_type_id = 'identification_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal identification type by ID
        api_response = api_instance.get_fiscal_identification_type(tenant_id, fiscal_authority_id, identification_type_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalIdentificationTypesApi->get_fiscal_identification_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalIdentificationTypesApi->get_fiscal_identification_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **fiscal_authority_id** | **str**|  | 
 **identification_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalIdentificationTypeDtoEnvelope**](FiscalIdentificationTypeDtoEnvelope.md)

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

# **get_fiscal_identification_types**
> FiscalIdentificationTypeDtoListEnvelope get_fiscal_identification_types(authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal identification types for an authority

Retrieves all fiscal identification types for the specified fiscal authority.

### Example


```python
import openapi_client
from openapi_client.models.fiscal_identification_type_dto_list_envelope import FiscalIdentificationTypeDtoListEnvelope
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
    api_instance = openapi_client.FiscalIdentificationTypesApi(api_client)
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal identification types for an authority
        api_response = api_instance.get_fiscal_identification_types(authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalIdentificationTypesApi->get_fiscal_identification_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalIdentificationTypesApi->get_fiscal_identification_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**FiscalIdentificationTypeDtoListEnvelope**](FiscalIdentificationTypeDtoListEnvelope.md)

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

# **get_fiscal_identification_types_count**
> Int32Envelope get_fiscal_identification_types_count(authority_id, api_version=api_version, x_api_version=x_api_version)

Get fiscal identification types count

Returns the total count of fiscal identification types for the specified fiscal authority.

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
    api_instance = openapi_client.FiscalIdentificationTypesApi(api_client)
    authority_id = 'authority_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get fiscal identification types count
        api_response = api_instance.get_fiscal_identification_types_count(authority_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of FiscalIdentificationTypesApi->get_fiscal_identification_types_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalIdentificationTypesApi->get_fiscal_identification_types_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_id** | **str**|  | 
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

# **update_fiscal_identification_type**
> EmptyEnvelope update_fiscal_identification_type(tenant_id, identification_type_id, api_version=api_version, x_api_version=x_api_version, fiscal_identification_type_update_dto=fiscal_identification_type_update_dto)

Update a fiscal identification type

Updates an existing fiscal identification type identified by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.fiscal_identification_type_update_dto import FiscalIdentificationTypeUpdateDto
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
    api_instance = openapi_client.FiscalIdentificationTypesApi(api_client)
    tenant_id = None # object | 
    identification_type_id = 'identification_type_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    fiscal_identification_type_update_dto = openapi_client.FiscalIdentificationTypeUpdateDto() # FiscalIdentificationTypeUpdateDto |  (optional)

    try:
        # Update a fiscal identification type
        api_response = api_instance.update_fiscal_identification_type(tenant_id, identification_type_id, api_version=api_version, x_api_version=x_api_version, fiscal_identification_type_update_dto=fiscal_identification_type_update_dto)
        print("The response of FiscalIdentificationTypesApi->update_fiscal_identification_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiscalIdentificationTypesApi->update_fiscal_identification_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 
 **identification_type_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **fiscal_identification_type_update_dto** | [**FiscalIdentificationTypeUpdateDto**](FiscalIdentificationTypeUpdateDto.md)|  | [optional] 

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

