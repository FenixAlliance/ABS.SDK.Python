# LicenseValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**how_to_resolve** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.license_validation_error import LicenseValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseValidationError from a JSON string
license_validation_error_instance = LicenseValidationError.from_json(json)
# print the JSON string representation of the object
print(LicenseValidationError.to_json())

# convert the object into a dict
license_validation_error_dict = license_validation_error_instance.to_dict()
# create an instance of LicenseValidationError from a dict
license_validation_error_from_dict = LicenseValidationError.from_dict(license_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


