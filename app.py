import streamlit as st
from transformers import pipeline
from langdetect import detect

# PAGE CONFIGURATION
st.set_page_config(
    page_title="SmartAction - Email Summarizer",
    layout="centered"
)

# HEADER 
st.title("SmartAction - Email Summarizer")
st.markdown("### Save time by automatically generating clear summaries of your emails.")
st.divider()

# FILE UPLOAD 
uploaded_file = st.file_uploader("Upload your email file (.txt)", type=["txt"])

if uploaded_file:
    # Read email content
    email_content = uploaded_file.read().decode("utf-8").strip()

    # Detect language
    try:
        lang = detect(email_content)
    except:
        lang = "en"

    st.write(f"Detected language: {lang}")

    # --- Select model based on language ---
    if lang.startswith("fr"):
        model_name = "csebuetnlp/mT5_multilingual_XLSum"  # fonctionne bien pour le français
    else:
        model_name = "facebook/bart-large-cnn"

    st.write(f"Using model: `{model_name}`")

    # Load model
    summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)

    # Show email content
    with st.expander("Show email content"):
        st.text_area("Email Content", email_content, height=250)

    # GENERATE SUMMARY BUTTON
    if st.button("Generate summary"):
        with st.spinner("Analyzing and summarizing..."):
            input_length = len(email_content.split())
            max_len = min(180, int(input_length * 0.8))
            min_len = min(60, int(input_length * 0.3))

            summary = summarizer(email_content, max_length=max_len, min_length=min_len, do_sample=False)
            result = summary[0]["summary_text"]

        st.success("Summary generated:")
        st.write(result)

else:
    st.info("Upload a text file (.txt) to start summarizing.")

# SIDEBAR 
st.sidebar.title("About")
st.sidebar.markdown("""
SmartAction is an AI-powered app that summarizes emails using Hugging Face models.

Developed by **Léa Hadj-Said**.
""")
