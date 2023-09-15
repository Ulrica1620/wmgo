import streamlit as st
# from rembg import remove
# from PIL import Image
# from io import BytesIO
# import base64
import sys
# sys.path.append('./pages')
# from pip._internal import main
# main(['install','fuzzywuzzy'])
# main(['install','ultralytics'])
# main(['uninstall','opencv-python'])
# main(['install','opencv-python-headless'])
# main(['install','pywavelets'])
# main(['install','google-api-python-client'])
# main(['install','google-auth'])
# main(['install','google-auth-httplib2'])

import subprocess

subprocess.run('sudo pip uninstall opencv-python')



st.set_page_config(layout="wide", page_title="Hello Page")

st.title("🖼️ Esperanto Watermark Project")
st.markdown(
    """
    This webpage app is built specifically for demonstrating our watermark project about
    ***inserting and detecting*** watermark based on images generated by ***DeepFloyd***.

    👈 **You can switch different pages on left-hand sidebar to play with different functions**
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')

st.subheader('📜 DeepFloyd IF Model Introduction')
st.markdown(
    """
    In this module, we will go through some basic ideas of a powerful modelL: *[DeepFloyd](https://github.com/deep-floyd/IF)*
    \n
    Starting with the structure of DeepFloyd, we also add comments about the model's most important features. Moreover, we also pointed out several noticeable caveats.
    \n
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')

st.subheader('🏙️ DeepFloyd Image Generation')
st.markdown(
    """
    In this module, we will show the images generated by DeepFloyd. It performs well on the task of generating human faces, image with texts, and etc.
    \n
    Here we provide an example where you can play with different prompts, and we are working on getting DeepFloyd running in backend.
    \n
    We also can let you select different image styles for transfering purposes.
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')
st.subheader('📷 Visible Watermark')
st.markdown(
    """
    In this module, we finished a simple trial of inserting visible watermark into the picture. 
    \n
    It is the watermark that we always encounter, visible and need some effort to remove. However, this visible watermark is not irreversible, which means it is not rubust enough.
    \n
    Here we provide a trial. You can upload your own image, and the watermark you choose. And then, you also can adjust the parameter *Alpha* to choose the visibility of your watermark. If ALpha is zero, there's no watermark in the picture.
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')
st.subheader('🔆 Invisible Watermark and Robustness Tests')
st.markdown(
    """
    This is the main module for our project. You can insert your own watermark into a customed image.
    \n
    This watermark is invisible to everyone, and really hard to remove.
    \n
    We also wanted to test the robustness of the watermark tools, and we conducted the following tests:
    - Cut
    - Scale
    - Cut + Scale
    - Rotate
    - Block
    - Salt & Pepper Noise
    - Adjust Brightness
    - Warp
    - Color Rotation
    - Fourier Attack
    \n
    Here in this module, we provide several trials for you:
    - You can see the outcome of our invisible watermark tool
    - You can attack the watermarked image by clicking your mouse
    - You can test the robustness of the watermark
    - You can try several reverse functions, aiming to extract better watermark after the image being "ruined" by strong attacks
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')
st.subheader('📅 Future Plans')
st.markdown(
    """
    - Get DeepFloyd IF running in backend
    - Polish the blog
    - Testing and debugging
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')

st.subheader('🙌 Leave Your Comments')
st.markdown(
    """
    Please leave your comments here and also take a look at what others said about this project.
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')

c1, c2 = st.columns(2)

with c1:
    st.info('**project address: Esperanto Watermark project address**', icon="💻")

with c2:
    st.info('**Contact: [@Wen Cheng](wen.cheng@esperantotech.com)**', icon="📩")

st.title("📕 Sources and Reference")
st.markdown(
    """
    - https://github.com/deep-floyd/IF 
    - https://stability.ai/blog/deepfloyd-if-text-to-image-model
    - https://www.nftparis.xyz/blog/introducing-deepfloyd-if-a-revolutionary-text-to-image-model-by-stability-ai
    - https://the-decoder.com/deepfloyd-if-is-a-crazy-good-text-to-image-model-and-open-source/
    - https://github.com/deep-floyd/IF
    - https://github.com/guofei9987/blind_watermark/tree/master
    - https://github.com/fire-keeper/BlindWatermark
    - https://bgremoval.streamlit.app/
    - https://onlinelibrary.wiley.com/doi/10.1002/0471745790.ch5 
    - https://link.springer.com/referenceworkentry/10.1007/0-387-30038 4_62#:~:text=Definition%3ADiscrete%20Wavelet%20Transform%20is,wavelet%2Dbased%20compression%20and%20coding. 
    - J. Liu et al., "An Optimized Image Watermarking Method Based on HD and SVD in DWT Domain," in IEEE Access, vol. 7, pp. 80849-80860, 2019, doi: 10.1109/ACCESS.2019.2915596.
    """
)

