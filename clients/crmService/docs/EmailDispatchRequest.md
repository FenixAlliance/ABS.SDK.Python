# EmailDispatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**message** | **str** |  | 
**button_link** | **str** |  | [optional] 
**button_text** | **str** |  | [optional] 
**alert_message** | **str** |  | [optional] 
**alert_type** | **str** |  | [optional] 
**culture** | **str** |  | 
**ui_culture** | **str** |  | 
**recipients** | **List[str]** |  | 
**contact_ids** | **List[str]** |  | [optional] 
**tenant_ids** | **List[str]** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**template_url** | **str** |  | [optional] 
**email_template_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_dispatch_request import EmailDispatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDispatchRequest from a JSON string
email_dispatch_request_instance = EmailDispatchRequest.from_json(json)
# print the JSON string representation of the object
print(EmailDispatchRequest.to_json())

# convert the object into a dict
email_dispatch_request_dict = email_dispatch_request_instance.to_dict()
# create an instance of EmailDispatchRequest from a dict
email_dispatch_request_from_dict = EmailDispatchRequest.from_dict(email_dispatch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


