
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

model = open("classifier.pkl", "rb")
classificador_estrelles = pickle.load(model)


def resultat_estrelles(Temperature, Luminosity, Radius, Absolute_magnitude,  Star_color, Spectral_Class):
    prediccio = classificador_estrelles.predict(
        [[Temperature, Luminosity, Radius, Absolute_magnitude, Star_color, Spectral_Class]])
    print(prediccio)
    return prediccio


def main():

    st.title("Classificació d'estrelles amb machine learning")
    st.text("Treball de recerca Pau Iznardo")

    Temperature = st.text_input("Temperatura")
    Luminosity = st.text_input("Lluminositat")
    Radius = st.text_input("Radi")
    Absolute_magnitude = st.text_input("Magnitud absoluta")
    Star_color = st.text_input("Color de l'estrella")
    Spectral_Class = st.text_input("Tipus d'espectre")

    result = ""
    if st.button("predicció"):
        result = resultat_estrelles(Temperature, Luminosity, Radius,
                                    Absolute_magnitude, Star_color, Spectral_Class)
    st.success("EL TIPUS D'ESTRELLA ÉS {}".format(result))
    st.text("[DE 0 a 0.499] ÉS UNA NANA MARRÓ")
    st.text("[DE 0.5 a 1.499] ÉS UNA NANA VERMELLA")
    st.text("[DE 1.5 a 2.499] ÉS UNA NANA BLANCA ")
    st.text("[DE 2.5 a 3.499] ÉS UNA ESTRELLA DE SEQÜÈNCIA PRINCIPAL ")
    st.text("[DE 3.5 a 4.499] ÉS UN ESTRELLA SUPERGEGANT ")
    st.text("[DE 4.5 a 5] ÉS UNA ESTRELLA HIPERGEGANT")


if __name__ == '__main__':
    main()
