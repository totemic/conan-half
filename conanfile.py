#!/usr/bin/env python

from conans import ConanFile, tools


class HalfConan(ConanFile):
    name = "half"
    version = "2.1.0"
    license = "MIT"

    description = "Library to provide an IEEE-754 conformant half-precision floating point type."
    url = "https://sourceforge.net/projects/half/"

    def source(self):
        zip_url = f"{self.url}/files/half/{self.version}/half-{self.version}.zip/download"
        tools.get(zip_url)

    def package(self):
        self.copy("LICENSE.txt")
        self.copy("*.hpp", keep_path=True)
