"""
Audio Player Controller (Method Overriding) - POLYMORPHISM

Parent class Media mein ek method hai play(). Child class Mp3Player
mein bhi ek method hai play() jo specific MP3 music chalata hai. Agar
hum child class ka object bana kar .play() call karein, toh parent ka
code chalega ya child ka, aur is concept ko kya kehte hain?
"""

class Media:
    def play(self):
        print("Playing generic media...")


class Mp3Player(Media):
    def play(self):   # SAME method name as the parent -- this OVERRIDES it
        print("Playing MP3 music track...")


player = Mp3Player()
player.play()

"""
ANSWER: The CHILD class's version of play() will run, NOT the
parent's. This concept is called METHOD OVERRIDING.

EXPLANATION:
- When a child class defines a method with the EXACT SAME NAME as one
  already existing in its parent class, the child's version
  "overrides" (replaces) the parent's version specifically for objects
  of that child class.
- Python always looks for a method starting from the object's OWN
  class first. Since Mp3Player defines its own play(), Python finds
  and runs THAT version for player.play() -- it never even needs to
  look at Media's play() in this case, because the child's own method
  takes priority.
- This is a form of POLYMORPHISM: the same method NAME (play()) behaves
  DIFFERENTLY depending on which class's object is calling it -- a
  Media object would print "Playing generic media...", while an
  Mp3Player object prints "Playing MP3 music track...", even though
  both are triggered by the same, identically-named method call.
"""
