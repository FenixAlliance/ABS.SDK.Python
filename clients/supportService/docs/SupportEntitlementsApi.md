# openapi_client.SupportEntitlementsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_support_entitlement_async**](SupportEntitlementsApi.md#create_support_entitlement_async) | **POST** /api/v2/SupportService/SupportEntitlements | Create a new support entitlement
[**delete_support_entitlement_async**](SupportEntitlementsApi.md#delete_support_entitlement_async) | **DELETE** /api/v2/SupportService/SupportEntitlements/{supportEntitlementId} | Delete a support entitlement
[**get_support_entitlement_async**](SupportEntitlementsApi.md#get_support_entitlement_async) | **GET** /api/v2/SupportService/SupportEntitlements/{supportEntitlementId} | Retrieve a support entitlement by ID
[**get_support_entitlements_async**](SupportEntitlementsApi.md#get_support_entitlements_async) | **GET** /api/v2/SupportService/SupportEntitlements | Retrieve a list of support entitlements
[**get_support_entitlements_count_async**](SupportEntitlementsApi.md#get_support_entitlements_count_async) | **GET** /api/v2/SupportService/SupportEntitlements/Count | Get the count of support entitlements
[**update_support_entitlement_async**](SupportEntitlementsApi.md#update_support_entitlement_async) | **PUT** /api/v2/SupportService/SupportEntitlements/{supportEntitlementId} | Update a support entitlement


# **create_support_entitlement_async**
> EmptyEnvelope create_support_entitlement_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_entitlement_create_dto=support_entitlement_create_dto)

Create a new support entitlement

Creates a new support entitlement for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_entitlement_create_dto import SupportEntitlementCreateDto
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_entitlement_create_dto = openapi_client.SupportEntitlementCreateDto() # SupportEntitlementCreateDto |  (optional)

    try:
        # Create a new support entitlement
        api_response = api_instance.create_support_entitlement_async(tenant_id, api_version=api_version, x_api_version=x_api_version, support_entitlement_create_dto=support_entitlement_create_dto)
        print("The response of SupportEntitlementsApi->create_support_entitlement_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->create_support_entitlement_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_entitlement_create_dto** | [**SupportEntitlementCreateDto**](SupportEntitlementCreateDto.md)|  | [optional] 

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

# **delete_support_entitlement_async**
> EmptyEnvelope delete_support_entitlement_async(tenant_id, support_entitlement_id, api_version=api_version, x_api_version=x_api_version)

Delete a support entitlement

Deletes a support entitlement by its unique identifier.

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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_entitlement_id = 'support_entitlement_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a support entitlement
        api_response = api_instance.delete_support_entitlement_async(tenant_id, support_entitlement_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->delete_support_entitlement_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->delete_support_entitlement_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_entitlement_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_entitlement_async**
> SupportEntitlementDtoEnvelope get_support_entitlement_async(tenant_id, support_entitlement_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a support entitlement by ID

Retrieves a single support entitlement by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.support_entitlement_dto_envelope import SupportEntitlementDtoEnvelope
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_entitlement_id = 'support_entitlement_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a support entitlement by ID
        api_response = api_instance.get_support_entitlement_async(tenant_id, support_entitlement_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->get_support_entitlement_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->get_support_entitlement_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_entitlement_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportEntitlementDtoEnvelope**](SupportEntitlementDtoEnvelope.md)

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

# **get_support_entitlements_async**
> SupportEntitlementDtoListEnvelope get_support_entitlements_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of support entitlements

Retrieves a list of support entitlements for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.support_entitlement_dto_list_envelope import SupportEntitlementDtoListEnvelope
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of support entitlements
        api_response = api_instance.get_support_entitlements_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->get_support_entitlements_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->get_support_entitlements_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupportEntitlementDtoListEnvelope**](SupportEntitlementDtoListEnvelope.md)

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

# **get_support_entitlements_count_async**
> Int32Envelope get_support_entitlements_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get the count of support entitlements

Returns the total count of support entitlements for the specified tenant with OData query support.

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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of support entitlements
        api_response = api_instance.get_support_entitlements_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupportEntitlementsApi->get_support_entitlements_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->get_support_entitlements_count_async: %s\n" % e)
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

# **update_support_entitlement_async**
> EmptyEnvelope update_support_entitlement_async(tenant_id, support_entitlement_id, api_version=api_version, x_api_version=x_api_version, support_entitlement_update_dto=support_entitlement_update_dto)

Update a support entitlement

Updates an existing support entitlement by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.support_entitlement_update_dto import SupportEntitlementUpdateDto
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
    api_instance = openapi_client.SupportEntitlementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    support_entitlement_id = 'support_entitlement_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    support_entitlement_update_dto = openapi_client.SupportEntitlementUpdateDto() # SupportEntitlementUpdateDto |  (optional)

    try:
        # Update a support entitlement
        api_response = api_instance.update_support_entitlement_async(tenant_id, support_entitlement_id, api_version=api_version, x_api_version=x_api_version, support_entitlement_update_dto=support_entitlement_update_dto)
        print("The response of SupportEntitlementsApi->update_support_entitlement_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportEntitlementsApi->update_support_entitlement_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **support_entitlement_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **support_entitlement_update_dto** | [**SupportEntitlementUpdateDto**](SupportEntitlementUpdateDto.md)|  | [optional] 

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

