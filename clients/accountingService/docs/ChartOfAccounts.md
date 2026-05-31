# ChartOfAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**file_url** | **str** |  | [optional] 
**childs** | [**List[Account]**](Account.md) |  | [optional] 

## Example

```python
from openapi_client.models.chart_of_accounts import ChartOfAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of ChartOfAccounts from a JSON string
chart_of_accounts_instance = ChartOfAccounts.from_json(json)
# print the JSON string representation of the object
print(ChartOfAccounts.to_json())

# convert the object into a dict
chart_of_accounts_dict = chart_of_accounts_instance.to_dict()
# create an instance of ChartOfAccounts from a dict
chart_of_accounts_from_dict = ChartOfAccounts.from_dict(chart_of_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


