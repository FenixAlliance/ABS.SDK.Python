# openapi_client.BillsOfLadingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bill_of_lading_async**](BillsOfLadingApi.md#create_bill_of_lading_async) | **POST** /api/v2/ShipmentsService/BillsOfLading | Create a bill of lading
[**create_bill_of_lading_line_async**](BillsOfLadingApi.md#create_bill_of_lading_line_async) | **POST** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId}/Lines | Create a bill of lading line
[**delete_bill_of_lading_async**](BillsOfLadingApi.md#delete_bill_of_lading_async) | **DELETE** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId} | Delete a bill of lading
[**delete_bill_of_lading_line_async**](BillsOfLadingApi.md#delete_bill_of_lading_line_async) | **DELETE** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId}/Lines/{lineId} | Delete a bill of lading line
[**get_bill_of_lading_by_id_async**](BillsOfLadingApi.md#get_bill_of_lading_by_id_async) | **GET** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId} | Get bill of lading by ID
[**get_bill_of_lading_line_by_id_async**](BillsOfLadingApi.md#get_bill_of_lading_line_by_id_async) | **GET** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId}/Lines/{lineId} | Get bill of lading line by ID
[**get_bill_of_lading_lines_async**](BillsOfLadingApi.md#get_bill_of_lading_lines_async) | **GET** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId}/Lines | Get bill of lading lines
[**get_bill_of_lading_lines_count_async**](BillsOfLadingApi.md#get_bill_of_lading_lines_count_async) | **GET** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId}/Lines/Count | Get bill of lading lines count
[**get_bills_of_lading_async**](BillsOfLadingApi.md#get_bills_of_lading_async) | **GET** /api/v2/ShipmentsService/BillsOfLading | Get all bills of lading
[**get_bills_of_lading_count_async**](BillsOfLadingApi.md#get_bills_of_lading_count_async) | **GET** /api/v2/ShipmentsService/BillsOfLading/Count | Get bills of lading count
[**patch_bill_of_lading_async**](BillsOfLadingApi.md#patch_bill_of_lading_async) | **PATCH** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId} | Patch a bill of lading
[**patch_bill_of_lading_line_async**](BillsOfLadingApi.md#patch_bill_of_lading_line_async) | **PATCH** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId}/Lines/{lineId} | Patch a bill of lading line
[**update_bill_of_lading_async**](BillsOfLadingApi.md#update_bill_of_lading_async) | **PUT** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId} | Update a bill of lading
[**update_bill_of_lading_line_async**](BillsOfLadingApi.md#update_bill_of_lading_line_async) | **PUT** /api/v2/ShipmentsService/BillsOfLading/{billOfLadingId}/Lines/{lineId} | Update a bill of lading line


# **create_bill_of_lading_async**
> EmptyEnvelope create_bill_of_lading_async(tenant_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_create_dto=bill_of_lading_create_dto)

Create a bill of lading

Creates a new bill of lading for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_create_dto import BillOfLadingCreateDto
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bill_of_lading_create_dto = openapi_client.BillOfLadingCreateDto() # BillOfLadingCreateDto |  (optional)

    try:
        # Create a bill of lading
        api_response = api_instance.create_bill_of_lading_async(tenant_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_create_dto=bill_of_lading_create_dto)
        print("The response of BillsOfLadingApi->create_bill_of_lading_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->create_bill_of_lading_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bill_of_lading_create_dto** | [**BillOfLadingCreateDto**](BillOfLadingCreateDto.md)|  | [optional] 

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

# **create_bill_of_lading_line_async**
> EmptyEnvelope create_bill_of_lading_line_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_line_create_dto=bill_of_lading_line_create_dto)

Create a bill of lading line

Creates a new line for a bill of lading.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_line_create_dto import BillOfLadingLineCreateDto
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bill_of_lading_line_create_dto = openapi_client.BillOfLadingLineCreateDto() # BillOfLadingLineCreateDto |  (optional)

    try:
        # Create a bill of lading line
        api_response = api_instance.create_bill_of_lading_line_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_line_create_dto=bill_of_lading_line_create_dto)
        print("The response of BillsOfLadingApi->create_bill_of_lading_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->create_bill_of_lading_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bill_of_lading_line_create_dto** | [**BillOfLadingLineCreateDto**](BillOfLadingLineCreateDto.md)|  | [optional] 

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

# **delete_bill_of_lading_async**
> EmptyEnvelope delete_bill_of_lading_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)

Delete a bill of lading

Deletes a bill of lading.

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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a bill of lading
        api_response = api_instance.delete_bill_of_lading_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->delete_bill_of_lading_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->delete_bill_of_lading_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
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

# **delete_bill_of_lading_line_async**
> EmptyEnvelope delete_bill_of_lading_line_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version)

Delete a bill of lading line

Deletes a line from a bill of lading.

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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a bill of lading line
        api_response = api_instance.delete_bill_of_lading_line_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->delete_bill_of_lading_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->delete_bill_of_lading_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
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

# **get_bill_of_lading_by_id_async**
> BillOfLadingDtoEnvelope get_bill_of_lading_by_id_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)

Get bill of lading by ID

Retrieves a specific bill of lading by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_dto_envelope import BillOfLadingDtoEnvelope
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get bill of lading by ID
        api_response = api_instance.get_bill_of_lading_by_id_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->get_bill_of_lading_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->get_bill_of_lading_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BillOfLadingDtoEnvelope**](BillOfLadingDtoEnvelope.md)

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

# **get_bill_of_lading_line_by_id_async**
> BillOfLadingLineDtoEnvelope get_bill_of_lading_line_by_id_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version)

Get bill of lading line by ID

Retrieves a specific line from a bill of lading.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_line_dto_envelope import BillOfLadingLineDtoEnvelope
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get bill of lading line by ID
        api_response = api_instance.get_bill_of_lading_line_by_id_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->get_bill_of_lading_line_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->get_bill_of_lading_line_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
 **line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BillOfLadingLineDtoEnvelope**](BillOfLadingLineDtoEnvelope.md)

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

# **get_bill_of_lading_lines_async**
> BillOfLadingLineDtoListEnvelope get_bill_of_lading_lines_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)

Get bill of lading lines

Retrieves all lines for a specific bill of lading.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_line_dto_list_envelope import BillOfLadingLineDtoListEnvelope
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get bill of lading lines
        api_response = api_instance.get_bill_of_lading_lines_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->get_bill_of_lading_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->get_bill_of_lading_lines_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BillOfLadingLineDtoListEnvelope**](BillOfLadingLineDtoListEnvelope.md)

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

# **get_bill_of_lading_lines_count_async**
> Int32Envelope get_bill_of_lading_lines_count_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)

Get bill of lading lines count

Returns the count of lines for a specific bill of lading.

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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get bill of lading lines count
        api_response = api_instance.get_bill_of_lading_lines_count_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->get_bill_of_lading_lines_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->get_bill_of_lading_lines_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
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

# **get_bills_of_lading_async**
> BillOfLadingDtoListEnvelope get_bills_of_lading_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all bills of lading

Retrieves all bills of lading for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_dto_list_envelope import BillOfLadingDtoListEnvelope
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all bills of lading
        api_response = api_instance.get_bills_of_lading_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->get_bills_of_lading_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->get_bills_of_lading_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**BillOfLadingDtoListEnvelope**](BillOfLadingDtoListEnvelope.md)

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

# **get_bills_of_lading_count_async**
> Int32Envelope get_bills_of_lading_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get bills of lading count

Returns the count of bills of lading for the specified tenant.

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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get bills of lading count
        api_response = api_instance.get_bills_of_lading_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of BillsOfLadingApi->get_bills_of_lading_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->get_bills_of_lading_count_async: %s\n" % e)
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

# **patch_bill_of_lading_async**
> EmptyEnvelope patch_bill_of_lading_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a bill of lading

Partially updates an existing bill of lading using JSON Patch.

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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a bill of lading
        api_response = api_instance.patch_bill_of_lading_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of BillsOfLadingApi->patch_bill_of_lading_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->patch_bill_of_lading_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
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

# **patch_bill_of_lading_line_async**
> EmptyEnvelope patch_bill_of_lading_line_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version, operation=operation)

Patch a bill of lading line

Partially updates an existing line on a bill of lading using JSON Patch.

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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    operation = [openapi_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch a bill of lading line
        api_response = api_instance.patch_bill_of_lading_line_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version, operation=operation)
        print("The response of BillsOfLadingApi->patch_bill_of_lading_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->patch_bill_of_lading_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
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

# **update_bill_of_lading_async**
> EmptyEnvelope update_bill_of_lading_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_update_dto=bill_of_lading_update_dto)

Update a bill of lading

Updates an existing bill of lading.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_update_dto import BillOfLadingUpdateDto
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bill_of_lading_update_dto = openapi_client.BillOfLadingUpdateDto() # BillOfLadingUpdateDto |  (optional)

    try:
        # Update a bill of lading
        api_response = api_instance.update_bill_of_lading_async(tenant_id, bill_of_lading_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_update_dto=bill_of_lading_update_dto)
        print("The response of BillsOfLadingApi->update_bill_of_lading_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->update_bill_of_lading_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bill_of_lading_update_dto** | [**BillOfLadingUpdateDto**](BillOfLadingUpdateDto.md)|  | [optional] 

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

# **update_bill_of_lading_line_async**
> EmptyEnvelope update_bill_of_lading_line_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_line_update_dto=bill_of_lading_line_update_dto)

Update a bill of lading line

Updates an existing line on a bill of lading.

### Example


```python
import openapi_client
from openapi_client.models.bill_of_lading_line_update_dto import BillOfLadingLineUpdateDto
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
    api_instance = openapi_client.BillsOfLadingApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_of_lading_id = 'bill_of_lading_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    bill_of_lading_line_update_dto = openapi_client.BillOfLadingLineUpdateDto() # BillOfLadingLineUpdateDto |  (optional)

    try:
        # Update a bill of lading line
        api_response = api_instance.update_bill_of_lading_line_async(tenant_id, bill_of_lading_id, line_id, api_version=api_version, x_api_version=x_api_version, bill_of_lading_line_update_dto=bill_of_lading_line_update_dto)
        print("The response of BillsOfLadingApi->update_bill_of_lading_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillsOfLadingApi->update_bill_of_lading_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_of_lading_id** | **str**|  | 
 **line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **bill_of_lading_line_update_dto** | [**BillOfLadingLineUpdateDto**](BillOfLadingLineUpdateDto.md)|  | [optional] 

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

