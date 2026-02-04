"""PDF utilities for MedDoc Flow.

This module provides functions for extracting text from PDF documents.
"""

from pypdf import PdfReader
from typing import BinaryIO


def extract_text_from_pdf(pdf_file: BinaryIO) -> str:
    """Extract text from a PDF file.
    
    Args:
        pdf_file: Binary file object containing the PDF data.
        
    Returns:
        str: Extracted text from all pages of the PDF.
    """
    pdf_reader = PdfReader(pdf_file)
    text = ""
    
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text
