# CourseCertificateTemplateUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_portal_id** | **str** |  | [optional] 
**website_theme_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**parent_web_content_id** | **str** |  | [optional] 
**parent_web_content_version_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_certificate_template_update_dto import CourseCertificateTemplateUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCertificateTemplateUpdateDto from a JSON string
course_certificate_template_update_dto_instance = CourseCertificateTemplateUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCertificateTemplateUpdateDto.to_json())

# convert the object into a dict
course_certificate_template_update_dto_dict = course_certificate_template_update_dto_instance.to_dict()
# create an instance of CourseCertificateTemplateUpdateDto from a dict
course_certificate_template_update_dto_from_dict = CourseCertificateTemplateUpdateDto.from_dict(course_certificate_template_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


