publish:
	@echo "--- 📦 Publishing to PyPI ---"
	rm -rf dist
	uv build
	uv publish

bump-version:
	@echo "--- 🔖 Bumping version ---"
	uv version --bump patch
