# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# DRAFT -- work in progress

from spack.package import *

class ZigBootstrap(CMakePackage):
    """The purpose of this project is to start with minimum system dependencies and end with a fully operational Zig compiler for any target."""

    homepage = "https://github.com/ziglang/zig-bootstrap"
    url = "https://github.com/ziglang/zig-bootstrap/archive/refs/tags/0.10.1.tar.gz"

    version("0.10.1", sha256="fa29851d467d842bf05d8f5dd79a143985367b3eeddcfb9ed383e9cade3f4e85")

    depends_on("gcc", type="build", when="@5.1:")   # C++ compiler capable of building LLVM, Clang, and LLD from source (GCC 5.1+ or Clang)
    #depends_on("cmake",type="build", when="@3.19:") # make, ninja, or any other build system supported by CMake
    #depends_on("python",type="build", when="@3:")

    #build_system("cmake", conditional("generic", when="platform=windows"), default="build")

    def cmake_args(self):
        args = ["-DCMAKE_GENERATOR=Ninja"]
        return args
