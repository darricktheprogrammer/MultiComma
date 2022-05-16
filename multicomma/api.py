"""
Docstring for main module in MultiComma.

A longer description...
"""

import sublime_plugin
from sublime import Region

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
		for i, region in enumerate(self.view.sel()):
			full_line_region = self.view.line(region)
			txt = self.view.substr(full_line_region)
			if txt.endswith(","):
				continue
			is_reverse_selection = region.a > region.b
			begin = region.a if not is_reverse_selection else region.b

			with_comma = add_comma_to_line_multi(txt, self._line_endings())
			self.view.replace(edit, full_line_region, with_comma)

			# Update the region after adding text, otherwise the selections
			# don't go back in the right place.
			edited_region = self.view.sel()[i]
			end = (
				edited_region.b
				if not is_reverse_selection
				else edited_region.a
			)

			self.view.sel().subtract(self.view.sel()[i])
			self.view.sel().subtract(full_line_region)
			self.view.sel().subtract(region)

			if region.empty():
				self.view.sel().add(region)
			elif is_reverse_selection:
				new_region = Region(end - 1, begin)
				self.view.sel().add(new_region)
			else:
				new_region = Region(begin, end - 1)
				self.view.sel().add(new_region)
