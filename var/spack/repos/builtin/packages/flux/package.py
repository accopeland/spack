# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Flux(MakefilePackage):
    """Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit."""

    homepage = "https://github.com/fluxcd/flux2"
    url = "https://github.com/fluxcd/flux2/archive/refs/tags/v2.3.0.tar.gz"

    license("Apache")

    version("2.3.0", sha256="62b65a2b665f7d18d37237f6e190dd2cb1dc6377ad193c00356a1c5b8b8151f5")
    version("2.2.3", sha256="bd7a284be9c7d16bc080ec9f559def1e3489bfa8fec49d7e95c352dc002b9724")
    version("2.2.2", sha256="08dcc510f840fb06047e83f8fa4b1f69495d787e64edb1ce918c24cef5fd992c")
    version("2.2.1", sha256="aa01a6b3ec41588d21a5eb637d1c77292e4ca4da68e92c606dd8a980d58ca4bd")
    version("2.2.0", sha256="0c18c368696a292ec9868c967a1e346f756aee8e1a6c0bca5a999196f652979c")
    version("2.1.2", sha256="5bf3d9654fd789e065c0e7c017e3b4594784f0e1b2f2fdd6ae43f33d814b5885")
    version("2.1.1", sha256="c42a9016d53e961a85c253fb167cd6e412c5d3beb69d1a07217d6f9af7acb852")
    version("2.1.0", sha256="5fd7e703f5724c9beae8adabe17b823c5cd4a381ac6f88dfff3ff3713ed08883")
    version("2.0.1", sha256="b4c57d94d81eea40ea7180e814d2e6984b8787d296a21b1b662397a9a23d5407")
    version("2.0.0", sha256="4731817f0edc9dfaf0c2c011a52845611794abf8c287c7f3a9f4d3d9df166d4a")

    depends_on("go@1.22.0")
    #6      go mod tidy -compat=1.22
    #7      go fmt ./...
    #8      go vet ./...
    #9      go: creating new go.mod: module tmp
    depends_on("kustomize")
     #>> 10     [ERROR]  kustomize is not installed
     #>> 11     make: *** [Makefile:53: cmd/flux/.manifests.done] Error 1
     # 12     make: *** Waiting for unfinished jobs....
     #13     Downloading sigs.k8s.io/controller-runtime/tools/setup-envtest@latest
     #14     go: downloading github.com/gonvenience/bunt v1.3.5
     #15     go: downloading github.com/fluxcd/cli-utils v0.36.0-flux.7
     #16     go: downloading github.com/hashicorp/go-cleanhttp v0.5.2
     #17     go: downloading github.com/fluxcd/pkg/ssa v0.39.1
#
#     ...
#
#     406    go: downloading github.com/grpc-ecosystem/grpc-gateway/v2 v2.16.0
     #407    go: downloading github.com/jmespath/go-jmespath/internal/testify v1.5.1
     #408    go: downloading google.golang.org/genproto/googleapis/api v0.0.0-20230822172742-b8732ec3820d
     #409    go: downloading github.com/golang/glog v1.1.2
     #410    go: downloading google.golang.org/genproto v0.0.0-20230822172742-b8732ec3820d
     #411    go: downloading golang.org/x/mod v0.17.0
     #412    cmd/flux/manifests.embed.go:27:12: pattern manifests/*.yaml: no matching files found
     #413    make: *** [Makefile:27: vet] Error 1
     #414    cd tests/integration && go mod tidy -compat=1.22
     #415    go: downloading github.com/Azure/azure-event-hubs-go/v3 v3.6.2
     #416    go: downloading cloud.google.com/go/pubsub v1.38.0
     #417    go: downloading github.com/chainguard-dev/git-urls v1.0.2
     #418    go: downloading github.com/fluxcd/test-infra/tftestenv v0.0.0-20240429114247-01ecf2cc78e4
     #419    go: downloading github.com/hashicorp/terraform-json v0.21.0

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass
