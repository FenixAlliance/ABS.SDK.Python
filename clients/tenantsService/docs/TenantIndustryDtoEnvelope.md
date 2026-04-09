# TenantIndustryDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TenantIndustryDto**](TenantIndustryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_industry_dto_envelope import TenantIndustryDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIndustryDtoEnvelope from a JSON string
tenant_industry_dto_envelope_instance = TenantIndustryDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantIndustryDtoEnvelope.to_json())

# convert the object into a dict
tenant_industry_dto_envelope_dict = tenant_industry_dto_envelope_instance.to_dict()
# create an instance of TenantIndustryDtoEnvelope from a dict
tenant_industry_dto_envelope_from_dict = TenantIndustryDtoEnvelope.from_dict(tenant_industry_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


