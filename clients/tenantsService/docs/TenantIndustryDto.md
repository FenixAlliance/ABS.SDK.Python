# TenantIndustryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_business_industry_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_industry_dto import TenantIndustryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIndustryDto from a JSON string
tenant_industry_dto_instance = TenantIndustryDto.from_json(json)
# print the JSON string representation of the object
print(TenantIndustryDto.to_json())

# convert the object into a dict
tenant_industry_dto_dict = tenant_industry_dto_instance.to_dict()
# create an instance of TenantIndustryDto from a dict
tenant_industry_dto_from_dict = TenantIndustryDto.from_dict(tenant_industry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


