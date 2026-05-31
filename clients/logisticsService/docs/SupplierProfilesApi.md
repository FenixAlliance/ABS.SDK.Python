# openapi_client.SupplierProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplier_profile_async**](SupplierProfilesApi.md#create_supplier_profile_async) | **POST** /api/v2/LogisticsService/SupplierProfiles | Create a supplier profile
[**delete_supplier_profile_async**](SupplierProfilesApi.md#delete_supplier_profile_async) | **DELETE** /api/v2/LogisticsService/SupplierProfiles/{supplierProfileId} | Delete a supplier profile
[**get_supplier_profile_by_id_async**](SupplierProfilesApi.md#get_supplier_profile_by_id_async) | **GET** /api/v2/LogisticsService/SupplierProfiles/{supplierProfileId} | Get supplier profile by ID
[**get_supplier_profiles_async**](SupplierProfilesApi.md#get_supplier_profiles_async) | **GET** /api/v2/LogisticsService/SupplierProfiles | Get all supplier profiles
[**get_supplier_profiles_count_async**](SupplierProfilesApi.md#get_supplier_profiles_count_async) | **GET** /api/v2/LogisticsService/SupplierProfiles/Count | Get supplier profiles count
[**update_supplier_profile_async**](SupplierProfilesApi.md#update_supplier_profile_async) | **PUT** /api/v2/LogisticsService/SupplierProfiles/{supplierProfileId} | Update a supplier profile


# **create_supplier_profile_async**
> EmptyEnvelope create_supplier_profile_async(tenant_id, api_version=api_version, x_api_version=x_api_version, supplier_profile_create_dto=supplier_profile_create_dto)

Create a supplier profile

Creates a new supplier profile for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.supplier_profile_create_dto import SupplierProfileCreateDto
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
    api_instance = openapi_client.SupplierProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    supplier_profile_create_dto = openapi_client.SupplierProfileCreateDto() # SupplierProfileCreateDto |  (optional)

    try:
        # Create a supplier profile
        api_response = api_instance.create_supplier_profile_async(tenant_id, api_version=api_version, x_api_version=x_api_version, supplier_profile_create_dto=supplier_profile_create_dto)
        print("The response of SupplierProfilesApi->create_supplier_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierProfilesApi->create_supplier_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **supplier_profile_create_dto** | [**SupplierProfileCreateDto**](SupplierProfileCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_supplier_profile_async**
> EmptyEnvelope delete_supplier_profile_async(tenant_id, supplier_profile_id, api_version=api_version, x_api_version=x_api_version)

Delete a supplier profile

Deletes a supplier profile.

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
    api_instance = openapi_client.SupplierProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    supplier_profile_id = 'supplier_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a supplier profile
        api_response = api_instance.delete_supplier_profile_async(tenant_id, supplier_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupplierProfilesApi->delete_supplier_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierProfilesApi->delete_supplier_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **supplier_profile_id** | **str**|  | 
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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_profile_by_id_async**
> SupplierProfileDtoEnvelope get_supplier_profile_by_id_async(tenant_id, supplier_profile_id, api_version=api_version, x_api_version=x_api_version)

Get supplier profile by ID

Retrieves a specific supplier profile by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.supplier_profile_dto_envelope import SupplierProfileDtoEnvelope
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
    api_instance = openapi_client.SupplierProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    supplier_profile_id = 'supplier_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get supplier profile by ID
        api_response = api_instance.get_supplier_profile_by_id_async(tenant_id, supplier_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupplierProfilesApi->get_supplier_profile_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierProfilesApi->get_supplier_profile_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **supplier_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupplierProfileDtoEnvelope**](SupplierProfileDtoEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supplier_profiles_async**
> SupplierProfileDtoListEnvelope get_supplier_profiles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all supplier profiles

Retrieves all supplier profiles for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.supplier_profile_dto_list_envelope import SupplierProfileDtoListEnvelope
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
    api_instance = openapi_client.SupplierProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all supplier profiles
        api_response = api_instance.get_supplier_profiles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupplierProfilesApi->get_supplier_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierProfilesApi->get_supplier_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SupplierProfileDtoListEnvelope**](SupplierProfileDtoListEnvelope.md)

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

# **get_supplier_profiles_count_async**
> Int32Envelope get_supplier_profiles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get supplier profiles count

Returns the count of supplier profiles for the specified tenant.

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
    api_instance = openapi_client.SupplierProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get supplier profiles count
        api_response = api_instance.get_supplier_profiles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SupplierProfilesApi->get_supplier_profiles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierProfilesApi->get_supplier_profiles_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supplier_profile_async**
> EmptyEnvelope update_supplier_profile_async(tenant_id, supplier_profile_id, api_version=api_version, x_api_version=x_api_version, supplier_profile_update_dto=supplier_profile_update_dto)

Update a supplier profile

Updates an existing supplier profile.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.supplier_profile_update_dto import SupplierProfileUpdateDto
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
    api_instance = openapi_client.SupplierProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    supplier_profile_id = 'supplier_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    supplier_profile_update_dto = openapi_client.SupplierProfileUpdateDto() # SupplierProfileUpdateDto |  (optional)

    try:
        # Update a supplier profile
        api_response = api_instance.update_supplier_profile_async(tenant_id, supplier_profile_id, api_version=api_version, x_api_version=x_api_version, supplier_profile_update_dto=supplier_profile_update_dto)
        print("The response of SupplierProfilesApi->update_supplier_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierProfilesApi->update_supplier_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **supplier_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **supplier_profile_update_dto** | [**SupplierProfileUpdateDto**](SupplierProfileUpdateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

