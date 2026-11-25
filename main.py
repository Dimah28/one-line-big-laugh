"""One Line, Big Laugh -- make.fun bounty u-coral-404-one-line-big-laugh-328fb857.

Writes a single hilarious one-liner (137 characters, well inside the
200-character gate) to /output/entry.txt.

The joke: a smart fridge snitches on its owner's midnight snacks to the
doctor, then escalates to a texted intervention -- "your 2 a.m.
relationship with cheese". Concrete setup (midnight snacks), absurdly
specific detail (2 a.m., cheese), surprise reversal at the end (the
appliance, not the human, stages the intervention), no word wasted.
"""

import os

LINE = (
    "My smart fridge emailed my doctor about my midnight snacks, then "
    "texted me: 'We need to talk about your 2 a.m. relationship with cheese.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert text.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
