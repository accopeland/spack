# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import inspect

from spack.package import *


class PerlIoSocketSsl(PerlPackage):
    """SSL sockets with IO::Socket interface
    
    FIXME: semi-broken due to issues with configure producing
    => Error: AttributeError: 'Adapter' object has no attribute 'build_method'

The 'perl-io-socket-ssl' package cannot find an attribute while trying to build from sources. This might be due to a change in Spack's package format to support multiple build-systems for a single package. You can fix this by updating the build recipe, and you can also report the issue as a bug. More information at https://spack.readthedocs.io/en/latest/packaging_guide.html#installation-procedure 
    

    Commenting out configure entirely allows build/install to proceed but you have to know to hit <ENTER> to 
    get around the perl test questions
    """

    homepage = "https://metacpan.org/dist/IO-Socket-SSL/view/lib/IO/Socket/SSL.pod"
    url = "https://cpan.metacpan.org/authors/id/S/SU/SULLR/IO-Socket-SSL-2.081.tar.gz"

    version("2.081", sha256="07bdf826a8d6b463316d241451c890d1012fa2499a83d8e3d00ce0a584618443")
    version("2.080", sha256="cd0ed303b08a72c5c256a9ec3bbb6ff61360be3a2ff6d775e4f6e25375fa8d1f")
    version("2.079", sha256="10352ba536a66f51d201b4e188325f3d53795d24bdc0dfbf3f1cb9ca354a5f77")
    version("2.078", sha256="4cf83737a72b0970948b494bc9ddab7f725420a0ca0152d25c7e48ef8fa2b6a1")
    version("2.077", sha256="5579a61ffc3520e1abe02f4507b56938f34b823d89c32ab051f3fbd3cf166a19")
    version("2.076", sha256="bdd148d9feaef1220251676d7053698fcf446c9850d706fe2e1c90ff232ed874")
    version("2.075", sha256="c30ee2220b1e181a968ebbc81861d0cadf334b001377a44105ae5a8637ddae8c")
    version("2.074", sha256="36486b6be49da4d029819cf7069a7b41ed48af0c87e23be0f8e6aba23d08a832")
    version("2.073", sha256="b2c0b34df97cb1aa816221cee2454a1efd89b86ccbda810389a30e0d08cf57c8")
    version("2.052", sha256="e4897a9b17cb18a3c44aa683980d52cef534cdfcb8063d6877c879bfa2f26673")

    depends_on("perl-net-ssleay", type=("build", "run"))

    #def configure(self, spec, prefix):
    #    #self.build_method = "Makefile.PL"
    #    #self.build_executable = inspect.getmodule(self).make
    #    # Should I do external tests?
    #    config_answers = ["n\n"]
    #    config_answers_filename = "spack-config.in"
#
#        with open(config_answers_filename, "w") as f:
#            f.writelines(config_answers)

        #with open(config_answers_filename, "r") as f:
        #    inspect.getmodule(self).perl("Makefile.PL", "INSTALL_BASE={0}".format(prefix), input=f)
