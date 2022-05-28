import requests as re
import streamlit as st
import json
host="http://127.0.0.1:8000"

#print(r.json())
st.title("Movie Reccomender System")
main_bg = "bg1.jpg"
main_bg_ext = "jpg"

side_bg = "bg1.jpg"
side_bg_ext = "jpg"


user=st.text_input("Enter UserId")
movie=st.text_input("Enter MovieName")


params=json.dumps({
'user_id': user,
'movies': movie})

if st.button("Get Recommendations from UserName"):
	r=re.post(host+"/moviePred_user_based/",params)
	st.write(r.json())
elif st.button("Get Recommendations from MovieName"):
	r=re.post(host+"/moviePred_item_based/",params)
	st.write(r.json())
#t:write(re.response)
