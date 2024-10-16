Name:		texlive-multenum
Version:	21775
Release:	2
Summary:	Multi-column enumerated lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multenum
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multenum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multenum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines an environment multienumerate, that produces an
enumerated array in which columns are vertically aligned on the
counter. The motivation was lists of answers for a text book,
where there are many rather small items; the multienumerate
environment goes some way to making such lists look neater.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multenum/multienum.sty
%doc %{_texmfdistdir}/doc/latex/multenum/README
%doc %{_texmfdistdir}/doc/latex/multenum/multienum.article
%doc %{_texmfdistdir}/doc/latex/multenum/multienum.pdf
%doc %{_texmfdistdir}/doc/latex/multenum/multienum.sample

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
