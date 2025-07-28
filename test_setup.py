#!/usr/bin/env python3
"""
Test script to verify the MediChat Pro setup is working correctly.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_file_reading():
    """Test that we can read the patient files correctly."""
    test_dir = "test_patient_records"
    
    if not os.path.exists(test_dir):
        print(f"❌ Test directory '{test_dir}' not found!")
        return False
    
    files = [f for f in os.listdir(test_dir) if f.endswith('.txt')]
    if not files:
        print(f"❌ No text files found in '{test_dir}'!")
        return False
    
    print(f"✅ Found {len(files)} test files:")
    for file in files:
        filepath = os.path.join(test_dir, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"  - {file}: {len(content)} characters")
        except Exception as e:
            print(f"  - {file}: ❌ Error reading file: {e}")
            return False
    
    return True

def test_imports():
    """Test that all required modules can be imported."""
    required_modules = [
        'streamlit',
        'pypdf', 
        'langchain',
        'langchain_community',
        'sentence_transformers'
    ]
    
    print("Testing module imports:")
    all_good = True
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"  ✅ {module}")
        except ImportError as e:
            print(f"  ❌ {module}: {e}")
            all_good = False
    
    return all_good

if __name__ == "__main__":
    print("🩺 MediChat Pro - Setup Test")
    print("=" * 40)
    
    # Test file reading
    files_ok = test_file_reading()
    print()
    
    # Test imports
    imports_ok = test_imports()
    print()
    
    if files_ok and imports_ok:
        print("🎉 All tests passed! Your MediChat Pro setup is ready.")
        print("\nTo run the application:")
        print("  streamlit run main.py")
    else:
        print("⚠️  Some issues were found. Please install missing dependencies:")
        print("  pip install -r requirements.txt")
