# ResponseStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**utc_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.response_status import ResponseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseStatus from a JSON string
response_status_instance = ResponseStatus.from_json(json)
# print the JSON string representation of the object
print(ResponseStatus.to_json())

# convert the object into a dict
response_status_dict = response_status_instance.to_dict()
# create an instance of ResponseStatus from a dict
response_status_from_dict = ResponseStatus.from_dict(response_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


