# nl_to_sql.py
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatGroq(
    temperature=0.3,
    groq_api_key='',
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

template = """
You are a SQL expert. Convert the following natural language question into an executable SQL query.
Only return the SQL query. Do not include explanations or code blocks.

Question: {question}
SQL:
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
sql_chain = LLMChain(llm=llm, prompt=prompt)

def generate_sql(natural_language: str) -> str:
    response = sql_chain.run(natural_language)
    return response.strip()
import re

def extract_sql_from_response(response: str) -> str:
    # Try to find the first SQL block
    code_blocks = re.findall(r"```sql(.*?)```", response, re.DOTALL | re.IGNORECASE)
    if code_blocks:
        return code_blocks[0].strip()
    
    # If no code blocks, try to find first SELECT/INSERT/UPDATE/etc statement
    match = re.search(r"(SELECT|INSERT|UPDATE|DELETE).*?;", response, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(0).strip()
    
    # Fallback: return raw response (might still be invalid)
    return response.strip()

def generate_sql(natural_language: str) -> str:
    raw_response = sql_chain.run(natural_language)
    return extract_sql_from_response(raw_response)
