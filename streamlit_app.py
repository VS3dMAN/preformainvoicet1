import streamlit as st
from PIL import Image

# Function to overlay two images
def overlay_images(user_image, overlay_image_path, output_path="output.png"):
    # Open user-uploaded image
    user_img = Image.open(user_image).convert("RGBA")

    # Open overlay image
    overlay_img = Image.open(overlay_image_path).convert("RGBA")

    # Ensure both images have the same size
    overlay_img = overlay_img.resize(user_img.size)

    # Blend the two images
    combined = Image.alpha_composite(user_img, overlay_img)

    # Save the result
    combined.save(output_path)
    return combined

# Streamlit app
def main():
    st.title("Image Overlay Application")

    # Fixed overlay image
    overlay_image_path = "overlay.png"

    # User uploads an image
    user_file = st.file_uploader("Upload an image (JPG or JPEG)", type=["jpg", "jpeg"])
    
    if user_file is not None:
        # Convert JPG to PNG for compatibility
        user_image = Image.open(user_file).convert("RGBA")

        # Display the uploaded image
        st.image(user_image, caption="Uploaded Image", use_column_width=True)

        # Perform the overlay
        st.write("Overlaying images...")
        output_image = overlay_images(user_file, overlay_image_path)

        # Display the output image
        st.image(output_image, caption="Output Image", use_column_width=True)

        # Provide a download link
        st.write("Download your output image below:")
        with open("output.png", "rb") as file:
            btn = st.download_button(
                label="Download Image",
                data=file,
                file_name="output.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
