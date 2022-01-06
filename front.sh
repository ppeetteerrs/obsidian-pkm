#!/bin/bash

for filename in $(pwd)/content/*.md; do
	if [[ "$filename" != *"index.md" ]]; then
		start=$(cat "$filename" | head -c 3);
		echo ""
		echo "========> Appending front matter to" "$filename"
		content=$(sed '1 { /^---/ { :a N; /\n---/! ba; d} }' "$filename")
		modified=$(date -Rr "$filename")
		echo "---\nupdated:" "$modified" "\n---\n$content" # > "$filename"
	fi
done