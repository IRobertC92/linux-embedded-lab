import unittest
from morse_code_decode import encode_to_morse, decode_from_morse, WORD_SEP

class TestMorseCode(unittest.TestCase):

    def test_single_letter(self):
        self.assertEqual(encode_to_morse("A"), ".-")
        self.assertEqual(decode_from_morse(".-"), "A")

    def test_word(self):
        text = "HELLO"
        morse = ".... . .-.. .-.. ---"
        self.assertEqual(encode_to_morse(text), morse)
        self.assertEqual(decode_from_morse(morse), text)

    def test_multiple_words(self):
        text = "HELLO WORLD"
        morse = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        self.assertEqual(encode_to_morse(text), morse)
        self.assertEqual(decode_from_morse(morse), text)

    def test_digits(self):
        text = "2025"
        morse = "..--- ----- ..--- ....."
        self.assertEqual(encode_to_morse(text), morse)
        self.assertEqual(decode_from_morse(morse), text)

    def test_punctuation(self):
        text = "HELLO, WORLD!"
        morse = ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
        self.assertEqual(encode_to_morse(text), morse)
        self.assertEqual(decode_from_morse(morse), text)

    def test_unknown_characters(self):
        text = "HI#"
        morse = ".... .. ?"
        self.assertEqual(encode_to_morse(text), morse)

    def test_case_insensitive(self):
        self.assertEqual(encode_to_morse("hello"), encode_to_morse("HELLO"))

    def test_extra_spaces_in_morse(self):
        morse = ".... . .-.. .-.. ---    /    .-- --- .-. .-.. -.."
        self.assertEqual(decode_from_morse(morse), "HELLO WORLD")

if __name__ == "__main__":
    unittest.main()