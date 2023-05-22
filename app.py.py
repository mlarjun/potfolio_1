import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="my webpage",page_icon="random",layout="wide",initial_sidebar_state="expanded", menu_items=None)


def load_animi(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def for_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

for_css("D:/websitee_for_potfolio/style/style.css.py")

animation = load_animi("https://assets1.lottiefiles.com/packages/lf20_mXdqmT1SH2.json")
image_for_web = Image.open("D:/websitee_for_potfolio/images/3862a487_1629423377319_1629423436308_keyframe_04_01.jpg")
image_for_web2 = Image.open("D:/websitee_for_potfolio/images/5-tips-for-students-to-improve-coding-skills-during-college.webp")
url_linked_in = "https://www.linkedin.com/in/arjun-c-v-86262223b"
with st.container():
    left_colum, right_colum = st.columns(2)
    with left_colum:
        st.subheader(":black[Hi my name is]")
        st.title(":black[Arjun]")
        st.subheader(":black[I am a python Developer]")
        st.write(""":violet[I am a self-learn software engineer
        i am passionated to work in ML and Data Science 
        environment ]""")
        st.write("[my linkedin profile>](https://www.linkedin.com/inz/arjun-c-v-86262223b)")
        st.write("[my git hub profile>](https://www.linkedin.com/inz/arjun-c-v-86262223b)")
    with right_colum:
        st_lottie(animation, height=300, key='CODING')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(""":violet[I have a diploma in Automobile Engineering & Bachelor Degree in Aeronautical Engineering 
        I have one year Digital_Marketing experience & one year experience as ML Data Associate. becoming a 
        Developer is always my aim but due to my mechanical educational background its getting delayed. 
        python is my coding language i am eagerly waiting for ML or Data Science or
        any python based internship.I also upskilling me every day Thank you]  
        """)
    with right_column:
        st.image(image_for_web2)


with st.container():
    st.write("---")
    st.header("my project")
    st.write("##")
    image_colum, text_colum = st.columns((1, 2))
    with image_colum:
        st.image(image_for_web2)
    with text_colum:
        st.subheader("insert some thing ")
        st.write(
            """
            write some thing
            """
        )
with st.container():
    st.write("---")
    st.write("##")
    st.header("Your opinion ")
    st.write("##")
    contact_form = """<form action="https://formsubmit.co/arjun830063@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message here" reired></textarea>
     <button type="submit">Send</button>
     </form>"""
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:ru
        st.empty()

