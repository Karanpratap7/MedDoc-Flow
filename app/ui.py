"""UI components for MedDoc Flow.

This module provides Streamlit UI components for the application.
"""

import streamlit as st
from typing import List, Optional


def pdf_uploader() -> Optional[List]:
    """Display a file uploader for PDF documents.
    
    Returns:
        Optional[List]: List of uploaded PDF files, or None if no files uploaded.
    """
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True,
        help="Upload one or more medical PDF documents"
    )
    
    return uploaded_files if uploaded_files else None
