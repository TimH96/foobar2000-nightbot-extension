"""
lib/scrape.py

methods for scraping window tiles, and exctracting and manipulating the output
"""

from pywinauto                      import Desktop
from pywinauto.controls.uiawrapper  import UIAWrapper

desk = Desktop(backend="uia")
win = desk.windows()
for i, w in enumerate(win):
    print(i, w.window_text())

i = int(input())
b : UIAWrapper = win[i]



def get_desktop(backend: str = 'uia') -> Desktop:
    """Builds and returns desktop object"""
    return Desktop(backend=backend)


while True:
    print(b.process_id())  # process id goes None when gone
    print(b.window_text())
    print(b.handle)