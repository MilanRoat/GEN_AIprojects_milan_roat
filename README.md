# GEN_AIprojects_milan_roat
this repository contains GEN_AI based Projects (BY MILAN ROAT)
### Planto.AI Vs Code Extension (using Langchain) 
planto.extension
this file contains original files created by - Milan Roat for a vs-code extension (by command name - 'Get Suggestion')
API Key used - GROQ API (the API key in extension.ts is empty for now . use your own key to get results) Model used - llama3-8b-8192
the main logic code for a this copilot to help/give suggestion of selected text is in extension.ts file.
#### to use this extension - Download Planto.ZIP file, follow the steps, save and compile all files -> press f5 now the window opened will have the extension loaded .
Features - 
->open any code file in any language
->select some code lines which you want to get results
->use 'Get Suggesion' command from extensions window . (i.e. press ctrl+shift+P)
->the results will be added to the code file.
the added screenshots below are while using this copilot for a selected code 

## 1] FINE_tuning_llama_model:
this project is focused on fine tuning llama 2 model 
based on a custom dataset
original dataset link - https://www.google.com/url?q=https%3A%2F%2Fhuggingface.co%2Fdatasets%2Ftimdettmers%2Fopenassistant-guanaco
this data set is reformed and out of 10k rows , only 1k rows are taken due to memory resource constraint
reformatted dataset based on llama template - https://huggingface.co/datasets/mlabonne/guanaco-llama2-1k

### to run this code , the system needs to be connected to a GPU


## 2] BioMistral Medical Query Generator
This project demonstrates the use of a quantized version of the BioMistral-7B model to generate responses for medical queries. The application provides an efficient and user-friendly interface for interacting with the model, enabling the exploration of medical text generation. The model is fine-tuned for medical applications, ensuring precise and reliable responses.

### Key Features
Medical Text Generation: Generates contextually accurate medical responses using the BioMistral-7B model.
Streamlit Integration: A responsive interface for querying the model.
Quantized Model Deployment: Utilizes a  quantized version of BioMistral-7B for efficient performance

Libraries and Tools
llama-cpp-python: To run the quantized BioMistral model locally.
Streamlit: For creating an interactive web interface.


## 3] Youtube Transcript generator 
This YouTube Transcript Summarizer is  using Streamlit, integrating the YouTube Transcript API and Google Gemini
Pro API to extract and generate concise, point-wise summaries of video content in multiple languages.

To Enhanced user interactivity , implemented features such as summary download options, and detailed transcript analysis,
optimizing accessibility and usability







