# openapi_client.BillingProfilesApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_profile_async**](BillingProfilesApi.md#create_billing_profile_async) | **POST** /api/v2/AccountingService/BillingProfiles | Creates a new billing profile
[**delete_billing_profile_async**](BillingProfilesApi.md#delete_billing_profile_async) | **DELETE** /api/v2/AccountingService/BillingProfiles/{billingProfileId} | Deletes a billing profile
[**get_billing_profile_by_id_async**](BillingProfilesApi.md#get_billing_profile_by_id_async) | **GET** /api/v2/AccountingService/BillingProfiles/{billingProfileId} | Gets a billing profile by id
[**get_billing_profiles_async**](BillingProfilesApi.md#get_billing_profiles_async) | **GET** /api/v2/AccountingService/BillingProfiles | Gets all billing profiles
[**get_billing_profiles_count_async**](BillingProfilesApi.md#get_billing_profiles_count_async) | **GET** /api/v2/AccountingService/BillingProfiles/Count | Gets the count of billing profiles
[**update_billing_profile_async**](BillingProfilesApi.md#update_billing_profile_async) | **PUT** /api/v2/AccountingService/BillingProfiles/{billingProfileId} | Updates an existing billing profile


# **create_billing_profile_async**
> EmptyEnvelope create_billing_profile_async(tenant_id, billing_profile_create_dto, api_version=api_version, x_api_version=x_api_version)

Creates a new billing profile

Adds a new billing profile record for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.billing_profile_create_dto import BillingProfileCreateDto
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
    api_instance = openapi_client.BillingProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billing_profile_create_dto = openapi_client.BillingProfileCreateDto() # BillingProfileCreateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Creates a new billing profile
        api_response = api_instance.create_billing_profile_async(tenant_id, billing_profile_create_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillingProfilesApi->create_billing_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingProfilesApi->create_billing_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billing_profile_create_dto** | [**BillingProfileCreateDto**](BillingProfileCreateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_profile_async**
> EmptyEnvelope delete_billing_profile_async(tenant_id, billing_profile_id, api_version=api_version, x_api_version=x_api_version)

Deletes a billing profile

Removes a billing profile from the system using its unique identifier.

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
    api_instance = openapi_client.BillingProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billing_profile_id = 'billing_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Deletes a billing profile
        api_response = api_instance.delete_billing_profile_async(tenant_id, billing_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillingProfilesApi->delete_billing_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingProfilesApi->delete_billing_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billing_profile_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_profile_by_id_async**
> BillingProfileDtoEnvelope get_billing_profile_by_id_async(tenant_id, billing_profile_id, api_version=api_version, x_api_version=x_api_version)

Gets a billing profile by id

Retrieves a specific billing profile using its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.billing_profile_dto_envelope import BillingProfileDtoEnvelope
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
    api_instance = openapi_client.BillingProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billing_profile_id = 'billing_profile_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets a billing profile by id
        api_response = api_instance.get_billing_profile_by_id_async(tenant_id, billing_profile_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillingProfilesApi->get_billing_profile_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingProfilesApi->get_billing_profile_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billing_profile_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BillingProfileDtoEnvelope**](BillingProfileDtoEnvelope.md)

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

# **get_billing_profiles_async**
> BillingProfileDtoIReadOnlyListEnvelope get_billing_profiles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets all billing profiles

Fetches all billing profiles for a tenant with support for OData queries.

### Example


```python
import openapi_client
from openapi_client.models.billing_profile_dto_i_read_only_list_envelope import BillingProfileDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.BillingProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets all billing profiles
        api_response = api_instance.get_billing_profiles_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillingProfilesApi->get_billing_profiles_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingProfilesApi->get_billing_profiles_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BillingProfileDtoIReadOnlyListEnvelope**](BillingProfileDtoIReadOnlyListEnvelope.md)

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

# **get_billing_profiles_count_async**
> Int32Envelope get_billing_profiles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Gets the count of billing profiles

Returns the number of billing profiles for a tenant, supporting OData filtering.

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
    api_instance = openapi_client.BillingProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Gets the count of billing profiles
        api_response = api_instance.get_billing_profiles_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillingProfilesApi->get_billing_profiles_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingProfilesApi->get_billing_profiles_count_async: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_profile_async**
> EmptyEnvelope update_billing_profile_async(tenant_id, billing_profile_id, billing_profile_update_dto, api_version=api_version, x_api_version=x_api_version)

Updates an existing billing profile

Modifies an existing billing profile using the provided data.

### Example


```python
import openapi_client
from openapi_client.models.billing_profile_update_dto import BillingProfileUpdateDto
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
    api_instance = openapi_client.BillingProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    billing_profile_id = 'billing_profile_id_example' # str | 
    billing_profile_update_dto = openapi_client.BillingProfileUpdateDto() # BillingProfileUpdateDto | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Updates an existing billing profile
        api_response = api_instance.update_billing_profile_async(tenant_id, billing_profile_id, billing_profile_update_dto, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillingProfilesApi->update_billing_profile_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingProfilesApi->update_billing_profile_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **billing_profile_id** | **str**|  | 
 **billing_profile_update_dto** | [**BillingProfileUpdateDto**](BillingProfileUpdateDto.md)|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

