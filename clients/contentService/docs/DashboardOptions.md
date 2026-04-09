# DashboardOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**icon_color** | **str** |  | [optional] 
**favicon** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dashboard_options import DashboardOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardOptions from a JSON string
dashboard_options_instance = DashboardOptions.from_json(json)
# print the JSON string representation of the object
print(DashboardOptions.to_json())

# convert the object into a dict
dashboard_options_dict = dashboard_options_instance.to_dict()
# create an instance of DashboardOptions from a dict
dashboard_options_from_dict = DashboardOptions.from_dict(dashboard_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


