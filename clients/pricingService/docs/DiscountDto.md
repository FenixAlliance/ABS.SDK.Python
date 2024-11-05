# DiscountDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**percent** | **float** |  | [optional] 
**item_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**discount_list_id** | **str** |  | [optional] 
**end_quantity** | **float** |  | [optional] 
**begin_quantity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.discount_dto import DiscountDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountDto from a JSON string
discount_dto_instance = DiscountDto.from_json(json)
# print the JSON string representation of the object
print(DiscountDto.to_json())

# convert the object into a dict
discount_dto_dict = discount_dto_instance.to_dict()
# create an instance of DiscountDto from a dict
discount_dto_from_dict = DiscountDto.from_dict(discount_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


