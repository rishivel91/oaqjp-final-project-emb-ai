# Final Project

## Emotion Detection using IBM Watson NLP

An educational Flask application that analyzes written text and reports five emotion scores: anger, disgust, fear, joy, and sadness. It also identifies the dominant emotion.

### Project structure
- \`EmotionDetection/emotion_detection.py\`: Watson NLP integration, formatted output, and HTTP 400 handling
- \`EmotionDetection/__init__.py\`: Python package
- \`emotion_detection.py\`: compatibility import for the initial lab exercises
- \`test_emotion_detection.py\`: repeatable unit tests (with mocked Watson responses)
- \`server.py\`: Flask web server and blank-input error handling
- \`templates/index.html\` and \`static/mywebscript.js\`: supplied web interface
- \`evidence/\`: source snapshots for the different assignment stages

### Lab usage
In your IBM Skills Network lab:
\`\`\`bash
cd /home/project/final_project
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_emotion_detection.py
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
python3 server.py
\`\`\`

Use the lab's port 5000 preview to open the application.

**Note:** The Watson NLP endpoint may only be reachable within the IBM Skills Network lab. Unit tests use mocked server responses so they can run without the remote service; these unit tests do not prove that the live Watson service is available. For assessment screenshots and terminal output, run the application in the actual lab and capture authentic results.
