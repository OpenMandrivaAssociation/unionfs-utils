%define name unionfs-utils
%define version 0.1
%define release %mkrel 1

%define lib_major 0
%define lib_name %mklibname %{name} %{lib_major}

%define common_description Unionfs is a Stackable Unification File System.

Summary: Userspace utilities for Unionfs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.fsl.cs.sunysb.edu/pub/unionfs/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.unionfs.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: automake1.9
BuildRequires: e2fsprogs-devel
Obsoletes: unionfs-tools
Provides: unionfs-tools

%description
%{common_description}

This package contains userspace utilities for Unionfs.

%package -n	%{lib_name}
Summary:	Unionfs utilities library
Group:		System/Libraries

%description -n	%{lib_name}
%{common_description}

This package contains the library needed to run programs dynamically
linked with Unionfs.

%package -n	%{lib_name}-devel
Summary:	Development tools for programs using Unionfs
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
%{common_description}

This package contains the header files and libraries needed for
developing programs using the Unionfs utilities library.

%prep
%setup -q -n %{name}

%build
./bootstrap
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/union*
%{_mandir}/man8/*.8*

%files -n %{lib_name}
%{_libdir}/libunionfs_utils.so.*

%files -n %{lib_name}-devel
%{_includedir}/unionfs_utils.h
%{_libdir}/libunionfs_utils.a
%{_libdir}/libunionfs_utils.la
%{_libdir}/libunionfs_utils.so
%{_mandir}/man3/*.3*


