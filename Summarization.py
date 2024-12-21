from transformers import pipeline

# Function to summarize text
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=130, min_length=50, do_sample=False)
    return summary[0]['summary_text']
