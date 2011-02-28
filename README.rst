************************
python-rsvg-dependencies
************************

This package contains all of the files required to run the `python-rsvg`_ module
compiled for Windows as provided by the GNOME Desktop Project's Windows binary
archive.

Binaries
========

This package provides the following binaries, which are required to run
``python-rsvg``, or are required to run one of the dependencies of
``python-rsvg``:

 - freetype6.dll
 - libcairo-2.dll
 - libfontconfig-1.dll
 - libpng14-14.dll
 - zlib1.dll
 - iconv.dll
 - intl.dll
 - libcroco-0.6-3.dll
 - libgdk_pixbuf-2.0-0.dll
 - libgio-2.0-0.dll
 - libglib-2.0-0.dll
 - libgmodule-2.0-0.dll
 - libgobject-2.0-0.dll
 - libgthread-2.0-0.dll
 - libpango-1.0-0.dll
 - libpangocairo-1.0-0.dll
 - libpangoft2-1.0-0.dll
 - libpangowin32-1.0-0.dll
 - librsvg-2-2.dll
 - libxml2-2.dll

License
=======

Individual binaries are licensed under the terms of the `GNU Lesser General
Public License`_, version 2, except where otherwise indicated:

 - Freetype is dual licensed under the terms of the `FreeType license`_ and the
   terms of the `GNU General Public License`_, version 2.
 - cairo, which is dual licensed under the terms of the `GNU Lesser General
   Public License`_, version 2, and the `Mozilla Public License`_.
 - fontconfig, which is licensed under the terms of the `fontconfig license`_.
 - libpng, which is licensed under the terms of the `libpng license`_.
 - zlib, which is licensed under the terms of the `zlib license`_.
 - libxml2, which is licensded under the terms of the `MIT license`_.
 - libiconv, which is licensed under the terms of the `GNU Lesser General Public
   License`_. (*Note*: iconv the program is under the terms of the GNU GPL,
   while the library is under the terms of the GNU LGPL).
 - gettext-runtime, which is licensed under the terms of the `GNU Lesser General
   Public License`_, version 2.0 and version 2.1 (see `GNU Lesser General Public
   License v2.1`_).
 - libcroco, which is licensed under the terms of the `GNU Lesser General Public
   License`_.
 - libgdk_pixbuf, which is licensed under the terms of the `GNU Lesser General
   Public License`_.
 - libglib, which is licensed under the terms of the `GNU Lesser General Public
   License`_.
 - libpango, which is licensed under the terms of the `GNU Lesser General Public
   License`_.
 - librsvg, which is licensed under the terms of the `GNU Lesser General Public
   License`_.

This individual package, its documentation, and the code required to build the
package, is licensed under the terms of the MIT License. See `LICENSE.RST`_.

Licensing notes
===============

Where possible I have attempted to remove any ambiguity with regards to the
version of the GNU (Lesser) General Public License used. Here are a few notes:

 - freetype's website contains the full text of the GNU GPLv2. I have not found
   any text to state that it is licensed under this and any later version.
 - cairo was relicensed under the GNU LGPL in 2004, predating version 3. I have
   yet to find any indication that it is "GNU LGPLv2 *or later*".
 - gettext-runtime (intl.dll) as provided by the GnuWin32 project contains the
   following statement: "The gettext-runtime package is under the LGPL, see
   files intl/COPYING.LIB-2.0 and intl/COPYING.LIB-2.1.".

All other source packages contained the exact text of the GNU LGPLv2, including:

 - libiconv
 - libcroco
 - libgdk_pixbuf
 - libpango
 - librsvg
 - libglib

This implies that these are licensed at the very least under the terms of the
GNU LGPLv2, if not later; however, as I have yet to find note that they are
explicitly licensed under version 2 *or later*, it would be safer to assume
unless otherwise informed that they are not.

Sources
=======

Binaries
--------

Binary packages were located at the following sources:

 - `GTK+ "development" bundle`_:
     - freetype6.dll
     - libcairo-2.dll
     - libfontconfig-1.dll 
     - libpng14-14.dll
     - zlib1.dll
     - intl.dll
     - libgdk_pixbuf-2.0-0.dll
     - libgio-2.0-0.dll
     - libglib-2.0-0.dll
     - libgmodule-2.0-0.dll
     - libgobject-2.0-0.dll
     - libgthread-2.0-0.dll
     - libpango-1.0-0.dll
     - libpangocairo-1.0-0.dll
     - libpangoft2-1.0-0.dll
     - libpangowin32-1.0-0.dll
 - `libcroco-0.6-3.dll`_
 - `librsvg-2-2.dll`_
 - `libxml2-2.dll (1)`_, `libxml2-2.dll (2)`_
 - `iconv.dll`_
 - `python-rsvg`_

Individual binaries from the GTK+ bundle can be found on the `GNOME Desktop
Project's Windows binaries page`_.

Sources
-------

Source packages for each of these can be found at the following locations:

 - `freetype6`_
 - `libcairo-2`_
 - `libfontconfig-1 `_
 - `libpng14-14`_
 - `zlib1`_
 - `intl`_
 - `libgdk_pixbuf-2.0-0`_
 - `libgio-2.0-0`_
 - `libglib-2.0-0`_
 - `libgmodule-2.0-0`_
 - `libgobject-2.0-0`_
 - `libgthread-2.0-0`_
 - `libpango-1.0-0`_
 - `libpangocairo-1.0-0`_
 - `libpangoft2-1.0-0`_
 - `libpangowin32-1.0-0`_
 - `libcroco-0.6-3`_
 - `librsvg-2-2`_
 - `libxml2-2`_
 - `iconv`_
 - `python-rsvg (source)`_

.. Links
.. =====
.. 
.. Licenses
.. --------
.. 
.. _`FreeType license`: LICENSE-FTL.TXT
.. _`GNU General Public License`: LICENSE-GPL.TXT
.. _`GNU Lesser General Public License`: LICENSE-LGPL.TXT
.. _`GNU Lesser General Public License v2.1`: LICENSE-LGPLV2.1.TXT
.. _`Mozilla Public License`: LICENSE-CAIRO.TXT
.. _`fontconfig`: LICENSE-FONTCONFIG.TXT
.. _`libpng license`: LICENSE-LIBPNG.TXT
.. _`zlib license`: LICENSE-ZLIB.TXT
.. _`MIT License`: LICENSE-LXML2.TXT
.. _`LICENSE.rst`: LICENSE.rst
.. 
.. Binaries
.. --------
.. 
.. _`GTK+ "development" bundle`: http://www.gtk.org/download-windows.html
.. _`libcroco-0.6-3.dll`: http://ftp.gnome.org/pub/GNOME/binaries/win32/libcroco/0.6/
.. _`librsvg-2-2.dll`: http://ftp.gnome.org/pub/GNOME/binaries/win32/librsvg/2.32/
.. _`libxml2-2.dll (1)`: http://gnuwin32.sourceforge.net/packages/libxml2.htm
.. _`libxml2-2.dll (2)`: http://www.zlatkovic.com/libxml.en.html
.. _`iconv.dll`: http://gnuwin32.sourceforge.net/packages/libiconv.htm
.. _`GNOME Desktop Project's Windows binaries page`: http://ftp.gnome.org/pub/GNOME/binaries/win32/
.. _`python-rsvg`: http://ftp.gnome.org/pub/GNOME/binaries/win32/gnome-python-desktop/2.32/
.. 
.. Sources
.. -------
.. 
.. _`freetype6`: http://www.freetype.org/download.htm
.. _`libcairo-2`: http://cairographics.org/download/
.. _`libfontconfig-1`: http://www.freedesktop.org/software/fontconfig/release/
.. _`libpng14-14`: http://www.libpng.org/pub/png/libpng.html
.. _`zlib1`: http://zlib.net/
.. _`intl`: http://www.gnu.org/software/gettext/
.. _`libgdk_pixbuf-2.0-0`: http://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/
.. _`libgio-2.0-0`: http://ftp.gnome.org/pub/GNOME/sources/glib/
.. _`libglib-2.0-0`: http://ftp.gnome.org/pub/GNOME/sources/glib/
.. _`libgmodule-2.0-0`: http://ftp.gnome.org/pub/GNOME/sources/glib/
.. _`libgobject-2.0-0`: http://ftp.gnome.org/pub/GNOME/sources/glib/
.. _`libgthread-2.0-0`: http://ftp.gnome.org/pub/GNOME/sources/glib/
.. _`libpango-1.0-0`: http://ftp.gnome.org/pub/GNOME/sources/pango/
.. _`libpangocairo-1.0-0`: http://ftp.gnome.org/pub/GNOME/sources/pango/
.. _`libpangoft2-1.0-0`: http://ftp.gnome.org/pub/GNOME/sources/pango/
.. _`libpangowin32-1.0-0`: http://ftp.gnome.org/pub/GNOME/sources/pango/
.. _`libcroco-0.6-3`: http://ftp.gnome.org/pub/GNOME/sources/libcroco/
.. _`librsvg-2-2`: http://ftp.gnome.org/pub/GNOME/sources/librsvg/
.. _`libxml2-2`: http://ftp.acc.umu.se/pub/GNOME/sources/libxml2/
.. _`iconv`: http://www.gnu.org/software/libiconv/
