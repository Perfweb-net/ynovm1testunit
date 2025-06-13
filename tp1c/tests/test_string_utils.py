import pytest
from src.string_utils import capitalize_words, count_words, remove_vowels

class TestStringUtils:
    def test_capitalize_mots_multiples(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_count_words_basique(self):
        assert count_words("hello world python") == 3
        assert count_words("") == 0

    def test_remove_vowels_basique(self):
        assert remove_vowels("hello") == "hll"
        assert remove_vowels("python") == "pythn"

    def test_capitalize_words_type_invalide(self):
        with pytest.raises(TypeError):
            capitalize_words(123)

    def test_count_words_type_invalide(self):
        with pytest.raises(TypeError):
            count_words(123)

    def test_remove_vowels_type_invalide(self):
        with pytest.raises(TypeError):
            remove_vowels(123) 