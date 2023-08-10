from pypdf import PdfReader


class CompileText:

    def __init__(self):
        self.reader = None
        self.no_pages = None
        self.doc = ""

    def get_text(self, file):
        """
        :type file: pdf
        Extract text from a pdf file and compile it within self.doc.
        """
        self.reader = PdfReader(file)
        self.no_pages = len(self.reader.pages)
        for i in range(self.no_pages):
            page = self.reader.pages[i]
            text = page.extract_text()
            self.doc += text
        return self.doc
