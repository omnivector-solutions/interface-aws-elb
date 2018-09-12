from charms.reactive import when
from charms.reactive import set_flag
from charms.reactive import Endpoint


class AwsElbRequires(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        if any(unit.received['instance_port']
               for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    def list_unit_data(self):
        """
        Get the list of the relation info for each unit.

        Returns a list of dicts, where each dict contains the elasticsearch
        cluster name, the host (address)
        and the port (as a string), as well as
        the relation ID and remote unit name that provided the site.

        For example::
            [
                {
                    'port': '80',
                },
            ]
        """
        units_data = []
        for relation in self.relations:
            for unit in relation.joined_units:
                instance_id = unit.received['instance_id']
                instance_region = unit.received['instance_region']
                instance_port = unit.received['instance_port']
                if not (instance_id and instance_region and instance_port):
                    continue
                units_data.append({
                    'instance_id': instance_id,
                    'instance_region': instance_region,
                    'instance_port': instance_port,
                })
        return units_data
