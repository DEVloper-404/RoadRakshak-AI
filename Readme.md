# 🚔 RoadRakshak: AI-Powered Traffic Enforcement Dashboard

RoadRakshak is an intelligent, high-performance traffic monitoring and enforcement dashboard prototype designed to demonstrate how AI computer vision can automate traffic violation detection, track repeat offenders, and streamline the fine issuance workflow (Challans) in real-time. 

Built with a sleek, low-latency, and authoritative interface, this prototype demonstrates a live surveillance environment complete with simulated real-time AI computer vision bounding boxes, behavioral tracking analytics, and legal action generation mechanisms.

---

## 🚀 Key Features

### 📷 1. Live Camera Streams with Real-Time AI Detection
*   **Dynamic Canvas Feeds:** Features a multi-camera grid layout (CAM-01 to CAM-06) operating smoothly on HTML5 canvas-driven vehicle simulation engines.
*   **AI Overlay Simulation:** Showcases live bounding boxes, confidence percentages, license plate extractions, and active scanning lines.
*   **Violation Callouts:** Immediately highlights an in-progress violation directly on the video window with instant visual anchors and contextual reasonings (e.g., *No Helmet*, *Speed Limit Violation*).

### ⚠️ 2. Live Automated Violation Ticker
*   **Dynamic Stream:** A continuous, real-time incoming feed of violations where fresh alerts smoothly slide into the top of the queue.
*   **Contextual Details:** Displays critical metadata at a glance: Challan ID, Number Plate (styled like an authentic Indian RTO vehicle plate), Violation Type, Location, and Time.
*   **Interactive Modal Inspection:** Clicking any violation queue expands a rigorous overview drawer highlighting AI-captured evidence photos, accuracy metrics, and direct execution actions.

### 🚨 3. High-Risk Emergency Alerts
*   **Pulsing Radar Alerts:** Isolatess critical, life-threatening, or heavily unlawful occurrences (e.g., *Wrong-Way Driving on Highways*) using glowing radar indicators.
*   **Localized Contextualization:** Includes exact location tracking parameters and an isolated multi-frame photo strip mimicking an AI vehicle identification engine sequence.

### 🏆 4. Repeat Violators Leaderboard
*   **Offender Ranking:** Tracks and displays an analytics table of chronic traffic rules violators complete with tiered podium distribution medals (🥇, 🥈, 🥉).
*   **Violation Distributions:** Includes horizontal analytical distribution bars mapping individual violation counts to help highway management identify dangerous trends.

### 📋 5. Actionable Legal Workflows
*   **Instant Challan Generator:** One-click automated rendering of a official, printable state challan receipt featuring standardized regional headers, barcode generation, vehicle details, legal act breakdowns, fine structures, and authority validation badges.
*   **Multi-Channel Communication Portal:** An integrated overlay module to instantly dispatch automated notifications via SMS, WhatsApp, or Email channels directly to the registered vehicle owner's mobile network.

---

## 🛠️ Tech Stack

*   **Frontend Core:** Semantic HTML5, CSS3 Custom Variables (CSS Architecture)
*   **Typography:** Google Fonts (`Inter` for UI, `JetBrains Mono` for alphanumeric plate strings & telemetry data)
*   **Simulation Engine:** Pure Vanilla JavaScript (utilizing Canvas API for vehicle paths, object collision logic bounding boxes, and reactive interval engines)
*   **Icons:** Scalable Vector Graphics (Inline SVGs)

---

## 📁 Repository Structure

```text
├── roadrakshak_dashboard.html   # Main monolithic app prototype (All-in-one distribution)
└── README.md                    # Project documentation