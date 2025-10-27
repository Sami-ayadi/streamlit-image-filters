import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Filter App", page_icon="🎨", layout="centered")

st.title("🎨 Image Filtering App")
st.markdown("Apply **Mean**, **Gaussian**, and **Median** filters dynamically.")

# === UPLOAD IMAGE ===
uploaded_file = st.file_uploader("📸 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    st.image(image, caption="🖼️ Original Image", use_column_width=True)

    # === CHOOSE FILTER ===
    st.sidebar.header("⚙️ Filter Settings")
    filter_type = st.sidebar.selectbox("Choose a filter", ["Mean", "Gaussian", "Median"])

    # === PARAMETERS ===
    if filter_type == "Mean":
        kernel_size = st.sidebar.slider("Kernel size", 3, 15, 3, step=2)
        filtered = cv2.blur(img_array, (kernel_size, kernel_size))

    elif filter_type == "Gaussian":
        kernel_size = st.sidebar.slider("Kernel size", 3, 15, 3, step=2)
        sigma = st.sidebar.slider("Sigma (blur intensity)", 0.0, 10.0, 1.0, step=0.5)
        filtered = cv2.GaussianBlur(img_array, (kernel_size, kernel_size), sigma)

    elif filter_type == "Median":
        kernel_size = st.sidebar.slider("Kernel size", 3, 15, 3, step=2)
        filtered = cv2.medianBlur(img_array, kernel_size)

    # === DISPLAY RESULT ===
    st.image(filtered, caption=f"🎯 {filter_type} Filter Result", use_column_width=True)

    # === DOWNLOAD BUTTON ===
    result_img = Image.fromarray(filtered)
    st.download_button(
        label="💾 Download Filtered Image",
        data=cv2.imencode('.png', cv2.cvtColor(filtered, cv2.COLOR_RGB2BGR))[1].tobytes(),
        file_name=f"{filter_type}_filtered.png",
        mime="image/png"
    )

else:
    st.info("Please upload an image to start.")
