# Node.js and MongoDB Tech Stack

We chose to build the central dashboard backend using Node.js and MongoDB, deviating from the initial recommendation of FastAPI and SQLite. This decision provides a robust Document-based database (MongoDB) suitable for handling unstructured/query-based violation metadata sent from the edge devices, and aligns the stack with real-time streaming capabilities (Node.js) required for our live multi-camera API endpoints.
