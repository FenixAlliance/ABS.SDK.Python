# LicenseAttributesListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.license_attributes_list_envelope import LicenseAttributesListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseAttributesListEnvelope from a JSON string
license_attributes_list_envelope_instance = LicenseAttributesListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LicenseAttributesListEnvelope.to_json())

# convert the object into a dict
license_attributes_list_envelope_dict = license_attributes_list_envelope_instance.to_dict()
# create an instance of LicenseAttributesListEnvelope from a dict
license_attributes_list_envelope_from_dict = LicenseAttributesListEnvelope.from_dict(license_attributes_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


