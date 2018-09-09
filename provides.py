from charms.reactive import Endpoint


class AwsElbProvides(Endpoint):

    def configure(self, port):
        """
        Configure the elasticsearch relation by providing:
            - port
        """

        for relation in self.relations:
            relation.to_publish.update({
                'port': port,
            })
