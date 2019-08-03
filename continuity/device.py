from continuity.types import __ContinuityType


class Device(object):
    def __init__(self, priv_addr):
        self.priv_addr = priv_addr
        self.pub_addr = None
        self.services = {}
        self.device_name = None

    def set_pub_addr(self, pub_addr):
        self.pub_addr = pub_addr

    def set_device_name(self, device_name):
        self.device_name = device_name

    def has_service(self, service):
        return self.services.get(service.type_id)

    def add_service(self, service):
        self.services[service.type_id] = service
