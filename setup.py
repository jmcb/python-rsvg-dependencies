#!/usr/bin/env python

from distutils.core import setup

def main ():
    return setup(name="rsvg_fixup", description="Provide path fix-up for pyrsvg.",
        long_description="""Unfortunately, the python-rsvg module provided by
        the GNOME Desktop Python project, while correctly installing the
        required files, does not put them in a location referred to in
        PYTHONPATH. Thus, it is necessary to include a secondary .pth file
        pointing to this subdirectory, in order to ensure that the rsvg module
        is importable.""", author="Jon McManus", author_email="jonathan@acss.net.au",
        url="http://github.com/jmcb/python-rsvg-dependencies/tree/pyrsvg-fixup",
        platforms="Microsoft Windows", download_url="http://www.wxwhatever.com/jmcb/rsvg",
        data_files=[(".", "rsvg.pth")])

if __name__=="__main__":
    main()
