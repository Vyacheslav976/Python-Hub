import pytest
from string_processor import StringProcessor

@pytest.mark.parametrize("input_text, output_text",
                         [
                             ("hello", "Hello."),
                             ("hello.", 'Hello.'),
                             ("Hello", "Hello.")
                         ])

    def pozitive_tests(input_text, output_text):
        stroka = StringProcessor()
        result = stroka.process(input_text)
        assert result == output_text

@pytest.mark.parametrize("input_text, output_text",
                         [
                             ("", '.'),
                             ("    ", '.')
                         ])

    def negative_tests(input_text, output_text):
        stroka = StringProcessor()
        result = stroka.process(input_text)
        assert result == output_text