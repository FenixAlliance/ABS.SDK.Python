# PointOfSaleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.point_of_sale_dto import PointOfSaleDto

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfSaleDto from a JSON string
point_of_sale_dto_instance = PointOfSaleDto.from_json(json)
# print the JSON string representation of the object
print(PointOfSaleDto.to_json())

# convert the object into a dict
point_of_sale_dto_dict = point_of_sale_dto_instance.to_dict()
# create an instance of PointOfSaleDto from a dict
point_of_sale_dto_from_dict = PointOfSaleDto.from_dict(point_of_sale_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


