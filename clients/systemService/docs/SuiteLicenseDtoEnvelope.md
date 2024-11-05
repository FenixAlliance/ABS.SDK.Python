# SuiteLicenseDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SuiteLicenseDto**](SuiteLicenseDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.suite_license_dto_envelope import SuiteLicenseDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SuiteLicenseDtoEnvelope from a JSON string
suite_license_dto_envelope_instance = SuiteLicenseDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SuiteLicenseDtoEnvelope.to_json())

# convert the object into a dict
suite_license_dto_envelope_dict = suite_license_dto_envelope_instance.to_dict()
# create an instance of SuiteLicenseDtoEnvelope from a dict
suite_license_dto_envelope_from_dict = SuiteLicenseDtoEnvelope.from_dict(suite_license_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


