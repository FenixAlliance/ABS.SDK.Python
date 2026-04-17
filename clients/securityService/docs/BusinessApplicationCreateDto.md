# BusinessApplicationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**is_multi_tenant** | **bool** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**is_single_page_application** | **bool** |  | [optional] 
**is_native_or_desktop_app** | **bool** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**privacy_policy_url** | **str** |  | [optional] 
**terms_and_conditions_url** | **str** |  | [optional] 
**require_https** | **bool** |  | [optional] 
**require_app_secret** | **bool** |  | [optional] 
**enable_client_oauth_login** | **bool** |  | [optional] 
**enable_web_o_auth_login** | **bool** |  | [optional] 
**enable_device_o_auth_login** | **bool** |  | [optional] 
**allow_access_to_suite_settings** | **bool** |  | [optional] 
**require_web_o_auth_reauthentication** | **bool** |  | [optional] 
**require_two_factor_reauthorization** | **bool** |  | [optional] 
**enable_embedded_browser_o_auth_login** | **bool** |  | [optional] 
**use_strict_mode_for_redirect_uris** | **bool** |  | [optional] 
**country_restricted** | **bool** |  | [optional] 
**spa_ui_engine** | **str** |  | [optional] 
**spa_static_files_root_path** | **str** |  | [optional] 
**spa_relative_app_path** | **str** |  | [optional] 
**spa_npm_start_script** | **str** |  | [optional] 
**spa_npm_publish_script** | **str** |  | [optional] 
**spa_relative_source_path** | **str** |  | [optional] 
**spa_relative_output_path** | **str** |  | [optional] 
**use_proxy_to_spa_development_server** | **bool** |  | [optional] 
**spa_development_server_uri** | **str** |  | [optional] 
**enable_git_repo_management** | **bool** |  | [optional] 
**git_repo_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.business_application_create_dto import BusinessApplicationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessApplicationCreateDto from a JSON string
business_application_create_dto_instance = BusinessApplicationCreateDto.from_json(json)
# print the JSON string representation of the object
print(BusinessApplicationCreateDto.to_json())

# convert the object into a dict
business_application_create_dto_dict = business_application_create_dto_instance.to_dict()
# create an instance of BusinessApplicationCreateDto from a dict
business_application_create_dto_from_dict = BusinessApplicationCreateDto.from_dict(business_application_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


