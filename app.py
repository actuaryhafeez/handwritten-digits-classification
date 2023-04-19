import streamlit as st
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import urllib.request
import pickle
from streamlit_drawable_canvas import st_canvas


html_temp = '''
    <div style = "background-color: rgba(25,25,112,0.06); padding-bottom: 20px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
    <center><h1>Handwritten Digit Recognition</h1></center>
    </div>
    '''
st.markdown(html_temp, unsafe_allow_html=True)

html_temp = '''
    <div>
    <h2></h2>
    <center><h3>Please upload Image for Classification</h3></center>
    </div>
    '''
st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown(html_temp, unsafe_allow_html=True)

opt = st.selectbox("How do you want to upload the image for classification?\n", ('Please Select', 'Upload image via link', 'Upload image from device'))

if opt == 'Upload image from device':
    file = st.file_uploader('Select', type = ['jpg', 'png', 'jpeg'])
    st.set_option('deprecation.showfileUploaderEncoding', False)
    if file is not None:
        image = Image.open(file)

elif opt == 'Upload image via link':
  
  try:
    img = st.text_input('Enter the Image Address')
    image = Image.open(urllib.request.urlopen(img))
    
  except:
    if st.button('Submit'):
      show = st.error("Please Enter a valid Image Address!")
      time.sleep(4)
      show.empty()

    
try:
  if image is not None:
    st.image(image, width = 300, caption = 'Uploaded Image')
    if st.button('Predict'):
      # Load the KNN model
      with open('model/digits_model.pkl', 'rb') as f:
        knn = pickle.load(f)

      # Preprocess the image
      # image = np.array(image.resize((8, 8), resample=Image.LANCZOS))
      image = np.array(image.resize((8, 8), Image.ANTIALIAS))

      img = image.flatten()
      img = np.array([img])

      # Make the prediction
      prediction = knn.predict(img)

      st.success('Hey! The uploaded digit has been predicted as {}'.format(prediction[0]))

except:
  pass
