# openapi_client.TrainingProgramsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_training_program_async**](TrainingProgramsApi.md#create_training_program_async) | **POST** /api/v2/HrmsService/TrainingPrograms | Create a training program
[**delete_training_program_async**](TrainingProgramsApi.md#delete_training_program_async) | **DELETE** /api/v2/HrmsService/TrainingPrograms/{programId} | Delete a training program
[**get_training_program_by_id_async**](TrainingProgramsApi.md#get_training_program_by_id_async) | **GET** /api/v2/HrmsService/TrainingPrograms/{programId} | Get training program by ID
[**get_training_programs_async**](TrainingProgramsApi.md#get_training_programs_async) | **GET** /api/v2/HrmsService/TrainingPrograms | Get training programs
[**get_training_programs_count_async**](TrainingProgramsApi.md#get_training_programs_count_async) | **GET** /api/v2/HrmsService/TrainingPrograms/Count | Count training programs
[**update_training_program_async**](TrainingProgramsApi.md#update_training_program_async) | **PUT** /api/v2/HrmsService/TrainingPrograms/{programId} | Update a training program


# **create_training_program_async**
> EmptyEnvelope create_training_program_async(tenant_id, api_version=api_version, x_api_version=x_api_version, training_program_create_dto=training_program_create_dto)

Create a training program

Creates a new training program for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.training_program_create_dto import TrainingProgramCreateDto
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
    api_instance = openapi_client.TrainingProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    training_program_create_dto = openapi_client.TrainingProgramCreateDto() # TrainingProgramCreateDto |  (optional)

    try:
        # Create a training program
        api_response = api_instance.create_training_program_async(tenant_id, api_version=api_version, x_api_version=x_api_version, training_program_create_dto=training_program_create_dto)
        print("The response of TrainingProgramsApi->create_training_program_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramsApi->create_training_program_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **training_program_create_dto** | [**TrainingProgramCreateDto**](TrainingProgramCreateDto.md)|  | [optional] 

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

# **delete_training_program_async**
> EmptyEnvelope delete_training_program_async(tenant_id, program_id, api_version=api_version, x_api_version=x_api_version)

Delete a training program

Deletes a training program for the specified tenant.

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
    api_instance = openapi_client.TrainingProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    program_id = 'program_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a training program
        api_response = api_instance.delete_training_program_async(tenant_id, program_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramsApi->delete_training_program_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramsApi->delete_training_program_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **program_id** | **str**|  | 
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

# **get_training_program_by_id_async**
> TrainingProgramDtoEnvelope get_training_program_by_id_async(tenant_id, program_id, api_version=api_version, x_api_version=x_api_version)

Get training program by ID

Retrieves a specific training program by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.training_program_dto_envelope import TrainingProgramDtoEnvelope
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
    api_instance = openapi_client.TrainingProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    program_id = 'program_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get training program by ID
        api_response = api_instance.get_training_program_by_id_async(tenant_id, program_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramsApi->get_training_program_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramsApi->get_training_program_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **program_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TrainingProgramDtoEnvelope**](TrainingProgramDtoEnvelope.md)

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

# **get_training_programs_async**
> TrainingProgramDtoListEnvelope get_training_programs_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get training programs

Retrieves training programs for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.training_program_dto_list_envelope import TrainingProgramDtoListEnvelope
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
    api_instance = openapi_client.TrainingProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get training programs
        api_response = api_instance.get_training_programs_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramsApi->get_training_programs_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramsApi->get_training_programs_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**TrainingProgramDtoListEnvelope**](TrainingProgramDtoListEnvelope.md)

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

# **get_training_programs_count_async**
> Int32Envelope get_training_programs_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Count training programs

Counts training programs for the specified tenant.

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
    api_instance = openapi_client.TrainingProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Count training programs
        api_response = api_instance.get_training_programs_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of TrainingProgramsApi->get_training_programs_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramsApi->get_training_programs_count_async: %s\n" % e)
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

# **update_training_program_async**
> EmptyEnvelope update_training_program_async(tenant_id, program_id, api_version=api_version, x_api_version=x_api_version, training_program_update_dto=training_program_update_dto)

Update a training program

Updates an existing training program for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.training_program_update_dto import TrainingProgramUpdateDto
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
    api_instance = openapi_client.TrainingProgramsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    program_id = 'program_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    training_program_update_dto = openapi_client.TrainingProgramUpdateDto() # TrainingProgramUpdateDto |  (optional)

    try:
        # Update a training program
        api_response = api_instance.update_training_program_async(tenant_id, program_id, api_version=api_version, x_api_version=x_api_version, training_program_update_dto=training_program_update_dto)
        print("The response of TrainingProgramsApi->update_training_program_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingProgramsApi->update_training_program_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **program_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **training_program_update_dto** | [**TrainingProgramUpdateDto**](TrainingProgramUpdateDto.md)|  | [optional] 

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

