## RegEx Methods

- `match(pattern: str, string: str) -> Match | None`: look for first match at beginning of string
- `search(pattern: str, string: str) -> Match | None`: scan through a string for first match
- `findall(pattern: str, string: str) -> List[str | Tuple[str, ...]]`: find all matches, returning entire match / tuple of subgroup matches

## Match Object
- `Match.group(group1: int, ...) -> None | str | Tuple[str, ...]`: `0` is entire match, `1` onwards is parenthsized subgroup
	- If group is inside unmatched part, return `None`
	- If group is matched multiple times, return last match
- `Match.groups() -> Tuple[str, ...]`: returns all subgroups, entire match is not included