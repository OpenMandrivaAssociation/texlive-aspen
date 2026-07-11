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
BuildSystem:	texlive
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

