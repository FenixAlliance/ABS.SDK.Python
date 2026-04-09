# BankUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_update_dto import BankUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankUpdateDto from a JSON string
bank_update_dto_instance = BankUpdateDto.from_json(json)
# print the JSON string representation of the object
print(BankUpdateDto.to_json())

# convert the object into a dict
bank_update_dto_dict = bank_update_dto_instance.to_dict()
# create an instance of BankUpdateDto from a dict
bank_update_dto_from_dict = BankUpdateDto.from_dict(bank_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


