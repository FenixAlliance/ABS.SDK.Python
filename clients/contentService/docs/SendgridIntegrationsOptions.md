# SendgridIntegrationsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**api_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sendgrid_integrations_options import SendgridIntegrationsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SendgridIntegrationsOptions from a JSON string
sendgrid_integrations_options_instance = SendgridIntegrationsOptions.from_json(json)
# print the JSON string representation of the object
print(SendgridIntegrationsOptions.to_json())

# convert the object into a dict
sendgrid_integrations_options_dict = sendgrid_integrations_options_instance.to_dict()
# create an instance of SendgridIntegrationsOptions from a dict
sendgrid_integrations_options_from_dict = SendgridIntegrationsOptions.from_dict(sendgrid_integrations_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


