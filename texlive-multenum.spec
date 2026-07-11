%global tl_name multenum
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Multi-column enumerated lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multenum
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multenum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multenum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines an environment multienumerate, that produces an enumerated array
in which columns are vertically aligned on the counter. The motivation
was lists of answers for a text book, where there are many rather small
items; the multienumerate environment goes some way to making such lists
look neater.

