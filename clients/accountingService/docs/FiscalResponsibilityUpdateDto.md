# FiscalResponsibilityUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_responsibility_update_dto import FiscalResponsibilityUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalResponsibilityUpdateDto from a JSON string
fiscal_responsibility_update_dto_instance = FiscalResponsibilityUpdateDto.from_json(json)
# print the JSON string representation of the object
print(FiscalResponsibilityUpdateDto.to_json())

# convert the object into a dict
fiscal_responsibility_update_dto_dict = fiscal_responsibility_update_dto_instance.to_dict()
# create an instance of FiscalResponsibilityUpdateDto from a dict
fiscal_responsibility_update_dto_from_dict = FiscalResponsibilityUpdateDto.from_dict(fiscal_responsibility_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


