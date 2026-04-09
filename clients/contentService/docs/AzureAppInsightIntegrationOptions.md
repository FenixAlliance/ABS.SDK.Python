# AzureAppInsightIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**enable_diagnostics_telemetry_module** | **bool** |  | [optional] 
**enable_authentication_tracking_java_script** | **bool** |  | [optional] 
**enable_request_tracking_telemetry_module** | **bool** |  | [optional] 
**inject_response_headers** | **bool** |  | [optional] 
**track_exceptions** | **bool** |  | [optional] 
**enable_w3_c_distributed_tracing** | **bool** |  | [optional] 
**add_auto_collected_metric_extractor** | **bool** |  | [optional] 
**enable_heartbeat** | **bool** |  | [optional] 
**enable_debug_logger** | **bool** |  | [optional] 
**endpoint_address** | **str** |  | [optional] 
**developer_mode** | **bool** |  | [optional] 
**application_version** | **str** |  | [optional] 
**connection_string** | **str** |  | [optional] 
**instrumentation_key** | **str** |  | [optional] 
**enable_adaptive_sampling** | **bool** |  | [optional] 
**enable_event_counter_collection_module** | **bool** |  | [optional] 
**enable_dependency_tracking_telemetry_module** | **bool** |  | [optional] 
**enable_azure_instance_metadata_telemetry_module** | **bool** |  | [optional] 
**enable_app_services_heartbeat_telemetry_module** | **bool** |  | [optional] 
**enable_performance_counter_collection_module** | **bool** |  | [optional] 
**enable_quick_pulse_metric_stream** | **bool** |  | [optional] 
**enable_legacy_correlation_headers_injection** | **bool** |  | [optional] 
**enable_active_telemetry_configuration_setup** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.azure_app_insight_integration_options import AzureAppInsightIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AzureAppInsightIntegrationOptions from a JSON string
azure_app_insight_integration_options_instance = AzureAppInsightIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(AzureAppInsightIntegrationOptions.to_json())

# convert the object into a dict
azure_app_insight_integration_options_dict = azure_app_insight_integration_options_instance.to_dict()
# create an instance of AzureAppInsightIntegrationOptions from a dict
azure_app_insight_integration_options_from_dict = AzureAppInsightIntegrationOptions.from_dict(azure_app_insight_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


