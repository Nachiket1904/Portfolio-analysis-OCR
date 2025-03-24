import streamlit as st
import base64
from groq import Groq
from PIL import Image
import io

# Groq API Configuration
GROQ_API_KEY = "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"  # Replace with your actual API key

def encode_image(image_bytes):
    return base64.b64encode(image_bytes).decode("utf-8")

def extract_text_from_image(image_bytes):
    client = Groq(api_key=GROQ_API_KEY)
    base64_image = encode_image(image_bytes)
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract the text from this image in a structured Markdown format."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )
    
    return chat_completion.choices[0].message.content

# Page configuration
st.set_page_config(
    page_title="Gemma-3 OCR",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description in main area
# st.markdown("""
#     # <img src="data:image/png;base64,{}" width="50" style="vertical-align: -12px;"> Gemma-3 OCR
# """.format(base64.b64encode(open("./assets/gemma3.png", "rb").read()).decode()), unsafe_allow_html=True)

# Add clear button to top right
col1, col2 = st.columns([6,1])
with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.rerun()

st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Gemma-3 Vision!</p>', unsafe_allow_html=True)
st.markdown("---")

# Move upload controls to sidebar
with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
        
        if st.button("Extract Text 🔍", type="primary"):
            with st.spinner("Processing image..."):
                try:
                    image_bytes = uploaded_file.getvalue()
                    extracted_text = extract_text_from_image(image_bytes)
                    st.session_state['ocr_result'] = extracted_text
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")

# Main content area for results
if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else:
    st.info("Upload an image and click 'Extract Text' to see the results here.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Groq Vision Model | [Report an Issue](https://github.com/patchy631/ai-engineering-hub/issues)")
