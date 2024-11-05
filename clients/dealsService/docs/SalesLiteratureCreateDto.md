# SalesLiteratureCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
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
from openapi_client.models.sales_literature_create_dto import SalesLiteratureCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SalesLiteratureCreateDto from a JSON string
sales_literature_create_dto_instance = SalesLiteratureCreateDto.from_json(json)
# print the JSON string representation of the object
print(SalesLiteratureCreateDto.to_json())

# convert the object into a dict
sales_literature_create_dto_dict = sales_literature_create_dto_instance.to_dict()
# create an instance of SalesLiteratureCreateDto from a dict
sales_literature_create_dto_from_dict = SalesLiteratureCreateDto.from_dict(sales_literature_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


