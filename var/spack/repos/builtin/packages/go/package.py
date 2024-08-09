# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from llnl.util import tty

from spack.package import *

# - vanilla CentOS 7, and possibly other systems, fail a test:
#   TestCloneNEWUSERAndRemapRootDisableSetgroups
#
#   The Fix, discussed here: https://github.com/golang/go/issues/16283
#   is to enable "user_namespace".
#
#   On a Digital Ocean image, this can be achieved by updating
#   `/etc/default/grub` so that the `GRUB_CMDLINE_LINUX` variable
#   includes `user_namespace.enable=1`, re-cooking the grub
#   configuration with `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`,
#   and then rebooting.
#
# - on CentOS 7 systems (and possibly others) you need to have the
#   glibc package installed or various static cgo tests fail.
#


class Go(Package):
    """The golang compiler and build environment"""

    homepage = "https://go.dev"
    url = "https://go.dev/dl/go1.20.2.src.tar.gz"
    git = "https://go.googlesource.com/go.git"

    extendable = True
    executables = ["^go$"]

    maintainers("alecbcs")

    license("BSD-3-Clause")

    version("1.22.6", sha256="9e48d99d519882579917d8189c17e98c373ce25abaebb98772e2927088992a51")
    version("1.22.5", sha256="ac9c723f224969aee624bc34fd34c9e13f2a212d75c71c807de644bb46e112f6")
    version("1.22.4", sha256="fed720678e728a7ca30ba8d1ded1caafe27d16028fab0232b8ba8e22008fb784")
    version("1.22.3", sha256="80648ef34f903193d72a59c0dff019f5f98ae0c9aa13ade0b0ecbff991a76f68")
    version("1.22.2", sha256="374ea82b289ec738e968267cac59c7d5ff180f9492250254784b2044e90df5a9")
    version("1.22.1", sha256="79c9b91d7f109515a25fc3ecdaad125d67e6bdb54f6d4d98580f46799caea321")
    version("1.22.0", sha256="4d196c3d41a0d6c1dfc64d04e3cc1f608b0c436bd87b7060ce3e23234e1f4d5c")
    version("1.21.13", sha256="71fb31606a1de48d129d591e8717a63e0c5565ffba09a24ea9f899a13214c34d")
    version("1.21.12", sha256="30e68af27bc1f1df231e3ab74f3d17d3b8d52a089c79bcaab573b4f1b807ed4f")
    version("1.21.11", sha256="42aee9bf2b6956c75a7ad6aa3f0a51b5821ffeac57f5a2e733a2d6eae1e6d9d2")
    version("1.21.10", sha256="900e0afe8900c1ee65a8a8c4f0c5a3ca02dcf85c1d1cb13a652be22c21399394")
    version("1.21.9", sha256="58f0c5ced45a0012bce2ff7a9df03e128abcc8818ebabe5027bb92bafe20e421")
    version("1.21.8", sha256="dc806cf75a87e1414b5b4c3dcb9dd3e9cc98f4cfccec42b7af617d5a658a3c43")
    version("1.21.7", sha256="00197ab20f33813832bff62fd93cca1c42a08cc689a32a6672ca49591959bff6")
    version("1.21.6", sha256="124926a62e45f78daabbaedb9c011d97633186a33c238ffc1e25320c02046248")
    version("1.21.5", sha256="285cbbdf4b6e6e62ed58f370f3f6d8c30825d6e56c5853c66d3c23bcdb09db19")
    version("1.21.3", sha256="186f2b6f8c8b704e696821b09ab2041a5c1ee13dcbc3156a13adcf75931ee488")

    # https://nvd.nist.gov/vuln/detail/CVE-2024-24790
    # https://nvd.nist.gov/vuln/detail/CVE-2024-24789
    version(
        "1.22.2",
        sha256="374ea82b289ec738e968267cac59c7d5ff180f9492250254784b2044e90df5a9",
        deprecated=True,
    )
    version(
        "1.22.1",
        sha256="79c9b91d7f109515a25fc3ecdaad125d67e6bdb54f6d4d98580f46799caea321",
        deprecated=True,
    )
    version(
        "1.22.0",
        sha256="4d196c3d41a0d6c1dfc64d04e3cc1f608b0c436bd87b7060ce3e23234e1f4d5c",
        deprecated=True,
    )
    version(
        "1.21.6",
        sha256="124926a62e45f78daabbaedb9c011d97633186a33c238ffc1e25320c02046248",
        deprecated=True,
    )
    version(
        "1.21.5",
        sha256="285cbbdf4b6e6e62ed58f370f3f6d8c30825d6e56c5853c66d3c23bcdb09db19",
        deprecated=True,
    )

    provides("golang")

    depends_on("bash", type="build")
    depends_on("sed", type="build")
    depends_on("grep", type="build")
    depends_on("go-or-gccgo-bootstrap", type="build")
    depends_on("go-or-gccgo-bootstrap@1.17.13:", type="build", when="@1.20:")
    depends_on("go-or-gccgo-bootstrap@1.20.6:", type="build", when="@1.22:")

    phases = ["build", "install"]

    def url_for_version(self, version):
        return f"https://go.dev/dl/go{version}.src.tar.gz"

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("version", output=str, error=str)
        match = re.search(r"go version go(\S+)", output)
        return match.group(1) if match else None

    def setup_build_environment(self, env):
        env.set("GOROOT_FINAL", self.spec.prefix.go)
        # We need to set CC/CXX_FOR_TARGET, otherwise cgo will use the
        # internal Spack wrappers and fail.
        env.set("CC_FOR_TARGET", self.compiler.cc)
        env.set("CXX_FOR_TARGET", self.compiler.cxx)
        env.set("GOMAXPROCS", make_jobs)

    def build(self, spec, prefix):
        # Build script depend on bash
        bash = which("bash")

        with working_dir("src"):
            bash(f"{'all' if self.run_tests else 'make'}.bash")

    def install(self, spec, prefix):
        install_tree(".", prefix.go)
        os.symlink(prefix.go.bin, prefix.bin)

    def setup_dependent_package(self, module, dependent_spec):
        """Called before go modules' build(), install() methods.

        In most cases, extensions will only need to set GOPATH and use go::

        env['GOPATH'] = self.source_path + ':' + env['GOPATH']
        go('get', '<package>', env=env)
        install_tree('bin', prefix.bin)
        """
        #  Add a go command/compiler for extensions
        module.go = self.spec["go"].command

    def generate_path_components(self, dependent_spec):
        if os.environ.get("GOROOT", False):
            tty.warn("GOROOT is set, this is not recommended")

        # Set to include paths of dependencies
        path_components = [dependent_spec.prefix]
        for d in dependent_spec.traverse():
            if d.package.extends(self.spec):
                path_components.append(d.prefix)
        return ":".join(path_components)

    def setup_dependent_build_environment(self, env, dependent_spec):
        # This *MUST* be first, this is where new code is installed
        env.prepend_path("GOPATH", self.generate_path_components(dependent_spec))

    def setup_dependent_run_environment(self, env, dependent_spec):
        # Allow packages to find this when using module files
        env.prepend_path("GOPATH", self.generate_path_components(dependent_spec))
