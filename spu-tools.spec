Summary: user space tools for Cell/B.E.
Name: spu-tools
Version: 1.1
Release: 6
License: GPL
Group: Applications/System
Source0: spu-tools.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: ncurses
BuildRequires: help2man
%define _prefix /usr

%description
The spu-tools package contains user space tools for Cell/B.E.
Currently, it contain two tools:
- spu-top: a tool like top to watch the SPU's on a Cell BE
System. It shows information about SPUs and running SPU contexts.
- spu-ps: a tool like ps, which dumps a report on the currently
running SPU contexts.

%prep
%setup -c -q

%build
cd src/
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd src/
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /%{_prefix}/bin/spu-top
%dir /%{_prefix}/bin/spu-ps
%dir /%{_prefix}/share/man/man1/spu-top.1.gz
%dir /%{_prefix}/share/man/man1/spu-ps.1.gz

%changelog
* Tue Sep 02 2008  Andre Detsch <adetsch@br.ibm.com> 1.1-6
- Enhanced PID retrieval.

* Fri Jul 04 2008  Andre Detsch <adetsch@br.ibm.com> 1.1-5
- Support for spu threads with arbitrary spufs entry names.

* Wed May 28 2008  Andre Detsch <adetsch@br.ibm.com> 1.1-4
- Added TID field to SPU view of spu-top.

* Fri Apr 11 2008  Andre Detsch <adetsch@br.ibm.com> 1.1-3
- Fix escape sequences handling on spu-top.
- Fixed help example for spu-ps.

* Tue Mar 18 2008 Andre Detsch <adetsch@br.ibm.com> 1.1-2
- Fixed load averange printing.

* Thu Mar 13 2008 Andre Detsch <adetsch@br.ibm.com> 1.1-1
- Making Per-Process view explanation a bit clearer.
- Additional space for some spu statistics.

* Thu Jun 14 2007  Andre Detsch <adetsch@br.ibm.com> 1.0-2
- Setting BuildRoot at spec file.
- General fixes (src/ChangeLog)

* Tue May 29 2007  Andre Detsch <adetsch@br.ibm.com> 1.0
- Package rename: spu-top to spu-tools.
- Complete rewrite for Cell SDK 3.0.

* Tue Apr 03 2007  Markus Deuling <deuling@de.ibm.com> 0.2
- Seperate Process info and IRQ stats.
- Use ncurses library.
- Retrieve number of CPUs in the system.
- Remove valid flag.

* Tue Mar 13 2007  Markus Deuling <deuling@de.ibm.com> 0.1
- Initial version.
