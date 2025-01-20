#streamlit for housing app 
import streamlit as st
import pandas as pd
import json
import requests

streamlit_options = json.load(open("streamlit_options.json"))

st.title(" House vlaue Prediction System    ")

# streamlit_options

# side_bar_options = model_info.get('options')
#     options = {}
#     for key, value in side_bar_options.items():
#         if key in ['ocean_proximity']:
#             options[key] = st.sidebar.selectbox(key, value)
#         else:
#             min_val, max_val = value
#             current_value = (min_val + max_val)/2
#             options[key] = st.sidebar.slider(key, min_val, max_val, value=current_value)
# st.write(options)

# if st.button('Predict'): 
  
#     # Convert options to df 
#     df = pd.Series(options).to_frame().T
#     df["income_cat"] = pd.cut(df["median_income"],
#                                bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
#                                labels=[1, 2, 3, 4, 5])
#     st.write(df)
#     y_hat = reloaded_model.predict(df)
#     st.write(f'The predicted median house value is: ${y_hat[0]:,}')

user_options = {}

for field_name, range in streamlit_options["slider_fields"].items():
    min_val, max_val = range
    current_value = round((min_val + max_val)/2)
    user_options[field_name] = st.sidebar.slider(field_name, min_val, max_val, value=current_value)

for field_name, values in streamlit_options["single_select_fields"].items():
    user_options[field_name] = st.sidebar.selectbox(field_name, values)

user_options

if st.button('Predict'):
    data = json.dumps(user_options, indent=2)
    r = requests.post("http://127.0.0.1:8000/predict", data = data)
    st.write(r.json())