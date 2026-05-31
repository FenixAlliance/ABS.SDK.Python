# openapi_client.MigrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrate**](MigrationsApi.md#migrate) | **POST** /api/v2/SystemService/Migrations/Migrate | Apply pending database migrations
[**migrations**](MigrationsApi.md#migrations) | **GET** /api/v2/SystemService/Migrations | Retrieve database migrations


# **migrate**
> StringListEnvelope migrate(api_version=api_version, x_api_version=x_api_version)

Apply pending database migrations

Applies all pending database migrations and returns the list of migrations that were applied.

### Example


```python
import openapi_client
from openapi_client.models.string_list_envelope import StringListEnvelope
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
    api_instance = openapi_client.MigrationsApi(api_client)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Apply pending database migrations
        api_response = api_instance.migrate(api_version=api_version, x_api_version=x_api_version)
        print("The response of MigrationsApi->migrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**StringListEnvelope**](StringListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations**
> StringListEnvelope migrations(pending=pending, api_version=api_version, x_api_version=x_api_version)

Retrieve database migrations

Retrieves the list of applied or pending database migrations.

### Example


```python
import openapi_client
from openapi_client.models.string_list_envelope import StringListEnvelope
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
    api_instance = openapi_client.MigrationsApi(api_client)
    pending = True # bool |  (optional)
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Retrieve database migrations
        api_response = api_instance.migrations(pending=pending, api_version=api_version, x_api_version=x_api_version)
        print("The response of MigrationsApi->migrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending** | **bool**|  | [optional] 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**StringListEnvelope**](StringListEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

