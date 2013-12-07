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
Release:	12
Source0:	http://download.filesystems.org/unionfs/unionfs-utils-0.x/%{origname}-%{version}.tar.gz
Patch0:		unionfs-utils-automake-1.13.patch
License:	GPL+
Group:		System/Kernel and hardware
URL:		http://unionfs.filesystems.org/
BuildRequires:	autoconf
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	libuuid-devel
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
%apply_patches

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

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



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-8mdv2011.0
+ Revision: 670745
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-7mdv2011.0
+ Revision: 608109
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-6mdv2010.1
+ Revision: 520289
- rebuilt for 2010.1

* Sat Oct 03 2009 Funda Wang <fwang@mandriva.org> 0.2.1-5mdv2010.0
+ Revision: 453189
- BR uuid

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 0.2.1-3mdv2009.1
+ Revision: 366392
- autoreconf

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.1-3mdv2009.0
+ Revision: 225899
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-2mdv2008.1
+ Revision: 179670
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 24 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 70785
- streamline file lists and protect against major change
- update URLs
- new devel policy
- spec clean
- new release 0.2.1


* Mon Nov 13 2006 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2007.0
+ Revision: 83729
- BuildRequires e2fsprogs-devel for libuuid
- initial unionfs-utils release
- Create unionfs-utils

