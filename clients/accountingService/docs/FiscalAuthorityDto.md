# FiscalAuthorityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_authority_dto import FiscalAuthorityDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalAuthorityDto from a JSON string
fiscal_authority_dto_instance = FiscalAuthorityDto.from_json(json)
# print the JSON string representation of the object
print(FiscalAuthorityDto.to_json())

# convert the object into a dict
fiscal_authority_dto_dict = fiscal_authority_dto_instance.to_dict()
# create an instance of FiscalAuthorityDto from a dict
fiscal_authority_dto_from_dict = FiscalAuthorityDto.from_dict(fiscal_authority_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


