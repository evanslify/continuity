#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from continuity import ContinuityMessage
from continuity.device import Device
import continuity.types as ContinuityTypes
import pyshark

types = [v for k, v in ContinuityTypes.__dict__.items()
         if callable(v) and '__' not in k]
type_table = {}
for i in types:
    type_table[i.type_id] = i


cap = pyshark.FileCapture(
    # './test-capture.pcapng',
    '/home/es/Desktop/cap-thsr.pcap',
    display_filter='btcommon.eir_ad.entry.company_id == 0x004c && \
        btle.advertising_header.pdu_type == 0x0 && !_ws.malformed \
        && !btle.crc.incorrect && btcommon.eir_ad.entry.data'
)


def setup_continuity_message(packet):
    """docstring for fname"""
    return ContinuityMessage(packet)
    # return message.get_data()


def setup_continuity_type(data):
    try:
        message_type = type_table[data[0]]
    except KeyError:
        print('Missing type', data[0])
        return None
    return message_type(data)


devices = {}


for i in cap:
    msg = setup_continuity_message(i)
    t = setup_continuity_type(msg.get_data())
    if not t:
        continue

    sender = msg.get_sender()
    if not devices.get(sender):
        devices[sender] = Device(sender)
    if not devices[sender].has_service(t):
        devices[sender].add_service(t)
    # if type(t) is ContinuityTypes.Hotspot:
    #     print(t)
print(devices)
