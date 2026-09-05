# RoadRakshak 2.0 (RR2) - Demo Guide

This directory contains the central dashboard and backend for the RoadRakshak traffic enforcement system.

## Prerequisites
1. **Node.js** installed on your machine.
2. **MongoDB** installed and running locally (`mongodb://127.0.0.1:27017`).

## 1. Starting the Server
Open a terminal and start the Node.js server:
```bash
cd dashboard
npm install
node server.js
```
The server will start on port `3000`.

## 2. Viewing the Dashboard
Open your laptop's web browser and go to:
```
http://localhost:3000
```
Here you will see the 6 static camera feeds looping, plus a 7th empty slot (`CAM-07 (LIVE)`) awaiting your mobile phone stream.

## 3. Streaming from your Phone (WebSockets Demo)
To stream live video from your phone's camera into the dashboard:
1. Find your laptop's local IP address (e.g., `192.168.1.100`).
2. Make sure your phone and laptop are connected to the **same Wi-Fi network**.
3. Open your phone's web browser (Chrome/Safari) and go to:
   ```
   http://<YOUR_LAPTOP_IP>:3000/streamer.html
   ```
4. Grant camera permissions if asked.
5. Tap the green **Start Broadcast** button.
6. Look at your laptop dashboard — your phone's live feed will instantly appear in the 7th camera slot!

## 4. Triggering Violations (Edge AI)
The backend exposes a `multipart/form-data` API endpoint at `POST /api/violations` for the autonomous edge Python model. 
When the model detects a violation, it pushes the JSON payload and video evidence to this endpoint. The server automatically saves it to MongoDB, saves the media, and instantly emits a `new_violation` WebSocket event so the officer sees it appear on the dashboard in real-time.
