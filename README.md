# Py-Wedding-Image-Rclone-Uploader

*Automated Google Drive Image Uploader for Events*

![Last Commit](https://img.shields.io/github/last-commit/pingmyheart/Py-Wedding-Image-Rclone-Uploader)
![Repo Size](https://img.shields.io/github/repo-size/pingmyheart/Py-Wedding-Image-Rclone-Uploader)
![Issues](https://img.shields.io/github/issues/pingmyheart/Py-Wedding-Image-Rclone-Uploader)
![Pull Requests](https://img.shields.io/github/issues-pr/pingmyheart/Py-Wedding-Image-Rclone-Uploader)
![License](https://img.shields.io/github/license/pingmyheart/Py-Wedding-Image-Rclone-Uploader)
![Top Language](https://img.shields.io/github/languages/top/pingmyheart/Py-Wedding-Image-Rclone-Uploader)
![Language Count](https://img.shields.io/github/languages/count/pingmyheart/Py-Wedding-Image-Rclone-Uploader)

## 🚀 Overview
This project provides a robust backend service for uploading images to a Google Drive folder
using [rclone](https://rclone.org/). Designed for event photo collection (e.g., weddings), it allows guests to upload
images via a simple HTTP API. Images are automatically and securely transferred to a designated Google Drive folder at
regular intervals.

## ✨ Features

- 📷 **Multi-image Upload:** Upload multiple images in a single request.
- 🔒 **Secure & Unique Filenames:** Each image is saved with a unique UUID-based filename.
- 🚀 **Automated Uploads:** Images are periodically uploaded to Google Drive using rclone.
- 🧩 **Docker-Ready:** Easily deployable as a Docker container.
- 🛡️ **Health & Readiness Endpoints:** For easy monitoring and orchestration.
- ⚡ **Concurrent Uploads:** Fast, multi-threaded file transfers.

## Tech Stack

- Python 3
- Flask (REST API)
- APScheduler (Task scheduling)
- rclone (Google Drive integration)
- Docker