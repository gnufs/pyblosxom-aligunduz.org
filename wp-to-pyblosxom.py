#!/usr/bin/python
"""
This is my wp-to-pyblosxom script which allows you to migrate from
Wordpress to PyBlosxom using a Wordpress export.

It makes a lot of assumptions.  If you use it, go through the code and
do some practice runs.

.. Note::

   One thing to note is that the Wordpress export dumps comment spam,
   too.  I spent a while going through all the comments removing the
   spam ones.  It's possible that there's data in the export that
   specifies what is and isn't spam, but I didn't spend enough time to
   find it.

---

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright 2009 Will Guaraldi

Revisions:
1.0 - 6/12/2009 - initial writing, used it on my blog
"""

import cgi
from xml.sax.saxutils import escape
import os
import time
import sys
import xml.dom.minidom
import textwrap

entries_path = os.path.join(os.curdir, "entries")
if not os.path.exists(entries_path):
    os.mkdir(entries_path)

comments_path = os.path.join(os.curdir, "comments")
if not os.path.exists(comments_path):
    os.mkdir(comments_path)

def get_s(elem, tag):
    s = elem.getElementsByTagName(tag)
    if not s:
        return ""
    s = s[0]
    if not s.childNodes:
        return ""
    s = "".join([s.nodeValue for s in s.childNodes])
    return s.encode("utf-8")

def xmlfield(name, value):
    value = str(value)
    return "<%(name)s>%(value)s</%(name)s>" % {"name": name,
                                               "value": cgi.escape(value)}

def generate_filename(title):
    title = "".join([(t.isalpha() or t.isdigit()) and t or "_" for t in title])
    return (title + ".txt").lower()

def format_body(body):
    body = body.replace("\r", "")
    # body = body.replace("\n\n", "\n</p>\n<p>\n")
    body = body.splitlines()
    inpre = False
    for i, line in enumerate(body):
        if line.startswith("<pre>"):
            inpre = True
            continue
        if line.startswith("</pre>"):
            inpre = False
        if not line.strip() and not inpre:
            body[i] = "</p>\n<p>"
        
    body = "<p>\n" + "\n".join(body) + "\n</p>"

    for mem in ["<ol>", "<ul>", "<pre>"]:
        body = body.replace("<p>\n" + mem, mem)

    for mem in ["</ol>", "</ul>", "</pre>"]:
        body = body.replace(mem + "\n</p>", mem)

    return body

def convert(filename):
    # FIXME - add code to remove <excerpt:encode>...</excerpt:encoded>
    # lines.

    # parse the file
    doc = xml.dom.minidom.parse(filename)

    # pull out the rss node from the document
    rss = doc.getElementsByTagName("rss")[0]

    # the rss has one channel--get that
    channel = rss.getElementsByTagName("channel")[0]

    for item in channel.getElementsByTagName("item"):
        status = get_s(item, "wp:status")
        if status == "draft":
            # FIXME - what to do with drafts?
            continue

        if status != "publish":
            continue

        title = get_s(item, "title")
        link = get_s(item, "link")
        body = get_s(item, "content:encoded")
        postdate = get_s(item, "wp:post_date")

        print "working on '%s'" % title
        
        # you can pull out the categories this way, but all my categories
        # sucked, so i just made it "miro"
        ## categories = item.getElementsByTagName("category")
        ## categories = set([cat.childNodes[0].nodeValue.encode("utf-8") for cat in categories])
        ## categories = [cat.lower() for cat in categories]

        ## if "uncategorized" in categories:
        ##     categories.remove("uncategorized")

        categories = ["miro"]

        fn = os.path.join(entries_path, generate_filename(title))
        f = open(fn, "w")
        output = []
        output.append(title)
        if categories:
            output.append("#tags %s" % "::".join(categories))
        output.append(format_body(body))
        f.write("\n".join(output))
        f.close()

        mtime = time.strptime(postdate, "%Y-%m-%d %H:%M:%S")
        mtime = time.mktime(mtime)

        print "   wrote entry to %s" % fn
        try:
            os.utime(fn, (mtime, mtime))
        except Exception, e:
            print "   failed to fix the mtime %s", e

        comments = item.getElementsByTagName("wp:comment")
        print "   this entry has %s comments" % len(comments)
        for c in comments:
            author = get_s(c, "wp:comment_author")
            link = get_s(c, "wp:comment_author_url")
            pubDate = get_s(c, "wp:comment_date")
            pubDate = time.strptime(pubDate, "%Y-%m-%d %H:%M:%S")
            pubDate = time.mktime(pubDate)
            description = get_s(c, "wp:comment_content")

            cmt = []
            cmt.append('<?xml version="1.0" encoding="utf-8"?>')
            cmt.append('<item>')
            cmt.append(xmlfield("title", title))
            cmt.append(xmlfield("author", author))
            cmt.append(xmlfield("link", link))
            cmt.append(xmlfield("source", ""))
            cmt.append(xmlfield("pubDate", pubDate))
            cmt.append(xmlfield("description", description))
            cmt.append("</item>")
            cmt = "\n".join(cmt)

            cmtfn = generate_filename(title)
            cmtfn = "%s-%s.cmt-" % (os.path.splitext(cmtfn)[0], pubDate)
            cmtfn = os.path.join(comments_path, cmtfn)
            print cmtfn

            f = open(cmtfn, "w")
            f.write(cmt)
            f.close()

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1:
        for mem in argv[1:]:
            convert(mem)
