"""Tests for lossless-prompt-minifier."""
import unittest
import json
from lossless_prompt_minifier.minifier import LosslessPromptMinifier


class TestMinifier(unittest.TestCase):
    def test_json_block_compaction(self):
        raw = "```json\n{\n  \"a\": 1,\n  \"b\": 2\n}\n```"
        res = LosslessPromptMinifier.minify(raw)
        self.assertIn('{"a":1,"b":2}', res["minified_text"])
        self.assertGreater(res["saved_chars"], 0)

    def test_whitespace_compaction(self):
        text = "Line 1\n\n\n\n\nLine 2"
        res = LosslessPromptMinifier.minify(text)
        self.assertEqual(res["minified_text"], "Line 1\n\nLine 2")
