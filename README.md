# mental_health_chatbot

# Problem Statement
In today’s digital and high-paced lifestyle, individuals often experience anxiety, depression, and emotional distress. However, many people hesitate to talk about their struggles due to stigma or lack of access to professional help. There’s a strong need for an empathetic, private, and accessible solution for mental wellness.

# Proposed Solution
The solution is a console-based Mental Health Chatbot that emulates supportive conversations using predefined emotional intelligence, natural language understanding, and coping strategies. Unlike standard AI chat interfaces, this bot is tailored for sensitive mental health support and includes session tracking, emotion detection, and context-aware responses.

# System Approach
Programming Language: Python
UI Type: Console-based Interface
Core Features:
Emotion detection using keyword matching
Crisis keyword recognition and support prompts
Mood rating system (1–10)
Personalized responses and coping strategies
Session summaries and feedback
Libraries Used: datetime, random, re, json

# Algorithm & Deployment
Emotion Detection Algorithm:
Extracts emotional keywords from user input
Scores the input against predefined emotional dictionaries (e.g., anxiety, depression, anger)
Selects the dominant emotion for response generation
Crisis Detection:
Scans for critical phrases indicating risk
Immediately returns emergency help suggestions
Mood Check-in:
Asks users to rate their mood
Adapts responses and coping strategies based on the rating

# Deployment:
Executed via local Python script on any machine
Can be easily migrated to a GUI (Streamlit) or API (FastAPI) for web-based use

# Result
Successfully simulates a safe, interactive emotional support environment
Detects emotional tones from conversation and reacts empathetically
Handles mood tracking and session summaries to provide feedback
Offers targeted coping strategies based on emotional state
Handles critical mental health risk scenarios and provides crisis support contacts

# Conclusion
The chatbot provides a simple yet powerful tool to initiate emotional self-checks and support. It encourages users to reflect on their mental state in a non-judgmental, private setting. By simulating human-like support, it lowers the barrier for those hesitant to speak to a counselor initially.

# Future Scope
Web Interface: Integrate with Streamlit or Flask for a UI-based experience
Voice Assistant: Add speech-to-text and text-to-speech support for accessibility
Chat History Export: Enable users to save their conversation for self-reflection or sharing with professionals
Mobile App: Deploy on Android via Kivy or WebView for accessibility
AI Integration: Replace rule-based emotion detection with fine-tuned transformer models for better accuracy





