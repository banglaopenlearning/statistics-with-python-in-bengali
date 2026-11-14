# পাইথন দিয়ে পরিসংখ্যান

An open, interactive textbook in Bengali for learning statistics with Python, by [Bangla Open Learning Lab](https://github.com/bangla-open-learning).

**Read the book:** https://bangla-open-learning.github.io/statistics-with-python-in-bengali/

## Working on the book

1. Install [Quarto](https://quarto.org/docs/get-started/) and Python 3.
2. Install the Python packages: `pip install -r requirements.txt`
3. Install a Bengali font for chart labels: [Noto Sans Bengali](https://fonts.google.com/noto/specimen/Noto+Sans+Bengali).
4. Preview while writing: `quarto preview`

## Publishing

Before pushing changes to code cells, run `quarto render` and commit the updated `_freeze/` folder. GitHub Actions then builds the site from those saved results and publishes it to GitHub Pages; it does not run your Python code.

## License

Text: CC BY-SA 4.0 · Code: MIT. See [LICENSE.md](LICENSE.md).
