# openapi_client.LoyaltyProgramsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_loyalty_programs_async**](LoyaltyProgramsApi.md#count_loyalty_programs_async) | **GET** /api/v2/SalesService/LoyaltyPrograms/Count | Get loyalty programs count
[**create_loyalty_program_async**](LoyaltyProgramsApi.md#create_loyalty_program_async) | **POST** /api/v2/SalesService/LoyaltyPrograms | Create a loyalty program
[**delete_loyalty_program_async**](LoyaltyProgramsApi.md#delete_loyalty_program_async) | **DELETE** /api/v2/SalesService/LoyaltyPrograms/{loyaltyProgramId} | Delete a loyalty program
[**get_loyalty_program_async**](LoyaltyProgramsApi.md#get_loyalty_program_async) | **GET** /api/v2/SalesService/LoyaltyPrograms/{loyaltyProgramId} | Get loyalty program by ID
[**get_loyalty_programs_async**](LoyaltyProgramsApi.md#get_loyalty_programs_async) | **GET** /api/v2/SalesService/LoyaltyPrograms | Get loyalty programs
[**update_loyalty_program_async**](LoyaltyProgramsApi.md#update_loyalty_program_async) | **PUT** /api/v2/SalesService/LoyaltyPrograms/{loyaltyProgramId} | Update a loyalty program


# **count_loyalty_programs_async**
> Int32Envelope count_loyalty_programs_async(tenant_id)

Get loyalty programs count

Returns the total count of loyalty programs for the specified tenant with OData filter support.

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
    api_instance = openapi_client.LoyaltyProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get loyalty programs count
        api_response = api_instance.count_loyalty_programs_async(tenant_id)
        print("The response of LoyaltyProgramsApi->count_loyalty_programs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyProgramsApi->count_loyalty_programs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loyalty_program_async**
> EmptyEnvelope create_loyalty_program_async(tenant_id, loyalty_program_create_dto=loyalty_program_create_dto)

Create a loyalty program

Creates a new loyalty program for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loyalty_program_create_dto import LoyaltyProgramCreateDto
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
    api_instance = openapi_client.LoyaltyProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loyalty_program_create_dto = openapi_client.LoyaltyProgramCreateDto() # LoyaltyProgramCreateDto |  (optional)

    try:
        # Create a loyalty program
        api_response = api_instance.create_loyalty_program_async(tenant_id, loyalty_program_create_dto=loyalty_program_create_dto)
        print("The response of LoyaltyProgramsApi->create_loyalty_program_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyProgramsApi->create_loyalty_program_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loyalty_program_create_dto** | [**LoyaltyProgramCreateDto**](LoyaltyProgramCreateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loyalty_program_async**
> EmptyEnvelope delete_loyalty_program_async(tenant_id, loyalty_program_id)

Delete a loyalty program

Deletes an existing loyalty program by its unique identifier.

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
    api_instance = openapi_client.LoyaltyProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loyalty_program_id = 'loyalty_program_id_example' # str | 

    try:
        # Delete a loyalty program
        api_response = api_instance.delete_loyalty_program_async(tenant_id, loyalty_program_id)
        print("The response of LoyaltyProgramsApi->delete_loyalty_program_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyProgramsApi->delete_loyalty_program_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loyalty_program_id** | **str**|  | 

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

# **get_loyalty_program_async**
> LoyaltyProgramDtoEnvelope get_loyalty_program_async(tenant_id, loyalty_program_id)

Get loyalty program by ID

Retrieves a single loyalty program by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.loyalty_program_dto_envelope import LoyaltyProgramDtoEnvelope
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
    api_instance = openapi_client.LoyaltyProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loyalty_program_id = 'loyalty_program_id_example' # str | 

    try:
        # Get loyalty program by ID
        api_response = api_instance.get_loyalty_program_async(tenant_id, loyalty_program_id)
        print("The response of LoyaltyProgramsApi->get_loyalty_program_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyProgramsApi->get_loyalty_program_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loyalty_program_id** | **str**|  | 

### Return type

[**LoyaltyProgramDtoEnvelope**](LoyaltyProgramDtoEnvelope.md)

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

# **get_loyalty_programs_async**
> LoyaltyProgramDtoListEnvelope get_loyalty_programs_async(tenant_id)

Get loyalty programs

Retrieves a list of loyalty programs for the specified tenant with OData query support.

### Example


```python
import openapi_client
from openapi_client.models.loyalty_program_dto_list_envelope import LoyaltyProgramDtoListEnvelope
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
    api_instance = openapi_client.LoyaltyProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get loyalty programs
        api_response = api_instance.get_loyalty_programs_async(tenant_id)
        print("The response of LoyaltyProgramsApi->get_loyalty_programs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyProgramsApi->get_loyalty_programs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**LoyaltyProgramDtoListEnvelope**](LoyaltyProgramDtoListEnvelope.md)

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

# **update_loyalty_program_async**
> EmptyEnvelope update_loyalty_program_async(tenant_id, loyalty_program_id, loyalty_program_update_dto=loyalty_program_update_dto)

Update a loyalty program

Updates an existing loyalty program by its unique identifier.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.loyalty_program_update_dto import LoyaltyProgramUpdateDto
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
    api_instance = openapi_client.LoyaltyProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    loyalty_program_id = 'loyalty_program_id_example' # str | 
    loyalty_program_update_dto = openapi_client.LoyaltyProgramUpdateDto() # LoyaltyProgramUpdateDto |  (optional)

    try:
        # Update a loyalty program
        api_response = api_instance.update_loyalty_program_async(tenant_id, loyalty_program_id, loyalty_program_update_dto=loyalty_program_update_dto)
        print("The response of LoyaltyProgramsApi->update_loyalty_program_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltyProgramsApi->update_loyalty_program_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **loyalty_program_id** | **str**|  | 
 **loyalty_program_update_dto** | [**LoyaltyProgramUpdateDto**](LoyaltyProgramUpdateDto.md)|  | [optional] 

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
**404** | Not Found |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

