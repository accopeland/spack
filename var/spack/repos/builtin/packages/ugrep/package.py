from spack.package import *


class Ugrep(AutotoolsPackage):
    """ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps and more: search file systems, source code, text, binary files, archives (cpio/tar/pax/zip), compressed files (gz/Z/bz2/lzma/xz/lz4/zstd), documents etc. A faster, user-friendly and compatible grep replacement."""

    homepage = "https://github.com/Genivia/ugrep/wiki"
    url = "https://github.com/Genivia/ugrep/archive/refs/tags/v3.10.0.tar.gz"

    version("3.10.0", sha256="9bde11c055b922b6c3cecf9e8eb0cb02db9832c46deaa76424df4c4b8a57a718")
