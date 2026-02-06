"""Vector store utilities for MedDoc Flow.

This module provides functions for creating and querying FAISS vector stores
using HuggingFace embeddings.
"""

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List


def create_faiss_index(text_chunks: List[str]) -> FAISS:
    """Create a FAISS index from text chunks.
    
    Args:
        text_chunks: List of text chunks to index.
        
    Returns:
        FAISS: A FAISS vector store containing the indexed text chunks.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )
    
    vectorstore = FAISS.from_texts(text_chunks, embeddings)
    
    return vectorstore


def retrive_relavent_docs(vectorstore: FAISS, query: str, k: int = 3) -> List:
    """Retrieve relevant documents from the vector store.
    
    Args:
        vectorstore: FAISS vector store to query.
        query: Query string to search for.
        k: Number of documents to retrieve (default: 3).
        
    Returns:
        List: List of relevant documents.
    """
    docs = vectorstore.similarity_search(query, k=k)
    
    return docs
