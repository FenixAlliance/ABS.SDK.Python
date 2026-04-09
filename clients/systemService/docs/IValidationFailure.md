# IValidationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**how_to_resolve** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.i_validation_failure import IValidationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of IValidationFailure from a JSON string
i_validation_failure_instance = IValidationFailure.from_json(json)
# print the JSON string representation of the object
print(IValidationFailure.to_json())

# convert the object into a dict
i_validation_failure_dict = i_validation_failure_instance.to_dict()
# create an instance of IValidationFailure from a dict
i_validation_failure_from_dict = IValidationFailure.from_dict(i_validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


