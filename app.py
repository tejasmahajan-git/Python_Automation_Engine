import streamlit as st
import os
import json

from system.engine import execute

st.title("📄 Text Processing Engine")

uploaded_file = st.file_uploader("Upload a text file")

# Sidebar options
st.sidebar.header("Processing Options")

uppercase = st.sidebar.checkbox("Uppercase", value=True)
reverse = st.sidebar.checkbox("Reverse", value=False)
remove_empty = st.sidebar.checkbox("Remove Empty Lines", value=True)

if uploaded_file:
    # Save uploaded file
    with open("temp_input.txt", "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded!")

    if st.button("Process File"):
        # Load config
        with open("config/config.json", "r") as f:
            config = json.load(f)

        # Update config dynamically
        config["files"]["input"] = "temp_input.txt"
        config["files"]["output"] = "temp_output.txt"

        config["process"] = {
            "uppercase": uppercase,
            "reverse": reverse,
            "remove_empty": remove_empty
        }

        # Save updated config
        with open("config/config.json", "w") as f:
            json.dump(config, f, indent=2)

        # Run pipeline
        execute(mode="manual")

        # Read output safely
        if os.path.exists("temp_output.txt"):
            with open("temp_output.txt", "r", encoding="utf-8", errors="ignore") as f:
                result = f.read()

            st.text_area("Processed Output", result, height=200)

            st.download_button(
                label="Download Output",
                data=result,
                file_name="processed.txt"
            )