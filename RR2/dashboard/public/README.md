# RoadRakshak — Traffic Control Room Dashboard

A four-page operator dashboard for AI traffic-violation enforcement: live camera
wall, detection feed, violation records, and enforcement analytics.

**This bundle is self-contained.** No `pip install`, no internet, no database,
no web framework. Python's standard library serves it and the pages use plain
HTML/CSS/JavaScript.

---

## 1. Requirements

| | |
|---|---|
| **Python** | 3.8 or newer (`python3 --version`) |
| **Browser** | Firefox, Chrome, or Chromium |
| **Disk** | ~40 MB |
| **Network** | None — runs fully offline |

Almost every Linux distribution ships Python 3 already. Check:

```bash
python3 --version
```

If it is missing:

```bash
sudo apt update && sudo apt install -y python3        # Debian / Ubuntu
sudo dnf install -y python3                           # Fedora / RHEL
sudo pacman -S python                                 # Arch
```

You do **not** need `pip`, `venv`, or any package.

---

## 2. Run it

```bash
cd roadrakshak-dashboard
./run.sh
```

or equivalently:

```bash
python3 serve.py
```

Your browser opens at **http://localhost:8090**. Stop with **Ctrl+C**.

`run.sh` just finds a working Python and hands over — use either.

### Options

```bash
./run.sh --port 9000          # different port
./run.sh --no-browser         # headless: do not try to open a browser
./run.sh --host 0.0.0.0       # reachable from other machines
```

---

## 3. Running on a headless machine

By default the dashboard binds to `127.0.0.1`, which is **local only**. To reach
it from another machine, bind to all interfaces:

```bash
./run.sh --host 0.0.0.0 --no-browser
```

Find the machine's address and open `http://<that-ip>:8090` from your laptop:

```bash
hostname -I
```

Open the port if a firewall is active:

```bash
sudo ufw allow 8090/tcp        # Ubuntu / Debian
sudo firewall-cmd --add-port=8090/tcp --permanent && sudo firewall-cmd --reload
```

> Bind to `0.0.0.0` only on a trusted network. There is no authentication —
> anyone who can reach the port can see the dashboard.

---

## 4. The four pages

| Page | What it shows |
|---|---|
| **Camera Wall** | Four live feeds with a dropdown on each panel to switch among all six cameras. Monitoring only — no alerts here. |
| **Detections** | The newest violation with the vehicle ringed, plus camera, location, plate, source clip and the time it happened. Older ones queue beside it. |
| **Violations** | Every record in a table. **Re-enter plate** on any row. Click a row for evidence and actions. |
| **Analytics** | Worst location, totals, fine value, and ranked bars by location and violation type. |

Violations appear **as the videos play**, timed to the moment the vehicle is on
screen. Give it about ten seconds after loading.

---

## 5. Changing the data

### Number plates

The **filename is the number plate**. Rename a file in `violation/` and reload
the page — nothing to rebuild.

```
<PLATE>__<VIOLATION>__<CAMERA>__<VEHICLE>.jpg

UP39T9319__OVER_SPEEDING__CAM-02__GOODS.jpg
CG15E1557__NO_HELMET__CAM-01__BIKE.jpg
UNKNOWN__WRONG_WAY__CAM-03__BIKE.jpg
```

- **Violation:** `NO_HELMET` · `TRIPLE_RIDING` · `WRONG_WAY` · `OVER_SPEEDING`
- **Camera:** `CAM-01` … `CAM-06`
- **Vehicle:** `BIKE` · `CAR` · `AUTO` · `GOODS` · `TRUCK` · `BUS`

`UNKNOWN` as the plate means OCR could not read it. The record still appears,
shows a dashed **NOT READ**, and **refuses to generate a challan** until an
officer supplies the plate with *Re-enter plate*.

See `violation/README.md` for the full convention.

### Camera names and locations

Edit `demo_data.json` — each camera has an `id`, `location` and `city`.

### Challans

**Generate Challan** opens `challan.html` as a printable A4 document. Nothing is
dispatched from the dashboard; an officer reviews it and prints or saves a PDF.

---

## 6. Run it as a service (optional)

To keep it running after you log out:

```bash
sudo tee /etc/systemd/system/roadrakshak.service > /dev/null <<'EOF'
[Unit]
Description=RoadRakshak Dashboard
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/full/path/to/roadrakshak-dashboard
ExecStart=/usr/bin/python3 serve.py --port 8090 --host 0.0.0.0 --no-browser
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now roadrakshak
systemctl status roadrakshak
```

Replace `YOUR_USERNAME` and the path first.

---

## 7. Troubleshooting

| Problem | Fix |
|---|---|
| `cannot bind ... Address already in use` | The server says which port and suggests the next one. Or free it: `sudo lsof -i :8090` then `kill <PID>`. |
| Browser does not open | Normal on a headless machine. Open `http://localhost:8090` yourself, or use `--no-browser`. |
| Panels are black | Check the six files exist in `media/videos/`. They are H.264, which every modern Linux browser plays. |
| No violations appear | Wait ~10 seconds — they are timed to the video. Confirm `violation/` holds `.jpg` files, and check `http://localhost:8090/api/violations` returns a list. |
| Feeds stop when you switch tabs | Already handled: the wall stays loaded and a watchdog resumes any paused video. |
| `python3: command not found` | Install Python 3 — see section 1. `run.sh` prints the command for your distro. |
| `needs Python 3.8 or newer` | An old Python is first on your `PATH`. Run `python3 serve.py` explicitly. |
| Reachable locally but not from another machine | You need `--host 0.0.0.0`, and the firewall port opened. |
| Permission denied on `serve.py` | Run `python3 serve.py` rather than `./serve.py`, or `chmod +x serve.py`. |

---

## 8. What is in this folder

```
roadrakshak-dashboard/
├── README.md            this file
├── run.sh               launcher — finds Python, then runs serve.py
├── serve.py             the server — Python standard library only
├── index.html           the four-page dashboard
├── challan.html         printable A4 challan
├── demo_data.json       cameras, locations, violation types and fines
├── media/videos/        six camera clips (H.264)
└── violation/           evidence images, named by number plate
```

---

## Note on scope

This bundle runs the **dashboard**. The detection pipeline — YOLO, tracking,
plate OCR and the training tools — lives in the main project under `edge/` and
`app/`, and needs PyTorch, Ultralytics, OpenCV and EasyOCR. The dashboard is
deliberately separated so it can run anywhere, including a machine with no
GPU and no internet.
