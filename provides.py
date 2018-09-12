from charms.reactive import Endpoint


class AwsElbProvides(Endpoint):

    def configure(self, instance_id, instance_region, instance_port):
        """
        Configure the aws-elb relation by providing:
            - instance_id
            - instance_region
            - instance_port
        """

        for relation in self.relations:
            relation.to_publish.update({
                'instance_id': instance_id,
                'instance_region': instance_region,
                'instance_port': instance_port,
            })
