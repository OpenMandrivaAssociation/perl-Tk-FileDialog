%define name	perl-Tk-FileDialog
%define version	1.3
%define release %mkrel 9

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

