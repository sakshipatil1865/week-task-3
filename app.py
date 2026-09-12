import streamlit as st 
import subprocess

st.title("Mini project - exploratory data analysis")
result = subprocess.run(
  ["Python","Day7.py"],
  capture_output=True,
  text=True
)
st.text(result.stdout)

if result.stderr:
  st.error(result.stderr)
