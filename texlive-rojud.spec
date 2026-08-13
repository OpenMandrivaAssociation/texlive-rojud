%global tl_name rojud
%global tl_revision 56895
%global tl_version 1.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A font with the images of the counties of Romania
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/rojud
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rojud.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rojud.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides a Type 1 font with images of the 42 counties of
Romania, constructed using a general method which is described in detail
in the documentation. The package name is an abbreviation of "judetele
Romaniei" (= counties of Romania).


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from rojud:
Map rojud.map
TL_DROPIN_EOF
