# SuiteLicenseDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SuiteLicenseDto]**](SuiteLicenseDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.suite_license_dto_list_envelope import SuiteLicenseDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SuiteLicenseDtoListEnvelope from a JSON string
suite_license_dto_list_envelope_instance = SuiteLicenseDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SuiteLicenseDtoListEnvelope.to_json())

# convert the object into a dict
suite_license_dto_list_envelope_dict = suite_license_dto_list_envelope_instance.to_dict()
# create an instance of SuiteLicenseDtoListEnvelope from a dict
suite_license_dto_list_envelope_from_dict = SuiteLicenseDtoListEnvelope.from_dict(suite_license_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


