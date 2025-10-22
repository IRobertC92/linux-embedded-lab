import pytest
from morse_code_decode import encode_to_morse, decode_from_morse, WORD_SEP


def test_single_letter():
    assert encode_to_morse("A") == ".-"
    assert decode_from_morse(".-") == "A"


def test_word():
    text = "HELLO"
    morse = ".... . .-.. .-.. ---"
    assert encode_to_morse(text) == morse
    assert decode_from_morse(morse) == text


def test_multiple_words():
    text = "HELLO WORLD"
    morse = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    assert encode_to_morse(text) == morse
    assert decode_from_morse(morse) == text


def test_digits():
    text = "2025"
    morse = "..--- ----- ..--- ....."
    assert encode_to_morse(text) == morse
    assert decode_from_morse(morse) == text


def test_punctuation():
    text = "HELLO, WORLD!"
    morse = ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
    assert encode_to_morse(text) == morse
    assert decode_from_morse(morse) == text


def test_unknown_characters():
    assert encode_to_morse("HI#") == ".... .. ?"


def test_case_insensitive():
    assert encode_to_morse("hello") == encode_to_morse("HELLO")


def test_extra_spaces_in_morse():
    morse = ".... . .-.. .-.. ---    /    .-- --- .-. .-.. -.."
    assert decode_from_morse(morse) == "HELLO WORLD"
