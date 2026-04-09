# StoreDataRetentionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_retention_time_span_ammount** | **int** |  | [optional] 
**retention_time_span** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.store_data_retention_policy import StoreDataRetentionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StoreDataRetentionPolicy from a JSON string
store_data_retention_policy_instance = StoreDataRetentionPolicy.from_json(json)
# print the JSON string representation of the object
print(StoreDataRetentionPolicy.to_json())

# convert the object into a dict
store_data_retention_policy_dict = store_data_retention_policy_instance.to_dict()
# create an instance of StoreDataRetentionPolicy from a dict
store_data_retention_policy_from_dict = StoreDataRetentionPolicy.from_dict(store_data_retention_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


