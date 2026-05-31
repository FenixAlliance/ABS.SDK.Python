# openapi_client.SeawayBillsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_seaway_bill_line_async**](SeawayBillsApi.md#add_seaway_bill_line_async) | **POST** /api/v2/LogisticsService/SeawayBills/{billId}/Lines | Add a line to seaway bill
[**cancel_seaway_bill_async**](SeawayBillsApi.md#cancel_seaway_bill_async) | **POST** /api/v2/LogisticsService/SeawayBills/{billId}/Cancel | Cancel a seaway bill
[**create_seaway_bill_async**](SeawayBillsApi.md#create_seaway_bill_async) | **POST** /api/v2/LogisticsService/SeawayBills | Create a seaway bill
[**delete_seaway_bill_async**](SeawayBillsApi.md#delete_seaway_bill_async) | **DELETE** /api/v2/LogisticsService/SeawayBills/{billId} | Delete a seaway bill
[**get_seaway_bill_by_id_async**](SeawayBillsApi.md#get_seaway_bill_by_id_async) | **GET** /api/v2/LogisticsService/SeawayBills/{billId} | Get seaway bill by ID
[**get_seaway_bill_lines_async**](SeawayBillsApi.md#get_seaway_bill_lines_async) | **GET** /api/v2/LogisticsService/SeawayBills/{billId}/Lines | Get seaway bill lines
[**get_seaway_bill_lines_count_async**](SeawayBillsApi.md#get_seaway_bill_lines_count_async) | **GET** /api/v2/LogisticsService/SeawayBills/{billId}/Lines/Count | Get seaway bill lines count
[**get_seaway_bills_async**](SeawayBillsApi.md#get_seaway_bills_async) | **GET** /api/v2/LogisticsService/SeawayBills | Get all seaway bills
[**get_seaway_bills_count_async**](SeawayBillsApi.md#get_seaway_bills_count_async) | **GET** /api/v2/LogisticsService/SeawayBills/Count | Get seaway bills count
[**issue_seaway_bill_async**](SeawayBillsApi.md#issue_seaway_bill_async) | **POST** /api/v2/LogisticsService/SeawayBills/{billId}/Issue | Issue a seaway bill
[**mark_seaway_bill_arrived_async**](SeawayBillsApi.md#mark_seaway_bill_arrived_async) | **POST** /api/v2/LogisticsService/SeawayBills/{billId}/MarkArrived | Mark seaway bill arrived
[**mark_seaway_bill_in_transit_async**](SeawayBillsApi.md#mark_seaway_bill_in_transit_async) | **POST** /api/v2/LogisticsService/SeawayBills/{billId}/MarkInTransit | Mark seaway bill in transit
[**release_seaway_bill_async**](SeawayBillsApi.md#release_seaway_bill_async) | **POST** /api/v2/LogisticsService/SeawayBills/{billId}/Release | Release a seaway bill
[**remove_seaway_bill_line_async**](SeawayBillsApi.md#remove_seaway_bill_line_async) | **DELETE** /api/v2/LogisticsService/SeawayBills/{billId}/Lines/{lineId} | Remove a seaway bill line
[**update_seaway_bill_async**](SeawayBillsApi.md#update_seaway_bill_async) | **PUT** /api/v2/LogisticsService/SeawayBills/{billId} | Update a seaway bill
[**update_seaway_bill_line_async**](SeawayBillsApi.md#update_seaway_bill_line_async) | **PUT** /api/v2/LogisticsService/SeawayBills/{billId}/Lines/{lineId} | Update a seaway bill line


# **add_seaway_bill_line_async**
> EmptyEnvelope add_seaway_bill_line_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)

Add a line to seaway bill

Adds a new line to a seaway bill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.waybill_line_create_dto import WaybillLineCreateDto
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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_create_dto = openapi_client.WaybillLineCreateDto() # WaybillLineCreateDto |  (optional)

    try:
        # Add a line to seaway bill
        api_response = api_instance.add_seaway_bill_line_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, waybill_line_create_dto=waybill_line_create_dto)
        print("The response of SeawayBillsApi->add_seaway_bill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->add_seaway_bill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **waybill_line_create_dto** | [**WaybillLineCreateDto**](WaybillLineCreateDto.md)|  | [optional] 

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

# **cancel_seaway_bill_async**
> EmptyEnvelope cancel_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Cancel a seaway bill

Cancels a seaway bill.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Cancel a seaway bill
        api_response = api_instance.cancel_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->cancel_seaway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->cancel_seaway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **create_seaway_bill_async**
> EmptyEnvelope create_seaway_bill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, seaway_bill_create_dto=seaway_bill_create_dto)

Create a seaway bill

Creates a new seaway bill for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.seaway_bill_create_dto import SeawayBillCreateDto
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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    seaway_bill_create_dto = openapi_client.SeawayBillCreateDto() # SeawayBillCreateDto |  (optional)

    try:
        # Create a seaway bill
        api_response = api_instance.create_seaway_bill_async(tenant_id, api_version=api_version, x_api_version=x_api_version, seaway_bill_create_dto=seaway_bill_create_dto)
        print("The response of SeawayBillsApi->create_seaway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->create_seaway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **seaway_bill_create_dto** | [**SeawayBillCreateDto**](SeawayBillCreateDto.md)|  | [optional] 

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

# **delete_seaway_bill_async**
> EmptyEnvelope delete_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Delete a seaway bill

Deletes a seaway bill.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a seaway bill
        api_response = api_instance.delete_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->delete_seaway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->delete_seaway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **get_seaway_bill_by_id_async**
> SeawayBillDtoEnvelope get_seaway_bill_by_id_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Get seaway bill by ID

Retrieves a specific seaway bill by its identifier.

### Example


```python
import openapi_client
from openapi_client.models.seaway_bill_dto_envelope import SeawayBillDtoEnvelope
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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get seaway bill by ID
        api_response = api_instance.get_seaway_bill_by_id_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->get_seaway_bill_by_id_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->get_seaway_bill_by_id_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SeawayBillDtoEnvelope**](SeawayBillDtoEnvelope.md)

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

# **get_seaway_bill_lines_async**
> WaybillLineDtoListEnvelope get_seaway_bill_lines_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Get seaway bill lines

Retrieves all lines for a specific seaway bill.

### Example


```python
import openapi_client
from openapi_client.models.waybill_line_dto_list_envelope import WaybillLineDtoListEnvelope
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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get seaway bill lines
        api_response = api_instance.get_seaway_bill_lines_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->get_seaway_bill_lines_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->get_seaway_bill_lines_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**WaybillLineDtoListEnvelope**](WaybillLineDtoListEnvelope.md)

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

# **get_seaway_bill_lines_count_async**
> Int32Envelope get_seaway_bill_lines_count_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Get seaway bill lines count

Returns the count of lines for a specific seaway bill.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get seaway bill lines count
        api_response = api_instance.get_seaway_bill_lines_count_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->get_seaway_bill_lines_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->get_seaway_bill_lines_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **get_seaway_bills_async**
> SeawayBillDtoListEnvelope get_seaway_bills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all seaway bills

Retrieves all seaway bills for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.seaway_bill_dto_list_envelope import SeawayBillDtoListEnvelope
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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all seaway bills
        api_response = api_instance.get_seaway_bills_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->get_seaway_bills_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->get_seaway_bills_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**SeawayBillDtoListEnvelope**](SeawayBillDtoListEnvelope.md)

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

# **get_seaway_bills_count_async**
> Int32Envelope get_seaway_bills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get seaway bills count

Returns the count of seaway bills for the specified tenant.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get seaway bills count
        api_response = api_instance.get_seaway_bills_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->get_seaway_bills_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->get_seaway_bills_count_async: %s\n" % e)
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

# **issue_seaway_bill_async**
> EmptyEnvelope issue_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Issue a seaway bill

Issues a seaway bill.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Issue a seaway bill
        api_response = api_instance.issue_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->issue_seaway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->issue_seaway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **mark_seaway_bill_arrived_async**
> EmptyEnvelope mark_seaway_bill_arrived_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Mark seaway bill arrived

Marks a seaway bill as arrived.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark seaway bill arrived
        api_response = api_instance.mark_seaway_bill_arrived_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->mark_seaway_bill_arrived_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->mark_seaway_bill_arrived_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **mark_seaway_bill_in_transit_async**
> EmptyEnvelope mark_seaway_bill_in_transit_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Mark seaway bill in transit

Marks a seaway bill as in transit.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Mark seaway bill in transit
        api_response = api_instance.mark_seaway_bill_in_transit_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->mark_seaway_bill_in_transit_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->mark_seaway_bill_in_transit_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **release_seaway_bill_async**
> EmptyEnvelope release_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)

Release a seaway bill

Releases a seaway bill.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Release a seaway bill
        api_response = api_instance.release_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->release_seaway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->release_seaway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **remove_seaway_bill_line_async**
> EmptyEnvelope remove_seaway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version)

Remove a seaway bill line

Removes a line from a seaway bill.

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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Remove a seaway bill line
        api_response = api_instance.remove_seaway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of SeawayBillsApi->remove_seaway_bill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->remove_seaway_bill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
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

# **update_seaway_bill_async**
> EmptyEnvelope update_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, seaway_bill_update_dto=seaway_bill_update_dto)

Update a seaway bill

Updates an existing seaway bill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.seaway_bill_update_dto import SeawayBillUpdateDto
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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    seaway_bill_update_dto = openapi_client.SeawayBillUpdateDto() # SeawayBillUpdateDto |  (optional)

    try:
        # Update a seaway bill
        api_response = api_instance.update_seaway_bill_async(tenant_id, bill_id, api_version=api_version, x_api_version=x_api_version, seaway_bill_update_dto=seaway_bill_update_dto)
        print("The response of SeawayBillsApi->update_seaway_bill_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->update_seaway_bill_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **seaway_bill_update_dto** | [**SeawayBillUpdateDto**](SeawayBillUpdateDto.md)|  | [optional] 

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

# **update_seaway_bill_line_async**
> EmptyEnvelope update_seaway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)

Update a seaway bill line

Updates an existing line on a seaway bill.

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.waybill_line_update_dto import WaybillLineUpdateDto
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
    api_instance = openapi_client.SeawayBillsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    bill_id = 'bill_id_example' # str | 
    line_id = 'line_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    waybill_line_update_dto = openapi_client.WaybillLineUpdateDto() # WaybillLineUpdateDto |  (optional)

    try:
        # Update a seaway bill line
        api_response = api_instance.update_seaway_bill_line_async(tenant_id, bill_id, line_id, api_version=api_version, x_api_version=x_api_version, waybill_line_update_dto=waybill_line_update_dto)
        print("The response of SeawayBillsApi->update_seaway_bill_line_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeawayBillsApi->update_seaway_bill_line_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **bill_id** | **str**|  | 
 **line_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **waybill_line_update_dto** | [**WaybillLineUpdateDto**](WaybillLineUpdateDto.md)|  | [optional] 

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

