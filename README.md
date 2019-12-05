# Apple Continuity Re-Implementation

This is a PoC, or a small script to help you to play with Continuity's broadcasting protocols.
The research is presented at Black Hat EU 2019 & HITCON 2019.
HITCON 2019 Presentation is in the [repo](https://github.com/evanslify/slides). Slides for BHEU will be released when the presentation is over.

Currently, this project only allows you to identify Continuity broadcast packets from a pcap, but however this could be changed and enabling you to read from a fifo pipe with ubertooth.

This project shall be expanded in the near future to support at least one protocol on Linux.

## Current abilities

- Track devices and show its Continuity capabilities

## To-do

- [ ] Implement de-cryption of GATT exchange session, with methods described in the research
- [ ] Emulating a Mac sending "Tethering Target Presense"
- [ ] Implementing Instant Hotspot

## Usage

1. Install `pyshark`.
2. Get a PCAP capture with ubertooth, and change filename in `example.py` accordingly.

