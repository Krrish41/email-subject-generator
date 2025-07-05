import gradio as gr
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning import APIClient

# Replace <your-api-key> ; <your-project-id> & <your-region>
API_KEY = "<your-api-key>"
PROJECT_ID = "<your-project-id>"
REGION = "<your-region>"

wml_credentials = {
    "apikey": API_KEY,
    "url": f"https://{REGION}.ml.cloud.ibm.com"
}

client = APIClient(wml_credentials)
client.set.default_project(PROJECT_ID)

model = Model(
    model_id="ibm/granite-3-3-8b-instruct",
    params={
        "max_new_tokens": 64,
        "temperature": 0.3,
        "repetition_penalty": 1.1,
        "decode_method": "greedy",
        "stop_sequences": ["\n"]
    },
    credentials=wml_credentials,
    project_id=PROJECT_ID
)

def generate_subject(email_body):
    prompt = f"Write a catchy and relevant subject line for the following marketing email:\n\n{email_body}\n\nSubject:"
    try:
        response = model.generate(prompt=prompt)
        return response['results'][0]['generated_text'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

gr.Interface(
    fn=generate_subject,
    inputs=gr.Textbox(lines=6, label="Email Body"),
    outputs=gr.Textbox(label="Generated Subject Line"),
    title="📬 AI Email Subject Line Generator (IBM Granite)",
    description="Paste your email body to generate a compelling subject line using IBM Granite 3.3 8B."
).launch()
