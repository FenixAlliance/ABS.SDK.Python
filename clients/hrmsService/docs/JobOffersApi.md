# openapi_client.JobOffersApi

All URIs are relative to *https://absuite.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_offer_async**](JobOffersApi.md#create_job_offer_async) | **POST** /api/v2/HrmsService/JobOffers | Create a job offer
[**delete_job_offer_async**](JobOffersApi.md#delete_job_offer_async) | **DELETE** /api/v2/HrmsService/JobOffers/{jobOfferId} | Delete a job offer
[**get_job_offer_by_id_async**](JobOffersApi.md#get_job_offer_by_id_async) | **GET** /api/v2/HrmsService/JobOffers/{jobOfferId} | Get job offer by ID
[**get_job_offers_async**](JobOffersApi.md#get_job_offers_async) | **GET** /api/v2/HrmsService/JobOffers | Get job offers
[**get_job_offers_count_async**](JobOffersApi.md#get_job_offers_count_async) | **GET** /api/v2/HrmsService/JobOffers/Count | Count job offers
[**update_job_offer_async**](JobOffersApi.md#update_job_offer_async) | **PUT** /api/v2/HrmsService/JobOffers/{jobOfferId} | Update a job offer


# **create_job_offer_async**
> EmptyEnvelope create_job_offer_async(tenant_id, api_version=api_version, x_api_version=x_api_version, job_offer_create_dto=job_offer_create_dto)

Create a job offer

Creates a new job offer for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.job_offer_create_dto import JobOfferCreateDto
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
    api_instance = openapi_client.JobOffersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    job_offer_create_dto = openapi_client.JobOfferCreateDto() # JobOfferCreateDto |  (optional)

    try:
        # Create a job offer
        api_response = api_instance.create_job_offer_async(tenant_id, api_version=api_version, x_api_version=x_api_version, job_offer_create_dto=job_offer_create_dto)
        print("The response of JobOffersApi->create_job_offer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobOffersApi->create_job_offer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **job_offer_create_dto** | [**JobOfferCreateDto**](JobOfferCreateDto.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_offer_async**
> EmptyEnvelope delete_job_offer_async(tenant_id, job_offer_id, api_version=api_version, x_api_version=x_api_version)

Delete a job offer

Deletes a job offer for the specified tenant.

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
    api_instance = openapi_client.JobOffersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    job_offer_id = 'job_offer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a job offer
        api_response = api_instance.delete_job_offer_async(tenant_id, job_offer_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobOffersApi->delete_job_offer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobOffersApi->delete_job_offer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **job_offer_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_offer_by_id_async**
> JobOfferDtoEnvelope get_job_offer_by_id_async(tenant_id, job_offer_id, api_version=api_version, x_api_version=x_api_version)

Get job offer by ID

Retrieves a specific job offer by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.job_offer_dto_envelope import JobOfferDtoEnvelope
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
    api_instance = openapi_client.JobOffersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    job_offer_id = 'job_offer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get job offer by ID
        api_response = api_instance.get_job_offer_by_id_async(tenant_id, job_offer_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobOffersApi->get_job_offer_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobOffersApi->get_job_offer_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **job_offer_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JobOfferDtoEnvelope**](JobOfferDtoEnvelope.md)

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

# **get_job_offers_async**
> JobOfferDtoListEnvelope get_job_offers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get job offers

Retrieves job offers for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.job_offer_dto_list_envelope import JobOfferDtoListEnvelope
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
    api_instance = openapi_client.JobOffersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get job offers
        api_response = api_instance.get_job_offers_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobOffersApi->get_job_offers_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobOffersApi->get_job_offers_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**JobOfferDtoListEnvelope**](JobOfferDtoListEnvelope.md)

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

# **get_job_offers_count_async**
> Int32Envelope get_job_offers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count job offers

Counts job offers for the specified tenant.

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
    api_instance = openapi_client.JobOffersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count job offers
        api_response = api_instance.get_job_offers_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of JobOffersApi->get_job_offers_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobOffersApi->get_job_offers_count_async: %s\n" % e)
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

# **update_job_offer_async**
> EmptyEnvelope update_job_offer_async(tenant_id, job_offer_id, api_version=api_version, x_api_version=x_api_version, body=body)

Update a job offer

Updates an existing job offer for the specified tenant.

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
    api_instance = openapi_client.JobOffersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    job_offer_id = 'job_offer_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update a job offer
        api_response = api_instance.update_job_offer_async(tenant_id, job_offer_id, api_version=api_version, x_api_version=x_api_version, body=body)
        print("The response of JobOffersApi->update_job_offer_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobOffersApi->update_job_offer_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **job_offer_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

