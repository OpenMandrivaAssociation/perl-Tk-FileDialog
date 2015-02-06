%define name	perl-Tk-FileDialog
%define version	1.3
%define release 12

Summary:	Tk::FileDialog Perl module
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Development/Perl
Source0:	http://cpan.uwinnipeg.ca/cpan/authors/id/B/BP/BPOWERS/Tk-FileDialog-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
A highly configurable File Dialog widget for Perl/Tk.

%prep
%setup -q -n Tk-FileDialog-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=%{buildroot}%{_prefix} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*



%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.3-10mdv2011.0
+ Revision: 658424
- rebuild for updated rpm-setup

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3-9mdv2010.0
+ Revision: 430608
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3-8mdv2009.0
+ Revision: 242075
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.3-6mdv2008.0
+ Revision: 23636
- rebuild


* Fri May 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-5mdk
- Fix Build
- use mkrel

* Mon Nov 15 2004 Austin Acton <austin@mandrake.org> 1.3-4mdk
- rebuild

* Sat Jul 17 2004 Austin Acton <austin@mandrake.org> 1.3-3mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-2mdk
- rebuild for new auto{prov,req}

