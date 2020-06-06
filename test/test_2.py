import abc
import sys

class HtmlWriter:
    def __init__(self, file=sys.stdout):
        self.file = file

    def out_header(self):
        self.file.write("<!doctype html>\n<html>\n")

    def out_title(self, title):
        self.file.write("<head><title>{}</title></head>\n".format(title))

    def out_start_body(self):
        self.file.write("<body>\n")

    def out_body(self, texts):
        for text in texts:
            self.file.write("<p>{}</p>\n".format(text))

    def out_end_body(self):
        self.file.write("</body>\n")

# Target
class Reporter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def header(cls, title):
        pass

    @abc.abstractmethod
    def main(self, contents):
        pass


    @abc.abstractmethod
    def footer(self):
        pass


class Car():
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

