# RoadRakshak Traffic Enforcement

The centralized traffic violation monitoring system that receives video snippets, payloads, and images from edge computer vision cameras to automate challan generation.

## Language

**Central Command Dashboard**:
The centralized UI where traffic officers review violations streamed from all edge cameras across the city.
_Avoid_: Local dashboard, edge UI.

**Edge Node / Camera**:
The physical junction enclosure (ICCC Rack) that runs headless AI computer vision (Stage-A detector), cropping evidence and sending lightweight JSON and images to the central system.
_Avoid_: Local camera, smart camera.

**Violation**:
A specific traffic rule infraction detected by the AI (e.g., No Helmet, Overspeeding). These are queued in the UI for an officer to review alongside video evidence.
_Avoid_: Incident (when referring to the specific infraction).

**Challan**:
The official legal document generated with one click after an officer reviews and validates the violation video cut.
_Avoid_: Fine, ticket.

**Review Process**:
The manual step where an officer watches the video cut of a vehicle's violation to confirm the AI's detection before generating a Challan.
_Avoid_: Automated fine, instant ticket.

**Video Cut**:
A 3-5 second compressed `.mp4` clip extracted by the Edge Node around the timestamp of a violation, serving as dynamic evidence for the Review Process.
_Avoid_: Video snippet, stream recording.

**Live Stream API**:
The network endpoint exposed by the central backend that allows users (including mobile phones on the same network) to view real-time video streams and switch between multiple edge camera feeds.
_Avoid_: RTSP Feed (when referring to the web/mobile accessible stream).

**Violation Payload**:
The structured, query-based data sent by the Edge Node to the Central Dashboard containing the details of the violation for human verification.
_Avoid_: Raw log.
