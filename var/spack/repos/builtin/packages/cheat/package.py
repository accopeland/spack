# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Cheat(MakefilePackage):
    """FIXME: Currently broken"""

    homepage = "https://github.com/cheat/cheat"
    url = "https://github.com/cheat/cheat/archive/refs/tags/4.4.0.tar.gz"

    version("4.4.0", sha256="8694d75896dcb1dfb91ed95ec37f7fe409ad2bde76e66f80b20be24ee92ae3ec")

    depends_on("go")

    def setup_build_environment(self, env):
        env.prepend_path("GOPATH", self.stage.path)

    def install(self, spec, prefix):
        go_args = ["build"]
        if self.spec.satisfies("+extended"):
            go_args.extend(["--tags", "extended"])

        go(*go_args)
        mkdirp(prefix.bin)
        install("hugo", prefix.bin)
