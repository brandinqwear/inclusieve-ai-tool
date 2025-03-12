import streamlit as st
import spacy
from textblob import TextBlob

# Bias-detectie functie
def detect_bias(text):
    bias_terms = {
        "hij": "de persoon", "zij": "de persoon", "man": "persoon", "vrouw": "persoon",
        "jongeman": "jonge persoon", "jongedame": "jonge persoon",
        "leidinggevende man": "leidinggevende", "sterke vrouw": "krachtige persoon",
        "zwart": "persoon van kleur", "blank": "wit"
    }
    found_bias = {}
    for term, suggestion in bias_terms.items():
        if term in text.lower():
            found_bias[term] = suggestion
    return found_bias

# Leesbaarheidsanalyse functie
def check_readability(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Tekstanalyse functie
def analyze_text(text):
    bias_results = detect_bias(text)
    readability_score = check_readability(text)
    return {
        "bias_detected": bias_results,
        "readability_score": readability_score
    }

# Streamlit UI
st.title("Inclusieve Tekstanalyse AI")
st.write("Deze tool detecteert bias en controleert de leesbaarheid van je tekst.")

# Gebruiker invoer
user_input = st.text_area("Voer een tekst in:")

if st.button("Analyseer Tekst"):
    if user_input:
        result = analyze_text(user_input)
        st.subheader("Analyse Resultaten:")
        
        # Bias-resultaten tonen
        if result["bias_detected"]:
            st.write("**Gevonden bias-termen:**")
            for term, suggestion in result["bias_detected"].items():
                st.write(f"- {term} → {suggestion}")
        else:
            st.write("Geen bias gedetecteerd!")
        
        # Leesbaarheidsanalyse tonen
        st.subheader("Leesbaarheidsanalyse:")
        st.write(f"**Polariteit:** {result['readability_score'][0]:.2f} (Negatief ↔ Positief)")
        st.write(f"**Subjectiviteit:** {result['readability_score'][1]:.2f} (Objectief ↔ Subjectief)")
    else:
        st.write("⚠️ Voer eerst een tekst in om te analyseren.")
