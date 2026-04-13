from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI(temperature= 0)


prompt = ChatPromptTemplate.from_template(
    """
    You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Keep the answer concise.
    Context:    {context}
    Question:   {question}
    Answer:
    """
)

generation_chain = prompt | llm | StrOutputParser

