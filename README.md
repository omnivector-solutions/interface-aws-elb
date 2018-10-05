# interface-aws-elb

This interface encapsulates the provides and requires Endpoint classes for the aws-elb relationship.


### Example Usage
Use the provides side of the `aws-elb` relationship to add units of your application to an ELB.

```python
@when('endpoint.aws-elb.joined')
@when_not('aws-elb.data.sent')
def send_data_to_aws_elb_endpoint():
    endpoint = endpoint_from_flag('endpoint.aws-elb.joined')
    endpoint.configure(
        instance_id=get_instance_id(),
        instance_region=get_instance_region(),
        instance_port=FLASK_HTTP_PORT,
        health_check_endpoint="/ping"
    )
    set_flag('aws-elb.data.sent')


@when_not('endpoint.aws-elb.joined')
def remove_data_sent():
    clear_flag('aws-elb.data.sent')
```


#### License
* GPLV3 (see `LICENSE` file)
