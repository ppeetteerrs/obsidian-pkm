#!/bin/sh

for filename in $(pwd)/content/*.md; do
    start=$(cat "$filename" | head -c 3);
	if [ "$start" != "---" ]; then
		echo "Appending front matter to" "$filename"
		echo -e "---\naliases: []\n---\n$(cat "$filename")" > "$filename"
	fi
done