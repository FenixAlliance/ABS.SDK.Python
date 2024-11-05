# ExtendedSalesLiteratureDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**sales_literature_type_id** | **str** |  | [optional] 
**sales_literature_type** | [**SalesLiteratureTypeDto**](SalesLiteratureTypeDto.md) |  | [optional] 
**tenant** | [**TenantDto**](TenantDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_sales_literature_dto import ExtendedSalesLiteratureDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedSalesLiteratureDto from a JSON string
extended_sales_literature_dto_instance = ExtendedSalesLiteratureDto.from_json(json)
# print the JSON string representation of the object
print(ExtendedSalesLiteratureDto.to_json())

# convert the object into a dict
extended_sales_literature_dto_dict = extended_sales_literature_dto_instance.to_dict()
# create an instance of ExtendedSalesLiteratureDto from a dict
extended_sales_literature_dto_from_dict = ExtendedSalesLiteratureDto.from_dict(extended_sales_literature_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


