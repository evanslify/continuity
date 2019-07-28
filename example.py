#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.continuity import ContinuityMessage
from src.continuity.types import Continuity, Hotspot, NearbyAction, NearbyInfo, TetheringTargetPresence, Hash
import pyshark

types = [Hotspot, Continuity, NearbyAction, NearbyInfo, TetheringTargetPresence, Hash]
type_table = {}

for i in types:
    type_table[i.type_id] = i


cap = pyshark.FileCapture(
    './test-capture.pcapng',
    display_filter='btcommon.eir_ad.entry.company_id == 0x004c && btle.advertising_header.pdu_type == 0x0 && !_ws.malformed && !btle.crc.incorrect'
)


def setup_continuity_message(packet):
    """docstring for fname"""
    message = ContinuityMessage(packet)
    return message.get_data()


def setup_continuity_type(data):
    message_type = type_table[data[0]]
    return message_type(data)


for i in cap:
    msg = setup_continuity_message(i)
    t = setup_continuity_type(msg)
    if type(t) is Hotspot:
        print(t)
