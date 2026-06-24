# AI Study Buddy Terminal Application

An interactive command-line application designed to supercharge your learning workflows. Powered by Google Gemini and the `google-genai` SDK.

## Features
- **Concept Explanations**: Ask anything and receive highly optimized breakdowns.
- **Quiz Generation**: Instantly build evaluation prompts directly inside your terminal session.
- **Study Schedules**: Creates and tracks local day-by-day study calendars.
- **Flashcard Engine**: Generates and preserves custom memory blocks using active Function Calling hooks.

## Setup Guide

1. Clone or navigate into the repository.
2. Build your localized Python isolation layer:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Upgrade packages to access the new SDK platform:
   ```bash
   pip install -q -U google-genai
   ```
4. Bind your credential tokens provided by [Google AI Studio](https://google.com):
   ```powershell
    $env:GEMINI_API_KEY="AIzaSyYourKeyHere..."
   ```

## How to Run
Fire up the main runtime environment:
```powershell
python main.py
```
