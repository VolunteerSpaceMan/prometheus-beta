import pytest
from src.anagram import is_anagram

def test_basic_anagrams():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_case_insensitive():
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("LISTEN", "silent") == True

def test_whitespace():
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("astronomer", "moon starer") == True

def test_non_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "javascript") == False

def test_same_letters_different_count():
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "aaa") == False

def test_empty_strings():
    assert is_anagram("", "") == True

def test_single_char():
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False

def test_invalid_input():
    with pytest.raises(TypeError):
        is_anagram(123, "hello")
    with pytest.raises(TypeError):
        is_anagram("hello", None)
    with pytest.raises(TypeError):
        is_anagram(None, None)