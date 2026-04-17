# AccountingPeriodUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**date_start** | **datetime** |  | [optional] 
**date_end** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.accounting_period_update_dto import AccountingPeriodUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingPeriodUpdateDto from a JSON string
accounting_period_update_dto_instance = AccountingPeriodUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AccountingPeriodUpdateDto.to_json())

# convert the object into a dict
accounting_period_update_dto_dict = accounting_period_update_dto_instance.to_dict()
# create an instance of AccountingPeriodUpdateDto from a dict
accounting_period_update_dto_from_dict = AccountingPeriodUpdateDto.from_dict(accounting_period_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


