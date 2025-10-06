import os
import streamlit as st
import time

# LangChain Imports
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import (
    FAISS,
)  # <-- FIXED: Corrected the typo from FAISSPO
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)  # <-- FIXED: Updated to modern import

from dotenv import load_dotenv

load_dotenv()

# --- App UI Configuration ---
st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(
        f"URL {i + 1}", key=f"url_{i}"
    )  # Added unique keys for inputs
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
db_folder_path = "faiss_store_huggingface"

main_placeholder = st.empty()
# Changed to a model available on the standard API tier
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Use a powerful, fast, and free-tier model
    temperature=0.9,
    max_output_tokens=500,  # The Gemini equivalent of max_tokens
)

# --- Main Logic ---
if process_url_clicked:
    # Filter out empty URLs to avoid errors
    valid_urls = [url for url in urls if url.strip()]
    if not valid_urls:
        main_placeholder.error("Please enter at least one URL.")
    else:
        with st.spinner("Processing URLs... This may take a moment."):
            # 1. Load Data
            loader = WebBaseLoader(web_paths=valid_urls)
            data = loader.load()

            # 2. Split Data
            text_splitter = RecursiveCharacterTextSplitter(
                separators=["\n\n", "\n", ".", ","], chunk_size=1000, chunk_overlap=200
            )
            docs = text_splitter.split_documents(data)

            # 3. Create Embeddings and Save to FAISS
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectorstore = FAISS.from_documents(docs, embeddings)

            # 4. Save FAISS index locally (Best Practice)
            vectorstore.save_local(db_folder_path)

        st.success("URLs processed and ready for questions!")
        time.sleep(2)


query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(db_folder_path):
        with st.spinner("Searching for the answer..."):
            # Load the FAISS index from the local folder
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectorstore = FAISS.load_local(
                db_folder_path, embeddings, allow_dangerous_deserialization=True
            )
            retriever = vectorstore.as_retriever()

            prompt = ChatPromptTemplate.from_template(
                """Answer the user's question based *only* on the context provided.
                If the answer is not in the context, say you don't have enough information.
                Also, list the exact sources you used.

                Context: {context}
IPI
                Question: {input}
                """
            )

            document_chain = create_stuff_documents_chain(llm, prompt)
            retrieval_chain = create_retrieval_chain(retriever, document_chain)

            result = retrieval_chain.invoke({"input": query})

            st.header("Answer")
            st.write(result["answer"])

            # Display sources
            sources = result.get("context", [])
            if sources:
                st.subheader("Sources:")
                unique_sources = set(doc.metadata["source"] for doc in sources)
                for source in unique_sources:
                    st.write(source)
    else:
        st.warning("You must process URLs before asking a question.")
