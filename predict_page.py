import streamlit as st
import pickle
import pandas as pd 

def load_model():
    with open('model_LR.pkl','rb') as file:
        data = pickle.load(file)
    return data

final_model = load_model()['final_model']

def show_predict_page():

    st.title(' Wild Blueberry Yield Prediction')
    st.write("""#### We need some information for prediction """)           
    st.write(""" \n """)           
    st.write(""" \n """)

    clonesize = st.selectbox( 'The average blueberry clone size in the field - Clone Size (m2)', options=[37.5, 25.0, 12.5, 20.0, 10.0, 40.0] )
    honeybee = st.selectbox( 'Honeybee density in the field - Honey Bee (bees/m2/min)', options=[0.75, 0.25, 0.5, 0.0, 6.64, 18.43, 0.537] )
    bumbles = st.selectbox( 'Bumblebee density in the field - Bumbles (bees/m2/min)', options=[0.25, 0.38, 0.117, 0.202, 0.0, 0.065, 0.042, 0.585, 0.293, 0.058] )
    andrena = st.selectbox( 'Andrena bee density in the field - Andrena (bees/m2/min)', options=[0.25, 0.38, 0.5, 0.63, 0.75, 0.409, 0.707, 0.0, 0.229, 0.147, 0.585, 0.234] )
    osmia = st.selectbox( ' Osmia bee density in the field - Osmia (bees/m2/min)', options=[0.25, 0.38, 0.5, 0.63, 0.75, 0.058, 0.101, 0.0, 0.033, 0.021, 0.585, 0.117] )
    AverageRainingDays = st.selectbox( 'The average of raining days of the entire bloom season - AverageRainingDays ', options=[0.26, 0.1, 0.39, 0.56, 0.06] )
    AverageOfUpperTRange = st.selectbox( 'The average of the upper band daily air temperature - AverageOfUpperTRange (℃) ', options=[71.9, 79.0, 64.7, 58.2, 65.6] )
    AverageOfLowerTRange = st.selectbox( ' The average of the lower band daily air temperature - AverageOfLowerTRange (℃)  ', options=[50.8, 55.9, 45.8, 41.2, 45.3] )
    seeds = st.slider( 'Seeds', 22.0 , 46.5, 0.5 )
    Average_TRange = (AverageOfUpperTRange+AverageOfLowerTRange)/2

    ok = st.button("Predict")
    
    columns_name = [ 'clonesize', 'honeybee', 'bumbles', 'andrena', 'osmia' ,'AverageRainingDays', 'seeds', 'Average_TRange' ]

    values = [ clonesize, honeybee, bumbles, andrena, osmia , AverageRainingDays, seeds, Average_TRange ]
    
    if ok:
        data = pd.DataFrame( data=[values] ,columns=columns_name )    
        predict_value = final_model.predict(data)
        
        st.write("# Yield : "+str(predict_value[0][0]) )
        # st.subheader("Yield : " )