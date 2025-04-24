import ollama
import streamlit as st
from PIL import Image
import base64
import io  
import time

st.title('ARCH-DETECT')
st.subheader('Curious about a building? Snap a photo or upload an image to find out about its architectural style!')

option_map = {
    0: "📸",
    1: "📤"
}

#UI coding came from Streamlit Documentation : https://docs.streamlit.io/


selection = st.segmented_control(
    "Select to snap a photo now or upload an image.",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
)

st.write(
    "Your selected option: "
   f"{'📸 Snap a photo' if selection == 0 else '📤 Upload image' if selection == 1 else None}"
)

enable = True 
image_input = None

if selection == 0:
    image_input = st.camera_input("Take a picture", disabled=not enable)
elif selection == 1:
    image_input = st.file_uploader('', type=["png", "jpg", "jpeg"])


if image_input:
    st.write("A description will pop up below once the architectural style has been detected!")
    
    
    with st.spinner("Wait for it...", show_time=True):
        #Code below referenced from Streamlit Documentation and Curiosity Data Analytics YouTube Video-- references in paper 
        st.image(image_input)
        image = Image.open(image_input)
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        client = ollama.Client()
        describe = client.chat(
            model="llava",  
            messages=[{
                'role': 'user',
                'content': (
                    'Identify any notable buildings in the image, if any. If the building is well-known, provide its name, relevance, and history in up to 250 words.'
                    'Identify the architectural style of the building, the possible time period it was made, and briefly describe the characteristics that define the style and movement in about 300 words.'
                    'Suggest some noteable architects known for that style.'
                    'Please also provide 3 famous buildings in the same style, including their names and locations.'
                    
            ),
            'images': [image_base64],
            }]
        )
        
  

    st.toast("Architectural style detected!", icon="✅")


    st.subheader('Architecture Summary')
    # Code below referenced from Curiosity Data Analytics YouTube Video-- references in paper 
    st.markdown(
        f"""
        <div style="color: white; padding: 10px; line-height: 1.6;">
        {describe['message']['content']}
        </div>
        """,
        unsafe_allow_html=True
    )


