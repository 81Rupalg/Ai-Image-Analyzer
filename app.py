import streamlit as st 
from PIL import Image
import numpy as np

st.title("AI Image Analyzer")

uploaded_file = st.file_uploader(
    "Upload An Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    st.image(
        image,
        caption="Upload Image"
    )
    
image_array = np.array(image)

st.write("Numpy Array")
# st.write(image_array)


# 1 image dimensions
height, width = image_array.shape[:2]

st.write("Height", height)
st.write("Width", width)

# 2 Number of channels

channels = image_array.shape[2]
st.write(" Channels:", channels)

# 3 Data type 

st.write("Data Type:", image_array.dtype)

# 4 Pixel value range

pixel = image_array[0, 0]
st.write("Pixel Value:", pixel)


# red
# green
# blue

# Image static

st.write(
    "Minimum Pixel Value:", 
     np.min(image_array)
)


