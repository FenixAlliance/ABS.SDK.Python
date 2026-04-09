# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** |  | [optional] 
**business_name** | **str** |  | [optional] 
**slogan** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**facebook_page_username** | **str** |  | [optional] 
**instagram_username** | **str** |  | [optional] 
**linked_in_username** | **str** |  | [optional] 
**twitter_handler** | **str** |  | [optional] 
**git_hub_username** | **str** |  | [optional] 
**contact_points** | [**List[ContactPoint]**](ContactPoint.md) |  | [optional] 

## Example

```python
from openapi_client.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


