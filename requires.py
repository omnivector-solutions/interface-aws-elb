from charms.reactive import when, when_not
from charms.reactive import clear_flag, set_flag
from charms.reactive import Endpoint


class AwsElbRequires(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        if any(unit.received['instance_port']
               for unit in self.all_joined_units):
            set_flag(self.expand_name('available'))

    @when_not('endpoint.{endpoint_name}.joined')
    def departed(self):
        clear_flag(self.expand_name('available'))

    def list_unit_data(self):
        """
        Get the list of the relation info for each unit.

        Returns a list of dicts, where each dict contains the instance_id,
        instance_region, instance_port, and health_check_endpoint.
        """
        units_data = []
        for relation in self.relations:
            for unit in relation.joined_units:
                instance_id = unit.received['instance_id']
                instance_region = unit.received['instance_region']
                instance_port = unit.received['instance_port']
                health_check_endpoint = unit.received['health_check_endpoint']
                if not (instance_id and instance_region and
                        instance_port and health_check_endpoint):
                    continue
                units_data.append({
                    'instance_id': instance_id,
                    'instance_region': instance_region,
                    'instance_port': instance_port,
                    'health_check_endpoint': health_check_endpoint,
                })
        return units_data
