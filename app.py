import streamlit as st
import pickle
import numpy as np
import pandas as pd


pickle_in = open("classifier.pkl", "rb")

classificator = pickle.load(pickle_in)  # our model


def result_stars(Temperature, Luminosity, Radius, Absolute_magnitude,  Star_color, Spectral_Class):
    prediction = classificator.predict(
        [[Temperature, Luminosity, Radius, Absolute_magnitude, Star_color, Spectral_Class]])
    print(prediction)
    return prediction


def main():

    st.title("Classificació d'estrelles amb machine learning")
    st.text("Treball de recerca Pau Iznardo")

    Temperature = st.text_input("Temperature")
    Luminosity = st.text_input("Luminosity")
    Radius = st.text_input("Radius")
    Absolute_magnitude = st.text_input("Absolute magnitude")
    Star_color = st.text_input("Star color")
    Spectral_Class = st.text_input("Spectral Class")

    result = ""
    if st.button("predict"):
        result = result_stars(Temperature, Luminosity, Radius,
                              Absolute_magnitude, Star_color, Spectral_Class)
    st.success("EL TIPUS D'ESTRELLA ÉS {}".format(result))


if __name__ == '__main__':
    main()
