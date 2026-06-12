# HttpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_context** | [**HttpContext**](HttpContext.md) |  | [optional] 
**method** | **str** |  | [optional] 
**scheme** | **str** |  | [optional] 
**is_https** | **bool** |  | [optional] 
**host** | [**HostString**](HostString.md) |  | [optional] 
**path_base** | [**PathString**](PathString.md) |  | [optional] 
**path** | [**PathString**](PathString.md) |  | [optional] 
**query_string** | [**QueryString**](QueryString.md) |  | [optional] 
**query** | [**List[StringStringValuesKeyValuePair]**](StringStringValuesKeyValuePair.md) |  | [optional] 
**protocol** | **str** |  | [optional] 
**headers** | **Dict[str, List[str]]** |  | [optional] [readonly] 
**cookies** | [**List[StringStringKeyValuePair]**](StringStringKeyValuePair.md) |  | [optional] 
**content_length** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**body** | **bytearray** |  | [optional] 
**body_reader** | **bytearray** |  | [optional] [readonly] 
**has_form_content_type** | **bool** |  | [optional] [readonly] 
**form** | [**List[StringStringValuesKeyValuePair]**](StringStringValuesKeyValuePair.md) |  | [optional] 
**route_values** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.http_request import HttpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HttpRequest from a JSON string
http_request_instance = HttpRequest.from_json(json)
# print the JSON string representation of the object
print(HttpRequest.to_json())

# convert the object into a dict
http_request_dict = http_request_instance.to_dict()
# create an instance of HttpRequest from a dict
http_request_from_dict = HttpRequest.from_dict(http_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


