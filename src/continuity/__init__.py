class ContinuityMessage(object):
    def __init__(self, packet):
        self.packet = packet
        pass

    def get_sender(self):
        return self.packet['btle'].advertising_address

    def get_data(self):
        return bytearray.fromhex(
            self.packet['btle'].btcommon_eir_ad_entry_data.replace(':', ' ')
        )
