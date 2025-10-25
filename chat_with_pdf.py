import os
import io
import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("LITELLM_API_KEY")
if not api_key:
    st.warning("⚠️ No API key detected. Please set OPENAI_API_KEY or LITELLM_API_KEY.")
os.environ["OPENAI_API_KEY"] = api_key

st.set_page_config(page_title="RAG Chat", page_icon="📚")
st.title("📚 Retrieval-Augmented Generation Chatbot")

def get_embeddings():
    if os.getenv("OPENAI_API_KEY"):
        return OpenAIEmbeddings(
            model="openai.text-embedding-3-small",
            openai_api_base="https://api.ai.it.cornell.edu/v1"
        )
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_llm():
    if os.getenv("OPENAI_API_KEY"):
        return ChatOpenAI(
            model="openai.gpt-4o-mini",
            temperature=0.2,
            openai_api_base="https://api.ai.it.cornell.edu/v1"
        )
    else:
        class Dummy:
            def invoke(self, _):
                return "⚠️ No API key available. Please set it before chatting."
        return Dummy()

embeddings = get_embeddings()
llm = get_llm()
vector_dir = ".chromadb"
vs = Chroma(collection_name="rag_docs", persist_directory=vector_dir, embedding_function=embeddings)

def parse_pdf(file_bytes):
    reader = PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def parse_txt(file_bytes):
    return file_bytes.decode("utf-8", errors="ignore")

def chunk_text(text, source, size=1000, overlap=150):
    splitter = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=overlap)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=c, metadata={"source": source}) for c in chunks]
    return docs

st.subheader("Upload your documents (.txt or .pdf)")
uploaded_files = st.file_uploader("Upload files", type=["txt", "pdf"], accept_multiple_files=True)
new_docs = []

if uploaded_files:
    for f in uploaded_files:
        content = parse_pdf(f.read()) if f.name.endswith(".pdf") else parse_txt(f.read())
        docs = chunk_text(content, f.name)
        new_docs.extend(docs)
    if new_docs:
        vs.add_documents(new_docs)
        vs.persist()
        st.success(f"✅ Indexed {len(new_docs)} chunks from {len(uploaded_files)} file(s).")

if "history" not in st.session_state:
    st.session_state["history"] = []

if st.button("🧹 Clear Chat History"):
    st.session_state["history"].clear()
    st.rerun()

for msg in st.session_state["history"]:
    with st.chat_message("user"):
        st.markdown(msg[0])
    with st.chat_message("assistant"):
        st.markdown(msg[1])

query = st.chat_input("Ask a question about your documents...")
if query:
    retriever = vs.as_retriever(search_kwargs={"k": 4})
    related_docs = retriever.invoke(query)
    context = "\n".join([f"[{d.metadata['source']}] {d.page_content}" for d in related_docs])

    template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Use the provided context to answer."),
        ("human", "Context:\n{context}\n\nQuestion: {question}")
    ])
    chain = template | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": query})

    with st.chat_message("user"):
        st.markdown(query)
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state["history"].append((query, answer))
