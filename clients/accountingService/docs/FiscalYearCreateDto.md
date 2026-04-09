# FiscalYearCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_year_create_dto import FiscalYearCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalYearCreateDto from a JSON string
fiscal_year_create_dto_instance = FiscalYearCreateDto.from_json(json)
# print the JSON string representation of the object
print(FiscalYearCreateDto.to_json())

# convert the object into a dict
fiscal_year_create_dto_dict = fiscal_year_create_dto_instance.to_dict()
# create an instance of FiscalYearCreateDto from a dict
fiscal_year_create_dto_from_dict = FiscalYearCreateDto.from_dict(fiscal_year_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


