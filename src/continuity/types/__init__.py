class ContinuityType(object):
    def __init__(self, message):
        self.message = message
        pass

    def match_pattern(self):
        pass

    def get_msg_length(self):
        return self.message[1]


class Continuity(ContinuityType):
    type_id = 0x0c

    def __init__(self, data):
        self.data = data
        pass


class Hotspot(ContinuityType):
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


class NearbyInfo(ContinuityType):
    type_id = 0x10

    def __init__(self, data):
        self.data = data
        pass


class NearbyAction(ContinuityType):
    type_id = 0x0f

    def __init__(self, data):
        self.data = data
        pass


class TetheringTargetPresence(ContinuityType):
    type_id = 0x0d

    def __init__(self, data):
        self.data = data
        pass


class Hash(ContinuityType):
    type_id = 0x01

    def __init__(self, data):
        self.data = data
        pass
