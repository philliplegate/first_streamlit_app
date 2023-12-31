import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Health Diner')
   
streamlit.header(' Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blkueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
      fruit_choice=streamlit.text_input('What fruit would you like information about')
      if not fruit_choice:
         streamlit.eror("Please select a fruit to get information.")
      else:
         fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
         fruityvice_normalized = pandas.json_normalize(fruity_response.json())
         streamlit.dataframe(fruityvice_normalized)

except URLError as e:
   streamlist.error()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)






