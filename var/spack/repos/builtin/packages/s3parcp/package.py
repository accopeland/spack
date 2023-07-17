# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class S3parcp(Package):
    """Faster than s3cp"""

    homepage = "https://github.com/chanzuckerberg/s3parcp"
    url = "https://github.com/chanzuckerberg/s3parcp/archive/refs/tags/v1.0.1.tar.gz"

    version("1.0.1", sha256="abeafa7be21512ad6265bab1b76740016939ad457ddb07991222c22091e192e3")

    depends_on("go")

    def setup_build_environment(self, env):
        env.prepend_path("GOPATH", self.stage.path)

    def install(self, spec, prefix):
        go_args = ["build"]
        if self.spec.satisfies("+extended"):
            go_args.extend(["--tags", "extended"])

        go(*go_args)
        mkdirp(prefix.bin)
        install("s3parcp", prefix.bin)
