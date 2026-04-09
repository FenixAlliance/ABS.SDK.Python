# EmailsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_template** | **str** |  | [optional] 
**action_template** | **str** |  | [optional] 
**receipt_template** | **str** |  | [optional] 
**welcome_template** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.emails_options import EmailsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EmailsOptions from a JSON string
emails_options_instance = EmailsOptions.from_json(json)
# print the JSON string representation of the object
print(EmailsOptions.to_json())

# convert the object into a dict
emails_options_dict = emails_options_instance.to_dict()
# create an instance of EmailsOptions from a dict
emails_options_from_dict = EmailsOptions.from_dict(emails_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


