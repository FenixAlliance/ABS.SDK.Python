# EmailGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.email_group_dto import EmailGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailGroupDto from a JSON string
email_group_dto_instance = EmailGroupDto.from_json(json)
# print the JSON string representation of the object
print(EmailGroupDto.to_json())

# convert the object into a dict
email_group_dto_dict = email_group_dto_instance.to_dict()
# create an instance of EmailGroupDto from a dict
email_group_dto_from_dict = EmailGroupDto.from_dict(email_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


