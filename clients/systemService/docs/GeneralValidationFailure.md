# GeneralValidationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**how_to_resolve** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.general_validation_failure import GeneralValidationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralValidationFailure from a JSON string
general_validation_failure_instance = GeneralValidationFailure.from_json(json)
# print the JSON string representation of the object
print(GeneralValidationFailure.to_json())

# convert the object into a dict
general_validation_failure_dict = general_validation_failure_instance.to_dict()
# create an instance of GeneralValidationFailure from a dict
general_validation_failure_from_dict = GeneralValidationFailure.from_dict(general_validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


