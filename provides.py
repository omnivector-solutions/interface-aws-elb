from charms.reactive import Endpoint


class AwsElbProvides(Endpoint):

    def configure(self, instance_id, instance_region,
                  instance_port, health_check_endpoint):
        """
        Configure the aws-elb relation by providing:
            - instance_id
            - instance_region
            - instance_port
            - health_check_endpoint
        """

        for relation in self.relations:
            relation.to_publish.update({
                'instance_id': instance_id,
                'instance_region': instance_region,
                'instance_port': instance_port,
                'health_check_endpoint': health_check_endpoint
            })
