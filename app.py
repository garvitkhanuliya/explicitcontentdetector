from flask import Flask, request, jsonify
from flask_cors import CORS
from nudenet import NudeDetector
from PIL import Image
import os
import tempfile

app = Flask(__name__)
CORS(app)

detector = NudeDetector()

UNSAFE_LABELS = {
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "ANUS_EXPOSED",
    "BUTTOCKS_EXPOSED",
}

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    suffix = os.path.splitext(file.filename)[1] or ".jpg"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        file.save(tmp.name)
        tmp_path = tmp.name

    try:
        with Image.open(tmp_path) as img:
            img_w, img_h = img.size

        detections = detector.detect(tmp_path)
        unsafe_detections = [d for d in detections if d["class"] in UNSAFE_LABELS]
        
        label = "EXPLICIT" if unsafe_detections else "SAFE"
        confidence = max((d["score"] for d in unsafe_detections), default=0.0)

        results = [{"label": d["class"], "score": round(d["score"], 3)} for d in unsafe_detections]

        return jsonify({
            "safe": len(unsafe_detections) == 0,
            "label": label,
            "confidence": round(confidence, 3),
            "detections": results,
            "blur_regions": unsafe_detections 
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(tmp_path): os.remove(tmp_path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)