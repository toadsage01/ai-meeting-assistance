# AI Meeting Assistance
**A generative AI pipeline that transforms monotonous meeting transcripts into expressive, human-like audio summaries and highlights.**

*This project moves beyond simple speech synthesis. It introduces an "AI Director" to interpret the context of a meeting, guide a voice engine on how to deliver key moments, and create engaging, natural-sounding audio recaps.*

## 😟 The Problem
After a long meeting, no one wants to read through a lengthy, dry transcript. Standard Text-to-Speech (TTS) systems can read it aloud, but they fail to capture the emphasis, tone, and important moments of the conversation. This results in flat, robotic audio that makes it difficult to quickly grasp the key takeaways and action items.

## ✨ Solution
We architected a two-stage AI pipeline that separates the task of understanding from the task of speaking:

1. The AI Director (The "Brain"): We use a powerful Large Language Model (Google Gemini) as a reasoning engine. Instead of just passing text to be read, we prompt the model to first interpret the meeting transcript for key decisions, action items, and emotional context. It then generates a layer of performance metadata—a "script" with instructions on where to pause, which words to emphasize, and the appropriate tone to use for different sections.

2. The Voice Engine (The "Talent"): The summarized text, now enriched with the AI Director's performance script, is passed to a high-fidelity voice synthesis engine (like Google's WaveNet). This engine follows the instructions to render a final audio file that sounds natural, expressive, and highlights the most important parts of the meeting.

This separation of concerns allows for a much richer and more useful audio summary.

## ⚙️ How It Works
The data flow is orchestrated through a serverless backend, making the system scalable and efficient.

```
[Meeting Transcript Text]
       │
       ▼
[Serverless Function (Vercel)]
       │
       ├─► 1. Call Gemini API (AI Director)
       │      - Summarize, find action items, analyze context
       │      - Generate performance metadata (e.g., SSML)
       │
       ▼
[Enriched Summary + Metadata]
       │
       ├─► 2. Call Google Cloud TTS API (Voice Engine)
       │      - Synthesize audio based on instructions
       │
       ▼
[Expressive Audio Summary (.mp3)]
```

## 🛠️ Tech Stack
This project combines modern AI services with a robust full-stack architecture.

AI & Machine Learning:

Reasoning Engine: Google Gemini API

Synthesis Engine: Google Cloud Text-to-Speech (WaveNet)

Core Logic: Python

Backend:

Runtime: Node.js

Deployment: Vercel Serverless Functions

Frontend (Example Interface):

HTML, CSS, JavaScript

## 🚀 Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
`Node.js` and `npm` installed

`Python` installed

`API keys` for Google Gemini and Google Cloud Platform

### Installation
* #### Clone the repo:

`git clone https://github.com/your-username/ai-meeting-assistance.git`

* #### Install NPM packages:

`cd ai-meeting-assistance`
`npm install`

* #### Install Python packages:

`pip install -r requirements.txt`

* #### Configure Environment Variables:
Create a `.env` file in the root directory and add your API keys:

```
GEMINI_API_KEY='YOUR_GEMINI_API_KEY'
GOOGLE_APPLICATION_CREDENTIALS='path/to/your/gcp-service-account.json'
```

* #### Run the development server:

`npm run dev`

Open `http://localhost:3000`[http://localhost:3000] to view it in the browser.

## 🔮 Future Work
This project serves as a strong foundation. Future enhancements could include:

1. Action Item Extraction: Automatically identify and list action items separately from the summary.

2. Real-time Transcription & Summarization: Implement WebSocket for live meeting assistance.

3. Speaker Identification: Enhance the AI Director to recognize different speakers and use unique voices for each in the summary.

4. Integration with Calendar/Email: Automatically send audio summaries and action items to meeting attendees.