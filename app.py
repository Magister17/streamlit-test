import streamlit as st
import numpy as np
import cv2
import pandas as pd
import base64

#-------------------------------------Funzioni--------------------------------#




#----------------------------------------INTRO--------------------------------#
st.title("Computer Vision App")

# Introduzione del testo
st.markdown('''
# Introduzione
> Applicazione di computer vision con focus threshold

## Setup

### Local Environment
```
virtualenv --python=python3.6 strealit_env
strealit_env/Scripts/activate
pip install streamlit opencv-python
pip freeze > requirements.txt
```
''')

#--------------------------------------SIDEBAR--------------------------------#
st.sidebar.markdown('''
## Demo dell'algoritmo
1. Carica un'immagine [estensione "png", "jpeg", "jpg", "bmap"]
2. Prova a modificare lo slider per vedere gli effetti
3. Scegli il tipo di Threshold
''')

# ---- Opzioni

st.set_option('deprecation.showfileUploaderEncoding', False)

# option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))
# genre = st.radio("What's your favorite movie genre", ('Comedy', 'Drama', 'Documentary'))
thresh_par = st.sidebar.slider("Threshold", 1, 255, 127)
option = st.sidebar.radio("Scegli il tipo di Threshold", ('THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TOZERO'))

thresh_sel_par = cv2.THRESH_BINARY
if option:
    if option == "THRESH_BINARY":
        thresh_sel_par = cv2.THRESH_BINARY
    elif option == "THRESH_BINARY_INV":
        thresh_sel_par = cv2.THRESH_BINARY_INV
    else:
        thresh_sel_par = cv2.THRESH_TOZERO


# ---- upload e decodifica
uploaded_file = st.sidebar.file_uploader("Upload Image", type = ["png", "jpeg", "jpg", "bmap"])
if uploaded_file is not None:
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # ---- processing dell'immagine
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret,thresh1 = cv2.threshold(gray,thresh_par,255,thresh_sel_par)

    # ---- print dell'immagine
    st.sidebar.image(gray, use_column_width = True )    # width = 700)
    st.sidebar.image(thresh1, use_column_width = True )    # width = 700)

#--------------------------------------CENTRAL--------------------------------#
st.subheader("Analisi Covid")
df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
df["data"] = [el[0:10] for el in df["data"].values.tolist()]

st.dataframe(df, height = 300, width = 700)