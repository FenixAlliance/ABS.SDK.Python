# LicenseValidationErrorListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LicenseValidationError]**](LicenseValidationError.md) |  | [optional] 

## Example

```python
from openapi_client.models.license_validation_error_list_envelope import LicenseValidationErrorListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseValidationErrorListEnvelope from a JSON string
license_validation_error_list_envelope_instance = LicenseValidationErrorListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LicenseValidationErrorListEnvelope.to_json())

# convert the object into a dict
license_validation_error_list_envelope_dict = license_validation_error_list_envelope_instance.to_dict()
# create an instance of LicenseValidationErrorListEnvelope from a dict
license_validation_error_list_envelope_from_dict = LicenseValidationErrorListEnvelope.from_dict(license_validation_error_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


