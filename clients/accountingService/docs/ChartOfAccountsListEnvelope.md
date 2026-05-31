# ChartOfAccountsListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ChartOfAccounts]**](ChartOfAccounts.md) |  | [optional] 

## Example

```python
from openapi_client.models.chart_of_accounts_list_envelope import ChartOfAccountsListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccountsListEnvelope from a JSON string
chart_of_accounts_list_envelope_instance = ChartOfAccountsListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ChartOfAccountsListEnvelope.to_json())

# convert the object into a dict
chart_of_accounts_list_envelope_dict = chart_of_accounts_list_envelope_instance.to_dict()
# create an instance of ChartOfAccountsListEnvelope from a dict
chart_of_accounts_list_envelope_from_dict = ChartOfAccountsListEnvelope.from_dict(chart_of_accounts_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


