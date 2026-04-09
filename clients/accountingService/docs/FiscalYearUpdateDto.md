# FiscalYearUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_year_update_dto import FiscalYearUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalYearUpdateDto from a JSON string
fiscal_year_update_dto_instance = FiscalYearUpdateDto.from_json(json)
# print the JSON string representation of the object
print(FiscalYearUpdateDto.to_json())

# convert the object into a dict
fiscal_year_update_dto_dict = fiscal_year_update_dto_instance.to_dict()
# create an instance of FiscalYearUpdateDto from a dict
fiscal_year_update_dto_from_dict = FiscalYearUpdateDto.from_dict(fiscal_year_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


