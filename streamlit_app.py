
import streamlit;
import pandas;

streamlit.title("My Parents New Healthy Diner");
streamlit.header("Breakfast Favorites");
streamlit.text("๐ฏOmega 3 & Blueberry Oatmeal");
streamlit.text("๐นKale , Spinach and Rocket Smoothie");
streamlit.text("๐Hard-Boiled Free-Range Egg");
streamlit.text("๐ฅ๐ Avacodo Toast")
streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit');
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana']);
streamlit.dataframe(my_fruit_list);

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list.loc[fruits_selected];
streamlit.dataframe(fruits_to_show);
