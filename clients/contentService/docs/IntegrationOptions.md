# IntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_mind_license_key** | **str** |  | [optional] 
**max_mind_db_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.integration_options import IntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationOptions from a JSON string
integration_options_instance = IntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(IntegrationOptions.to_json())

# convert the object into a dict
integration_options_dict = integration_options_instance.to_dict()
# create an instance of IntegrationOptions from a dict
integration_options_from_dict = IntegrationOptions.from_dict(integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


