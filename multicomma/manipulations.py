def add_comma_to_line(txt, characters_to_prepend=" ]}),"):
	for i in range(len(txt), 0, -1):
		char_idx = i - 1
		char = txt[char_idx]
		if char not in characters_to_prepend:
			try:
				next_char = txt[char_idx + 1]
			except IndexError:
				next_char = None
			if not txt.endswith(",") and next_char != ",":
				txt = txt[: char_idx + 1] + "," + txt[char_idx + 1 :]
			break
	return txt


def add_comma_to_line_multi(txt, line_ending, characters_to_prepend=" ]}),"):
	lines = [
		add_comma_to_line(line, characters_to_prepend)
		for line in txt.split(line_ending)
	]
	return line_ending.join(lines)
