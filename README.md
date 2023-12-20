# EIR (Emergency Imperative Response) Project

## Overview

EIR is a revolutionary project developed by Shashank Singh and Pranay Tiwari, designed to act as a virtual paramedic during emergencies. The program allows users to send a short video and live location to nearby hospitals and police stations via email. Additionally, an AI system provides step-by-step guidance on life-saving measures, enhancing the user's ability to respond effectively to critical situations.

## Purpose

The primary goal of EIR is to streamline emergency response procedures by leveraging technology. By combining GPS tracking, video recording, and AI-driven voice interaction, the project aims to provide immediate assistance and ensure that crucial information reaches the relevant authorities promptly.

## Features and Functionalities

1. **GPS Tracking:**
   - Retrieves the user's live location using the freegeoip.app API.
   - Includes the location data in emergency emails.

2. **Video Recording:**
   - Captures a 15-second video using the device's camera.
   - Saves the recorded video as 'Video_Output.mp4' for attachment in emergency emails.

3. **AI Voice Interaction:**
   - Utilizes text-to-speech and speech recognition technologies.
   - Guides users through specific emergency scenarios, providing essential information and steps.

## Installation Instructions

Follow these steps to set up and run the EIR project on your machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/EIR-Project.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd EIR-Project
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Prerequisites

Ensure you have the following prerequisites installed on your machine:

- Python 3.x
- Requests library
- OpenCV (cv2)
- SpeechRecognition
- pyttsx3
- BeautifulSoup4

## Usage Guidelines

1. **Run the Program:**
   ```bash
   python main.py
   ```

2. **Follow Voice Prompts:**
   - Respond to the AI's voice prompts during emergency scenarios.
   - Provide necessary information or follow the instructions to send an emergency email.

## Contribution Guidelines

If you wish to contribute to the EIR project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

Feel free to contribute to the project and enhance its functionality!

---

**Note:** Ensure that you have Python installed, along with the required external libraries specified in the prerequisites section, before running the program.
