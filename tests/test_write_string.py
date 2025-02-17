import os
import pytest
import tempfile
from src.write_string import write_string_to_file

def test_write_string_to_file_success():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test writing a string to the file
        test_content = "Hello, world!"
        write_string_to_file(temp_path, test_content)
        
        # Verify the content was written correctly
        with open(temp_path, 'r') as file:
            assert file.read() == test_content
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_write_string_to_file_empty_string():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test writing an empty string
        write_string_to_file(temp_path, "")
        
        # Verify the file is empty
        with open(temp_path, 'r') as file:
            assert file.read() == ""
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_write_string_to_file_invalid_file_path():
    # Test with non-string file path
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "test content")

def test_write_string_to_file_invalid_content():
    # Test with non-string content
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_non_existent_directory():
    # Test writing to a non-existent directory
    with pytest.raises(OSError):
        write_string_to_file("/non/existent/directory/file.txt", "test content")