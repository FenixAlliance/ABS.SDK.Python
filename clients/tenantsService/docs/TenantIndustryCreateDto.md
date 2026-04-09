# TenantIndustryCreateDto


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
from openapi_client.models.tenant_industry_create_dto import TenantIndustryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantIndustryCreateDto from a JSON string
tenant_industry_create_dto_instance = TenantIndustryCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantIndustryCreateDto.to_json())

# convert the object into a dict
tenant_industry_create_dto_dict = tenant_industry_create_dto_instance.to_dict()
# create an instance of TenantIndustryCreateDto from a dict
tenant_industry_create_dto_from_dict = TenantIndustryCreateDto.from_dict(tenant_industry_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


