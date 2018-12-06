#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-Coverage
Version  : 0.23
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Pod-Coverage-0.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Pod-Coverage-0.23.tar.gz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0+
Requires: perl-Pod-Coverage-bin = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::Symdump)

%description
No detailed description available

%package bin
Summary: bin components for the perl-Pod-Coverage package.
Group: Binaries

%description bin
bin components for the perl-Pod-Coverage package.


%package dev
Summary: dev components for the perl-Pod-Coverage package.
Group: Development
Requires: perl-Pod-Coverage-bin = %{version}-%{release}
Provides: perl-Pod-Coverage-devel = %{version}-%{release}

%description dev
dev components for the perl-Pod-Coverage package.


%prep
%setup -q -n Pod-Coverage-0.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Pod/Coverage.pm
/usr/lib/perl5/vendor_perl/5.28.1/Pod/Coverage/CountParents.pm
/usr/lib/perl5/vendor_perl/5.28.1/Pod/Coverage/ExportOnly.pm
/usr/lib/perl5/vendor_perl/5.28.1/Pod/Coverage/Overloader.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/pod_cover

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Coverage.3
/usr/share/man/man3/Pod::Coverage::CountParents.3
/usr/share/man/man3/Pod::Coverage::ExportOnly.3
/usr/share/man/man3/Pod::Coverage::Overloader.3
