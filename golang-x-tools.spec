# Generated by go2rpm
%bcond_without check

# https://github.com/golang/tools
%global goipath         golang.org/x/tools
%global forgeurl        https://github.com/golang/tools
%global commit          2e9de471ebd3a3af420e4dd35a826936b94da7f6

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-golangorg-tools-devel < 0-28
}

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

%global commands benchcmp bundle callgraph compilebench cover digraph eg fiximports getgo go-contrib-init godex godoc goimports gopls gomvpkg gorename gotype goyacc guru html2article present splitdwarf ssadump stress stringer toolstash

Name:           %{goname}
Version:        0
Release:        30%{?dist}
Summary:        Various packages and tools that support the Go programming language

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/atom)
BuildRequires:  golang(golang.org/x/net/websocket)

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


%build
for cmd in %commands; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# Fix conflict with rubygem-bundler
mv %{buildroot}%{_bindir}/bundle %{buildroot}%{_bindir}/gobundle

%if %{with check}
%check
%gocheck -d cmd/stringer -d imports
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
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-29.20190622git2e9de47
- Add Obsoletes for old names

* Tue Apr 16 16:42:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-28.20190622git2e9de47
- Bump to commit 2e9de471ebd3a3af420e4dd35a826936b94da7f6

* Mon Mar 04 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-27.20190219git9394956
- Fix conflict with rubygem-bundler (#1685237)

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-26.20190219git9394956
- Bump to upstream 9394956cfdc50651347ab69dbde09af8a8e24776

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.1.gitce871d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-24.2.gitce871d1
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.1.gitce871d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 0-23.1.gitce871d1
- Package goyacc
  resolves: #1576672

* Wed Apr 04 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-22.1.gitce871d1
- Update to go spec 3.0

* Mon Feb 19 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-21.1.20180214gitce871d1
- Autogenerate some parts using the new macros

* Thu Feb 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-20.1.20180214gitce871d1
- Bump to upstream ce871d178848e3eea1e8795e5cfb74053dde4bb9

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.1.git9deed8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-15.1.git9deed8c
- Polish the spec file
  related: #1279381

* Wed Sep 07 2016 jchaloup <jchaloup@redhat.com> - 0-14.1.git9deed8c
- Bump to upstream 9deed8c6c1c89e0b6d68d727f215de8e851d1064
  resolves: #1373868

* Fri Aug 26 2016 jchaloup <jchaloup@redhat.com> - 0-13.1.git1cdaff4
- Include missing templates and static directories
  resolves: #1370456

* Fri Aug 05 2016 jchaloup <jchaloup@redhat.com> - 0-12.1.git1cdaff4
- Do not ship vet and cover binaries anymore, they are shipped via golang-bin
  resolves: #1268206

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-11.1.git1cdaff4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Wed Apr 27 2016 jchaloup <jchaloup@redhat.com> - 0-10.1.git1cdaff4
- Bump to upstream 1cdaff4a02c554c9fb39dda0b56241c5f0949d91
  related: #1279381

* Wed Apr 13 2016 jchaloup <jchaloup@redhat.com> - 0-9.1.git997b354
- Run tests only on golang architectures

* Thu Mar 03 2016 jchaloup <jchaloup@redhat.com>
- Polish spec file
  don't check go/importer on ppc

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.1.git997b354
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 10 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-6.1.git997b354
- Update to golang_arches

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.0.git997b354
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 jchaloup <jchaloup@redhat.com> - 0-5.0.git997b354
- Update a list of provided packages

* Thu Oct 15 2015 jchaloup <jchaloup@redhat.com> - 0-4.0.git997b354
- Bump to upstream 997b3545fd86c3a2d8e5fe6366174d7786e71278

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.0.hga7e14835e46b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 jchaloup <jchaloup@redhat.com> - 0-2.0.hga7e14835e46b
- Bump to a7e14835e46bb13da10fa8b9c9c5e7f2f378f568
- Add new tools presented in the commit
- Change import paths to new prefix schema golang.org/x/...
- Add new subpackage and keep the only one for back-compatibility
  resolves: #1199617

* Tue Aug 19 2014 Vincent Batts <vbatts@fedoraproject.org> - 0-1.0.hgd32b5854c941
- updating to the current latest go.tools

* Tue Aug 19 2014 Vincent Batts <vbatts@fedoraproject.org> - 0-0.9.hg17c8fe23290a
- setting an epoch for godoc to fix bz1099074

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.hg17c8fe23290a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Vincent Batts <vbatts@redhat.com> 0-0.7.hg17c8fe23290a
- fix bz1129281 and cleanup file ownership

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.hg17c8fe23290a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Vincent Batts <vbatts@redhat.com> 0-0.5.hg17c8fe23290a
- working on the arch dependencies
- clean up file ownership

* Thu Dec 05 2013 Vincent Batts <vbatts@redhat.com> 0-0.4.hg17c8fe23290a
- golang-godoc to obsolete the package from golang 1.1.2

* Tue Nov 12 2013 Vincent Batts <vbatts@redhat.com> 0-0.3.hg17c8fe23290a
- removing conflicting directory ownership

* Tue Nov 12 2013 Vincent Batts <vbatts@redhat.com> 0-0.2.hg17c8fe23290a
- adding subpackages for all available commands

* Sun Nov 10 2013 Vincent Batts <vbatts@redhat.com> 0-0.1.hg17c8fe23290a
- initial build
