"""
Docstring for main module in MultiComma.

A longer description...
"""

import sublime_plugin


class MultiCommaCommand(sublime_plugin.TextCommand):
	characters_to_prepend = " ]}),"

	def add_comma_to_line(self, txt):
		for i in range(len(txt), 0, -1):
			char_idx = i - 1
			if txt[char_idx] not in self.characters_to_prepend:
				if not txt.endswith(","):
					txt = txt[: char_idx + 1] + "," + txt[char_idx + 1 :]
				break
		return txt

	def add_comma_to_line_multi(self, txt, line_ending):
		lines = [
			self.add_comma_to_line(line) for line in txt.split(line_ending)
		]
		return line_ending.join(lines)

	def run(self, edit, **args):
		for region in self.view.sel():
			line = self.view.line(region)
			txt = self.view.substr(line)
