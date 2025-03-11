import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_existing_text_file():
    """Test reading an existing text file with simple content."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_read_file_with_unicode():
    """Test reading a file with Unicode characters."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "こんにちは世界"
        finally:
            os.unlink(temp_file.name)

def test_nonexistent_file():
    """Test reading a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("nonexistent_file.txt")

def test_file_permissions(monkeypatch):
    """Test handling permission-related errors."""
    def mock_open(*args, **kwargs):
        raise PermissionError("Permission denied")
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            monkeypatch.setattr('builtins.open', mock_open)
            with pytest.raises(PermissionError):
                read_text_file(temp_file.name)
        finally:
            os.unlink(temp_file.name)