# Schwyte-ML-Image-Enhancement

## Overview
This project implements an automated Twitter bot designed to enhance images. It continuously monitors Twitter mentions for a specific user, identifies tweets with attached low-resolution images, downloads these images, and then applies a Super-Resolution model (specifically a Residual Dense Network - RDN) to generate high-resolution versions. Finally, the bot posts these enhanced images back to Twitter as a reply to the original tweet, providing an automated image enhancement service via Twitter.

## Tech Stack
*   **Python**: Primary programming language.
*   **tweepy**: Python library for accessing the Twitter API.
*   **wget**: Utility for downloading files from the web.
*   **ISR (Image Super-Resolution)**: Python library for applying Super-Resolution models, specifically utilizing the RDN model.
*   **Pillow (PIL)**: Python Imaging Library for image manipulation.
*   **NumPy**: Library for numerical operations, used in image processing.

## Features
*   Monitors Twitter mentions for new image-containing tweets.
*   Automatically downloads low-resolution images from tweets.
*   Applies a Residual Dense Network (RDN) model for image super-resolution.
*   Uploads and posts the enhanced high-resolution images as replies on Twitter.
*   Operates continuously as an automated service.

## Project Structure
```
.
├── .gitignore
├── API.py              # Handles Twitter API interactions (fetching mentions, posting replies)
├── ISR_resolve.py      # Contains the image super-resolution logic using ISR library
├── main.py             # Main script orchestrating the entire process
├── README.md           # Project documentation
├── release.sh          # Likely a script for deployment or release procedures
├── requirements.txt    # Lists Python dependencies
└── .git/               # Git version control directory
```
*(Note: Temporary directories `tmp/low_res/` and `tmp/hi_res/` are created during runtime for image storage.)*

## Getting Started

### Prerequisites
*   Python 3.x
*   Twitter Developer Account with API v2 access
*   Twitter API credentials:
    *   Bearer Token
    *   API Key
    *   API Key Secret
    *   Access Token
    *   Access Token Secret

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Piyush/Schwyte-ML-Image-Enhancement.git
    cd Schwyte-ML-Image-Enhancement
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration
Set your Twitter API credentials as environment variables:
```bash
export BEARER_TOKEN="YOUR_BEARER_TOKEN"
export API_KEY="YOUR_API_KEY"
export API_KEY_SECRET="YOUR_API_KEY_SECRET"
export ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
export ACCESS_TOKEN_SECRET="YOUR_ACCESS_TOKEN_SECRET"
```

### Usage
Run the main script to start the Twitter bot:
```bash
python main.py
```
The bot will then continuously monitor mentions, process images, and post replies.

## Additional Info
This project serves as an example of integrating machine learning models with social media platforms for automated services.