# ObjectEmailDispatchRequest


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
**payload** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.object_email_dispatch_request import ObjectEmailDispatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectEmailDispatchRequest from a JSON string
object_email_dispatch_request_instance = ObjectEmailDispatchRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectEmailDispatchRequest.to_json())

# convert the object into a dict
object_email_dispatch_request_dict = object_email_dispatch_request_instance.to_dict()
# create an instance of ObjectEmailDispatchRequest from a dict
object_email_dispatch_request_from_dict = ObjectEmailDispatchRequest.from_dict(object_email_dispatch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


