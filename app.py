import streamlit as st
import numpy as np
import pandas as pd
import pickle  # If using a saved similarity model

# Load the dataset
Books = pd.read_csv("Books.csv")  
Ratings = pd.read_csv("Ratings.csv")
Users = pd.read_csv("Users.csv")


# Load preprocessed pivot table & similarity scores
pt = pd.read_pickle("pivot_table.pkl")  
similarity_scores = pickle.load(open("similarity.pkl", "rb"))

# Function to get book recommendations (Modify this as per your Jupyter Notebook logic)
def recommend(book_name):
    # index fetch
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]

    recommended_books = []
    book_authors = []
    book_covers = []

    for i in similar_items:
        book_title = pt.index[i[0]]
        recommended_books.append(book_title)

        # Fetch author and cover URL (Modify this according to your dataset)
        author = Books[Books['Book-Title'] == book_title]['Book-Author'].values[0]
        cover_url = Books[Books['Book-Title'] == book_title]['Image-URL-L'].values[0]  # Large image URL

        book_authors.append(author)
        book_covers.append(cover_url)

    return recommended_books, book_authors, book_covers
# Streamlit UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Courier New', monospace;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📖 Book Recommender System")

book_name = st.text_input("Enter a book title:")

if st.button("Get Recommendations"):
    recommended_books, book_authors, book_covers = recommend(book_name)

    if "Book not found" in recommended_books:
        st.warning(recommended_books[0])
    else:
        st.subheader("Recommended Books:")

        # Create a row layout using columns
        cols = st.columns(len(recommended_books))  # Creates a column for each book

        for i, book in enumerate(recommended_books):
            with cols[i]:  # Assign each book to a separate column
                st.image(book_covers[i], width=150)  # Display book cover
                st.write(f"**{book}**")  # Display book title
                st.write(f"*{book_authors[i]}*")  # Display author name

