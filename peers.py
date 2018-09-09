from charms.reactive import set_flag, clear_flag, when
from charms.reactive import Endpoint


class AwsElbPeer(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def peer_joined(self):
        set_flag(self.expand_name('cluster.available'))

    @when('endpoint.{endpoint_name}.departed')
    def peer_departed(self):
        clear_flag(self.expand_name('cluster.available'))
