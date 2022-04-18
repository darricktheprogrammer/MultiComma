"""
Docstring for main module in MultiComma.

A longer description...
"""

import sublime_plugin
from .manipulations import add_comma_to_line_multi


class MultiCommaCommand(sublime_plugin.TextCommand):
	characters_to_prepend = " ]}),"

	LINE_ENDINGS = {
		"unix": "\n",
		"windows": "\r\n",
	}

	def _line_endings(self):
		return self.LINE_ENDINGS[self.view.line_endings().lower()]

	def run(self, edit, **args):
		for region in self.view.sel():
			expanded_region = self.view.line(region)
			txt = self.view.substr(expanded_region)
			with_comma = add_comma_to_line_multi(txt, self._line_endings())
			self.view.replace(edit, expanded_region, with_comma)
