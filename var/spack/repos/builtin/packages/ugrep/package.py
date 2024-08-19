from spack.package import *


class Ugrep(AutotoolsPackage):
    """ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps and more: search file systems, source code, text, binary files, archives (cpio/tar/pa
x/zip), compressed files (gz/Z/bz2/lzma/xz/lz4/zstd), documents etc. A faster, user-friendly and compatible grep replacement."""

    homepage = "https://github.com/Genivia/ugrep/wiki"
    url = "https://github.com/Genivia/ugrep/archive/refs/tags/v3.10.0.tar.gz"

    version("3.12.6", sha256="96415667f88f32bf2cd478db8f488e29ff293576e66f2d39e223a3bae1a15eb4")
    version("3.12.5", sha256="5ff60ea5b5f2fe2068bbc0b0d9072fe55eb310e094588bdb2324d9123aa92114")
    version("3.12.4", sha256="a36d20492026a36b8436c91f65189c7ea98b4b599c4704f170159c1d9676dc3b")
    version("3.12.3", sha256="df234817047bb58e25bb7625b3c3f8514a4ab9346e2fb9e9209c4b7192b67bd8")
    version("3.12.2", sha256="37c207f5363fad2aea2d9793b9131fba5c2ba5d4360be575a6956c1aeba629c5")
    version("3.12.1", sha256="a442ac9c0961746374d0627e6ec52d5c6250541640aeb9a698eb40382d0ec44c")
    version("3.12.0", sha256="f69330b74a2d2e46c878c19da3453e97d92ae960d0e1a92a853481cb889fca3e")
    version("3.11.2", sha256="a314cc6fe149eef9bc0f0d69c6b331d9d4491a100677c1b3fbb2159806cca2dd")
    version("3.11.1", sha256="0a36d7bb62c49262b433eb301d8de6b90233a23446a71484738cd35650cc5c91")
    version("3.10.0", sha256="9bde11c055b922b6c3cecf9e8eb0cb02db9832c46deaa76424df4c4b8a57a718")
