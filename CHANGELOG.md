# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
- **Copied Frontend UI**: Migrated the visual HTML/CSS/JS frontend from `rr demo` to `RR2/dashboard/public`. This serves as the foundation for the real-time WebRTC dashboard.
- **Node.js Initialization**: Initialized `package.json` inside `RR2/dashboard` to manage isolated backend dependencies.
- **Architectural Setup**: Established the `RR2` workspace structure (`dashboard` and `model` folders), wrote `CONTEXT.md` to define domain terminology, and documented the Tech Stack switch to Node.js/MongoDB in `docs/adr/0001-nodejs-mongodb-stack.md`.

- **Node.js Backend**: Built `server.js` with Express, Socket.io, and Multer to handle autonomous model JSON payloads and serve the `public/` directory.
- **MongoDB Schema**: Created `models/Violation.js` schema reflecting `demo_data.json` for 1:1 mapping with UI.
- **Live Phone Streamer**: Created `streamer.html` for a mobile phone to capture and push frames via WebSockets.
- **UI Integration**: Added `CAM-07` to `demo_data.json` and wired `index.html` to consume live WebSockets frames and autonomous violation events in real time.

- **Documentation**: Added `RR2/README.md` detailing how to start the Node.js server, open the dashboard, and broadcast the WebSocket camera feed from a mobile phone.

- **Edge Model Environment**: Created a fully isolated Python `venv` inside `RR2/model` and added `requirements.txt` (YOLO, OpenCV, EasyOCR, requests).
- **Video Processor Pipeline**: Built `process_video.py`, a functional Python edge script that processes a local video file, extracts image evidence, bundles the JSON payload, and POSTs it directly to the Node.js dashboard endpoint as `multipart/form-data`.
