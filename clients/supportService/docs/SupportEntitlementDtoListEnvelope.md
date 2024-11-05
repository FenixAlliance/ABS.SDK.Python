# SupportEntitlementDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SupportEntitlementDto]**](SupportEntitlementDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.support_entitlement_dto_list_envelope import SupportEntitlementDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupportEntitlementDtoListEnvelope from a JSON string
support_entitlement_dto_list_envelope_instance = SupportEntitlementDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupportEntitlementDtoListEnvelope.to_json())

# convert the object into a dict
support_entitlement_dto_list_envelope_dict = support_entitlement_dto_list_envelope_instance.to_dict()
# create an instance of SupportEntitlementDtoListEnvelope from a dict
support_entitlement_dto_list_envelope_from_dict = SupportEntitlementDtoListEnvelope.from_dict(support_entitlement_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


