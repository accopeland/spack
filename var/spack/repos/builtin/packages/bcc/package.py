# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Bcc(CMakePackage):
    """BCC - Tools for BPF-based Linux IO analysis, networking, monitoring, and more"""

    homepage = "https://github.com/iovisor/bcc"
    url = "https://github.com/iovisor/bcc/releases/download/v0.26.0/bcc-src-with-submodule.tar.gz"

    version("0.26.0", sha256="cd6c3580ece8f3e99cdc25155dc77d09c1f10dd9d8a13105f468af45963030b0")

    depends_on("arping")
    depends_on("bison",when="build")
    #depends_on("clang-format") llvm@16
    depends_on("cmake",when="build")
    #depends_on("dh-python")
    depends_on("ethtool")
    depends_on("flex",when="build")
    #depends_on("inetutils-ping")
    depends_on("iperf")
    depends_on("libbpf")  # maybe submodule already?
    #depends_on("libclang")
    depends_on("libedit")
    #depends_on("libelf")  # should deprecate in favor of elfutils ?
    ##depends_on("elfutils") # need gelf.h containing GElf_Nhdr
    #depends_on("libfl") # flex
    depends_on("libzip")
    depends_on("lzma")
    depends_on("llvm")
    depends_on("luajit") #@5.1")
    depends_on("python@3")
    depends_on("py-netaddr")
    depends_on("py-pyroute2")
    #depends_on("py-distutils")

    #python3-netaddr python3-pyroute2 python3-distutils python3

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
