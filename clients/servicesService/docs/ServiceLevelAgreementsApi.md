# openapi_client.ServiceLevelAgreementsApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_level_agreement_async**](ServiceLevelAgreementsApi.md#create_service_level_agreement_async) | **POST** /api/v2/ServicesService/ServiceLevelAgreements | Create a service level agreement
[**delete_service_level_agreement_async**](ServiceLevelAgreementsApi.md#delete_service_level_agreement_async) | **DELETE** /api/v2/ServicesService/ServiceLevelAgreements/{serviceLevelAgreementId} | Delete a service level agreement
[**get_service_level_agreement_by_id_async**](ServiceLevelAgreementsApi.md#get_service_level_agreement_by_id_async) | **GET** /api/v2/ServicesService/ServiceLevelAgreements/{serviceLevelAgreementId} | Get a service level agreement by ID
[**get_service_level_agreements_async**](ServiceLevelAgreementsApi.md#get_service_level_agreements_async) | **GET** /api/v2/ServicesService/ServiceLevelAgreements | Get all service level agreements
[**get_service_level_agreements_count_async**](ServiceLevelAgreementsApi.md#get_service_level_agreements_count_async) | **GET** /api/v2/ServicesService/ServiceLevelAgreements/Count | Get service level agreements count
[**update_service_level_agreement_async**](ServiceLevelAgreementsApi.md#update_service_level_agreement_async) | **PUT** /api/v2/ServicesService/ServiceLevelAgreements/{serviceLevelAgreementId} | Update a service level agreement


# **create_service_level_agreement_async**
> Envelope create_service_level_agreement_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_level_agreement_create_dto=service_level_agreement_create_dto)

Create a service level agreement

Creates a new service level agreement for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_level_agreement_create_dto import ServiceLevelAgreementCreateDto
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
    api_instance = openapi_client.ServiceLevelAgreementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_level_agreement_create_dto = openapi_client.ServiceLevelAgreementCreateDto() # ServiceLevelAgreementCreateDto |  (optional)

    try:
        # Create a service level agreement
        api_response = api_instance.create_service_level_agreement_async(tenant_id, api_version=api_version, x_api_version=x_api_version, service_level_agreement_create_dto=service_level_agreement_create_dto)
        print("The response of ServiceLevelAgreementsApi->create_service_level_agreement_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelAgreementsApi->create_service_level_agreement_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_level_agreement_create_dto** | [**ServiceLevelAgreementCreateDto**](ServiceLevelAgreementCreateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **delete_service_level_agreement_async**
> Envelope delete_service_level_agreement_async(tenant_id, service_level_agreement_id, api_version=api_version, x_api_version=x_api_version)

Delete a service level agreement

Deletes a service level agreement by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
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
    api_instance = openapi_client.ServiceLevelAgreementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_level_agreement_id = 'service_level_agreement_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a service level agreement
        api_response = api_instance.delete_service_level_agreement_async(tenant_id, service_level_agreement_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelAgreementsApi->delete_service_level_agreement_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelAgreementsApi->delete_service_level_agreement_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_level_agreement_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

# **get_service_level_agreement_by_id_async**
> ServiceLevelAgreementDtoEnvelope get_service_level_agreement_by_id_async(tenant_id, service_level_agreement_id, api_version=api_version, x_api_version=x_api_version)

Get a service level agreement by ID

Retrieves a service level agreement by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.service_level_agreement_dto_envelope import ServiceLevelAgreementDtoEnvelope
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
    api_instance = openapi_client.ServiceLevelAgreementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_level_agreement_id = 'service_level_agreement_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get a service level agreement by ID
        api_response = api_instance.get_service_level_agreement_by_id_async(tenant_id, service_level_agreement_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelAgreementsApi->get_service_level_agreement_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelAgreementsApi->get_service_level_agreement_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_level_agreement_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceLevelAgreementDtoEnvelope**](ServiceLevelAgreementDtoEnvelope.md)

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

# **get_service_level_agreements_async**
> ServiceLevelAgreementDtoIReadOnlyListEnvelope get_service_level_agreements_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all service level agreements

Retrieves all service level agreements for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.service_level_agreement_dto_i_read_only_list_envelope import ServiceLevelAgreementDtoIReadOnlyListEnvelope
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
    api_instance = openapi_client.ServiceLevelAgreementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all service level agreements
        api_response = api_instance.get_service_level_agreements_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelAgreementsApi->get_service_level_agreements_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelAgreementsApi->get_service_level_agreements_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ServiceLevelAgreementDtoIReadOnlyListEnvelope**](ServiceLevelAgreementDtoIReadOnlyListEnvelope.md)

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

# **get_service_level_agreements_count_async**
> Int32Envelope get_service_level_agreements_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get service level agreements count

Returns the count of service level agreements for the specified tenant.

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
    api_instance = openapi_client.ServiceLevelAgreementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get service level agreements count
        api_response = api_instance.get_service_level_agreements_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ServiceLevelAgreementsApi->get_service_level_agreements_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelAgreementsApi->get_service_level_agreements_count_async: %s\n" % e)
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

# **update_service_level_agreement_async**
> Envelope update_service_level_agreement_async(tenant_id, service_level_agreement_id, api_version=api_version, x_api_version=x_api_version, service_level_agreement_update_dto=service_level_agreement_update_dto)

Update a service level agreement

Updates an existing service level agreement.

### Example


```python
import openapi_client
from openapi_client.models.envelope import Envelope
from openapi_client.models.service_level_agreement_update_dto import ServiceLevelAgreementUpdateDto
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
    api_instance = openapi_client.ServiceLevelAgreementsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    service_level_agreement_id = 'service_level_agreement_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    service_level_agreement_update_dto = openapi_client.ServiceLevelAgreementUpdateDto() # ServiceLevelAgreementUpdateDto |  (optional)

    try:
        # Update a service level agreement
        api_response = api_instance.update_service_level_agreement_async(tenant_id, service_level_agreement_id, api_version=api_version, x_api_version=x_api_version, service_level_agreement_update_dto=service_level_agreement_update_dto)
        print("The response of ServiceLevelAgreementsApi->update_service_level_agreement_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceLevelAgreementsApi->update_service_level_agreement_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **service_level_agreement_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **service_level_agreement_update_dto** | [**ServiceLevelAgreementUpdateDto**](ServiceLevelAgreementUpdateDto.md)|  | [optional] 

### Return type

[**Envelope**](Envelope.md)

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

