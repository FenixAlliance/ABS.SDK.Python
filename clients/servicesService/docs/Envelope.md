# Envelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.envelope import Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of Envelope from a JSON string
envelope_instance = Envelope.from_json(json)
# print the JSON string representation of the object
print(Envelope.to_json())

# convert the object into a dict
envelope_dict = envelope_instance.to_dict()
# create an instance of Envelope from a dict
envelope_from_dict = Envelope.from_dict(envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


