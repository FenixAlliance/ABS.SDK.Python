# openapi_client.UserOptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_system_user_option**](UserOptionsApi.md#create_system_user_option) | **POST** /api/v2/SystemService/Users/{userId}/Options | Create a new user option (admin)
[**delete_system_user_option**](UserOptionsApi.md#delete_system_user_option) | **DELETE** /api/v2/SystemService/Users/{userId}/Options/{optionId} | Delete a user option (admin)
[**get_system_user_option_by_id**](UserOptionsApi.md#get_system_user_option_by_id) | **GET** /api/v2/SystemService/Users/{userId}/Options/{optionId} | Retrieve a single user option by its ID (admin)
[**get_system_user_options**](UserOptionsApi.md#get_system_user_options) | **GET** /api/v2/SystemService/Users/{userId}/Options | Retrieve a list of user options (admin)
[**get_system_user_options_count**](UserOptionsApi.md#get_system_user_options_count) | **GET** /api/v2/SystemService/Users/{userId}/Options/Count | Get the count of user options (admin)
[**update_system_user_option**](UserOptionsApi.md#update_system_user_option) | **PUT** /api/v2/SystemService/Users/{userId}/Options/{optionId} | Update a user option (admin)


# **create_system_user_option**
> EmptyEnvelope create_system_user_option(user_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_create_dto=option_create_dto)

Create a new user option (admin)

Admin endpoint to create an option for any user

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
    api_instance = openapi_client.UserOptionsApi(api_client)
    user_id = 'user_id_example' # str | 
    key = 'key_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_create_dto = openapi_client.OptionCreateDto() # OptionCreateDto |  (optional)

    try:
        # Create a new user option (admin)
        api_response = api_instance.create_system_user_option(user_id, key, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version, option_create_dto=option_create_dto)
        print("The response of UserOptionsApi->create_system_user_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOptionsApi->create_system_user_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **delete_system_user_option**
> EmptyEnvelope delete_system_user_option(user_id, option_id, api_version=api_version, x_api_version=x_api_version)

Delete a user option (admin)

Admin endpoint to delete an option for any user

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
    api_instance = openapi_client.UserOptionsApi(api_client)
    user_id = 'user_id_example' # str | 
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a user option (admin)
        api_response = api_instance.delete_system_user_option(user_id, option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UserOptionsApi->delete_system_user_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOptionsApi->delete_system_user_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **get_system_user_option_by_id**
> OptionDtoEnvelope get_system_user_option_by_id(user_id, option_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a single user option by its ID (admin)

Admin endpoint to retrieve a single option for any user

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
    api_instance = openapi_client.UserOptionsApi(api_client)
    user_id = 'user_id_example' # str | 
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a single user option by its ID (admin)
        api_response = api_instance.get_system_user_option_by_id(user_id, option_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UserOptionsApi->get_system_user_option_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOptionsApi->get_system_user_option_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **get_system_user_options**
> OptionDtoListEnvelope get_system_user_options(user_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)

Retrieve a list of user options (admin)

Admin endpoint to retrieve options for any user

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
    api_instance = openapi_client.UserOptionsApi(api_client)
    user_id = 'user_id_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve a list of user options (admin)
        api_response = api_instance.get_system_user_options(user_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UserOptionsApi->get_system_user_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOptionsApi->get_system_user_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
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

# **get_system_user_options_count**
> Int32Envelope get_system_user_options_count(user_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)

Get the count of user options (admin)

Admin endpoint to get the count of options for any user

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
    api_instance = openapi_client.UserOptionsApi(api_client)
    user_id = 'user_id_example' # str | 
    portal_id = 'portal_id_example' # str |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get the count of user options (admin)
        api_response = api_instance.get_system_user_options_count(user_id, portal_id=portal_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of UserOptionsApi->get_system_user_options_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOptionsApi->get_system_user_options_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **portal_id** | **str**|  | [optional] 
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

# **update_system_user_option**
> EmptyEnvelope update_system_user_option(user_id, option_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)

Update a user option (admin)

Admin endpoint to update an option for any user

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
    api_instance = openapi_client.UserOptionsApi(api_client)
    user_id = 'user_id_example' # str | 
    option_id = 'option_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    option_update_dto = openapi_client.OptionUpdateDto() # OptionUpdateDto |  (optional)

    try:
        # Update a user option (admin)
        api_response = api_instance.update_system_user_option(user_id, option_id, api_version=api_version, x_api_version=x_api_version, option_update_dto=option_update_dto)
        print("The response of UserOptionsApi->update_system_user_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserOptionsApi->update_system_user_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

