# openapi_client.OptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_system_option**](OptionsApi.md#create_system_option) | **POST** /api/v2/SystemService/Options | Create a new system option
[**delete_system_option**](OptionsApi.md#delete_system_option) | **DELETE** /api/v2/SystemService/Options/{optionId} | Delete a system option
[**get_system_option_by_id**](OptionsApi.md#get_system_option_by_id) | **GET** /api/v2/SystemService/Options/{optionId} | Retrieve a single system option by its ID
[**get_system_option_by_key**](OptionsApi.md#get_system_option_by_key) | **GET** /api/v2/SystemService/Options/Key/{key} | Retrieve a single system option by its key
[**get_system_options**](OptionsApi.md#get_system_options) | **GET** /api/v2/SystemService/Options | Retrieve a list of system options
[**get_system_options_count**](OptionsApi.md#get_system_options_count) | **GET** /api/v2/SystemService/Options/Count | Get the count of system options
[**update_system_option**](OptionsApi.md#update_system_option) | **PUT** /api/v2/SystemService/Options/{optionId} | Update a system option
[**upsert_system_option**](OptionsApi.md#upsert_system_option) | **PUT** /api/v2/SystemService/Options/Upsert/{key} | Create or update a system option by key


# **create_system_option**
> EmptyEnvelope create_system_option(key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_create_dto=option_create_dto)

Create a new system option

Create a new system option

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.option_create_dto import OptionCreateDto
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
    api_instance = openapi_client.OptionsApi(api_client)
    key = 'key_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_create_dto = openapi_client.OptionCreateDto() # OptionCreateDto |  (optional)

    try:
        # Create a new system option
        api_response = api_instance.create_system_option(key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_create_dto=option_create_dto)
        print("The response of OptionsApi->create_system_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->create_system_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **option_create_dto** | [**OptionCreateDto**](OptionCreateDto.md)|  | [optional] 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_option**
> EmptyEnvelope delete_system_option(option_id, api_version=api_version, x_api_version=x_api_version)

Delete a system option

Delete a system option

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
    api_instance = openapi_client.OptionsApi(api_client)
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a system option
        api_response = api_instance.delete_system_option(option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->delete_system_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->delete_system_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_option_by_id**
> OptionDtoEnvelope get_system_option_by_id(option_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single system option by its ID

Retrieve a single system option by its ID

### Example


```python
import openapi_client
from openapi_client.models.option_dto_envelope import OptionDtoEnvelope
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
    api_instance = openapi_client.OptionsApi(api_client)
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single system option by its ID
        api_response = api_instance.get_system_option_by_id(option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_system_option_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_system_option_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OptionDtoEnvelope**](OptionDtoEnvelope.md)

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

# **get_system_option_by_key**
> OptionDtoEnvelope get_system_option_by_key(portal_id, key, api_version=api_version, x_api_version=x_api_version)

Retrieve a single system option by its key

Retrieve a single system option by its key

### Example


```python
import openapi_client
from openapi_client.models.option_dto_envelope import OptionDtoEnvelope
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
    api_instance = openapi_client.OptionsApi(api_client)
    portal_id = 'portal_id_example' # str | 
    key = 'key_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single system option by its key
        api_response = api_instance.get_system_option_by_key(portal_id, key, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_system_option_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_system_option_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
 **key** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OptionDtoEnvelope**](OptionDtoEnvelope.md)

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

# **get_system_options**
> OptionDtoListEnvelope get_system_options(portal_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of system options

Retrieve a list of system options for a portal

### Example


```python
import openapi_client
from openapi_client.models.option_dto_list_envelope import OptionDtoListEnvelope
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
    api_instance = openapi_client.OptionsApi(api_client)
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of system options
        api_response = api_instance.get_system_options(portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_system_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_system_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**OptionDtoListEnvelope**](OptionDtoListEnvelope.md)

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

# **get_system_options_count**
> Int32Envelope get_system_options_count(portal_id, api_version=api_version, x_api_version=x_api_version)

Get the count of system options

Get the count of system options for a portal

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
    api_instance = openapi_client.OptionsApi(api_client)
    portal_id = 'portal_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of system options
        api_response = api_instance.get_system_options_count(portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of OptionsApi->get_system_options_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->get_system_options_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **str**|  | 
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

# **update_system_option**
> EmptyEnvelope update_system_option(option_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)

Update a system option

Update a system option

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.option_update_dto import OptionUpdateDto
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
    api_instance = openapi_client.OptionsApi(api_client)
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_update_dto = openapi_client.OptionUpdateDto() # OptionUpdateDto |  (optional)

    try:
        # Update a system option
        api_response = api_instance.update_system_option(option_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)
        print("The response of OptionsApi->update_system_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->update_system_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **option_update_dto** | [**OptionUpdateDto**](OptionUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_system_option**
> EmptyEnvelope upsert_system_option(key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)

Create or update a system option by key

Create or update a system option by key

### Example


```python
import openapi_client
from openapi_client.models.empty_envelope import EmptyEnvelope
from openapi_client.models.option_update_dto import OptionUpdateDto
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
    api_instance = openapi_client.OptionsApi(api_client)
    key = 'key_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_update_dto = openapi_client.OptionUpdateDto() # OptionUpdateDto |  (optional)

    try:
        # Create or update a system option by key
        api_response = api_instance.upsert_system_option(key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)
        print("The response of OptionsApi->upsert_system_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptionsApi->upsert_system_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **option_update_dto** | [**OptionUpdateDto**](OptionUpdateDto.md)|  | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

