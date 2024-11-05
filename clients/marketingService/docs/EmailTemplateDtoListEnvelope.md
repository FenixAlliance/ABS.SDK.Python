# EmailTemplateDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[EmailTemplateDto]**](EmailTemplateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_template_dto_list_envelope import EmailTemplateDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateDtoListEnvelope from a JSON string
email_template_dto_list_envelope_instance = EmailTemplateDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateDtoListEnvelope.to_json())

# convert the object into a dict
email_template_dto_list_envelope_dict = email_template_dto_list_envelope_instance.to_dict()
# create an instance of EmailTemplateDtoListEnvelope from a dict
email_template_dto_list_envelope_from_dict = EmailTemplateDtoListEnvelope.from_dict(email_template_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


