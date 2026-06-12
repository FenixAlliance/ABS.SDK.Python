# openapi_client.ProofsOfDeliveryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_proof_of_delivery_line_async**](ProofsOfDeliveryApi.md#add_proof_of_delivery_line_async) | **POST** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Lines | Add a line to proof of delivery
[**attach_delivery_note_async**](ProofsOfDeliveryApi.md#attach_delivery_note_async) | **POST** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/DeliveryNotes/{noteId} | Attach a delivery note
[**create_proof_of_delivery_async**](ProofsOfDeliveryApi.md#create_proof_of_delivery_async) | **POST** /api/v2/LogisticsService/ProofsOfDelivery | Create a proof of delivery
[**delete_proof_of_delivery_async**](ProofsOfDeliveryApi.md#delete_proof_of_delivery_async) | **DELETE** /api/v2/LogisticsService/ProofsOfDelivery/{podId} | Delete a proof of delivery
[**detach_delivery_note_async**](ProofsOfDeliveryApi.md#detach_delivery_note_async) | **DELETE** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/DeliveryNotes/{noteId} | Detach a delivery note
[**dispute_proof_of_delivery_async**](ProofsOfDeliveryApi.md#dispute_proof_of_delivery_async) | **POST** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Dispute | Dispute a proof of delivery
[**get_proof_of_delivery_by_id_async**](ProofsOfDeliveryApi.md#get_proof_of_delivery_by_id_async) | **GET** /api/v2/LogisticsService/ProofsOfDelivery/{podId} | Get proof of delivery by ID
[**get_proof_of_delivery_delivery_notes_async**](ProofsOfDeliveryApi.md#get_proof_of_delivery_delivery_notes_async) | **GET** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/DeliveryNotes | Get attached delivery notes
[**get_proof_of_delivery_delivery_notes_count_async**](ProofsOfDeliveryApi.md#get_proof_of_delivery_delivery_notes_count_async) | **GET** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/DeliveryNotes/Count | Get delivery notes count
[**get_proof_of_delivery_lines_async**](ProofsOfDeliveryApi.md#get_proof_of_delivery_lines_async) | **GET** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Lines | Get proof of delivery lines
[**get_proof_of_delivery_lines_count_async**](ProofsOfDeliveryApi.md#get_proof_of_delivery_lines_count_async) | **GET** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Lines/Count | Get proof of delivery lines count
[**get_proofs_of_delivery_async**](ProofsOfDeliveryApi.md#get_proofs_of_delivery_async) | **GET** /api/v2/LogisticsService/ProofsOfDelivery | Get all proofs of delivery
[**get_proofs_of_delivery_count_async**](ProofsOfDeliveryApi.md#get_proofs_of_delivery_count_async) | **GET** /api/v2/LogisticsService/ProofsOfDelivery/Count | Get proofs of delivery count
[**patch_proof_of_delivery_async**](ProofsOfDeliveryApi.md#patch_proof_of_delivery_async) | **PATCH** /api/v2/LogisticsService/ProofsOfDelivery/{podId} | Patch a proof of delivery
[**patch_proof_of_delivery_line_async**](ProofsOfDeliveryApi.md#patch_proof_of_delivery_line_async) | **PATCH** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Lines/{lineId} | Patch a proof of delivery line
[**reject_proof_of_delivery_async**](ProofsOfDeliveryApi.md#reject_proof_of_delivery_async) | **POST** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Reject | Reject a proof of delivery
[**remove_proof_of_delivery_line_async**](ProofsOfDeliveryApi.md#remove_proof_of_delivery_line_async) | **DELETE** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Lines/{lineId} | Remove a proof of delivery line
[**sign_proof_of_delivery_async**](ProofsOfDeliveryApi.md#sign_proof_of_delivery_async) | **POST** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Sign | Sign a proof of delivery
[**update_proof_of_delivery_async**](ProofsOfDeliveryApi.md#update_proof_of_delivery_async) | **PUT** /api/v2/LogisticsService/ProofsOfDelivery/{podId} | Update a proof of delivery
[**update_proof_of_delivery_line_async**](ProofsOfDeliveryApi.md#update_proof_of_delivery_line_async) | **PUT** /api/v2/LogisticsService/ProofsOfDelivery/{podId}/Lines/{lineId} | Update a proof of delivery line


# **add_proof_of_delivery_line_async**
> EmptyEnvelope add_proof_of_delivery_line_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_line_create_dto=proof_of_delivery_line_create_dto)

Add a line to proof of delivery

Adds a new line to a proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.proof_of_delivery_line_create_dto import ProofOfDeliveryLineCreateDto
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    proof_of_delivery_line_create_dto = openapi_client.ProofOfDeliveryLineCreateDto() # ProofOfDeliveryLineCreateDto |  (optional)

    try:
        # Add a line to proof of delivery
        api_response = api_instance.add_proof_of_delivery_line_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_line_create_dto=proof_of_delivery_line_create_dto)
        print("The response of ProofsOfDeliveryApi->add_proof_of_delivery_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->add_proof_of_delivery_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **proof_of_delivery_line_create_dto** | [**ProofOfDeliveryLineCreateDto**](ProofOfDeliveryLineCreateDto.md)|  | [optional] 

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

# **attach_delivery_note_async**
> EmptyEnvelope attach_delivery_note_async(tenant_id, pod_id, note_id, api_version=api_version, x_api_version=x_api_version)

Attach a delivery note

Attaches a delivery note to a proof of delivery.

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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    note_id = 'note_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Attach a delivery note
        api_response = api_instance.attach_delivery_note_async(tenant_id, pod_id, note_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->attach_delivery_note_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->attach_delivery_note_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **note_id** | **str**|  | 
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
**400** | Bad Request |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proof_of_delivery_async**
> EmptyEnvelope create_proof_of_delivery_async(tenant_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_create_dto=proof_of_delivery_create_dto)

Create a proof of delivery

Creates a new proof of delivery for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.proof_of_delivery_create_dto import ProofOfDeliveryCreateDto
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    proof_of_delivery_create_dto = openapi_client.ProofOfDeliveryCreateDto() # ProofOfDeliveryCreateDto |  (optional)

    try:
        # Create a proof of delivery
        api_response = api_instance.create_proof_of_delivery_async(tenant_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_create_dto=proof_of_delivery_create_dto)
        print("The response of ProofsOfDeliveryApi->create_proof_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->create_proof_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **proof_of_delivery_create_dto** | [**ProofOfDeliveryCreateDto**](ProofOfDeliveryCreateDto.md)|  | [optional] 

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

# **delete_proof_of_delivery_async**
> EmptyEnvelope delete_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)

Delete a proof of delivery

Deletes a proof of delivery.

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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a proof of delivery
        api_response = api_instance.delete_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->delete_proof_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->delete_proof_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
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

# **detach_delivery_note_async**
> EmptyEnvelope detach_delivery_note_async(tenant_id, pod_id, note_id, api_version=api_version, x_api_version=x_api_version)

Detach a delivery note

Detaches a delivery note from a proof of delivery.

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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    note_id = 'note_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Detach a delivery note
        api_response = api_instance.detach_delivery_note_async(tenant_id, pod_id, note_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->detach_delivery_note_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->detach_delivery_note_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **note_id** | **str**|  | 
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

# **dispute_proof_of_delivery_async**
> EmptyEnvelope dispute_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, dispute_proof_of_delivery_request=dispute_proof_of_delivery_request)

Dispute a proof of delivery

Disputes a proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.dispute_proof_of_delivery_request import DisputeProofOfDeliveryRequest
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    dispute_proof_of_delivery_request = openapi_client.DisputeProofOfDeliveryRequest() # DisputeProofOfDeliveryRequest |  (optional)

    try:
        # Dispute a proof of delivery
        api_response = api_instance.dispute_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, dispute_proof_of_delivery_request=dispute_proof_of_delivery_request)
        print("The response of ProofsOfDeliveryApi->dispute_proof_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->dispute_proof_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **dispute_proof_of_delivery_request** | [**DisputeProofOfDeliveryRequest**](DisputeProofOfDeliveryRequest.md)|  | [optional] 

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

# **get_proof_of_delivery_by_id_async**
> ProofOfDeliveryDtoEnvelope get_proof_of_delivery_by_id_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)

Get proof of delivery by ID

Retrieves a specific proof of delivery by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.proof_of_delivery_dto_envelope import ProofOfDeliveryDtoEnvelope
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get proof of delivery by ID
        api_response = api_instance.get_proof_of_delivery_by_id_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->get_proof_of_delivery_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->get_proof_of_delivery_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProofOfDeliveryDtoEnvelope**](ProofOfDeliveryDtoEnvelope.md)

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

# **get_proof_of_delivery_delivery_notes_async**
> DeliveryNoteDtoListEnvelope get_proof_of_delivery_delivery_notes_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)

Get attached delivery notes

Retrieves all delivery notes attached to a proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.delivery_note_dto_list_envelope import DeliveryNoteDtoListEnvelope
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get attached delivery notes
        api_response = api_instance.get_proof_of_delivery_delivery_notes_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->get_proof_of_delivery_delivery_notes_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->get_proof_of_delivery_delivery_notes_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**DeliveryNoteDtoListEnvelope**](DeliveryNoteDtoListEnvelope.md)

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

# **get_proof_of_delivery_delivery_notes_count_async**
> Int32Envelope get_proof_of_delivery_delivery_notes_count_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)

Get delivery notes count

Returns the count of delivery notes attached to a proof of delivery.

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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get delivery notes count
        api_response = api_instance.get_proof_of_delivery_delivery_notes_count_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->get_proof_of_delivery_delivery_notes_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->get_proof_of_delivery_delivery_notes_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
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

# **get_proof_of_delivery_lines_async**
> ProofOfDeliveryLineDtoListEnvelope get_proof_of_delivery_lines_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)

Get proof of delivery lines

Retrieves all lines for a specific proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.proof_of_delivery_line_dto_list_envelope import ProofOfDeliveryLineDtoListEnvelope
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get proof of delivery lines
        api_response = api_instance.get_proof_of_delivery_lines_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->get_proof_of_delivery_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->get_proof_of_delivery_lines_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProofOfDeliveryLineDtoListEnvelope**](ProofOfDeliveryLineDtoListEnvelope.md)

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

# **get_proof_of_delivery_lines_count_async**
> Int32Envelope get_proof_of_delivery_lines_count_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)

Get proof of delivery lines count

Returns the count of lines for a specific proof of delivery.

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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get proof of delivery lines count
        api_response = api_instance.get_proof_of_delivery_lines_count_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->get_proof_of_delivery_lines_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->get_proof_of_delivery_lines_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
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

# **get_proofs_of_delivery_async**
> ProofOfDeliveryDtoListEnvelope get_proofs_of_delivery_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all proofs of delivery

Retrieves all proofs of delivery for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.proof_of_delivery_dto_list_envelope import ProofOfDeliveryDtoListEnvelope
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all proofs of delivery
        api_response = api_instance.get_proofs_of_delivery_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->get_proofs_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->get_proofs_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**ProofOfDeliveryDtoListEnvelope**](ProofOfDeliveryDtoListEnvelope.md)

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

# **get_proofs_of_delivery_count_async**
> Int32Envelope get_proofs_of_delivery_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get proofs of delivery count

Returns the count of proofs of delivery for the specified tenant.

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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get proofs of delivery count
        api_response = api_instance.get_proofs_of_delivery_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->get_proofs_of_delivery_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->get_proofs_of_delivery_count_async: %s\n" % e)
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

# **patch_proof_of_delivery_async**
> EmptyEnvelope patch_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a proof of delivery

Partially updates an existing proof of delivery using JSON Patch.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a proof of delivery
        api_response = api_instance.patch_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ProofsOfDeliveryApi->patch_proof_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->patch_proof_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_proof_of_delivery_line_async**
> EmptyEnvelope patch_proof_of_delivery_line_async(tenant_id, pod_id, line_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a proof of delivery line

Partially updates an existing proof of delivery line using JSON Patch.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a proof of delivery line
        api_response = api_instance.patch_proof_of_delivery_line_async(tenant_id, pod_id, line_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of ProofsOfDeliveryApi->patch_proof_of_delivery_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->patch_proof_of_delivery_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_proof_of_delivery_async**
> EmptyEnvelope reject_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, reject_proof_of_delivery_request=reject_proof_of_delivery_request)

Reject a proof of delivery

Rejects a proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.reject_proof_of_delivery_request import RejectProofOfDeliveryRequest
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    reject_proof_of_delivery_request = openapi_client.RejectProofOfDeliveryRequest() # RejectProofOfDeliveryRequest |  (optional)

    try:
        # Reject a proof of delivery
        api_response = api_instance.reject_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, reject_proof_of_delivery_request=reject_proof_of_delivery_request)
        print("The response of ProofsOfDeliveryApi->reject_proof_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->reject_proof_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **reject_proof_of_delivery_request** | [**RejectProofOfDeliveryRequest**](RejectProofOfDeliveryRequest.md)|  | [optional] 

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

# **remove_proof_of_delivery_line_async**
> EmptyEnvelope remove_proof_of_delivery_line_async(tenant_id, pod_id, line_id, api_version=api_version, x_api_version=x_api_version)

Remove a proof of delivery line

Removes a line from a proof of delivery.

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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a proof of delivery line
        api_response = api_instance.remove_proof_of_delivery_line_async(tenant_id, pod_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of ProofsOfDeliveryApi->remove_proof_of_delivery_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->remove_proof_of_delivery_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **line_id** | **str**|  | 
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

# **sign_proof_of_delivery_async**
> EmptyEnvelope sign_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, sign_proof_of_delivery_request=sign_proof_of_delivery_request)

Sign a proof of delivery

Signs a proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.sign_proof_of_delivery_request import SignProofOfDeliveryRequest
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    sign_proof_of_delivery_request = openapi_client.SignProofOfDeliveryRequest() # SignProofOfDeliveryRequest |  (optional)

    try:
        # Sign a proof of delivery
        api_response = api_instance.sign_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, sign_proof_of_delivery_request=sign_proof_of_delivery_request)
        print("The response of ProofsOfDeliveryApi->sign_proof_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->sign_proof_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **sign_proof_of_delivery_request** | [**SignProofOfDeliveryRequest**](SignProofOfDeliveryRequest.md)|  | [optional] 

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

# **update_proof_of_delivery_async**
> EmptyEnvelope update_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_update_dto=proof_of_delivery_update_dto)

Update a proof of delivery

Updates an existing proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.proof_of_delivery_update_dto import ProofOfDeliveryUpdateDto
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    proof_of_delivery_update_dto = openapi_client.ProofOfDeliveryUpdateDto() # ProofOfDeliveryUpdateDto |  (optional)

    try:
        # Update a proof of delivery
        api_response = api_instance.update_proof_of_delivery_async(tenant_id, pod_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_update_dto=proof_of_delivery_update_dto)
        print("The response of ProofsOfDeliveryApi->update_proof_of_delivery_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->update_proof_of_delivery_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **proof_of_delivery_update_dto** | [**ProofOfDeliveryUpdateDto**](ProofOfDeliveryUpdateDto.md)|  | [optional] 

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

# **update_proof_of_delivery_line_async**
> EmptyEnvelope update_proof_of_delivery_line_async(tenant_id, pod_id, line_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_line_update_dto=proof_of_delivery_line_update_dto)

Update a proof of delivery line

Updates an existing line on a proof of delivery.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.proof_of_delivery_line_update_dto import ProofOfDeliveryLineUpdateDto
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
    api_instance = openapi_client.ProofsOfDeliveryApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pod_id = 'pod_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    proof_of_delivery_line_update_dto = openapi_client.ProofOfDeliveryLineUpdateDto() # ProofOfDeliveryLineUpdateDto |  (optional)

    try:
        # Update a proof of delivery line
        api_response = api_instance.update_proof_of_delivery_line_async(tenant_id, pod_id, line_id, api_version=api_version, x_api_version=x_api_version, proof_of_delivery_line_update_dto=proof_of_delivery_line_update_dto)
        print("The response of ProofsOfDeliveryApi->update_proof_of_delivery_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofsOfDeliveryApi->update_proof_of_delivery_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pod_id** | **str**|  | 
 **line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **proof_of_delivery_line_update_dto** | [**ProofOfDeliveryLineUpdateDto**](ProofOfDeliveryLineUpdateDto.md)|  | [optional] 

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

