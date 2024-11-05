# EmailSignatureCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**author_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**html_content** | **str** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_signature_create_dto import EmailSignatureCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSignatureCreateDto from a JSON string
email_signature_create_dto_instance = EmailSignatureCreateDto.from_json(json)
# print the JSON string representation of the object
print(EmailSignatureCreateDto.to_json())

# convert the object into a dict
email_signature_create_dto_dict = email_signature_create_dto_instance.to_dict()
# create an instance of EmailSignatureCreateDto from a dict
email_signature_create_dto_from_dict = EmailSignatureCreateDto.from_dict(email_signature_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


