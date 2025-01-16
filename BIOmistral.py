import streamlit as st
from llama_cpp import Llama

st.set_page_config(page_title="Medical Q&A with BioMistral (Quantized)", page_icon="🔬", layout="wide")

# Loading downloded quantized model
model_path =  r'C:\Users\hp\Contacts\pythonProject\datasets\Gemini\BioMistral-7B.Q4_K_S.gguf'
 
llm = Llama(model_path=model_path)

# this code is for  Sidebar - Title and Description
with st.sidebar:
    st.title("BioMistral Q&A")
    st.write("""
    Ask medical questions powered by the BioMistral model, a cutting-edge AI language model.
    This tool can help answer questions on a wide range of medical topics.
    """)


st.title("Medical Q&A with BioMistral (Quantized)")


response_placeholder = st.empty()

st.markdown("""
    <style>
    .question-box {
        padding: 10px;
        background-color: #f0f8ff;
        border-radius: 8px;
        font-size: 18px;
        color: #333;
    }
    .answer-box {
        padding: 15px;
        background-color: #f1f1f1;
        border-radius: 8px;
        font-size: 18px;
        color: #333;
    }
    .loading {
        font-size: 18px;
        color: #007bff;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


question = st.text_area("Enter your medical question here:", height=150, max_chars=500, key="input_text")


if st.button("Get Answer"):
    if question.strip():
        # Show a loading spinner while processing the question
        with response_placeholder.container():
            st.markdown('<p class="loading">Processing your question...</p>', unsafe_allow_html=True)
            response = llm(f"Q: {question}\nA: ", max_tokens=200, stop=["\n"])

          
            st.markdown(f'<div class="answer-box"><strong>Answer:</strong><br>{response["choices"][0]["text"].strip()}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid question to get an answer.")
else:
    st.markdown('<p class="loading">Enter a medical question and click "Get Answer" to receive a response.</p>', unsafe_allow_html=True)

## this could be optional 
st.markdown("""
    <div style="text-align: center; font-size: 12px; color: #888;">
    Powered by BioMistral Model (Quantized) with Llama.cpp
    </div>
""", unsafe_allow_html=True)


