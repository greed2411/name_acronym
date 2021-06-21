# name acronyms

> "If I'm gonna tell a real story, I'm gonna start with my name." - Kendrick Lamar

Find your destiny 🔮 in computer science🖥️📚 just by looking at the acronyms present in your name!

are you curious to know what kind of Computer Science & IT acronyms are present in your name? are you curious to know what kind of file extension acronyms are present in your name?

Lame, but I did the job of finding what all are present for my name. Actually works on any string tho.

The list of acronyms and their expansions were scraped from:
* [List of computing and IT abbreviations](https://en.wikipedia.org/wiki/List_of_computing_and_IT_abbreviations)
* [List of filename extensions](https://en.wikipedia.org/wiki/List_of_filename_extensions)

using just [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). 

on side note, TIL how to make [overlapping regex patterns](https://stackoverflow.com/questions/11430863/how-to-find-overlapping-matches-with-a-regexp/) in Python.


## Usage


```sh
λ python main.py "jaivarsan"
input str: jaivarsan

Wikipedia List of computing and IT abbreviations: 
----------------------------------------
AI : Artificial Intelligence
var : variable
RSA : Rivest Shamir Adleman
SAN : Storage Area Network
----------------------------------------

Wikipedia List of filename extensions: 
----------------------------------------
.ai : Adobe Illustrator Artwork
.v : Coq source file Verilog source file
.ar : Argon - for 3D Modeling
.rs : Rust language source
----------------------------------------
```

one more example:

```sh
λ python main.py "Albus Percival Wulfric Brian Dumbledore"
input str: Albus Percival Wulfric Brian Dumbledore

Wikipedia List of computing and IT abbreviations: 
----------------------------------------
AL : Active Link Access List
LB : Load Balancer
PE : Physical Extents
RC : Region Code Release Candidate Run Commands
UL : Upload
LF : Line Feed Low Frequency
IC : Integrated Circuit
RIA : Rich Internet Application
UMB : Upper Memory Block
MB : Megabyte
LED : Light-Emitting Diode
EDO : Extended Data Out
----------------------------------------

Wikipedia List of filename extensions: 
----------------------------------------
.b : BASIC language source Grand Theft Auto 3 save file bc arbitrary precision calculator language file
.p : Database PROGRESS source code PASCAL source code file Parser source code file
.e : E language source code
.rc : Configuration file Resource Compiler script file
.c : C language source
Note that on case-sensitive platforms like Unix and with the gcc compiler the uppercase .C extension indicates a C++ source file. Unix file archive
.v : Coq source file Verilog source file
.f : Forth language source code file Fortran language source code file (in fixed form)
.r : Ratfor file Script file
.d : D Programming Language source file Directory containing configuration files (informal standard)
.mb : Maya Binary
.dor : Roland Digital audio file
.o : Object file
----------------------------------------
```

