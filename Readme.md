# **ResearchBoT: AI-Powered News Research Tool 📈**

**ResearchBoT** is a powerful, interactive Streamlit application designed to streamline news research. It leverages a modern AI stack, including Google's Gemini models and LangChain, to allow users to input news article URLs, process their content, and ask questions in natural language to receive accurate, source-cited answers.

## **Features**

* **Web-Based UI**: Simple and intuitive interface built with **Streamlit**.  
* **Dynamic Data Ingestion**: Process up to three news article URLs simultaneously.  
* **Automated Content Scraping**: Uses LangChain's WebBaseLoader to efficiently fetch article content.  
* **Intelligent Text Chunking**: Employs RecursiveCharacterTextSplitter to break down articles into manageable chunks for analysis.  
* **Advanced Embeddings**: Leverages **HuggingFace's** all-MiniLM-L6-v2 model to create meaningful vector embeddings.  
* **High-Speed Retrieval**: Uses **FAISS** (Facebook AI Similarity Search) to create a local vector store for lightning-fast information retrieval.  
* **Generative Q\&A**: Powered by **Google's gemini-2.5-flash model** to provide concise answers based on the provided articles.  
* **Source Citation**: Automatically lists the source URLs used to generate an answer, ensuring transparency and verifiability.

## **Tech Stack & Architecture**

The application is built on a robust, modern AI stack designed for efficient retrieval-augmented generation (RAG).

#### **Data Ingestion & Processing**

#### **Question & Answering**

## **Installation & Setup**

Follow these steps to get ResearchBoT running on your local machine.

### **Prerequisites**

* Python 3.8+  
* Git

### **1\. Clone the Repository**

git clone \<your-repository-url\>  
cd ResearchBoT-News-Research

### **2\. Create and Activate a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

\# For Windows  
python \-m venv venv  
venv\\Scripts\\activate

\# For macOS/Linux  
python3 \-m venv venv  
source venv/bin/activate

### **3\. Install Dependencies**

Install all the required Python packages using the requirements.txt file.

pip install \-r requirements.txt

### **4\. Set Up Environment Variables**

You'll need a Google API key to use the Gemini model.

1. Create a new file named .env in the root of the project directory.  
2. Add your Google API key to the .env file:  
   GOOGLE\_API\_KEY="your\_google\_api\_key\_here"

## **How to Run the Application**

Once the setup is complete, you can launch the Streamlit application with a single command:

streamlit run main.py

Your web browser should automatically open to the application's UI.

## **How It Works**

1. **Input URLs**: The user provides up to three news article URLs in the sidebar.  
2. **Process Data**: When the "Process URLs" button is clicked, the application scrapes the content from each URL.  
3. **Chunk & Embed**: The scraped text is split into smaller, overlapping chunks. Each chunk is then converted into a numerical vector (embedding) using the HuggingFace all-MiniLM-L6-v2 model.  
4. **Create Vector Store**: The embeddings are stored and indexed in a local **FAISS** vector store, which is saved to the faiss\_store\_huggingface directory.  
5. **Ask a Question**: The user types a question into the main input box.  
6. **Retrieve Relevant Context**: The application embeds the user's question and uses FAISS to find the most relevant text chunks from the processed articles.  
7. **Generate Answer**: The question and the retrieved text chunks are sent to the **Google Gemini LLM**. The model synthesizes the information to generate a comprehensive answer.  
8. **Display Results**: The final answer and the source URLs of the documents it was based on are displayed to the user.

## **License**

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for more details.