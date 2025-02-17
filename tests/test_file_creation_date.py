import os
import pytest
import datetime
from src.file_creation_date import get_file_creation_date

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Test content")
    return str(file_path)

def test_get_file_creation_date_exists(temp_file):
    """Test getting creation date for an existing file."""
    creation_date = get_file_creation_date(temp_file)
    assert isinstance(creation_date, datetime.datetime)
    assert creation_date <= datetime.datetime.now()

def test_get_file_creation_date_non_existent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_creation_date("/path/to/non/existent/file.txt")

def test_get_file_creation_date_no_permission(monkeypatch):
    """Test handling of permission errors."""
    def mock_path_exists(path):
        return True
    
    def mock_stat(path):
        raise PermissionError("Permission denied")
    
    monkeypatch.setattr(os.path, 'exists', mock_path_exists)
    monkeypatch.setattr(os, 'stat', mock_stat)
    
    with pytest.raises(PermissionError):
        get_file_creation_date("/path/to/restricted/file.txt")

def test_get_file_creation_date_type(temp_file):
    """Ensure the return type is a datetime object."""
    result = get_file_creation_date(temp_file)
    assert isinstance(result, datetime.datetime)
    assert result.tzinfo is None  # Naive datetime