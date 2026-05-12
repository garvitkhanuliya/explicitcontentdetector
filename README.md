# Explicit Content Detector 

**Explicit Content Detector** is a specialized security application developed to provide automated, real-time protection against sensitive visual media. It utilizes Machine Learning to perform deep pixel analysis and apply a "Safe Preview" blur before a user is exposed to harmful content.

##  Project Overview
In the contemporary digital era, the risk of accidental exposure to explicit imagery ("cyberflashing") on platforms like WhatsApp and Telegram is a major vulnerability. This project bridges that safety gap by:
*   **Deep Pixel Analysis:** Moving beyond metadata to interpret actual visual features.
*   **Proactive Shielding:** Triggering a Gaussian blur using the HTML5 Canvas API.
*   **Privacy-Centric:** Processing data entirely in volatile memory (RAM) so images are never saved.

## 🚀 Key Features
*   **ML-Powered Detection:** Integrated `NudeNet` library for high-accuracy classification.
*   **Real-Time Feedback:** Dynamic logs showing detection labels and confidence scores.
*   **Custom Thresholding:** Sensitivity toggle to balance security and false positives.
*   **Privacy-by-Design:** No cloud intervention; all processing happens locally.

## 🛠️ Tech Stack
*   **Backend:** Python 3.13, Flask
*   **AI/ML:** NudeNet (Deep Learning), OpenCV, Pillow
*   **Frontend:** HTML5, CSS3 (Cyber-Security Dark Theme), JavaScript (ES6+)
*   **Tools:** VS Code, Git

## 📂 System Architecture
The project follows a **Client-Server Architecture**:
1.  **Frontend:** Manages user interaction and instantaneous Gaussian blurring.
2.  **Backend:** Flask server handles image ingestion and neural network inference.

## 💻 Installation & Setup

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/garvitkhanuliya/explicitcontentdetector.git

   pip install flask flask-cors nudenet opencv-python pillow
   3. **Run the Application:**
   * **Automatic:** Double-click `run_all.bat`.
   * **Manual:** Run `python app.py` and open `index.html` in your browser.

## 🛡️ Security Measures
*   **Zero-Persistence:** Scanned images stay in RAM and are cleared immediately after inference.
*   **Localhost Isolation:** No third-party APIs or cloud storage, eliminating MITM attack risks.
*   **Input Sanitization:** Validates "Magic Bytes" to ensure files are genuine images, not malicious scripts.

## 🔮 Future Scope
*   **Real-Time Video Analysis:** Scanning live streams at 30+ FPS using GPU acceleration.
*   **Browser Extension:** Background protection for WhatsApp Web and Instagram.
*   **Content Substitution:** Replacing explicit images with neutral placeholders via Generative AI.