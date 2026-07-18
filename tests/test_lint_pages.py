import sys
from pathlib import Path

# Add Jules-workspace to sys.path so we can import the modules
sys.path.insert(0, str(Path("Jules-workspace").resolve()))

from lint_pages import lint_file, parse_allowed_classes


def test_parse_allowed_classes(tmp_path):
    # Create a dummy css file
    css_content = """
    .valid-class { color: red; }
    .another-class { margin: 0; }
    #id-selector { color: blue; }
    .bg-dark { background: #333; }
    """
    css_file = tmp_path / "main.css"
    css_file.write_text(css_content)

    classes = parse_allowed_classes(css_file)
    assert "valid-class" in classes
    assert "another-class" in classes
    assert "bg-dark" in classes
    assert "id-selector" not in classes


def test_lint_file_inline_style_violation(tmp_path):
    html_content = '<div style="color: red;">Hello</div>'
    html_file = tmp_path / "test.html"
    html_file.write_text(html_content)

    result = lint_file(html_file, allowed_classes=frozenset())
    assert not result.passed
    assert len(result.errors) == 1
    assert "STRICT VIOLATION: Inline style" in result.errors[0].message


def test_lint_file_forbidden_class(tmp_path):
    html_content = '<ul class="list-disc"><li>Item</li></ul>'
    html_file = tmp_path / "test.html"
    html_file.write_text(html_content)

    result = lint_file(
        html_file, allowed_classes=frozenset(["list-disc"])
    )  # list-disc is explicitly banned
    assert not result.passed

    error_msgs = [e.message for e in result.errors]
    assert any("FORBIDDEN" in msg for msg in error_msgs)


def test_lint_file_valid_html(tmp_path):
    html_content = '<div class="content-block"><p>Hello</p></div>'
    html_file = tmp_path / "test.html"
    html_file.write_text(html_content)

    result = lint_file(html_file, allowed_classes=frozenset(["content-block"]))
    assert result.passed
    assert len(result.errors) == 0
