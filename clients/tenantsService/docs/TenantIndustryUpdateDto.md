# TenantIndustryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_business_industry_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_industry_update_dto import TenantIndustryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIndustryUpdateDto from a JSON string
tenant_industry_update_dto_instance = TenantIndustryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantIndustryUpdateDto.to_json())

# convert the object into a dict
tenant_industry_update_dto_dict = tenant_industry_update_dto_instance.to_dict()
# create an instance of TenantIndustryUpdateDto from a dict
tenant_industry_update_dto_from_dict = TenantIndustryUpdateDto.from_dict(tenant_industry_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


