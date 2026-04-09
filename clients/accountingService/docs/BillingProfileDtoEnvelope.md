# BillingProfileDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BillingProfileDto**](BillingProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.billing_profile_dto_envelope import BillingProfileDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileDtoEnvelope from a JSON string
billing_profile_dto_envelope_instance = BillingProfileDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BillingProfileDtoEnvelope.to_json())

# convert the object into a dict
billing_profile_dto_envelope_dict = billing_profile_dto_envelope_instance.to_dict()
# create an instance of BillingProfileDtoEnvelope from a dict
billing_profile_dto_envelope_from_dict = BillingProfileDtoEnvelope.from_dict(billing_profile_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


