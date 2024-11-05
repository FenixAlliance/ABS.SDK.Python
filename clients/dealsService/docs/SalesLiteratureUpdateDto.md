# SalesLiteratureUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**sales_literature_type_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_literature_update_dto import SalesLiteratureUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SalesLiteratureUpdateDto from a JSON string
sales_literature_update_dto_instance = SalesLiteratureUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SalesLiteratureUpdateDto.to_json())

# convert the object into a dict
sales_literature_update_dto_dict = sales_literature_update_dto_instance.to_dict()
# create an instance of SalesLiteratureUpdateDto from a dict
sales_literature_update_dto_from_dict = SalesLiteratureUpdateDto.from_dict(sales_literature_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


