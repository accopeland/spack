# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import inspect

from spack.package import *

class PerlNetSsleay(PerlPackage):
    """Perl extension for using OpenSSL"""

    homepage = "https://metacpan.org/pod/Net::SSLeay"
    #url = "http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Net-SSLeay-1.82.tar.gz"
    url = "https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-1.93_02.tar.gz"

    version("1.93_02", sha256="1a11d1ae63e9fc85c90279085957aec81a15af985d7cff185b66154f7032fcdf")
    version("1.93_01", sha256="876d022fbc719631b11d6bb4b6e78db3c19bbca578093c376c8f9900a4432aa3")
    version("1.92", sha256="47c2f2b300f2e7162d71d699f633dd6a35b0625a00cbda8c50ac01144a9396a9")
    version("1.91_03", sha256="a8a5c30ae78a932ee3d19764a07285c37711f4e76d4004be8d1093eb193aaa39")
    version("1.91_02", sha256="770bf7c420b7083d3c9c1f46fd3b1497f20c38623ee0f6eb792331b0d79f9748")
    version("1.91_01", sha256="bae9400f0655dfb39b0779d3f6445a52954705ad75cccdd7d6e55a6f13b65dfa")
    version("1.90", sha256="f8696cfaca98234679efeedc288a9398fcf77176f1f515dbc589ada7c650dc93")
    version("1.85", sha256="9d8188b9fb1cae3bd791979c20554925d5e94a138d00414f1a6814549927b0c8")
    version("1.82", sha256="5895c519c9986a5e5af88e3b8884bbdc70e709ee829dc6abb9f53155c347c7e5")

    depends_on("perl")
    depends_on("openssl")
    depends_on("perl-mime-base64")

    def configure(self, spec, prefix):
#        self.build_method = "Makefile.PL"
#        self.build_executable = inspect.getmodule(self).make
        # Do you want to run external tests?
        config_answers = ["\n"]
        config_answers_filename = "spack-config.in"

        with open(config_answers_filename, "w") as f:
            f.writelines(config_answers)

        with open(config_answers_filename, "r") as f:
            env["OPENSSL_PREFIX"] = self.spec["openssl"].prefix
            #inspect.getmodule(self).perl("Makefile.PL", "INSTALL_BASE={0}".format(prefix), input=f)
