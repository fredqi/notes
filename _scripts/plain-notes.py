#!/usr/bin/env python
### plain-notes.py ---
##
## Filename: plain-notes.py
## Author: Fred Qi
## Created: 2014-07-03 18:01:48(+0400)
##
## Last-Updated: 2014-07-05 22:48:59(+0400) [by Fred Qi]
##     Update #: 781
######################################################################
##
### Commentary:
##
##  This python script is designed to clip contents fromt the Internet and
##  covert the main body into plain text with light formating (reStructuredText,
##  Markdown, etc.).
##
######################################################################
##
### Change Log:
##
##
######################################################################

import re
import os
import os.path
import urllib2

import pypandoc
from readability.readability import Document

from StringIO import StringIO
from PIL import Image
from PIL.ImageFileIO import ImageFileIO

import argparse

from pocket import pocket


def download_images(urls, folder):
    """Download images from given URLs."""

    if os.path.exists(folder) and not os.path.isdir(folder):
        return None
    if not os.path.exists(folder) and len(urls) > 0:
        os.mkdir(folder)

    images = list()
    headers={'User-Agent': 'Mozilla Firefox for Ubuntu canonical - 1.0'}
    for fn, url in urls:
        print 'Downloading', fn, url
        req = urllib2.Request(url, headers=headers)
        con = urllib2.urlopen(req)
        data = con.read()
        img = Image.open(ImageFileIO(StringIO(data)))
        imgext = '%s' % img.format
        imgfn, _ = os.path.splitext(fn)
        imgfn = fn + '.' + imgext.lower()
        imgfn = os.path.join(folder, imgfn)
        images.append((imgfn, url))
        img.save(imgfn)

    return images


def patch_image_alt(html):
    """Search all the image urls in the given html content."""
    img_tmpl = u'<img src="%s" alt="%s-%02d" />'
    re_url = re.compile('<img[^>]+/?>', re.I)
    re_src = re.compile('src="([^"]+)"', re.I)
    re_alt = re.compile('alt="([^"]+)"', re.I)

    urls = re_url.findall(html)
    for idx, url in enumerate(urls):
        img_url = re_src.search(url)
        alt_txt = re_alt.search(url)
        if img_url and alt_txt:
            img_url = img_url.group(1)
            alt_txt = alt_txt.group(1).replace(' ', '-')
            print alt_txt, img_url
            url_new = img_tmpl % (img_url.encode('utf-8'),
                                  alt_txt.encode('utf-8'),
                                  idx + 1)
            html = html.replace(url, url_new)

    return html


def download_html_as_text(url, filename=None, format_to='rst'):
    """Download HTML content from url and convert it to plain text."""
    # Construct internet connection
    headers = {'User-Agent' : 'Mozilla Firefox for Ubuntu canonical - 1.0'}
    req = urllib2.Request(url, headers=headers)
    con = urllib2.urlopen(req)
    html = con.read()

    # Fetch and convert main contents
    article = Document(html).summary()
    if len(article) < 1024:
        article = html

    article = patch_image_alt(article)
    title = Document(html).short_title()
    text = pypandoc.convert(article, format_to, format='html')

    title_utf8 = title.encode('utf-8')
    lines_insert = [u'\n\n',
                    u'='*len(title_utf8), u'\n',
                    title_utf8, u'\n',
                    u'='*len(title_utf8), u'\n\n', 
                    u':URL: ' + url,  u'\n\n']
    title = title.split('|,-')[0]

    # Search for urls of images
    imgurl_pattern = '\.\.\s+\|([^|]+)\|\s+image::\s+(https?://\S+)'
    imgurl_re = re.compile(imgurl_pattern, re.I)
    image_urls = imgurl_re.findall(text)

    if filename is None:
        filename = title.split('-')[0].strip().replace(' ', '-')

    txtfile = open(filename + '-bak.' + format_to, 'w')
    txtfile.writelines(lines_insert)
    txtfile.write(text.encode('utf-8'))
    txtfile.close()

    # Replace online image URLs with local paths.
    images = download_images(image_urls, filename + '-images')
    for img, link in images:
        text = text.replace(link, img)

    txtfile = open(filename + '.' + format_to, 'w')
    txtfile.writelines(lines_insert)
    txtfile.write(text.encode('utf-8'))
    txtfile.close()


def download_pocket_favorite():
    pi = pocket()
    pi.load_token()
    list_favorite = pi.retrieve_favorite()
    
    for key, val in list_favorite['list'].iteritems():
        title, url = pi.extract_title_url(val)
        if url.find('blogspot') > 0:
            print 'Not supported [blogspot]:', url
            continue
        print title, '\n  Downloading from', url
        download_html_as_text(url)
        pi.modify_items([key], 'unfavorite')
        pi.modify_items([key], 'archive')


if '__main__' == __name__:

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--output-style',
                        nargs=1, default='rst',
                        help='Style of the output plain text.')
    subparsers = parser.add_subparsers(title='List of subcommands')
    parser_url = subparsers.add_parser('url')
    parser_url.add_argument('urls',
                            metavar='URLS', nargs='+',
                            help='List of URLs to be processed.')
    parser_url.add_argument('-f', '--filename',
                            metavar='FILE', nargs=1,
                            help='List of URLs to be processed.')
    parser_pocket = subparsers.add_parser('pocket')

    args = parser.parse_args()

    if hasattr(args, 'urls'):
        print args
        if args.filename and 1 == len(args.urls):
            print 'Downloading contents from:'
            print '   ', args.urls[0]
            download_html_as_text(args.urls[0], args.filename[0])
        else:
            for url in args.urls:
                print 'Downloading contents from:'
                print '   ', url
                download_html_as_text(url)
    else:
        # Get URLs from pocket favorite list
        download_pocket_favorite()
        

######################################################################
### plain-notes.py ends here
