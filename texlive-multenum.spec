# revision 21775
# category Package
# catalog-ctan /macros/latex/contrib/multenum
# catalog-date 2011-03-20 19:39:20 +0100
# catalog-license lppl1
# catalog-version undef
Name:		texlive-multenum
Version:	20170414
Release:	1
Summary:	Multi-column enumerated lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multenum
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multenum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multenum.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110320-2
+ Revision: 754183
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110320-1
+ Revision: 719079
- texlive-multenum
- texlive-multenum
- texlive-multenum
- texlive-multenum

