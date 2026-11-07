"""Core Lossless Prompt Minifier implementation."""
import json
import re
from typing import Dict, Any


class LosslessPromptMinifier:
    @staticmethod
    def minify_json_blocks(text: str) -> str:
        def repl(match):
            raw = match.group(1)
            try:
                parsed = json.loads(raw)
                return "```json\n" + json.dumps(parsed, separators=(",", ":")) + "\n```"
            except Exception:
                return match.group(0)

        return re.sub(r"```json\s*([\s\S]*?)\s*```", repl, text)

    @staticmethod
    def minify_markdown_whitespace(text: str) -> str:
        text = re.sub(r"\n{3,}", "\n\n", text)
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines)

    @classmethod
    def minify(cls, prompt: str) -> Dict[str, Any]:
        orig_len = len(prompt)
        step1 = cls.minify_json_blocks(prompt)
        step2 = cls.minify_markdown_whitespace(step1)
        final_len = len(step2)

        saved = orig_len - final_len
        ratio = (saved / orig_len) if orig_len > 0 else 0.0

        return {
            "original_chars": orig_len,
            "minified_chars": final_len,
            "saved_chars": saved,
            "reduction_ratio": round(ratio, 3),
            "minified_text": step2
        }
