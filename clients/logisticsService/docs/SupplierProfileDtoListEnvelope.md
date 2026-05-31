# SupplierProfileDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SupplierProfileDto]**](SupplierProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.supplier_profile_dto_list_envelope import SupplierProfileDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierProfileDtoListEnvelope from a JSON string
supplier_profile_dto_list_envelope_instance = SupplierProfileDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupplierProfileDtoListEnvelope.to_json())

# convert the object into a dict
supplier_profile_dto_list_envelope_dict = supplier_profile_dto_list_envelope_instance.to_dict()
# create an instance of SupplierProfileDtoListEnvelope from a dict
supplier_profile_dto_list_envelope_from_dict = SupplierProfileDtoListEnvelope.from_dict(supplier_profile_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


