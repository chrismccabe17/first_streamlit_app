import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard boiled, free-range Egg')
streamlit.text(avocado:'Avocado toast')
streamlit.header('Build your own fruit smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
