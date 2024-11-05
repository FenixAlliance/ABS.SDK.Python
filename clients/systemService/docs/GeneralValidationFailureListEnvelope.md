# GeneralValidationFailureListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[GeneralValidationFailure]**](GeneralValidationFailure.md) |  | [optional] 

## Example

```python
from openapi_client.models.general_validation_failure_list_envelope import GeneralValidationFailureListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralValidationFailureListEnvelope from a JSON string
general_validation_failure_list_envelope_instance = GeneralValidationFailureListEnvelope.from_json(json)
# print the JSON string representation of the object
print(GeneralValidationFailureListEnvelope.to_json())

# convert the object into a dict
general_validation_failure_list_envelope_dict = general_validation_failure_list_envelope_instance.to_dict()
# create an instance of GeneralValidationFailureListEnvelope from a dict
general_validation_failure_list_envelope_from_dict = GeneralValidationFailureListEnvelope.from_dict(general_validation_failure_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


