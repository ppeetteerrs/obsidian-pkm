#!/bin/bash

cp -r obsidian/* content/docs

find content/docs -type f -print0 | while IFS= read -r -d '' filename; do
	if [[ "$filename" == *".md" ]]; then
		if [[ "$filename" != *"index.md" ]]; then
			echo ""
			echo "========> Appending front matter to" "$filename"
			content=$(sed "1 { /^---/ { :a N; /\n---/! ba; d} }" "$filename")
			content=$(echo "$content" | sed "s/\\\\\\\\/\\\\\\\\\\\\\\\\/g")
			title=$(basename "$filename" .md | sed -e "s/\b\(.\)/\u\1/g")
			modified=$(date -I -r "$filename")
			echo -e "---\ntitle: $title\nupdated: $modified\ndate: $modified\ntemplate: 'docs/page.html'\n---\n" > "$filename"
			echo "$content" >> "$filename"
		fi
	fi
done

for dirname in $(find content/docs -type d | sed -n 's|^content/||p' ); do
	echo -e "---\ntitle: '$dirname'\ntemplate: 'docs/section.html'\nsort_by: date\n---\n" > content/"$dirname"/_index.md
done