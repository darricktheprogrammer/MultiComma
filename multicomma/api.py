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
		new_regions = []
		for region in self.view.sel():
			print("original: {}, {}".format(region.begin() ,region.end()))
			expanded_region = self.view.line(region)
			txt = self.view.substr(expanded_region)
			with_comma = add_comma_to_line_multi(txt, self._line_endings())
			self.view.replace(edit, expanded_region, with_comma)
			# self.view.sel().subtract(expanded_region)
			# if self._line_endings() in txt:
			# if region.a != region.b:
			if region.empty():
				# single cursor point. Revert ST moving it to the right.
				# new_cursor_pos = self.view.text_point(region.begin(), region.end())
				# new_regions.append(new_cursor_pos)
				self.view.sel().subtract(region)
				region.a += 1
				region.b += 1
				# new_regions.append(region)

				print("updated: {}, {}".format(region.begin(), region.end()))
				# self.view.sel().add(target)
				# self.view.run_command("move", {"by": "characters", "forward": False})
			else:
				self.view.sel().add(region)
				# if region.b > region.a:
				# 	region.b = expanded_region.b
				# else:
				# 	region.a = expanded_region.a
				# new_regions.append(region)
			print("expanded: {}, {}".format(expanded_region.begin(), expanded_region.end()))
			print()
		# self.view.sel().clear()
		# self.view.sel().add_all(new_regions)
