"""TEI Parser Tests."""

from uedition.ext.tei.parser import format_iso8601_date


def test_format_iso8601_date() -> None:
    """Test that the date reformatter works."""
    assert format_iso8601_date(None, "2022-01-04") == "04.01.2022"
    assert format_iso8601_date(None, "2022-01") == "01.2022"
    assert format_iso8601_date(None, "2022") == "2022"
    assert format_iso8601_date(None, "Not a date") == ""
    assert format_iso8601_date(None, ["Not a date"]) == ""
