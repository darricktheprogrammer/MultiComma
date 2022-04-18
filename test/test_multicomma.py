#!/usr/bin/env python3
from multicomma.api import MultiCommaCommand


class TestSingleLine:
	def test_AddCommaToLine_GivenSimpleText_AppendsComma(self):
		txt = "sample text"
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == "sample text,"

	def test_AddCommaToLine_AlreadyContainsComma_ReturnsOriginalString(self):
		txt = "sample text,"
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == "sample text,"

	def test_AddCommaToLine_EndsWithBracket_AppendsBeforeBracket(self):
		txt = "sample text]"
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == "sample text,]"

	def test_AddCommaToLine_EndsWithCurlyBracket_AppendsBeforeBracket(self):
		txt = "sample text}"
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == "sample text,}"

	def test_AddCommaToLine_EndsWithParenthesis_AppendsBeforeBracket(self):
		txt = "sample text)"
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == "sample text,)"

	def test_AddCommaToLine_SingleCharacter_AppendsComma(self):
		txt = "a"
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == "a,"

	def test_AddCommaToLine_EmptyLine_ReturnsOriginalString(self):
		txt = ""
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == ""

	def test_AddCommaToLine_OnlyWhitespace_ReturnsOriginalString(self):
		txt = "      "
		result = MultiCommaCommand().add_comma_to_line(txt)
		assert result == "      "


class TestMultiLine:
	def test_AddCommaToLineMulti_GivenSimpleText_AppendsComma(self):
		txt = (
			"sample text 1\n"
			"sample text 2\n"
			"sample text 3"
			)
		expected = (
			"sample text 1,\n"
			"sample text 2,\n"
			"sample text 3,"
			)
		result = MultiCommaCommand().add_comma_to_line_multi(txt, "\n")
		assert result == expected

	def test_AddCommaToLineMulti_WithBlankLine_DoesNotAppendToBlankLine(self):
		txt = (
			"sample text 1\n"
			"\n"
			"sample text 3"
			)
		expected = (
			"sample text 1,\n"
			"\n"
			"sample text 3,"
			)
		result = MultiCommaCommand().add_comma_to_line_multi(txt, "\n")
		assert result == expected

	def test_AddCommaToLineMulti_GivenCRLFLIneEnding_AppendsComma(self):
		txt = (
			"sample text 1\r\n"
			"sample text 2\r\n"
			"sample text 3"
			)
		expected = (
			"sample text 1,\r\n"
			"sample text 2,\r\n"
			"sample text 3,"
			)
		result = MultiCommaCommand().add_comma_to_line_multi(txt, "\r\n")
		assert result == expected

	def test_AddCommaToLineMulti_InconsistentIndentation_AppendsComma(self):
		txt = (
			"sample text 1\n"
			"	sample text 2\n"
			" sample text 3"
			)
		expected = (
			"sample text 1,\n"
			"	sample text 2,\n"
			" sample text 3,"
			)
		result = MultiCommaCommand().add_comma_to_line_multi(txt, "\n")
		assert result == expected

	def test_AddCommaToLineMulti_BracketWrapped_AppendsCommaBeforeBracket(self):
		txt = (
			"(sample text 1\n"
			"	sample text 2\n"
			" sample text 3)"
			)
		expected = (
			"(sample text 1,\n"
			"	sample text 2,\n"
			" sample text 3,)"
			)
		result = MultiCommaCommand().add_comma_to_line_multi(txt, "\n")
		assert result == expected
