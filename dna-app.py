#####################
# Import libraries
#####################

import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt

#####################
# Page header
#####################

image = Image.open('dna_PNG.png')

st.image(image)

st.write("""

# DNA Nucleotide Count Web App :sunglasses:

This app counts the nucleotide composition of query DNA!


***
""")

#####################
# DNA Sequence Input Textbox
#####################

# st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query\nGAACACGTGGAGGGACCTTAAAGGTCATCGATGCATGAAATGCCGGTTGAAGGTTGAGCCCAAAAGGGTGAATGCATGCATGCAAATGCCAAGGGTGTTTTTTACG"

# sequence = st.sidebar.text_area("Sequenceinput", sequence_input, height=256)
sequence = st.text_area('Sequence input', sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skips first line
sequence = ''.join(sequence)  # Concatenates list to string

st.write("""
***
""")

# Prints the Input DNA sequence
st.header('Input (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. Print dictionary
st.subheader('1. Print dictionary')


def dna_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = dna_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# 2. Print Text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

