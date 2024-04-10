# llm_context

```sh
# Install dependencies
pip install -e .
```

Usage:
```
concatsrc path/to/dir1/ path/to/another/dir/ path/to/file.py [--ext .py .html] 
```

Concatenates all `.py` and `html` files in the provided folders and files. If you don't pass the --ext flag, it tajes all extensions. The output is printed to stdout, in the following format:
```
# --- file: path/to/file.py
<src of file.py>

# --- file: path/to/dir1/a.html
<src of a.html>
```

On max, you can copy the output to clipboard via:
`concatsrc . | pbcopy`
