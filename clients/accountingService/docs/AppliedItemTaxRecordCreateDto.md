# AppliedItemTaxRecordCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tax_policy_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**tax_amount_in_usd** | **float** |  | [optional] 
**tax_base_amount_in_usd** | **float** |  | [optional] 
**billing_item_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.applied_item_tax_record_create_dto import AppliedItemTaxRecordCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedItemTaxRecordCreateDto from a JSON string
applied_item_tax_record_create_dto_instance = AppliedItemTaxRecordCreateDto.from_json(json)
# print the JSON string representation of the object
print(AppliedItemTaxRecordCreateDto.to_json())

# convert the object into a dict
applied_item_tax_record_create_dto_dict = applied_item_tax_record_create_dto_instance.to_dict()
# create an instance of AppliedItemTaxRecordCreateDto from a dict
applied_item_tax_record_create_dto_from_dict = AppliedItemTaxRecordCreateDto.from_dict(applied_item_tax_record_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


