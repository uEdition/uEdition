"""Tests for the Sphinx extension configuration."""

from uedition.ext.config import Rule, RuleSelector, RuleSelectorAttribute


def test_rule_selector_conversion() -> None:
    """Test that the simple rule selector is correctly converted."""
    rule = Rule(selector="head")
    assert rule == Rule(selector={"tag": "head"})


def test_rule_selector_namespace_expansion() -> None:
    """Test that the tei: namespace prefix is correctly converted."""
    selector = RuleSelector(tag="tei:head")
    assert selector.tag == "{http://www.tei-c.org/ns/1.0}head"


def test_rule_selector_keep_list() -> None:
    """Test that a list of attributes in the selector is left alone."""
    selector = RuleSelector(tag="tei:head", attributes=[{"attr": "level", "value": "1"}])
    assert selector.attributes == [RuleSelectorAttribute(attr="level", value="1")]


def test_rule_selector_convert_single_attribute() -> None:
    """Test that a single attribute in the selector is correctly coerced into a list."""
    selector = RuleSelector(tag="tei:head", attributes={"attr": "level", "value": "1"})
    assert selector.attributes == [RuleSelectorAttribute(attr="level", value="1")]
