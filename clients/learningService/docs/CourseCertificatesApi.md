# openapi_client.CourseCertificatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_course_certificate_async**](CourseCertificatesApi.md#create_course_certificate_async) | **POST** /api/v2/LearningService/CourseCertificates | Create a course certificate
[**create_course_certificate_template_async**](CourseCertificatesApi.md#create_course_certificate_template_async) | **POST** /api/v2/LearningService/CourseCertificates/Template | Create a certificate template
[**delete_course_certificate_async**](CourseCertificatesApi.md#delete_course_certificate_async) | **DELETE** /api/v2/LearningService/CourseCertificates/{courseCertificateId} | Delete a course certificate
[**delete_course_certificate_template_async**](CourseCertificatesApi.md#delete_course_certificate_template_async) | **DELETE** /api/v2/LearningService/CourseCertificates/Template/{courseCertificateTemplateId} | Delete a certificate template
[**get_course_certificate_async**](CourseCertificatesApi.md#get_course_certificate_async) | **GET** /api/v2/LearningService/CourseCertificates/{courseCertificateId} | Get course certificate by ID
[**get_course_certificate_template_async**](CourseCertificatesApi.md#get_course_certificate_template_async) | **GET** /api/v2/LearningService/CourseCertificates/Template/{courseCertificateTemplateId} | Get certificate template by ID
[**get_course_certificate_templates_async**](CourseCertificatesApi.md#get_course_certificate_templates_async) | **GET** /api/v2/LearningService/CourseCertificates/Template | Get all certificate templates
[**get_course_certificates_async**](CourseCertificatesApi.md#get_course_certificates_async) | **GET** /api/v2/LearningService/CourseCertificates | Get all course certificates
[**get_course_certificates_count_async**](CourseCertificatesApi.md#get_course_certificates_count_async) | **GET** /api/v2/LearningService/CourseCertificates/Count | Get course certificates count
[**update_course_certificate_async**](CourseCertificatesApi.md#update_course_certificate_async) | **PUT** /api/v2/LearningService/CourseCertificates/{courseCertificateId} | Update a course certificate


# **create_course_certificate_async**
> create_course_certificate_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_completion_certificate_create_dto=course_completion_certificate_create_dto)

Create a course certificate

Creates a new course certificate for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_completion_certificate_create_dto import CourseCompletionCertificateCreateDto
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_completion_certificate_create_dto = openapi_client.CourseCompletionCertificateCreateDto() # CourseCompletionCertificateCreateDto |  (optional)

    try:
        # Create a course certificate
        api_instance.create_course_certificate_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_completion_certificate_create_dto=course_completion_certificate_create_dto)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->create_course_certificate_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_completion_certificate_create_dto** | [**CourseCompletionCertificateCreateDto**](CourseCompletionCertificateCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_course_certificate_template_async**
> create_course_certificate_template_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_certificate_template_create_dto=course_certificate_template_create_dto)

Create a certificate template

Creates a new course certificate template for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_certificate_template_create_dto import CourseCertificateTemplateCreateDto
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_certificate_template_create_dto = openapi_client.CourseCertificateTemplateCreateDto() # CourseCertificateTemplateCreateDto |  (optional)

    try:
        # Create a certificate template
        api_instance.create_course_certificate_template_async(tenant_id, api_version=api_version, x_api_version=x_api_version, course_certificate_template_create_dto=course_certificate_template_create_dto)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->create_course_certificate_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_certificate_template_create_dto** | [**CourseCertificateTemplateCreateDto**](CourseCertificateTemplateCreateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_certificate_async**
> delete_course_certificate_async(tenant_id, course_certificate_id, api_version=api_version, x_api_version=x_api_version)

Delete a course certificate

Deletes a course certificate for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_certificate_id = 'course_certificate_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a course certificate
        api_instance.delete_course_certificate_async(tenant_id, course_certificate_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->delete_course_certificate_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_certificate_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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

# **delete_course_certificate_template_async**
> delete_course_certificate_template_async(tenant_id, course_certificate_template_id, api_version=api_version, x_api_version=x_api_version)

Delete a certificate template

Deletes a course certificate template for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_certificate_template_id = 'course_certificate_template_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Delete a certificate template
        api_instance.delete_course_certificate_template_async(tenant_id, course_certificate_template_id, api_version=api_version, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->delete_course_certificate_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_certificate_template_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

void (empty response body)

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

# **get_course_certificate_async**
> CourseCompletionCertificateDto get_course_certificate_async(tenant_id, course_certificate_id, api_version=api_version, x_api_version=x_api_version)

Get course certificate by ID

Retrieves a specific course certificate by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_completion_certificate_dto import CourseCompletionCertificateDto
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_certificate_id = 'course_certificate_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course certificate by ID
        api_response = api_instance.get_course_certificate_async(tenant_id, course_certificate_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCertificatesApi->get_course_certificate_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->get_course_certificate_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_certificate_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseCompletionCertificateDto**](CourseCompletionCertificateDto.md)

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

# **get_course_certificate_template_async**
> CourseCertificateTemplateDto get_course_certificate_template_async(tenant_id, course_certificate_template_id, api_version=api_version, x_api_version=x_api_version)

Get certificate template by ID

Retrieves a specific course certificate template by its ID.

### Example


```python
import openapi_client
from openapi_client.models.course_certificate_template_dto import CourseCertificateTemplateDto
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_certificate_template_id = 'course_certificate_template_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get certificate template by ID
        api_response = api_instance.get_course_certificate_template_async(tenant_id, course_certificate_template_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCertificatesApi->get_course_certificate_template_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->get_course_certificate_template_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_certificate_template_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**CourseCertificateTemplateDto**](CourseCertificateTemplateDto.md)

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

# **get_course_certificate_templates_async**
> List[CourseCertificateTemplateDto] get_course_certificate_templates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all certificate templates

Retrieves all course certificate templates for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_certificate_template_dto import CourseCertificateTemplateDto
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all certificate templates
        api_response = api_instance.get_course_certificate_templates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCertificatesApi->get_course_certificate_templates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->get_course_certificate_templates_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseCertificateTemplateDto]**](CourseCertificateTemplateDto.md)

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

# **get_course_certificates_async**
> List[CourseCompletionCertificateDto] get_course_certificates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get all course certificates

Retrieves all course certificates for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_completion_certificate_dto import CourseCompletionCertificateDto
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get all course certificates
        api_response = api_instance.get_course_certificates_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCertificatesApi->get_course_certificates_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->get_course_certificates_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

[**List[CourseCompletionCertificateDto]**](CourseCompletionCertificateDto.md)

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

# **get_course_certificates_count_async**
> int get_course_certificates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)

Get course certificates count

Returns the count of course certificates for the specified tenant.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get course certificates count
        api_response = api_instance.get_course_certificates_count_async(tenant_id, api_version=api_version, x_api_version=x_api_version)
        print("The response of CourseCertificatesApi->get_course_certificates_count_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->get_course_certificates_count_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 

### Return type

**int**

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

# **update_course_certificate_async**
> update_course_certificate_async(tenant_id, course_certificate_id, api_version=api_version, x_api_version=x_api_version, course_completion_certificate_update_dto=course_completion_certificate_update_dto)

Update a course certificate

Updates an existing course certificate for the specified tenant.

### Example


```python
import openapi_client
from openapi_client.models.course_completion_certificate_update_dto import CourseCompletionCertificateUpdateDto
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
    api_instance = openapi_client.CourseCertificatesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    course_certificate_id = 'course_certificate_id_example' # str | 
    api_version = 'api_version_example' # str |  (optional)
    x_api_version = 'x_api_version_example' # str |  (optional)
    course_completion_certificate_update_dto = openapi_client.CourseCompletionCertificateUpdateDto() # CourseCompletionCertificateUpdateDto |  (optional)

    try:
        # Update a course certificate
        api_instance.update_course_certificate_async(tenant_id, course_certificate_id, api_version=api_version, x_api_version=x_api_version, course_completion_certificate_update_dto=course_completion_certificate_update_dto)
    except Exception as e:
        print("Exception when calling CourseCertificatesApi->update_course_certificate_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **course_certificate_id** | **str**|  | 
 **api_version** | **str**|  | [optional] 
 **x_api_version** | **str**|  | [optional] 
 **course_completion_certificate_update_dto** | [**CourseCompletionCertificateUpdateDto**](CourseCompletionCertificateUpdateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

