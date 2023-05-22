# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from glob import glob

from spack.package import *


class AsperaCli(Package):
    """The Aspera CLI client for the Fast and Secure Protocol (FASP)."""

    #homepage = "https://asperasoft.com"
    #url = "https://download.asperasoft.com/download/sw/cli/3.7.7/aspera-cli-3.7.7.608.927cce8-linux-64-release.sh"
    homepage = "https://github.com/IBM/aspera-cli"
    url = "https://github.com/IBM/aspera-cli/archive/refs/tags/v4.12.0.tar.gz"

    version("4.12.0", sha256="0c5ecfe2d079350174065a1a76ce98ca47d2da361257d4eb67844367c33baab6")
    #version("3.7.7", sha256="83efd03b699bdb1cac6c62befb3812342d6122217f4944f732ae7a135d578966")

    version(
        "3.7.7",
        sha256="83efd03b699bdb1cac6c62befb3812342d6122217f4944f732ae7a135d578966",
        url="https://download.asperasoft.com/download/sw/cli/3.7.7/aspera-cli-3.7.7.608.927cce8-linux-64-release.sh",
        expand=False,
    )

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.cli.bin)

    def install(self, spec, prefix):
        runfile = glob(join_path(self.stage.source_path, "aspera-cli*.sh"))[0]
        # Update destination path
        filter_file(
            "INSTALL_DIR=~/.aspera",
            "INSTALL_DIR=%s" % prefix,
            runfile,
            string=True,
            stop_at="__ARCHIVE_FOLLOWS__",
        )
        # Install
        chmod = which("chmod")
        chmod("+x", runfile)
        runfile = which(runfile)
        runfile()
