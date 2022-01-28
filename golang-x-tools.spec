# Generated by go2rpm
%bcond_without check

# https://github.com/golang/tools
%global goipath         golang.org/x/tools
%global forgeurl        https://github.com/golang/tools
Version:                0.1.9

%gometa

%global common_description %{expand:
This package holds the source for various tools that support the Go programming
language.

Some of the tools, godoc and vet for example, are included in binary Go
distributions.

Others, including the Go guru and the test coverage tool, can be fetched with go
get.

Packages include a type-checker for Go and an implementation of the Static
Single Assignment form (SSA) representation for Go programs.}

%global golicenses      LICENSE PATENTS
%global godocs          AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

%global commands benchcmp bundle callgraph compilebench cover digraph eg fiximports getgo go-contrib-init godex godoc goimports gomvpkg gorename gotype goyacc guru html2article present splitdwarf ssadump stress stringer toolstash

Name:           %{goname}
Release:        %autorelease -p
Summary:        Various packages and tools that support the Go programming language

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang-tests

%description
%{common_description}

%package -n golang-godoc
Summary:        Documentation tool for the Go programming language
Provides:       golang(%{goipath}/cmd/godoc) = %{version}-%{release}
Epoch:          1
Obsoletes:      golang-godoc = 1.1.2

%description -n golang-godoc
Godoc extracts and generates documentation for Go programs.

%package -n golang-gotype
Summary:        Go programming language source code analysis tool
Provides:       golang(%{goipath}/cmd/gotype) = %{version}-%{release}

%description -n golang-gotype
The gotype command, like the front-end of a Go compiler, parses and type-checks
a single Go package. Errors are reported if the analysis fails; otherwise
gotype is quiet (unless -v is set).

%package -n golang-html2article
Summary:        Tool for creating articles from HTML files
Provides:       golang(%{goipath}/cmd/html2article) = %{version}-%{release}

%description -n golang-html2article
This program takes an HTML file and outputs a corresponding article file
in present format. See: golang.org/x/tools/present

%package        callgraph
Summary:        Tool for reporting the call graph of a Go program
Provides:       golang(%{goipath}/cmd/callgraph) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-callgraph < 0-28

%description    callgraph
%{summary}.

%package        compilebench
Summary:        Benchmarks the speed of the Go compiler
Provides:       golang(%{goipath}/cmd/compilebench) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-compilebench < 0-28

%description    compilebench
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/compilebench for more information.

%package        cover
Summary:        Tool for analyzing Go coverage profiles
Provides:       golang(%{goipath}/cmd/cover) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-cover < 0-28

%description    cover
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/cover for more information.

%package        digraph
Summary:        Tool for queries over unlabelled directed graphs in text form
Provides:       golang(%{goipath}/cmd/digraph) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-digraph < 0-28

%description    digraph
The digraph command performs queries over unlabelled directed graphs
represented in text form.

%package        gorename
Summary:        Tool for precise type-safe renaming of identifiers in Go code
Provides:       golang(%{goipath}/cmd/gorename) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-gorename < 0-28

%description    gorename
The gorename command performs precise type-safe renaming of identifiers in Go
source code.

%package        stringer
Summary:        Tool to automate creating methods satisfying the fmt.Stringer interface
Provides:       golang(%{goipath}/cmd/stringer) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-stringer < 0-28

%description    stringer
Stringer is a tool to automate the creation of methods that satisfy the
fmt.Stringer interface.

%package        godex
Summary:        Tool to dump exported information for Go packages or objects
Provides:       golang(%{goipath}/cmd/godex) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-godex < 0-28

%description    godex
The godex command prints (dumps) exported information of packages or selected
package objects.

See https://godoc.org/golang.org/x/tools/cmd/godex for more information.

%package        benchcmp
Summary:        Displays performance changes between benchmarks for the Go programming language
Provides:       golang(%{goipath}/cmd/benchcmp) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-benchcmp < 0-28

%description    benchcmp
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/benchcmp for more information.

%package        bundle
Summary:        Creates a single-source-file version of a source package
Provides:       golang(%{goipath}/cmd/bundle) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-bundle < 0-28

%description    bundle
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/bundle for more information.

%package        eg
Summary:        Example-based refactoring for the Go programming language
Provides:       golang(%{goipath}/cmd/eg) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-eg < 0-28

%description    eg
%{summary}.

See `eg -help` for more information.

%package        fiximports
Summary:        Fixes import declarations to use the canonical import path
Provides:       golang(%{goipath}/cmd/fiximports) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-fiximports < 0-28

%description    fiximports
%{summary}.

%package        getgo
Summary:        Installs Go to the user's system
Provides:       golang(%{goipath}/cmd/getgo) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-getgo < 0-28

%description    getgo
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/getgo for more information.

%package        go-contrib-init
Summary:        Helps new Go contributors get their development environment set up
Provides:       golang(%{goipath}/cmd/go-contrib-init) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-go-contrib-init < 0-28

%description    go-contrib-init
The go-contrib-init command helps new Go contributors get their development
environment set up for the Go contribution process.

It aims to be a complement or alternative to
https://golang.org/doc/contribute.html.

%package        goimports
Summary:        Go programming language import line formatter
Provides:       golang(%{goipath}/cmd/goimports) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-goimports < 0-28

%description    goimports
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/goimports for more information.

%package        gomvpkg
Summary:        Tool to move Go packages, updating import declarations
Provides:       golang(%{goipath}/cmd/gomvpkg) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-gomvpkg < 0-28

%description    gomvpkg
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/gomvpkg for more information.

%package        gopls
Summary:        LSP server for Go
Provides:       golang(%{goipath}/cmd/gopls) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-gopls < 0-28

%description    gopls
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/gopls for more information.

%package        guru
Summary:        Tool for answering questions about Go source code
Provides:       golang(%{goipath}/cmd/guru) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-guru < 0-28

%description    guru
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/guru for more information.

%package        present
Summary:        Display slide presentations and articles
Provides:       golang(%{goipath}/cmd/present) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-present < 0-28

%description    present
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/present for more information.

%package        splitdwarf
Summary:        Uncompress and copy the DWARF segment of a Mach-O executable into the "dSYM" file
Provides:       golang(%{goipath}/cmd/splitdwarf) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-splitdwarf < 0-28

%description    splitdwarf
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/splitdwarf for more information.

%package        ssadump
Summary:        Tool for displaying and interpreting the SSA form of Go programs
Provides:       golang(%{goipath}/cmd/ssadump) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-ssadump < 0-28

%description    ssadump
%{summary}.

%package        stress
Summary:        Tool for catching sporadic failures
Provides:       golang(%{goipath}/cmd/stress) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-stress < 0-28

%description    stress
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/stress for more information.

%package        toolstash
Summary:        Provides a way to save, run, and restore a known good copy of the Go toolchain
Provides:       golang(%{goipath}/cmd/toolstash) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-toolstash < 0-28

%description    toolstash
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/toolstash for more information.

%package        goyacc
Summary:        Goyacc is a version of yacc for Go
Provides:       golang(%{goipath}/cmd/goyacc) = %{version}-%{release}
# Remove in F33:
Obsoletes:      golang-googlecode-tools-goyacc < 0-28

%description    goyacc
%{summary}.

See https://godoc.org/golang.org/x/tools/cmd/goyacc for more information.

%gopkg

%prep
%goprep
find . -type f -name "*.go" -exec sed -i "s|mvdan.cc/xurls/v2|mvdan.cc/xurls|" "{}" +;


%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in %commands; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/$cmd
done
%gobuild -o %{gobuilddir}/bin/gopls %{goipath}/gopls

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# Fix conflict with rubygem-bundler
mv %{buildroot}%{_bindir}/bundle %{buildroot}%{_bindir}/gobundle

%if %{with check}
%check
%gocheck -t cmd -d imports -t internal/lsp -d go/pointer -d internal/imports -t gopls/internal -d internal/packagesdriver -d go/packages
%endif

%files -n golang-godoc
%{_bindir}/godoc

%files -n golang-gotype
%{_bindir}/gotype

%files -n golang-html2article
%{_bindir}/html2article

%files    godex
%{_bindir}/godex

%files    callgraph
%{_bindir}/callgraph

%files    compilebench
%{_bindir}/compilebench

%files    cover
%{_bindir}/cover

%files    digraph
%{_bindir}/digraph

%files    gorename
%{_bindir}/gorename

%files    stringer
%{_bindir}/stringer

%files    eg
%{_bindir}/eg

%files    fiximports
%{_bindir}/fiximports

%files    getgo
%{_bindir}/getgo

%files    go-contrib-init
%{_bindir}/go-contrib-init

%files    benchcmp
%{_bindir}/benchcmp

%files    bundle
%{_bindir}/gobundle

%files    goimports
%{_bindir}/goimports

%files    gomvpkg
%{_bindir}/gomvpkg

%files    gopls
%{_bindir}/gopls

%files    guru
%{_bindir}/guru

%files    present
%{_bindir}/present

%files    splitdwarf
%{_bindir}/splitdwarf

%files    ssadump
%{_bindir}/ssadump

%files    stress
%{_bindir}/stress

%files    toolstash
%{_bindir}/toolstash

%files    goyacc
%{_bindir}/goyacc

%gopkgfiles

%changelog
%autochangelog
