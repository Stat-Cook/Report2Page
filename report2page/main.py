from .configparse import ConfigParse
from .filespider import FileSpider
from dominate import document, tags

def main(path):

    cp = ConfigParse(path)
    paths = cp.paths

    doc = document(title="Generated pages")
    with doc:
        for folder in paths:
            tags.h1(folder)
            fs = FileSpider(folder)

            for page in fs.html_pages:
                tags.p(tags.code(tags.a(page, href=f"{folder}/{page}")))

    with open("index.html", "w") as f:
        f.write(str(doc))

    return doc
