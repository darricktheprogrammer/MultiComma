"""
Docstring for main module in MultiComma.

A longer description...
"""

import sublime_plugin


class MultiCommaCommand(sublime_plugin.TextCommand):
	characters_to_prepend = " ]}),"

	def run(self, edit, **args):
		for region in self.view.sel():
