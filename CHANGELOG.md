# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
- **Copied Frontend UI**: Migrated the visual HTML/CSS/JS frontend from `rr demo` to `RR2/dashboard/public`. This serves as the foundation for the real-time WebRTC dashboard.
- **Node.js Initialization**: Initialized `package.json` inside `RR2/dashboard` to manage isolated backend dependencies.
- **Architectural Setup**: Established the `RR2` workspace structure (`dashboard` and `model` folders), wrote `CONTEXT.md` to define domain terminology, and documented the Tech Stack switch to Node.js/MongoDB in `docs/adr/0001-nodejs-mongodb-stack.md`.
