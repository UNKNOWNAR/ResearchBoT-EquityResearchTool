# 🧠 ResearchBot: News Research Tool  

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[GitHub Repo](https://github.com/UNKNOWNAR/ResearchBotBot-EquityResearchTool.git)  

**ResearchBot** is an AI-powered tool for **news and equity research**, allowing you to fetch, embed, index, and query articles — especially in financial and stock market domains.  

---

## 🚀 Features  

- **URL & File Input**: Enter up to 3 article URLs or upload `.txt` files containing multiple links.  
- **Automated Fetching**: Uses LangChain’s `WebBaseLoader` / UnstructuredURL loader to fetch article content.  
- **Text Processing & Splitting**: Breaks down long articles into manageable chunks.  
- **Semantic Embeddings**: Uses OpenAI’s embeddings to convert text into dense vectors.  
- **Efficient Retrieval**: Stores vectors in **FAISS** for fast similarity search.  
- **Conversational Q&A**: Ask natural-language questions and get answers with **source URLs** for validation.  

---

## 🛠️ Installation & Setup  

Clone the repo:

```bash
git clone https://github.com/UNKNOWNAR/ResearchBotBot-EquityResearchTool.git
Change into the project directory:

bash
Copy code
cd ResearchBotBot-EquityResearchTool
Install required packages:

bash
Copy code
pip install -r requirements.txt
Add your OpenAI API key:

Create a .env file at the root.

Add the following line:

ini
Copy code
OPENAI_API_KEY=your_api_key_here
▶️ Usage / Example
Launch the app with:

bash
Copy code
streamlit run main.py
Then:

On the sidebar, input URLs or upload a .txt file with URLs.

Click “Process URLs” to fetch, split, embed, and index article content.

Ask your query in the input UI — ResearchBot returns an answer derived from the documents, along with source links.

📁 Project Structure
bash
Copy code
ResearchBotBot-EquityResearchTool/
├── main.py                      # Streamlit application entry point  
├── requirements.txt             # Dependencies  
├── faiss_store_openai.pkl       # Local FAISS index file (after processing)  
├── .env                         # Environment config (OpenAI key)  
└── README.md                    # This file  
🧠 How It Works
Load & Fetch: Use LangChain to scrape and structure article content.

Split Text: Divide large documents into chunks for embedding.

Embed: Convert chunks into vectors via OpenAI embeddings.

Index & Store: Use FAISS to index vectors for similarity queries.

Query & Answer: On a question input, retrieve relevant chunks and send them to the LLM to generate an answer, citing sources.

💡 Future Enhancements
Summarization across multiple articles

Sentiment / bias detection

Topic clustering & trend visualization

Support for live news APIs and data feeds

📫 Contributing & Contact
Feel free to open issues, suggest features, or submit pull requests.
Connect on LinkedIn or shoot me a message if you want to collaborate.