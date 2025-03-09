import pytest
from src.substring_finder import longest_common_substring

def test_basic_common_substring():
    """Test finding a basic common substring"""
    assert longest_common_substring("hello", "help") == "hel"

def test_full_string_match():
    """Test when one string is a complete substring of another"""
    assert longest_common_substring("abcde", "cde") == "cde"

def test_no_common_substring():
    """Test when there are no common substrings"""
    assert longest_common_substring("cat", "dog") == ""

def test_empty_strings():
    """Test behavior with empty strings"""
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("test", "") == ""
    assert longest_common_substring("", "test") == ""

def test_same_string():
    """Test when both input strings are identical"""
    assert longest_common_substring("python", "python") == "python"

def test_case_sensitive():
    """Test case sensitivity"""
    assert len(longest_common_substring("Hello", "hello")) == 0, \
        "Should return an empty string for case-insensitive match"

def test_multiple_common_substrings():
    """Test with multiple possible common substrings"""
    result = longest_common_substring("abcabcabc", "bcabca")
    assert result in ["bcabca", "bcabc"], \
        f"Unexpected result: {result}"

def test_long_strings():
    """Test with longer strings"""
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "mnopqrstuvwxyz"
    assert longest_common_substring(str1, str2) == "mnopqrstuvwxyz"