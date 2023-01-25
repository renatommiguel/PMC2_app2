import streamlit as st
import pandas as pd

page_title = "Portfolio"
name = "Renato Matos Miguel"
content = """
Hello there.\n
This is my first webpage using streamlit.\\
I am an engineer, graduate in Brazil and in Germany. \\
Today I live in the Netherlands with my wife and daughter.\\
I do miss my family a lot, and I am quite worried about my brother :`(
"""
st.set_page_config(layout="wide")
st.title(page_title)
col1, col2 = st.columns(2)
images_path = r"./app2/resources/images/"
with col1:
    st.image(images_path + "photo.png", width=400)

with col2:
    st.title(name)
    st.info(content)
content1 = """These are the apps in my portfolio"""
st.write(content1)

col3, col4, col5 = st.columns([3, 1, 3])

df = pd.read_csv(r"./app2/resources/data.csv", sep=";")

for index, row in df.iterrows():
    def func():
        st.header(row["title"])
        st.write(row["description"])
        st.image(images_path + row["image"])
        st.write(f"[Sorce code]({row['url']})")  # markdown

    if int(index) % 2 == 0:
        with col3:
            func()
    else:
        with col5:
            func()



