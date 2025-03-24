# 📚 Book Recommender System  

A **book recommendation system** built using **Numpy, Pandas, Scikit-learn and Machine Learning**, supporting **Popularity-based and Collaborative filtering based** approaches.  

## 🚀 Features  
✅ Recommend books based on user input  
✅ Collaborative filtering for suggesting similar books   
✅ Display book covers & authors  
✅ Interactive UI using Streamlit  

## 📂 Dataset  
- Used this **Kaggle dataset** https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset containing three files namely-Books.csv, Ratings.csv, Users.csv.
- For Popularity-Based Recommender System, we used average rating on books having >=250 ratings.
- Improvised to Collaborative Filtering Recommender System where we used users who have give more than 200 ratings on books and books which have got more than 50 ratings to calculate Euclidean distances between them to get the most similar book.  
  

## ⚡ How to Run Locally  
```bash
git clone https://github.com/almishhoda04/book-recommender.git
cd book-recommender
streamlit run app.py
