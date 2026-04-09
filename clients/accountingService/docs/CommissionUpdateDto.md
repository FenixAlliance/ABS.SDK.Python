# CommissionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**base_amount** | **float** |  | [optional] 
**added_percent** | **float** |  | [optional] 
**added_amount** | **float** |  | [optional] 
**tax_comission** | **float** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**salary_id** | **str** |  | [optional] 
**emisor_wallet_account_id** | **str** |  | [optional] 
**receiver_wallet_account_id** | **str** |  | [optional] 
**emisor_contact_id** | **str** |  | [optional] 
**receiver_contact_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.commission_update_dto import CommissionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionUpdateDto from a JSON string
commission_update_dto_instance = CommissionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CommissionUpdateDto.to_json())

# convert the object into a dict
commission_update_dto_dict = commission_update_dto_instance.to_dict()
# create an instance of CommissionUpdateDto from a dict
commission_update_dto_from_dict = CommissionUpdateDto.from_dict(commission_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


