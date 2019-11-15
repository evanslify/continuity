#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from continuity.helper import setup_continuity_message
from continuity.helper import setup_continuity_type
from continuity.PrivateAddrSolver import PrivateAddrSolver
import continuity.types as ContinuityTypes
import pyshark
import binascii

types = [v for k, v in ContinuityTypes.__dict__.items()
         if callable(v) and '__' not in k]
type_table = {}
for i in types:
    type_table[i.type_id] = i


cap = pyshark.FileCapture(
    '/tmp/pipe',
    display_filter='btcommon.eir_ad.entry.company_id == 0x004c && \
        btle.advertising_header.pdu_type == 0x0 && !_ws.malformed \
        && !btle.crc.incorrect && btcommon.eir_ad.entry.data'
)


devices = {}
irk = binascii.unhexlify('')
ipad_irk = binascii.unhexlify('')

for i in cap:
    msg = setup_continuity_message(i)
    t = setup_continuity_type(msg.get_data(), type_table)
    if not t:
        continue

    sender = msg.get_sender()
    solver = PrivateAddrSolver(sender, irk)
    ipad_solver = PrivateAddrSolver(sender, ipad_irk)
    if solver and solver.parse():
        print('i ', msg.get_data().hex(), t, sender)
    if ipad_solver and ipad_solver.parse():
        print('ip', msg.get_data().hex(), t, sender)
