from urllib.request import urlopen
import json

class LDSScriptures():
  def __init__(self):
    self._old_testament=None
    self._new_testament=None
    self._book_of_mormon=None
    self._doctrine_and_covenants=None
    self._pearl_of_great_price=None
  def oldTestament(self):
    if not self._old_testament:
      raise Exception('Old Testament not yet supported')
    return self._old_testament
  def newTestament(self):
    if not self._new_testament:
      raise Exception('New Testament not yet supported')
    return self._new_testament
  def bookOfMormon(self):
    if not self._book_of_mormon:
      self._load_book_of_mormon()
    return self._book_of_mormon
  def doctrineAndCovenants(self):
    if not self._doctrine_and_covenants:
      raise Exception('D&C not yet supported')
    return self._doctrine_and_covenants
  def pearlOfGreatPrice(self):
    if not self._pearl_of_great_price:
      raise Exception('Pearl of Great Price not yet supported')
    return self._pearl_of_great_price
  
  def _load_book_of_mormon(self):
    url='https://raw.githubusercontent.com/bcbooks/scriptures-json/master/book-of-mormon.json'
    with urlopen(url) as f:
      obj=json.load(f)
    self._book_of_mormon=Volume(obj)
  

class Volume():
  def __init__(self,obj):
    self._object=obj
    self._books=[]
    for i,b in enumerate(self._object['books']):
      self._books.append(Book(self,b,i+1))
  def _repr_html_(self):
    return self.title()
  def object(self):
    return self._object
  def title(self):
    return self._object['title']
  def bookTitles(self):
    return [b.title() for b in self._books]
  def bookIDs(self):
    return [b.ID() for b in self._books]
  def allBooks(self):
    return self._books
  def allChapters(self):
    ret=[]
    for b in self._books:
      ret=ret+b.allChapters()
    return ret
  def allVerses(self):
    ret=[]
    for b in self._books:
      ret=ret+b.allVerses()
    return ret
    
class Book():
  def __init__(self,volume,obj,book_number):
    self._volume=volume
    self._object=obj
    self._book_number=book_number
    self._chapters=[]
    if 'sections' in self._object:
      self._object['chapters']=self._object['sections']
    for c in self._object['chapters']:
      self._chapters.append(Chapter(self,c))
  def _repr_html_(self):
    return self.title()
  def object(self):
    return self._object
  def title(self):
    return self._object.get('full_title',self._object.get('title'))
  def bookNumber(self):
    return self._book_number
  def ID(self):
    return self._object['lds_slug']
  def volume(self):
    return self._volume
  def numChapters(self):
    return len(self._chapters)
  def chapter(self,num):
    return self._chapters[num-1]
  def allChapters(self):
    return self._chapters
  def allVerses(self):
    ret=[]
    for c in self._chapters:
      ret=ret+c.allVerses()
    return ret
    
class Chapter():
  def __init__(self,book,obj):
    self._book=book
    self._object=obj
    self._verses=[]
    for v in self._object['verses']:
      self._verses.append(Verse(self,v))
  def _repr_html_(self):
    return self.reference()
  def object(self):
    return self._object
  def chapterNumber(self):
    return self._object['chapter']
  def reference():
    self._object['reference']
  def book(self):
    return self._book
  def volume(self):
    return self._book.volume()
  def numVerses(self):
    return len(self._verses)
  def verse(self,num):
    return self._verses[num-1]
  def allVerses(self):
    return self._verses
    
class Verse():
  def __init__(self,chapter,obj):
    self._chapter=chapter
    self._object=obj
  def _repr_html_(self):
    return self.reference()+'  '+self.text()
  def object(self):
    return self._object
  def verseNumber(self):
    return self._object['verse']
  def reference(self):
    return self._object['reference']
  def text(self):
    return self._object['text']
  def chapter(self):
    return self._chapter
  def book(self):
    return self._chapter.book()
  def volume(self):
    return self._chapter.volume()
