from spack.package import *


class PyYamllint(Package):
    """A linter for YAML files.

yamllint does not only check for syntax validity, but for weirdnesses like key repetition and cosmetic problems such as lines length, trailing spaces, indentation, etc."""

    homepage = "https://yamllint.readthedocs.io/"
    url = "https://pypi.org/project/yamllint/"

    # version("1.2.3", "0123456789abcdef0123456789abcdef")

    def install(self, spec, prefix):
        make()
        make("install")
