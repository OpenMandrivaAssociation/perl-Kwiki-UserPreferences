%define upstream_name	 Kwiki-UserPreferences
Name:		perl-%{upstream_name}
Version:	0.13
Release:	6

Summary:	Kwiki User Preferences Plugin 
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Kwiki-UserPreferences
Source0:	https://cpan.metacpan.org/authors/id/I/IN/INGY/Kwiki-UserPreferences-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
Enable the setting of various User Preferences.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 403387
- rebuild using %0.13 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.13-7mdv2009.0
+ Revision: 257524
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.13-6mdv2009.0
+ Revision: 245616
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-4mdv2008.1
+ Revision: 133636
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-3mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-2mdk
- better sources URL
- better buildrequires syntax

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk 
- first mandriva release

