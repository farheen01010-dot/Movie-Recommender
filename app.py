import streamlit as st
from recommender import recommend

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")

    else:

        recommendations = recommend(movie_name)

        if len(recommendations) == 0:
            st.error("Movie not found!")

        else:

            st.subheader("Recommended Movies")

            for movie in recommendations:
                st.write(movie)