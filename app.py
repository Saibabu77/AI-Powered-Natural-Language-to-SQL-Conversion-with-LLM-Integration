# app.py
import streamlit as st
from nl_to_sql import generate_sql
from db_utils import run_query

st.title(" Natural Language to SQL")
user_input = st.text_input("Ask your question:", placeholder="e.g. Show total sales by region in 2023")

if user_input:
    with st.spinner("Generating SQL..."):
        sql_query = generate_sql(user_input)
        st.code(sql_query, language='sql')

        result = run_query(sql_query)
        if isinstance(result, str):
            st.error(result)
        else:
            st.dataframe(result)
