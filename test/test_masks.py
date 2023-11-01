from src.masks import maskin_bil_number, masking_the_card


def test_masking_the_card():
    assert masking_the_card("7000792289606361") == "7000 79** **** 6361"
    assert masking_the_card("") == ""


def test_maskin_bil_number():
    assert maskin_bil_number("73654108430135874305") == "**4305"
    assert maskin_bil_number("") == ""
