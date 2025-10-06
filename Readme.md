# 🧠 ResearchBot: News Research Tool

**ResearchBot** is a user-friendly, AI-powered news research assistant built for effortless information retrieval and analysis.  
It allows users to load news article URLs, process content through LangChain, and interact with a conversational AI (ChatGPT) to extract meaningful insights — especially in the **stock market and financial** domains.

---

## 🚀 Features

✅ **URL & File Loading**
- Load single or multiple article URLs directly.
- Upload text files containing multiple URLs for batch processing.

✅ **Smart Content Extraction**
- Uses **LangChain's UnstructuredURL Loader** to fetch and structure article content seamlessly.

✅ **Intelligent Embeddings**
- Generates semantic embeddings using **OpenAI’s Embeddings API**.

✅ **Efficient Similarity Search**
- Leverages **FAISS**, a high-performance vector search library, for rapid and accurate retrieval of relevant article segments.

✅ **Conversational Query Interface**
- Ask questions naturally via **ChatGPT** and receive concise, contextually relevant answers.
- Each answer includes **source URLs** for transparency and reference.

---

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/codebasics/langchain.git
2️⃣ Navigate to the project directory
bash
Copy code
cd 2_news_research_tool_project
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set up your OpenAI API key
Create a .env file in the project root and add your key:

bash
Copy code
OPENAI_API_KEY=your_api_key_here
▶️ Usage
Run the Streamlit app:
bash
Copy code
streamlit run main.py
Steps:
Open the web app (it will launch automatically in your browser).

On the sidebar:

Enter article URLs manually, or

Upload a .txt file containing multiple URLs.

Click “Process URLs” to:

Load and extract article data.

Split text into chunks.

Generate embeddings via OpenAI.

Store them efficiently in FAISS for retrieval.

Once processing completes:

Ask any question related to the articles.

ResearchBot will return context-aware answers with source URLs.

📁 Project Structure
File	Description
main.py	The main Streamlit application script.
requirements.txt	Contains the Python package dependencies.
faiss_store_openai.pkl	Pickle file to store FAISS index for future use.
.env	Environment file storing your OpenAI API key.

🧩 Example Articles Used
Here are some sample URLs used in the demo:

Tata Motors, Mahindra gain certificates for production-linked payouts

Tata Motors launches Punch iCNG, price starts at Rs 7.1 lakh

Buy Tata Motors, target of Rs 743: KR Choksey

🧠 How It Works (High-Level Flow)
Data Ingestion: Load and extract article content from URLs using LangChain.

Text Processing: Split articles into semantically meaningful chunks.

Vectorization: Convert text chunks into embeddings via OpenAI’s Embeddings API.

Indexing: Store embeddings in FAISS for efficient similarity-based retrieval.

Query & Response: Use ChatGPT to answer user questions based on retrieved contexts, with citations.

💡 Future Enhancements
Multi-domain support (finance, health, tech, etc.)

Integration with live news APIs

Topic-wise article clustering and summaries

Multi-modal data ingestion (text, audio, video transcripts)

📬 Connect
If you found this project interesting or have suggestions for improvement, feel free to connect!

Author: Arinjay Sarkar