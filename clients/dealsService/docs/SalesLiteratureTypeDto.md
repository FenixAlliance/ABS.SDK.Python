# SalesLiteratureTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_literature_type_dto import SalesLiteratureTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SalesLiteratureTypeDto from a JSON string
sales_literature_type_dto_instance = SalesLiteratureTypeDto.from_json(json)
# print the JSON string representation of the object
print(SalesLiteratureTypeDto.to_json())

# convert the object into a dict
sales_literature_type_dto_dict = sales_literature_type_dto_instance.to_dict()
# create an instance of SalesLiteratureTypeDto from a dict
sales_literature_type_dto_from_dict = SalesLiteratureTypeDto.from_dict(sales_literature_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


