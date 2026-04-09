# ContactPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_point_type** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 
**contact_type** | **str** |  | [optional] 
**contact_option** | **str** |  | [optional] 
**area_served** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contact_point import ContactPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPoint from a JSON string
contact_point_instance = ContactPoint.from_json(json)
# print the JSON string representation of the object
print(ContactPoint.to_json())

# convert the object into a dict
contact_point_dict = contact_point_instance.to_dict()
# create an instance of ContactPoint from a dict
contact_point_from_dict = ContactPoint.from_dict(contact_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


