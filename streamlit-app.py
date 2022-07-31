import streamlit
streamlit.title('This is my first streamlit code')

streamlit.header('Todays Menu')
streamlit.text('🥣Tarri Poha')
streamlit.text('🥗 🐔Chola Samosa')
streamlit.text(' 🥑🍞Idli Sambar')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
