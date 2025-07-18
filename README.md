# Life Story Generator

**Life Story Generator** is a simple interactive web app that allows users to share their personal stories and get AI-powered responses. It leverages **Google Gemini API** for text generation and is built with **Gradio** for a minimal, intuitive UI.

## Features

* **Summarize** → Get a short 2–3 sentence summary of your story.
* **Infer Mood** → Detects the overall mood or tone of your story.
* **Roast Me** → Provides a light-hearted, funny roast of your story.
* **Motivate Me** → Generates a positive and encouraging message based on your story.

## Tech Stack

* **Python**
* **Google Gemini API** (for AI text generation)
* **Gradio** (for the web interface)
* **Hugging Face Spaces** (for hosting)

## Live Demo

You can try the app here:
👉 **[Live on Hugging Face](https://binayaaaa-life-story-generator.hf.space)**

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/binayaginesh/Life_Story_Generator.git
   cd Life_Story_Generator
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Gemini API key:**

   * Create a `.env` file and add:

     ```
     GEMINI_API_KEY=your_api_key_here
     ```

5. **Run the app locally:**

   ```bash
   python app.py
   ```

## Project Structure

```
.
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .env.example        # Example environment file
└── README.md           # Project documentation
```

## Hosting

This project is deployed on **Hugging Face Spaces**, making it easy to share and demo.

## License

This project is open-source and available under the **MIT License**.

---


