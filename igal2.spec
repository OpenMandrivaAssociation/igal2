%define	oname	igal

Name:		igal2
Version:	2.1
Release:	3
License:	GPLv2+
Group:		Text tools
URL:		https://igal.trexler.at/
Source0:	http://igal.trexler.at/%{name}-%{version}.tar.gz
Patch0:		igal2.patch
Patch1:		igal2-2.0-fix-destdir-and-fhs-paths.patch
Summary:	Easy and flexible online Image GALlery generator
BuildArch:	noarch

%rename		%{oname}

Requires:	perl
Requires:	imagemagick

%description
Igal2 is a quick, easy and flexible program meant to help you place your
digital images online. It generates a pretty good-looking set of HTML
slides even with its default settings -- which can otherwise be easily
changed with a good number of command-line options or by altering igal2's
HTML and CSS template files.


%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .fhs~

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/%{name}/{README,ChangeLog,COPYING}
install -m 755 utilities/igal2-recursive.sh %{buildroot}%{_bindir}

%files
%doc ChangeLog
%{_bindir}/%{oname}
%{_bindir}/%{name}
%{_bindir}/%{name}.sh
%{_bindir}/%{name}-recursive.sh
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jul 01 2012 Johnny A. Solbu <solbu@mandriva.org> 2.1-1
+ Revision: 807659
- New version
- Spec cleanup
- Fix licence
- Fix mixed-use-of-spaces-and-tabs
- README contains install instruction, so we'll drop it.
- Docs are installed in the wrong place, moving to correct location

* Tue Jul 12 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0-2
+ Revision: 689759
- fix DESTDIR support and FHS compliance in Makefile (P1)

  + Johnny A. Solbu <solbu@mandriva.org>
    - More spec cleanup
    - Imported package
    - Spec cleanup
    - import igal2

