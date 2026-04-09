# AccountingPeriodDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**date_start** | **datetime** |  | [optional] 
**date_end** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.accounting_period_dto import AccountingPeriodDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingPeriodDto from a JSON string
accounting_period_dto_instance = AccountingPeriodDto.from_json(json)
# print the JSON string representation of the object
print(AccountingPeriodDto.to_json())

# convert the object into a dict
accounting_period_dto_dict = accounting_period_dto_instance.to_dict()
# create an instance of AccountingPeriodDto from a dict
accounting_period_dto_from_dict = AccountingPeriodDto.from_dict(accounting_period_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


