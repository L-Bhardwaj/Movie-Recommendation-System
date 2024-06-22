import streamlit as st 
import pickle
# import pandas as pd

movies_list = pickle.load(open('movies.pkl', 'rb'))

movie_list=movies_list['title'].values


similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=movies_list[movie_list==movie].index[0]
    distances=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x: x[1])
    
    recommended_movies=[]
    for i in distances[1:6]:
        movie_id=i[0]
        # fetch poster of movie from api
        
        recommended_movies.append(movie_list[i[0]])
    return recommended_movies

st.title('Movie Recommendation System')
st.write('Welcome to the Movie Recommendation System. Please enter the name of the movie you like and we will recommend you some movies based on that.')


selected_movie_name = st.selectbox(
    "Enter the movie name: ",
    movie_list)

if st.button('Recommend'):
    recommended_movies=recommend(selected_movie_name)
    st.write('\tYou have selected:', selected_movie_name)
    st.write('Here are some recommendations for you:')
    st.write(' ')
    for i in recommended_movies:
        st.write(i)
     
    

