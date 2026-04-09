# GoogleAnalytics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**tracking_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_analytics import GoogleAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAnalytics from a JSON string
google_analytics_instance = GoogleAnalytics.from_json(json)
# print the JSON string representation of the object
print(GoogleAnalytics.to_json())

# convert the object into a dict
google_analytics_dict = google_analytics_instance.to_dict()
# create an instance of GoogleAnalytics from a dict
google_analytics_from_dict = GoogleAnalytics.from_dict(google_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


