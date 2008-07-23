%define	name      cdb0.75
%define	src_name  cdb
%define version   0.75
%define release   %mkrel 3

Summary:	Constant DataBase
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Databases
URL:		http://cr.yp.to/cdb.html
Source0:	%{src_name}-%{version}.tar.bz2

# Thanks to Gentoo.
Patch0:		%{src_name}-%{version}-errno.patch.bz2

BuildRoot:	%{_tmppath}/%{src_name}-%{version}-root

%description
cdb is a fast, reliable, lightweight package for
creating and reading constant databases.


%package devel
Summary: Static libraries and headers for cdb-%{version}
Group: Development/Databases

%description devel
Libraries and header files needed to develop
applications using cdb databases


%prep

%setup -q -n %{src_name}-%{version}
%patch0 -p0

%build
make it

%install
rm -rf $RPM_BUILD_ROOT

# install bin files
install -d %{buildroot}%{_libdir}/cdb-0.75/
install -m 755 cdbdump %{buildroot}%{_libdir}/cdb-0.75/
install -m 755 cdbget %{buildroot}%{_libdir}/cdb-0.75/
install -m 755 cdbmake %{buildroot}%{_libdir}/cdb-0.75/
install -m 755 cdbmake-12 %{buildroot}%{_libdir}/cdb-0.75/
install -m 755 cdbmake-sv %{buildroot}%{_libdir}/cdb-0.75/
install -m 755 cdbstats %{buildroot}%{_libdir}/cdb-0.75/
install -m 755 cdbtest %{buildroot}%{_libdir}/cdb-0.75/

# install devel files
install -d %{buildroot}%{_libdir}/cdb-0.75/
install -m 644 *.h %{buildroot}%{_libdir}/cdb-0.75/
install -m 644 *.a %{buildroot}%{_libdir}/cdb-0.75/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc CHANGES README TODO VERSION
%{_libdir}/cdb-0.75/cdb*

%files devel
%defattr(-,root,root)
%doc README
%{_libdir}/cdb-0.75/*.h
%{_libdir}/cdb-0.75/*.a


