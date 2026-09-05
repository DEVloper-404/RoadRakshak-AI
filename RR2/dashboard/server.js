const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const mongoose = require('mongoose');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const Violation = require('./models/Violation');

const app = express();
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

// Database Connection
mongoose.connect('mongodb://127.0.0.1:27017/roadrakshak', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log("MongoDB Connected"))
  .catch(err => console.log("MongoDB Connection Error:", err));

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Multer Storage config for media uploads
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'public/uploads/')
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, uniqueSuffix + path.extname(file.originalname))
  }
});
const upload = multer({ storage: storage });

// API Endpoints
// GET Violations
app.get('/api/violations', async (req, res) => {
  try {
    const violations = await Violation.find().sort({ createdAt: -1 });
    res.json({ files: violations });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// POST Violation from Autonomous Edge Model
app.post('/api/violations', upload.single('media'), async (req, res) => {
  try {
    const data = JSON.parse(req.body.payload);
    
    if (req.file) {
      data.image = 'uploads/' + req.file.filename; // Map to public/uploads
    }

    // Set ts
    data.ts = new Date().toTimeString().slice(0, 8);

    const newViolation = new Violation(data);
    await newViolation.save();

    // Broadcast the new violation via WebSockets instantly
    io.emit('new_violation', newViolation);

    res.status(201).json({ message: 'Violation recorded successfully', id: newViolation.id });
  } catch (error) {
    console.error("Error saving violation:", error);
    res.status(500).json({ error: error.message });
  }
});

// Update Violation Status/Plate
app.put('/api/violations/:id', async (req, res) => {
  try {
    const updated = await Violation.findOneAndUpdate(
      { id: req.params.id }, 
      req.body, 
      { new: true }
    );
    res.json(updated);
  } catch(error) {
    res.status(500).json({ error: error.message });
  }
});

// WebSocket Streaming Logic
io.on('connection', (socket) => {
  console.log('Client connected:', socket.id);

  // Broadcaster (phone) sending video frames
  socket.on('stream_frame', (frameData) => {
    // Broadcast instantly to all viewers except the sender
    socket.broadcast.emit('live_stream', frameData);
  });

  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
