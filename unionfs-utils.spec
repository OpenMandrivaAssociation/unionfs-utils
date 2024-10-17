%define origname	unionfs_utils

%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

%define common_description Unionfs is a Stackable Unification File System.

%define _disable_lto 1
%define _disable_rebuild_configure 1

Summary:	Userspace utilities for Unionfs
Name:		unionfs-utils
Version:	0.2.1
Release:	25
Source0:	http://download.filesystems.org/unionfs/unionfs-utils-0.x/%{origname}-%{version}.tar.gz
Patch0:		unionfs-utils-automake-1.13.patch
License:	GPL+
Group:		System/Kernel and hardware
URL:		https://unionfs.filesystems.org/
BuildRequires:	autoconf
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	libuuid-devel
Obsoletes:	unionfs-tools

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
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname %name 0 -d} < %{EVRD}

%description -n	%{develname}
%{common_description}

This package contains the header files and libraries needed for
developing programs using the Unionfs utilities library.

%prep
%setup -q -n %{origname}-%{version}
%autopatch -p1

%build
autoreconf -fi
export CC='gcc -fgnu89-inline'
%configure
%make_build

%install
%make_install

%files
%{_bindir}/union*
%{_mandir}/man8/*.8*

%files -n %{libname}
%{_libdir}/libunionfs_utils.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/unionfs_utils.h
%{_libdir}/libunionfs_utils.so
%{_mandir}/man3/*.3*

