# ItemTaxPolicyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**zero** | **bool** |  | [optional] 
**reduced** | **bool** |  | [optional] 
**withholding** | **bool** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
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
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_tax_policy_dto import ItemTaxPolicyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTaxPolicyDto from a JSON string
item_tax_policy_dto_instance = ItemTaxPolicyDto.from_json(json)
# print the JSON string representation of the object
print(ItemTaxPolicyDto.to_json())

# convert the object into a dict
item_tax_policy_dto_dict = item_tax_policy_dto_instance.to_dict()
# create an instance of ItemTaxPolicyDto from a dict
item_tax_policy_dto_from_dict = ItemTaxPolicyDto.from_dict(item_tax_policy_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


