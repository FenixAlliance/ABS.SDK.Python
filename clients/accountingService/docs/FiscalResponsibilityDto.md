# FiscalResponsibilityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_responsibility_dto import FiscalResponsibilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalResponsibilityDto from a JSON string
fiscal_responsibility_dto_instance = FiscalResponsibilityDto.from_json(json)
# print the JSON string representation of the object
print(FiscalResponsibilityDto.to_json())

# convert the object into a dict
fiscal_responsibility_dto_dict = fiscal_responsibility_dto_instance.to_dict()
# create an instance of FiscalResponsibilityDto from a dict
fiscal_responsibility_dto_from_dict = FiscalResponsibilityDto.from_dict(fiscal_responsibility_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


