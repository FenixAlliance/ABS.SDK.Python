# FiscalRegimeUpdateDto


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
from openapi_client.models.fiscal_regime_update_dto import FiscalRegimeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalRegimeUpdateDto from a JSON string
fiscal_regime_update_dto_instance = FiscalRegimeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(FiscalRegimeUpdateDto.to_json())

# convert the object into a dict
fiscal_regime_update_dto_dict = fiscal_regime_update_dto_instance.to_dict()
# create an instance of FiscalRegimeUpdateDto from a dict
fiscal_regime_update_dto_from_dict = FiscalRegimeUpdateDto.from_dict(fiscal_regime_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


