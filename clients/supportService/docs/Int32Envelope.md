# Int32Envelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.int32_envelope import Int32Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of Int32Envelope from a JSON string
int32_envelope_instance = Int32Envelope.from_json(json)
# print the JSON string representation of the object
print(Int32Envelope.to_json())

# convert the object into a dict
int32_envelope_dict = int32_envelope_instance.to_dict()
# create an instance of Int32Envelope from a dict
int32_envelope_from_dict = Int32Envelope.from_dict(int32_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


