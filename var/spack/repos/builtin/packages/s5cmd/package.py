# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class S5cmd(Package):
    """Parallel S3 and local filesystem execution tool. """

    homepage = "https://github.com/peak/s5cmd"
    url = "https://github.com/peak/s5cmd/releases/download/v2.0.0/s5cmd_2.0.0_Linux-64bit.tar.gz"

    version("2.1.0-beta.1", sha256="de5efa37941ef83e892662aefc936603a1a8acbc5a6a9e003a71721a7140b610")
    version("2.0.0", sha256="0ac2ae20a73d9f1747a19288224d07c846fad41f7f122dc1dea48162eb0ef4b4")

    depends_on("go")

    def setup_build_environment(self, env):
        env.prepend_path("GOPATH", self.stage.path)

    def install(self, spec, prefix):
        go_args = ["build"]
        if self.spec.satisfies("+extended"):
            go_args.extend(["--tags", "extended"])

        go(*go_args)
        mkdirp(prefix.bin)
        install("s5cmd", prefix.bin)
