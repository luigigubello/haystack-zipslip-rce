# haystack-zipslip-rce

The function **fetch_archive_from_http()** in a **haystack.utils** has an arbitrary file overwrite vulnerability (a.k.a zip slip vulnerability) which could lead to remote code execution. 

The Python library **tarfile** is vulnerable to zip slip ([tarfile: Traversal attack vulnerability issue21109](https://bugs.python.org/issue21109)), and in the function **fetch_archive_from_http** there are no security checks on the filenames inside the archive file.

Tested on **farm-haystack 1.25.4**.

### PoC

```
docker build -t haystack-poc . 
docker run -it haystack-poc bash
python app.py
python app.py
```
