# PointOfSaleCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.point_of_sale_create_dto import PointOfSaleCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfSaleCreateDto from a JSON string
point_of_sale_create_dto_instance = PointOfSaleCreateDto.from_json(json)
# print the JSON string representation of the object
print(PointOfSaleCreateDto.to_json())

# convert the object into a dict
point_of_sale_create_dto_dict = point_of_sale_create_dto_instance.to_dict()
# create an instance of PointOfSaleCreateDto from a dict
point_of_sale_create_dto_from_dict = PointOfSaleCreateDto.from_dict(point_of_sale_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


