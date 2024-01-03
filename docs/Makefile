render:
	for dot_file in diagrams/*.dot; do \
		png_file="$${dot_file%.*}.png"; \
		dot -Tpng "$$dot_file" -Gdpi=300 -o "$$png_file"; \
	done