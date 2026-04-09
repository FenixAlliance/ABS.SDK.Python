# BusinessApplicationSimpleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.business_application_simple_dto import BusinessApplicationSimpleDto

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessApplicationSimpleDto from a JSON string
business_application_simple_dto_instance = BusinessApplicationSimpleDto.from_json(json)
# print the JSON string representation of the object
print(BusinessApplicationSimpleDto.to_json())

# convert the object into a dict
business_application_simple_dto_dict = business_application_simple_dto_instance.to_dict()
# create an instance of BusinessApplicationSimpleDto from a dict
business_application_simple_dto_from_dict = BusinessApplicationSimpleDto.from_dict(business_application_simple_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


