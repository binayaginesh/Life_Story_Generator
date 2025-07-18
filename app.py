import google.generativeai as genai
from dotenv import load_dotenv
import gradio as gr 
import os

load_dotenv()  
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def chat(user_message):
    response = model.generate_content(user_message)
    return response.text

def summarise_story(story):
    prompt = f"summarize this in 2-3 sentences:\n\n{story}"
    return chat(prompt)

def infer_story(story):
    prompt=f"infer the mood of this story:\n\n{story}"
    return chat(prompt)

def roast_me(story):
    prompt=f"Roast this story in a funny but light-hearted way. Don’t be too mean!\n\n{story}"
    return chat(prompt)
    
def motivate_me(story):
    prompt=f"Motivate me with a positive message based on this story:\n\n{story}"
    return chat(prompt)

with gr.Blocks(css="""
    .gradio-container {text-align: center;}
    .center-text h1 {text-align: center;}
    .spacer {margin-top: 20px; margin-bottom: 20px;}
""") as demo:

   
    gr.Markdown("<h1 class='center-text'> ✨ Life Story Generator ✨")  # Title
    gr.Markdown("<div class='spacer'></div>")
    story_input = gr.Textbox(label="Enter your story", placeholder="Type your story here...")

    gr.Markdown("<div class='spacer'></div>")
    with gr.Row():
        summarise_button = gr.Button("Summarise")
        infer_button = gr.Button("Infer Mood")
        roast_button = gr.Button("Roast Me")
        expand_button = gr.Button("Motivate Me")
        
    gr.Markdown("<div class='spacer'></div>")    
    output_box = gr.Textbox(label="Result")
    
    expand_button.click(
    fn=motivate_me,
    inputs=story_input,
    outputs=output_box
    )
    
    roast_button.click(
    fn=roast_me,
    inputs=story_input,
    outputs=output_box
    )
    
    infer_button.click(
    fn=infer_story,
    inputs=story_input,
    outputs=output_box
    )
    
    summarise_button.click(
    fn=summarise_story,
    inputs=story_input,
    outputs=output_box
    )

demo.launch()
    
    
    
