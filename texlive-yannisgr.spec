# revision 22613
# category Package
# catalog-ctan /fonts/greek/yannis
# catalog-date 2011-05-22 00:38:15 +0200
# catalog-license gpl2
# catalog-version undef
Name:		texlive-yannisgr
Version:	20110522
Release:	9
Summary:	Greek fonts by Yannis Haralambous
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/yannis
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yannisgr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yannisgr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A family of 7-bit fonts with a code table designed for setting
modern polytonic Greek. The fonts are provided as Metafont
source; macros to produce a Greek variant of Plain TeX
(including a hyphenation table adapted to the fonts' code
table) are provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/yannisgr/csc_misce.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/gen_m_acc.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/greekcsc.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/it_digits.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/it_lig.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/it_lower.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/ligcsc.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/m_accent.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/m_greek.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/mrgrbf10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/mrgrrg10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/mrgrsl10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/mrgrti10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgen_acc.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgraccent.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrbase.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrbf10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgreek.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrlig.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrlower.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrpunct.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrrg10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrsc10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrsl10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrti10.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/rgrupper.mf
%{_texmfdistdir}/fonts/source/public/yannisgr/scsc.mf
%{_texmfdistdir}/fonts/tfm/public/yannisgr/mrgrbf10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/mrgrrg10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/mrgrsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/mrgrti10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/rgrbf10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/rgrrg10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/rgrsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/rgrsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/yannisgr/rgrti10.tfm
%doc %{_texmfdistdir}/doc/fonts/yannisgr/00changes.txt
%doc %{_texmfdistdir}/doc/fonts/yannisgr/README
%doc %{_texmfdistdir}/doc/fonts/yannisgr/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/yannisgr/monsyl.txt
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgreekmacros.tex
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgrhyph.tex
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgrpaper.lis
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgrpaper.tex
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgrsc10.300gf
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgrsc10.lis
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgrsc10.pl
%doc %{_texmfdistdir}/doc/fonts/yannisgr/rgrtestfont.tex
%doc %{_texmfdistdir}/doc/fonts/yannisgr/tomakeformat.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110522-2
+ Revision: 757740
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110522-1
+ Revision: 719961
- texlive-yannisgr
- texlive-yannisgr
- texlive-yannisgr

