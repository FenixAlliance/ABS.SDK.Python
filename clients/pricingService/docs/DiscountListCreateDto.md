# DiscountListCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.discount_list_create_dto import DiscountListCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountListCreateDto from a JSON string
discount_list_create_dto_instance = DiscountListCreateDto.from_json(json)
# print the JSON string representation of the object
print(DiscountListCreateDto.to_json())

# convert the object into a dict
discount_list_create_dto_dict = discount_list_create_dto_instance.to_dict()
# create an instance of DiscountListCreateDto from a dict
discount_list_create_dto_from_dict = DiscountListCreateDto.from_dict(discount_list_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


