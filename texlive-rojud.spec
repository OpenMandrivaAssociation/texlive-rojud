Name:		texlive-rojud
Version:	56895
Release:	2
Summary:	A font with the images of the counties of Romania
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rojud
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rojud.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rojud.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a Type 1 font with images of the 42
counties of Romania, constructed using a general method which
is described in detail in the documentation. The package name
is an abbreviation of "judetele Romaniei" (= counties of
Romania).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/rojud
%{_texmfdistdir}/fonts/type1/public/rojud
%{_texmfdistdir}/fonts/tfm/public/rojud
%{_texmfdistdir}/fonts/map/dvips/rojud
%doc %{_texmfdistdir}/doc/fonts/rojud

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
