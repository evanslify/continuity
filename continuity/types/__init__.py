class __ContinuityType(object):
    def __init__(self, message):
        self.message = message
        pass

    def match_pattern(self):
        pass

    def get_msg_length(self):
        return self.message[1]


class Continuity(__ContinuityType):
    type_id = 0x0c

    def __init__(self, data):
        self.data = data
        pass


class Hotspot(__ContinuityType):
    type_id = 0x0e

    def __init__(self, data):
        self.data = data
        pass

    def __str__(self):
        try:
            return 'Battery {}, Cell type {}, Signal {}'.format(
                self.get_battery_level(),
                self.get_cell_type(),
                self.get_signal_quality()
            )
        except IndexError as e:
            print('Malformed Hotspot', self.data)
            raise e

    def get_battery_level(self):
        return self.data[4]

    def get_cell_type(self):
        return self.data[6]

    def get_signal_quality(self):
        return self.data[7]


class NearbyInfo(__ContinuityType):
    type_id = 0x10

    def __init__(self, data):
        self.data = data
        pass


class NearbyAction(__ContinuityType):
    type_id = 0x0f

    def __init__(self, data):
        self.data = data
        pass


class TetheringTargetPresence(__ContinuityType):
    type_id = 0x0d

    def __init__(self, data):
        self.data = data
        pass


class Hash(__ContinuityType):
    type_id = 0x01

    def __init__(self, data):
        self.data = data
        pass


class IBeacon(__ContinuityType):
    type_id = 0x02

    def __init__(self, data):
        self.data = data
        pass


class AirPrint(__ContinuityType):
    type_id = 0x03

    def __init__(self, data):
        self.data = data
        pass


class TVSetup(__ContinuityType):
    type_id = 0x04

    def __init__(self, data):
        self.data = data
        pass


class AWDL(__ContinuityType):
    type_id = 0x05

    def __init__(self, data):
        self.data = data
        pass


class HomeKit(__ContinuityType):
    type_id = 0x06

    def __init__(self, data):
        self.data = data
        pass


class ProximityPairing(__ContinuityType):
    type_id = 0x07

    def __init__(self, data):
        self.data = data
        pass


class HeySiri(__ContinuityType):
    type_id = 0x08

    def __init__(self, data):
        self.data = data
        pass


class AirPlayTarget(__ContinuityType):
    type_id = 0x09

    def __init__(self, data):
        self.data = data
        pass


class AirPlaySoloSource(__ContinuityType):
    type_id = 0x0a

    def __init__(self, data):
        self.data = data
        pass


class MagicSwitch(__ContinuityType):
    type_id = 0x0b

    def __init__(self, data):
        self.data = data
        pass


class HomeKitNew(__ContinuityType):
    type_id = 0x11

    def __init__(self, data):
        self.data = data
        pass
