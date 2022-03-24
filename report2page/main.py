from dominate import document, tags
import re

from .configparse import ConfigParse
from .filespider import FileSpider

strip_type = lambda s: re.sub(".html$", "", s)


def main(path):
    cp = ConfigParse(path)
    paths = cp.paths

    doc = document(title="Generated pages")

    with doc.head:
        tags.link(rel='stylesheet', href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css")
        tags.link(rel='stylesheet', href="bootstrap-toc.css")
        tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/v4-shims.min.css')
        tags.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css')

    with doc:
        with tags.div(cls="container template-reference-index"):
            with tags.div(cls="row"):
                with tags.table(cls="ref-index"):
                    for folder in paths:
                        with tags.tbody():
                            with tags.tr():
                                tags.th(tags.h2(folder))

                        fs = FileSpider(folder)

                        for page in fs.html_pages:
                            with tags.tbody():
                                with tags.tr():
                                    tags.td(tags.p(tags.code(tags.a(
                                        strip_type(page),
                                        href=f"{folder}/{page}"))))

    with open("index.html", "w") as f:
        f.write(str(doc))

    return doc
