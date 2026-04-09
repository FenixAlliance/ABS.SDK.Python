# CourseCertificateTemplateCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**course_id** | **str** |  | 
**business_id** | **str** |  | 
**web_portal_id** | **str** |  | [optional] 
**website_theme_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**parent_web_content_id** | **str** |  | [optional] 
**parent_web_content_version_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_certificate_template_create_dto import CourseCertificateTemplateCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCertificateTemplateCreateDto from a JSON string
course_certificate_template_create_dto_instance = CourseCertificateTemplateCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCertificateTemplateCreateDto.to_json())

# convert the object into a dict
course_certificate_template_create_dto_dict = course_certificate_template_create_dto_instance.to_dict()
# create an instance of CourseCertificateTemplateCreateDto from a dict
course_certificate_template_create_dto_from_dict = CourseCertificateTemplateCreateDto.from_dict(course_certificate_template_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


