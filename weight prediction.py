import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import seaborn as sns
data=pd.read_csv(r"C:\Users\srija\Downloads\baseball_players.csv")
df=pd.DataFrame(data)
print("Top 10 values:",df.head(10))
X=df[["Height(inches)","Age"]]
y=df["Height(inches)"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
model= LinearRegression()
model.fit(X_train,y_train)
st.title("Weight Prediction")
st.subheader("Predicting Height Based on their Information")
st.write("Fill The Below Contents Properly")
n=st.text_input("Enter respective BasketBall Player Name:")
AGE=st.slider("Age:",min_value=10,max_value=60,value=25)
HEIGHT=st.number_input("Enter the weight:",min_value=20.00,max_value=300.00,value=50.0)
st.write("Predict the Height")
if st.button("___**Predict**____"):
    with st.spinner("Predicting"):
        pred = model.predict([[AGE,HEIGHT]])
        print("Prediction:",pred)
    if pred[0] >=250.0:
        st.success(f"{n} is a bulk man")
        st.balloons()
    elif  pred[0] >=150.0:
        st.warning(f"{n} is a gym man with extraordinary muscles")
        st.snow()
    elif pred[0] <=150.0:
        st.warning(f"{n} is a strong man")
    else:
        st.error(f"{n} is not eligible ")




