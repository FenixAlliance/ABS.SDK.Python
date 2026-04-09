# InfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_email** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.info_request import InfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InfoRequest from a JSON string
info_request_instance = InfoRequest.from_json(json)
# print the JSON string representation of the object
print(InfoRequest.to_json())

# convert the object into a dict
info_request_dict = info_request_instance.to_dict()
# create an instance of InfoRequest from a dict
info_request_from_dict = InfoRequest.from_dict(info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


