# FiscalPeriodUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_period_update_dto import FiscalPeriodUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalPeriodUpdateDto from a JSON string
fiscal_period_update_dto_instance = FiscalPeriodUpdateDto.from_json(json)
# print the JSON string representation of the object
print(FiscalPeriodUpdateDto.to_json())

# convert the object into a dict
fiscal_period_update_dto_dict = fiscal_period_update_dto_instance.to_dict()
# create an instance of FiscalPeriodUpdateDto from a dict
fiscal_period_update_dto_from_dict = FiscalPeriodUpdateDto.from_dict(fiscal_period_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


