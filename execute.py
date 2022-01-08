import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import List

OBSIDIAN_DIR = Path("obsidian")
DOCS_DIR = Path("content/docs")


def rm_front(content: List[str]) -> List[str]:
    """
    Remove obsidian-specific front matters
    """
    if len(content) == 0 or not content[0].startswith("---"):
        return content

    frontmatter_end = -1
    for i, line in enumerate(content[1:]):
        if line.startswith("---"):
            frontmatter_end = i
            break

    if frontmatter_end > 0:
        return content[frontmatter_end + 2 :]

    return content


def filter_lines(file: Path, content: List[str]) -> List[str]:
    """
    1. Replace obsidian relative links to valid absolute links
    2. Double escape latex newline
    """
    parent_dir = f"{file.parents[0]}".replace("content/", "/")
    replaced_links = [
        re.sub(
            r"(\[.+?\])\((?!http)(.+?)(?:.md)?\)", r"\1(" + parent_dir + r"/\2)", line
        )
        for line in content
    ]
    replaced_slashes = [re.sub(r"\\\\$", r"\\\\\\\\", line) for line in replaced_links]
    return replaced_slashes


def write_front(file: Path, content: List[str]) -> List[str]:
    title = " ".join(
        [item if item.isupper() else item.title() for item in file.stem.split(" ")]
    )
    modified = datetime.fromtimestamp(os.path.getmtime(file))
    return [
        "---",
        f"title: {title}",
        f"date: {modified}",
        f"updated: {modified}",
        "template: docs/page.html",
        "---",
        *content,
    ]


shutil.copytree(
    OBSIDIAN_DIR,
    DOCS_DIR,
    dirs_exist_ok=True,
    ignore=lambda _, contents: [item for item in contents if item.startswith(".")],
)

md_files = list(DOCS_DIR.glob("**/*.md"))
for md_file in md_files:
    content = [line.rstrip() for line in open(md_file, "r").readlines()]
    if str(md_file).endswith("_index.md"):
        continue

    content = rm_front(content)
    content = filter_lines(md_file, content)
    content = write_front(md_file, content)
    open(md_file, "w").write("\n".join(content))

md_dirs = list(DOCS_DIR.glob("**/**"))
for md_dir in md_dirs:
    title = str(md_dir).replace("content/", "")
    content = [
        "---",
        f"title: {title}",
        "template: docs/section.html",
        "sort_by: date",
        "---",
    ]
    open(md_dir / "_index.md", "w").write("\n".join(content))
