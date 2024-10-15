# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Duc(AutotoolsPackage):
    """
    Duc, a library and suite of tools for inspecting disk usage
    """

    homepage = "https://github.com/zevv/duc"
    url = "https://github.com/zevv/duc/archive/refs/tags/1.4.5.tar.gz"

    license("LGPL")

    version("1.4.5", sha256="4da84fc9ea3894f6445a72492ee7cfa287d89d4136bddf7cd2dbac5a3e974865")
    version("1.4.4", sha256="9df541922a8bc1dd9f12849f4cafcecc9ad84fcc0c89e353a23f3662d845eb75")
    version("1.4.3", sha256="2d4a14c8c3c20caf70d7ba9a3ebdbc9fe95db34ebb738f77e0d70538298f46d0")
    version("1.4.2", sha256="25540377b9920745cbc3a8d94ac4c670d38db7aa9b8d14a0d44de08e086f42df")
    version("1.4.1", sha256="2ecd1d75f31f2890d2d590bfe6362039d05e20dcf7eb507923379aac86e9c801")
    version("1.4.0", sha256="25012019ad1da63a9533c1751c5d09a979988f577d47945485a9b1b1855a62f9")
    version("1.3.3", sha256="332502972044ee7fdd85e952f128011e00e125d87fc218b9599e050c03258d26")
    version("1.3.2", sha256="6679e5a7d60229bc0806e865f6c75285b18e0471aa7c759da73d7ad8900aae8c")
    version("1.3", sha256="06afd1d092801f4f990176efeb762cb2f72a3f9af431b91434fa2666e639ced4")
    version("1.2", sha256="4ec5d235d146c298f1fb6a062bdd2e30bd8caa01da2e689af135ef5b8d3a409a")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("pkg-config", type="build")
    depends_on("m4", type="build")

    variant("leveldb", default=True, description="Use leveldb as db backend [True]")
    depends_on("leveldb", when="+leveldb")

    variant("sqlite", default=False, description="Use sqlite as db backend [False]")
    depends_on("sqlite@3:", when="+sqlite")

    variant("lmdb", default=False, description="Use lmdb as db backend [False]")
    depends_on("lmdb", when="+lmdb")

    variant("tokyocabinet", default=False, description="Use tokyocabinet as db backend [False]")
    depends_on("tokyocabinet")
    depends_on("tokyocabinet", when="+tokyocabinet")

    variant("ncurses", default=True, description="UI support via ncurses")
    depends_on("ncurses", when="+ncurses", type=["build", "run"])

    variant("cairo", default=False, description="Enable cairo for graph support")
    depends_on("cairo", when="+cairo")
    depends_on("pango", when="+cairo")
    depends_on("libx11", when="+cairo") #--enable-opengl --disable-x11

    @property
    def libs(self):
        libraries = []
        libraries.append("tinfo")
        return find_libraries(libraries, root=self.prefix, recursive=True)

    def setup_build_environment(self, env):
        env.set("LIBS", "-ltinfo")

    def configure_args(self):
        # Need: LIBS="-ltinfo" ./configure --with-db-backend=sqlite3 --disable-cairo --disable-x11
        # args = ["--disable-ui", "--disable-cairo", "--disable-opengl", "--disable-x11"]
        config_args=["--disable-x11", "--disable-opengl"]
        if self.spec.satisfies("+leveldb"):
            config_args.append("--with-db-backend=leveldb")
        if self.spec.satisfies("+sqlite"):
            config_args.append("--with-db-backend=sqlite")
        if self.spec.satisfies("+lmdb"):
            config_args.append("--with-db-backend=lmdb")
        if self.spec.satisfies("+tokyocabinet"):
            config_args.append("--with-db-backend=tokyocabinet")
        if self.spec.satisfies("+cairo"):
            config_args.append("--enable-cairo")
        if self.spec.satisfies("+ncurses"):
            config_args.append("--enable-ui")
        return config_args

    def install(self, spec, prefix):
        make("install", f"PREFIX={prefix}")

