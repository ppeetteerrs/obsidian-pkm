[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet)

## Overview
RegEx patterns are made up of characters, groups and ranges:
- **Characters**: match a single character
- **Group**: match all chracters in group (AND)
- **Range**: match any character in range (OR)

## Characters
| RegEx            | Meaning                                               |
| ---------------- | ----------------------------------------------------- |
| `.`              | Anything except `\n`, `\r`. Means literal dot in `[]` |
| `\d`             | Digit                                                 |
| `\D`             | Not digit                                             |
| `\s`             | Whitespace (tab, space, newline, etc.)                |
| `\S`             | Not whitespace                                        |
| `\w`             | `[A-Za-z0-9_]`                                        |
| `\W`             | `[^A-Za-z0-9_]`                                       |
| `\t`, `\r`, `\n` | Normal meanings                                       |
| `$`              | end of string                                         |
| `^`              | start of string                                       |

## Quantifiers
| RegEx            | Meaning                                         |
| ---------------- | ----------------------------------------------- |
| `x?`             | 0 or 1 time                                     |
| `x{a,b}`         | `x` between `a` and `b` times (inclusive)       |
| `x+`             | 1 or more                                       |
| `x*`             | 0 or more                                       |
| `x<quantifier>?` | Non-greedy match (as little string as possible) |
| `$`              | end of string                                   |

## Lookahead / Lookbehind
| RegEx     | Meaning                           |
| --------- | --------------------------------- |
| `x(?=y)`  | match x if x is followed by y     |
| `x(?!y)`  | match x if x is not followed by y |
| `x(?<=y)` | match x if x is preceded by y     |
| `x(?<!y)` | match x if x is not preceded by y |

## Groups and Ranges
| RegEx                 | Meaning                                                 |
| --------------------- | ------------------------------------------------------- |
| <code>x&#124;y</code> | x or y (default global group, use inside group / range) |
| `[<characters>]`      | match any enclosed character                            |
| `[^<characters>]`     | match any non-enclosed character                        |
| `(x)`                 | capturing group, use via `$1, ..., $9`                  |
| `\n`                  | backreference to group `n`                              |
| `(?:x)`               | non-capturing group                                     |

See [here](https://stackoverflow.com/questions/49809122/vertical-bar-symbol-within-a-markdown-table) on how to display `|` inside a Markdown table.