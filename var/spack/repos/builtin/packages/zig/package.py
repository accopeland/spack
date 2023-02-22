# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Zig(CMakePackage):
    """A general-purpose programming language and toolchain for maintaining
    robust, optimal, and reusable software.
    """

    homepage = "https://ziglang.org/"
    git = "https://github.com/ziglang/zig.git"
    url = "https://github.com/ziglang/zig/archive/refs/tags/0.10.0.tar.gz"

    version("0.10.0", sha256="805a3789776ed2835c41d12139568a406c9827bb8363a70d6f96340a95ffa8f2")
    #version("0.9.1", tag="0.9.1")

    variant(
        "build_type",
        values=("Release", "RelWithDebInfo", "MinSizeRel"),
        default="Release",
        description="CMake build type",
    )

    depends_on("llvm@15 targets=all") #, when="@0.10.0:")
    #depends_on("llvm@13 targets=all", when="@0.9.1:")
    #depends_on("llvm@11.0.0: targets=all")

    #depends_on("git", type="build")
    depends_on("ccache")

    provides("ziglang")

    def cmake_args(self):
        return [
            self.define("ZIG_USE_CCACHE", True),
            self.define("ZIG_STATIC_LLVM", True),
            self.define("ZIG_STATIC_ZLIB", True),
        ]
