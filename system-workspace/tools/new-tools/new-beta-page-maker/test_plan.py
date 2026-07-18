import re


def test_plan():
    with open("plans/01-أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ-plan.md") as f:
        content = f.read()

    # 1. Content Depth (at least 4 blocks)
    blocks = re.findall(r"=== BLOCK \d+:", content)
    assert len(blocks) >= 4, f"Failed: Found {len(blocks)} blocks, expected at least 4."

    # 2. Golden Flow components check
    assert "(Component: TEMPLATE_C_HEADER.html)" in content, "Missing Header component"
    assert "(Component: TEMPLATE_C_TABLE.html)" in content, "Missing Table/Matrix component"
    assert "(Component: TEMPLATE_C_EXAM.html)" in content, "Missing Exam component"

    # 3. Class Usage
    assert 'class="text-accent"' in content, "Missing .text-accent in definitions"

    # 4. Correct Metadata
    assert "[AUTHOR_NAME]: أ. حنا خفيف" in content, "Incorrect author name"
    assert "[AUTHOR_PHONE]:  " in content, "Incorrect author phone"

    print("All tests passed.")


if __name__ == "__main__":
    test_plan()
