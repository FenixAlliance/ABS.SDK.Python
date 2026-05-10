# ItemWarrantyPolicyCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**is_extended_warranty** | **bool** |  | [optional] 
**is_free** | **bool** |  | [optional] 
**reduce** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**allow_international** | **bool** |  | [optional] 
**hours** | **int** |  | [optional] 
**days** | **int** |  | [optional] 
**weeks** | **int** |  | [optional] 
**months** | **int** |  | [optional] 
**years** | **int** |  | [optional] 
**value** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**custom_state** | **str** |  | [optional] 
**custom_city** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_warranty_policy_create_dto import ItemWarrantyPolicyCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemWarrantyPolicyCreateDto from a JSON string
item_warranty_policy_create_dto_instance = ItemWarrantyPolicyCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemWarrantyPolicyCreateDto.to_json())

# convert the object into a dict
item_warranty_policy_create_dto_dict = item_warranty_policy_create_dto_instance.to_dict()
# create an instance of ItemWarrantyPolicyCreateDto from a dict
item_warranty_policy_create_dto_from_dict = ItemWarrantyPolicyCreateDto.from_dict(item_warranty_policy_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


