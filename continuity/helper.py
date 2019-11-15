from continuity import ContinuityMessage


def setup_continuity_message(packet):
    """docstring for fname"""
    return ContinuityMessage(packet)
    # return message.get_data()


def setup_continuity_type(data, type_table):
    try:
        message_type = type_table[data[0]]
    except KeyError:
        print('Missing type', data[0])
        return None
    return message_type(data)
