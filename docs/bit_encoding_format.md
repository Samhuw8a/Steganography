# Bit Format
#### META
- Erstes R-Val des Bildes hat die Anzahl der LSB, die verändert worden sind. (immer die 2 LSB)
- File-Hash (Sha256, 256 bits)
- File-Name (Ascii-String)
----
#### FILE-BITS
- Steg-Tag [STEG]
- File-Content (komprimiert mit LZMA und AES encoded file-Content)
- Steg-Tag [Steg]
