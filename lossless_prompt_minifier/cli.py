"""CLI for lossless-prompt-minifier."""
import sys
import argparse
from .minifier import LosslessPromptMinifier


def main():
    parser = argparse.ArgumentParser(description="Lossless Prompt Minifier")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        prompt = "# Title\n\nHere is the config:\n\n```json\n{\n    \"port\": 5432\n}\n```\n\n\nDone."
        res = LosslessPromptMinifier.minify(prompt)
        print(f"Reduction: {res['reduction_ratio']*100:.1f}%")
        print("Minified Output:")
        print(res["minified_text"])
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
