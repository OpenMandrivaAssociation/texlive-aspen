%global tl_name aspen
%global tl_revision 78984

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	Simple crypto notation in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aspen
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aspen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aspen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Aspen package implements LaTeX commands closely related to what is
often called security protocol notation, standard protocol engineering
notation, standard protocol notation, or protocol narrations.
Optionally, the Aspen package also implements LaTeX commands for
Burrows-Abadi-Needham logic (BAN logic). The name Aspen can be an
abbreviation for A Security Protocol Engineering Notation, but another
possible abbreviation is Anderson-inspired Standard Protocol Engineering
Notation, in memory of the late Professor Ross J. Anderson who has meant
so much for the fields of computer security, distributed systems, and,
in particular, security engineering.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/aspen
%dir %{_datadir}/texmf-dist/tex/latex/aspen
%doc %{_datadir}/texmf-dist/doc/latex/aspen/COPYRIGHT
%doc %{_datadir}/texmf-dist/doc/latex/aspen/README.md
%doc %{_datadir}/texmf-dist/doc/latex/aspen/aspen-doc.ltx
%doc %{_datadir}/texmf-dist/doc/latex/aspen/aspen-doc.pdf
%{_datadir}/texmf-dist/tex/latex/aspen/aspen.sty
