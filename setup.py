#!/usr/bin/env python
from distutils.core import setup

def main ():
    dlls = ["bin/%s" % dll for dll in ["freetype6.dll", "libcairo-2.dll",
        "libfontconfig-1.dll", "libpng14-14.dll", "zlib1.dll", "iconv.dll",
        "intl.dll", "libcroco-0.6-3.dll", "libgdk_pixbuf-2.0-0.dll",
        "libgio-2.0-0.dll", "libglib-2.0-0.dll", "libgmodule-2.0-0.dll",
        "libgobject-2.0-0.dll", "libgthread-2.0-0.dll", "libpango-1.0-0.dll",
        "libpangocairo-1.0-0.dll", "libpangoft2-1.0-0.dll",
        "libpangowin32-1.0-0.dll", "librsvg-2-2.dll", "libxml2-2.dll"]]

    licenses = ["doc/%s" % license for license in ["LICENSE-LGPL.TXT",
        "LICENSE-CAIRO.TXT","LICENSE-FONTCONFIG.TXT", "LICENSE-LIBPNG.TXT",
        "LICENSE-ZLIB.TXT", "LICENSE-LXML2.TXT", "LICENSE-GPL.TXT",
        "LICENSE-LGPLV2.1.TXT"]]

    others = ["README.rst", "LICENSE.rst"]

    long_description = """    This package contains dynamic link dependencies required to run the
    python-rsvg library (as provided by the gnome-python-desktop
    package) on Windows. GNOME provides pre-build binaries for this
    package for Windows Systems (see
    <http://ftp.acc.umu.se/pub/GNOME/binaries/win32/gnome-python-desktop>)
    but this package does not resolve all of the dependencies required
    to actuall run it -- nor does it provide the librsvg dynamic link
    library.

    Please see README.rst for more details."""

    classifiers = ["Development Status :: 6 - Mature",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: GNU Library or Lesser General Public License (LGPL)",
        "License :: MIT License", "License :: zlib/libpng License",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries"]

    return setup(name="rsvg-dependencies", version="0.1",
        maintainer="Jonathan McManus", maintainer_email="jonathan@acss.net.au", author="various",
        url="http://www.github.com/jmcb/python-rsvg-dependencies",
        download_url="http://www.wxwhatever.com/jmcb/rsvg", platforms="Microsoft Windows",
        description="Dynamic link library dependencies for pyrsvg.",
        license="GNU LGPLv2, MIT, MPL, FTL, FontConfig, libpng, zlib, others.",
        data_files=[(".", dlls + licenses + others)],
        long_description=long_description, classifiers=classifiers)

if __name__=="__main__":
    main ()
