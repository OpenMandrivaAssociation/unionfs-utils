%define name		unionfs-utils
%define origname	unionfs_utils
%define version		0.2.1

%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

%define common_description Unionfs is a Stackable Unification File System.

Summary:	Userspace utilities for Unionfs
Name:		%{name}
Version:	%{version}
Release:	%mkrel 3
Source0:	http://download.filesystems.org/unionfs/unionfs-utils-0.x/%{origname}-%{version}.tar.gz
License:	GPL+
Group:		System/Kernel and hardware
URL:		http://unionfs.filesystems.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	autoconf
BuildRequires:	e2fsprogs-devel
Obsoletes:	unionfs-tools
Provides:	unionfs-tools

%description
%{common_description}

This package contains userspace utilities for Unionfs.

%package -n	%{libname}
Summary:	Unionfs utilities library
Group:		System/Libraries

%description -n	%{libname}
%{common_description}

This package contains the library needed to run programs dynamically
linked with Unionfs.

%package -n	%{develname}
Summary:	Development tools for programs using Unionfs
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %name 0 -d}

%description -n	%{develname}
%{common_description}

This package contains the header files and libraries needed for
developing programs using the Unionfs utilities library.

%prep
%setup -q -n %{origname}-%{version}

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

%files -n %{libname}
%{_libdir}/libunionfs_utils.so.%{major}*

%files -n %{develname}
%{_includedir}/unionfs_utils.h
%{_libdir}/libunionfs_utils.*a
%{_libdir}/libunionfs_utils.so
%{_mandir}/man3/*.3*

