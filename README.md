#  Explicit Content Detector (SafeScan)

**Explicit Content Detector** is a specialized security application developed to provide automated, real-time protection against sensitive visual media. It is built for the MCA 2nd Semester curriculum at **Uttaranchal University**.

##  Project Overview
In the contemporary digital era, the risk of "cyberflashing" on platforms like WhatsApp and Telegram is a major vulnerability. This tool acts as a proactive defense:
*   **Deep Pixel Analysis:** Uses the **NudeNet** library to identify anatomical patterns.
*   **Privacy-by-Design:** All processing occurs in **Volatile Memory (RAM)**; images are never saved.
*   **Global Shielding:** Automatically applies a Gaussian blur to detected explicit content.

## How to Run

###  Prerequisites
First, install the required Python libraries:
```bash
pip install flask flask-cors nudenet opencv-python pillow
Start the Backend
Open your terminal in the project folder and run the server:
```bash
python app.py

then run the html file
