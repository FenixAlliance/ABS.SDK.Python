# CommissionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**base_amount** | **float** |  | [optional] 
**added_percent** | **float** |  | [optional] 
**added_amount** | **float** |  | [optional] 
**tax_comission** | **float** |  | [optional] 
**salary_id** | **str** |  | [optional] 
**emisor_wallet_account_id** | **str** |  | [optional] 
**receiver_wallet_account_id** | **str** |  | [optional] 
**emisor_contact_id** | **str** |  | [optional] 
**receiver_contact_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.commission_create_dto import CommissionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionCreateDto from a JSON string
commission_create_dto_instance = CommissionCreateDto.from_json(json)
# print the JSON string representation of the object
print(CommissionCreateDto.to_json())

# convert the object into a dict
commission_create_dto_dict = commission_create_dto_instance.to_dict()
# create an instance of CommissionCreateDto from a dict
commission_create_dto_from_dict = CommissionCreateDto.from_dict(commission_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


