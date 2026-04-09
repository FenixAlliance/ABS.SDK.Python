# EmailTemplateCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**html_content** | **str** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 
**code_type** | **str** |  | [optional] 
**marketing_campaign_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_template_create_dto import EmailTemplateCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateCreateDto from a JSON string
email_template_create_dto_instance = EmailTemplateCreateDto.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateCreateDto.to_json())

# convert the object into a dict
email_template_create_dto_dict = email_template_create_dto_instance.to_dict()
# create an instance of EmailTemplateCreateDto from a dict
email_template_create_dto_from_dict = EmailTemplateCreateDto.from_dict(email_template_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


