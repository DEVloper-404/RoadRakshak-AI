const mongoose = require('mongoose');

const violationSchema = new mongoose.Schema({
  id: { type: String, required: true, unique: true },
  plate: { type: String, default: null },
  plateSource: { type: String, default: 'ocr' },
  camera: { type: String, required: true },
  location: { type: String, required: true },
  city: { type: String, default: '' },
  at: { type: Number, default: 0 },
  type: { type: String, required: true },
  label: { type: String, required: true },
  severity: { type: String, default: 'amber' },
  fine: { type: Number, default: 0 },
  section: { type: String, default: '' },
  note: { type: String, default: '' },
  vehicle: { type: String, default: 'Two Wheeler' },
  speed: { type: Number, default: null },
  limit: { type: Number, default: null },
  confidence: { type: Number, default: 0 },
  sourceVideo: { type: String, default: '' },
  capturedAt: { type: String, default: '' },
  occurredAt: { type: String, default: '' },
  image: { type: String, required: true },
  status: { type: String, default: 'PENDING' },
  ts: { type: String, default: '' },
  edited: { type: Boolean, default: false }
}, { timestamps: true });

module.exports = mongoose.model('Violation', violationSchema);
