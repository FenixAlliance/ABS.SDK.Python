# ItemTaxPolicyRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tax_policy_id** | **str** |  | [optional] 
**item_price_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_tax_policy_record_dto import ItemTaxPolicyRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTaxPolicyRecordDto from a JSON string
item_tax_policy_record_dto_instance = ItemTaxPolicyRecordDto.from_json(json)
# print the JSON string representation of the object
print(ItemTaxPolicyRecordDto.to_json())

# convert the object into a dict
item_tax_policy_record_dto_dict = item_tax_policy_record_dto_instance.to_dict()
# create an instance of ItemTaxPolicyRecordDto from a dict
item_tax_policy_record_dto_from_dict = ItemTaxPolicyRecordDto.from_dict(item_tax_policy_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


