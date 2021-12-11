
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
    st.text("Tots els valors s'han d'introduir en forma numèrica")
    st.text("Els decimals s'han d'ìndicar amb un punt")

    Temperature = st.text_input("Temperatura (en graus kelvin)")
    Luminosity = st.text_input("Lluminositat (respecte el sol)")
    Radius = st.text_input("Radi (respecte el sol)")
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
    st.text(
        "-----------------------------------------------------------------------------")
    st.text("Color de les estrelles en forma numèrica")
    st.text("Red (vermell) == 10")
    st.text("Blue white (blanc blau) == 2")
    st.text("White(blanc) == 11")
    st.text("Yellowish White(blanc grogenc) == 15 ")
    st.text("Pale yellow orange(groc pàlid taronja) == 9")
    st.text("Blue(blau) == 0")
    st.text("Whitish(blanquinós) == 13")
    st.text("yellow-white (Blanc grog) == 17")
    st.text("Orange(taronja) == 7")
    st.text("White-yellow(Grog blanc) == 12")
    st.text("yellowish(grogenc) == 18")
    st.text("Orange-Red(vermell taronja) == 8 ")
    st.text(
        "-----------------------------------------------------------------------------")
    st.text("Tipus d'espectre en forma numèrica")
    st.text("Espectre M == 5")
    st.text("Espectre B == 1")
    st.text("Espectre A == 0")
    st.text("Espectre F == 2")
    st.text("ESPECTRE O == 6")
    st.text("ESPECTRE K == 4")
    st.text("ESPECTRE G == 3")


if __name__ == '__main__':
    main()
