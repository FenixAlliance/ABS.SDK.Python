# IValidationFailureListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[IValidationFailure]**](IValidationFailure.md) |  | [optional] 

## Example

```python
from openapi_client.models.i_validation_failure_list_envelope import IValidationFailureListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of IValidationFailureListEnvelope from a JSON string
i_validation_failure_list_envelope_instance = IValidationFailureListEnvelope.from_json(json)
# print the JSON string representation of the object
print(IValidationFailureListEnvelope.to_json())

# convert the object into a dict
i_validation_failure_list_envelope_dict = i_validation_failure_list_envelope_instance.to_dict()
# create an instance of IValidationFailureListEnvelope from a dict
i_validation_failure_list_envelope_from_dict = IValidationFailureListEnvelope.from_dict(i_validation_failure_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


