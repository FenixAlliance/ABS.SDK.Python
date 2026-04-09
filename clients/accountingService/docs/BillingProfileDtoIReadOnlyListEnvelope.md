# BillingProfileDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BillingProfileDto]**](BillingProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.billing_profile_dto_i_read_only_list_envelope import BillingProfileDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileDtoIReadOnlyListEnvelope from a JSON string
billing_profile_dto_i_read_only_list_envelope_instance = BillingProfileDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BillingProfileDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
billing_profile_dto_i_read_only_list_envelope_dict = billing_profile_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of BillingProfileDtoIReadOnlyListEnvelope from a dict
billing_profile_dto_i_read_only_list_envelope_from_dict = BillingProfileDtoIReadOnlyListEnvelope.from_dict(billing_profile_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


