# openapi_client.BankProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bank_profiles**](BankProfilesApi.md#get_bank_profiles) | **GET** /api/v2/AccountingService/BankProfiles | Get all bank profiles for a tenant
[**get_bank_profiles_count**](BankProfilesApi.md#get_bank_profiles_count) | **GET** /api/v2/AccountingService/BankProfiles/Count | Get bank profiles count


# **get_bank_profiles**
> BankProfileDtoListEnvelope get_bank_profiles(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all bank profiles for a tenant

Retrieves all bank profiles for the specified tenant using OData query options.

### Example


```python
import openapi_client
from openapi_client.models.bank_profile_dto_list_envelope import BankProfileDtoListEnvelope
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
    api_instance = openapi_client.BankProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all bank profiles for a tenant
        api_response = api_instance.get_bank_profiles(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankProfilesApi->get_bank_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankProfilesApi->get_bank_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BankProfileDtoListEnvelope**](BankProfileDtoListEnvelope.md)

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

# **get_bank_profiles_count**
> Int32Envelope get_bank_profiles_count(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get bank profiles count

Returns the count of bank profiles for the specified tenant.

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
    api_instance = openapi_client.BankProfilesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get bank profiles count
        api_response = api_instance.get_bank_profiles_count(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BankProfilesApi->get_bank_profiles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankProfilesApi->get_bank_profiles_count: %s\n" % e)
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

