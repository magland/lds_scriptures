# lds_scriptures

Python access to the scriptures of the Church of Jesus Christ of Latter-day Saints

## Overview

This package provides python access to the scriptures of the Church of Jesus Christ of Latter-day Saints. It pulls data from [bcbooks/scriptures-json](https://github.com/bcbooks/scriptures-json), and that project obtained the data from the [Mormon Documentation Project](http://scriptures.nephi.org/).

## License

Everything here is in the public domain. My own personal request is that you treat these sacred texts with respect.

## Installation

```
pip install lds_scriptures
```

## Example usage

```
from lds_scriptures import LDSScriptures
```

```
scriptures=LDSScriptures()
BookOfMormon=scriptures.bookOfMormon()
display(BookOfMormon)
```

```
display(BookOfMormon.bookTitles())
```

```
ch=BookOfMormon.allBooks()[0].chapter(11)
vv=ch.verse(17)
display(vv)

print('')

verses=BookOfMormon.allVerses()
display(verses[1381])
```

```
print(len(verses))
```

## TODO (Help is welcome)

* Support the other 4 standard volumes of scripture (right now only the Book of Mormon may be loaded)
* Provide better documentation

