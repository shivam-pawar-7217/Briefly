import streamlit as st
from news_scraper import get_news
from Summarization import summarize_text

# Set the page title and layout
st.set_page_config(page_title="AI News Summarizer", layout="wide")

# App header
st.title("AI News Summarizer")
st.subheader("Get summarized news articles from various categories like business, market, sports, and more.")

# Dropdown to select news category
categories = ["Business", "Market", "Sports", "Technology", "Entertainment", "Health"]
category = st.selectbox("Choose a category", categories)

# Fetching the news based on selected category
news_articles = get_news(category.lower())

# Check if the news_articles list is empty
if not news_articles:
    st.error(f"No articles found for {category}. Please try again later.")
else:
    st.subheader(f"Top Articles for {category} News")

    # Display article titles in a selectbox
    article_titles = [article['title'] for article in news_articles]

    # Select article from the list of article titles
    selected_article = st.selectbox("Choose an article to summarize", article_titles)

    # Try fetching the content of the selected article
    article_content = next((article.get('content') for article in news_articles if article['title'] == selected_article), None)

    # If content is found, display it, otherwise show an error
    if article_content:
        st.write("### Article Content")
        st.write(article_content)

        # Summarization Button
        if st.button("Summarize"):
            summary = summarize_text(article_content)
            st.subheader("Summary")
            st.write(summary)
    else:
        st.error("Unable to retrieve content for the selected article.")
