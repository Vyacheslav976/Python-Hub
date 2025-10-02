import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.pozitive
@pytest.mark.parametrize("input_str, expected_str",
                         [
                             ("hello", "Hello"),
                             ("privet people", 'Privet people'),
                             ("Test", "Test"),
                             ("privet Nikolay", "Privet Nikolay")
                         ])

def capitalize_pozitive(input_str, expected_str):
    assert string_utils.capitalize(input_str) == expected_str

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_str",
                         [
                             ("", ""),
                             ("    ", "    "),
                             ("123abc", "123abc"),
                         ])

def capitalize_negative(input_str, expected_str):
    assert string_utils.capitalize(input_str) == expected_str


@pytest.mark.pozitive
@pytest.mark.parametrize("input_str, expected_str",
                        [
                            (" hello", "hello"),
                            (" Privet Nikolay", "Privet Nikolay"),
                            ('  04 april 2025', "04 april 2025")
                        ])

def trim_pozitive(input_str, expected_str):
    assert string_utils.trim(input_str) == expected_str

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_str",
                        [
                            ("", ""),
                            ("    ", ""),
                            ("   123abc", "123abc"),
                        ])
def trim_negative(input_str, expected_str):
    assert string_utils.trim(input_str) == expected_str

@pytest.mark.pozitive
@pytest.mark.parametrize("input_str, symbol, boolean",
                          [
                              ("SkyPro", "S", True),
                              ("1234qwer", "q", True),
                              ("04 april 2025", "2", True),
                              ("04 april 2025", " ", True),
                          ])
def contains_pozitive(input_str, symbol, boolean):
    assert string_utils.contains(input_str, symbol) == boolean

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, boolean"
                          [
                              ("SkyPro", "R", False),
                              ("04 april 2025", "7", False),
                          ])
def contains_negative(input_str, symbol, boolean):
    assert string_utils.contains(input_str, symbol) == boolean

@pytest.mark.pozitive
@pytest.mark.parametrize("input_str, symbol, expected_str"
                          [
                              ("SkyPro", "S", "kyPro"),
                              ("1234qwer", "q", "1234wer"),
                              ("04 april 2025", "2", "04 april 05"),
                              ("04 april 2025", " ", "04april2025"),
                          ])
def delete_symbol_pozitive(input_str, symbol, expected_str):
    assert string_utils.delete_symbol(input_str, symbol) == expected_str

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_str"
                          [
                              ("SkyPro", "n", "SkyPro"),
                              ("04 april 2025", "7", "04 april 2025"),
                              ("", "  ", ""),
                          ])
def delete_symbol_negative(input_str, symbol, expected_str):
    assert  string_utils.contains(input_str, symbol) == expected_str

