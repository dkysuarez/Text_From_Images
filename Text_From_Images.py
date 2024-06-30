import streamlit as st
from PIL import Image
from pytesseract import *

# Configure the Tesseract executable path
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Title of the application
st.title('OCR Web App')

# Instructions section
st.markdown('### Instructions:')
st.write("1. Upload an image with text.")
st.write("2. The extracted text from the image will be displayed.")
st.write("3. You can copy the text to the clipboard by clicking the button.")

# Load an image from the user
uploaded_file = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file), caption='Selected Image', use_column_width=True)
    
    # Extract text from the image
    result = pytesseract.image_to_string(Image.open(uploaded_file))
    
    # Display the extracted text in a column
    if result:
        st.markdown('### Extracted Text:')
        st.write(result)
        
        # Button to copy the text to the clipboard
        if st.button('Copy Text'):
            if 'text_to_copy' not in st.session_state:
                st.session_state.text_to_copy = result
                st.write("Text copied to clipboard.")
            else:
                st.write("The text has already been copied to the clipboard.")
