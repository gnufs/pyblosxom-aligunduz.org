# -*- coding: utf-8 -*-
# =============================================================
# This is the config file for PyBlosxom.  You should go through 
# the file and fill in values for the various properties.  This 
# affects the behavior of your blog.
#
# The PyBlosxom documentation has additional information on 
# configuration variables.
# =============================================================

# Don't touch this next line.
py = {}


# Codebase configuration
# ======================

# If you did not install PyBlosxom as a library (i.e. python setup.py install)
# then uncomment this next line and point it to your PyBlosxom installation
# directory.
# Note, this should be the directory that holds the "Pyblosxom" 
# directory (note the case--uppercase P lowercase b!).
#py["codebase"] = "/usr/lib/python2.6/site-packages"

import os

blogdir = "/srv/http/blog/"

# Blog configuration
# ==================

# What is the title of this blog?
py["blog_title"] = "GLOG"

# What is the description of this blog?
py["blog_description"] = "Free People, Free Society"

# Who are the author(s) of this blog?
py["blog_author"] = "Ali Gündüz"

# What is the email address through which readers of the blog may contact
# the authors?
py["blog_email"] = "email@example.com"

# These are the rights you give to others in regards to the content
# on your blog.  Generally, this is the copyright information.
# This is used in the Atom feeds.  Leaving this blank or not filling
# it in correctly could result in a feed that doesn't validate.
py["blog_rights"] = "Copyright 2008, 2009, 2010 Ali Gündüz"

# What is this blog's primary language (for outgoing RSS feed)?
py["blog_language"] = "en"

# Encoding for output.  This defaults to utf-8.
py["blog_encoding"] = "utf-8"

# What is the locale for this blog?  This is used when formatting dates
# and other locale-sensitive things.  Make sure the locale is valid for
# your system.  See the PyBlosxom documentation for details.
#py["locale"] = "en_US.iso-8859-1"

# Where are this blog's entries kept?
py["datadir"] = os.path.join(blogdir, "entries")

# Where are this blog's flavours kept?
py["flavourdir"] = os.path.join(blogdir, "flavours")

# List of strings with directories that should be ignored (e.g. "CVS")
# ex: py['ignore_directories'] = ["CVS", "temp"]
py["ignore_directories"] = []

# Should I stick only to the datadir for items or travel down the directory
# hierarchy looking for items?  If so, to what depth?
# 0 = infinite depth (aka grab everything)
# 1 = datadir only
# n = n levels down
py["depth"] = 0

# How many entries should I show on the home page and category pages?
# If you put 0 here, then I will show all pages.
# Note: this doesn't affect date-based archive pages.
py["num_entries"] = 10

# What is the default flavour you want to use when the user doesn't
# specify a flavour in the request?
py["default_flavour"] = "html"



# Logging configuration
# =====================

# Where should PyBlosxom write logged messages to?
# If set to "NONE" log messages are silently ignored.
# Falls back to sys.stderr if the file can't be opened for writing.
#py["log_file"] = os.path.join(blogdir, "logs", "pyblosxom.log")

# At what level should we log to log_file?
# One of: "critical", "error", "warning", "info", "debug"
# For production, "warning" or "error' is recommended.
#py["log_level"] = "warning"

# This lets you specify which channels should be logged.
# If specified, only messages from the listed channels are logged.
# Each plugin logs to it's own channel, therefor channelname == pluginname.
# Application level messages are logged to a channel named "root".
# If you use log_filter and ommit the "root" channel here, app level messages 
# are not logged! log_filter is mainly interesting to debug a specific plugin.
#py["log_filter"] = ["root", "plugin1", "plugin2"]



# Plugin configuration
# ====================

# Plugin directories:
# You can now specify where you plugins all lives, there are two types
# of plugindirectories, the standard pyblosxom plugins, and the xmlrpc
# plugins.  You can list out as many directories you want, but they
# should only contain the related plugins.
# Example: py['plugin_dirs'] = [ "/home/joe/blog/plugins",
#                                "/var/lib/pyblosxom/plugins" ]
py["plugin_dirs"] = [os.path.join(blogdir, "plugins")]

# There are two ways for PyBlosxom to load plugins.  The first is the
# default way which involves loading all the plugins in the lib/plugins
# directory in alphanumeric order.  The second is by specifying a
# "load_plugins" key here.  Doing so will cause us to load only the
# plugins you name and we will load them in the order you name them.
# The "load_plugins" key is a list of strings where each string is
# the name of a plugin module (i.e. the filename without the .py at
# the end).
# If you specify an empty list, then this will load no plugins.
# ex: py["load_plugins"] = ["pycalendar", "pyfortune", "pyarchives"]
py["load_plugins"] = ["wbgpager","entrytitle"]

py["wbgpager_count_from"] = 1
py["wbgpager_linkstyle"] = 1

# ======================
# Optional Configuration
# ======================

# What should this blog use as its base url?
#py["base_url"] = "http://www.example.com/weblog"

# Default parser/preformatter. Defaults to plain (does nothing)
#py["parser"] = "plain"



# Caching configuration
# =====================

# Using Caching? Caching speeds up rendering the page that is going to be
# shown. Even if you are not using pyblosxom special features, caching can
# improve rendering speed of certain flavours that can show a large number of
# files at one time. Choose a cache mechanism you'd like, see the
# Pyblosxom/cache/ directory, and read the source on how to enable caching with
# the particular cache driver, you need to set two variables:
#py["cacheDriver"] = "xxxx"
#py["cacheConfig"] = ""



# Static rendering
# ================

# Doing static rendering?  Static rendering essentially "compiles" your
# blog into a series of static html pages.  For more details, see the
# documentation.
# 
# What directory do you want your static html pages to go into?
#py["static_dir"] = "/path/to/static/dir"

# What flavours should get generated?
#py["static_flavours"] = ["html"]

# What other paths should we statically render?
# This is for additional urls handled by other plugins like the booklist
# and plugin_info plugins.  If there are multiple flavours you want
# to capture, specify each:
# ex: py["static_urls"] = ["/booklist.rss", "/booklist.html"]
#py["static_urls"] = ["/path/to/url1", "/path/to/url2"]

# Whether (1) or not (0) you want to create date indexes using month
# names?  (ex. /2004/Apr/01)  Defaults to 1 (yes).
#py["static_monthnames"] = 1

# Whether (1) or not (0) you want to create date indexes using month
# numbers?  (ex. /2004/04/01)  Defaults to 0 (no).
#py["static_monthnumbers"] = 0
