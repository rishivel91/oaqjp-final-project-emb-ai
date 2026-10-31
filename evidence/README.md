# Assessment evidence

The files in this folder are source-code snapshots for separate graded stages.
- \`2a_emotion_detection.py\`: initial API request stage
- \`3a_output_formatting.py\`: API result formatting stage

For the remaining evidence, run commands in the actual course lab under
\`/home/project/final_project\` and save authentic outputs:

\`\`\`bash
python3 -c "from emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
python3 -m unittest test_emotion_detection.py -v
python3 -m pylint server.py
python3 server.py
\`\`\`

- \`2b_application_creation\`, \`3b_formatted_output_test\`, \`4b_packaging_test\`, \`5b_unit_testing_result\`, and \`8b_static_code_analysis\`: authentic logs, not examples
- \`6b_deployment_test.png\`: screenshot of the live application's emotion response
- \`7c_error_handling_interface.png\`: screenshot of the blank-input error message

Tests in \`test_emotion_detection.py\` use mocks so they can run without live Watson access; this does not confirm that the remote service is working.
