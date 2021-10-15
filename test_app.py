#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:56:48 2021

@author: jonahbrown-joel
"""


import markdown

markdown_text = '''# This is a test
me is a python
```python
import os, sys
```
'''

mkd_string = (markdown.markdown(markdown_text,
                        extensions=['fenced_code', 'codehilite']))


import markdown2

py_string = """
           ```python
            if True:
                print "hi"
            ```
            """

# https://github.com/richleland/pygments-css
mkd_string =  
markdown2.markdown(py_string)
markdown.markdown(py_string)
markdown.markdown(py_string, extensions=['codehilite'])  # Adds a class "codehilite" to your code, but this will do nothing 
markdown.markdown(py_string, extensions=['fenced_code'])
markdown.markdown(py_string, extensions=['fenced_code', 'codehilite'])
markdown.markdown(py_string)
markdown2.markdown("> This is a paragraph and I am **bold**")
Out[2]: u'<blockquote>\n  <p>This is a paragraph and I am <strong>bold</strong></p>\n</blockquote>\n'

In [3]: code = """```python
if True:
    print "hi"
```"""
   ...: 

In [4]: markdown2.markdown(code, extras=['fenced-code-blocks'])
Out[4]: u'<div class="codehilite"><pre><code><span class="k">if</span> <span class="bp">True</span><span class="p">:</span>\n    <span class="k">print</span> <span class="s">&quot;hi&quot;</span>\n</code></pre></div>\n'

file_path = '/Users/jonahbrown-joel/Library/Mobile Documents/com~apple~CloudDocs/Data_Science_Blog/Blog_Content/G - Useful Snippets/Useful Snippets.md'
file = open(file_path, 'r')
file_contents = file.read()
mkd_string = markdown.markdown(file_contents, extensions=['fenced_code', 'codehilite'] )
###############
# how to use a div class with css
#mkd_string = markdown.markdown(py_string, extensions=['fenced_code', 'codehilite'])

# change 'highlight' to 'codehilite' in the css

app = Flask(__name__
          , template_folder = path_templates)
Markdown(app)  # construct a 'Markdown' so that you can use markdown


@app.route("/cheese")
def home():
    return "Hello, World!"


@app.route('/test')  # This is the home page
def test_page():
    return render_template('zz_Test_page.html'
                         , mkd_text = mkd_string)

if __name__ == "__main__":
    # app.run(debug=True)  # change to this when you deploy
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))