This script recursively enumerates the content of a directory. The output format has been tailored to assist with managing my photo archive.

The script has two optional arguments and an option. The first argument is the directory to enumerate (default `.`). The second is the output file path (default `Output.txt`). The option `-e` or `--extensions` determines whether file extensions are included in the output.

Examples of script execution

```
python.exe .\EnumerateDir.py
python.exe .\EnumerateDir.py D:\PhotosJpg\2021
python.exe .\EnumerateDir.py -e D:\PhotosJpg\2021 Output.txt
```

This script assumes

1. the directory path contains a date in format `YYYY-MM-DD`
2. the file name starts with a date in format `YYYYMMDD`

The first line of the output is the root directory path. Subsequent lines of the output are files in that directory path with or without file extension depending on the script option.

```
'{relative directory}' '{file name}{file extension}'
```
