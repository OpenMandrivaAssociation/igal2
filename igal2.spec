%define	oname	igal

Name:		igal2
Version: 	2.0
Release: 	2
License: 	GPLv2
Group:		Text tools
URL:		http://igal.trexler.at/
Source0: 	http://igal.trexler.at/%{name}-%{version}.tar.gz
Patch0:		igal2.patch
Patch1:		igal2-2.0-fix-destdir-and-fhs-paths.patch
Summary: 	Easy and flexible online Image GALlery generator
BuildArch:	noarch

%rename		%{oname}

Requires: 	perl
Requires:	ImageMagick

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

%files
%doc README ChangeLog
%{_bindir}/%{oname}
%{_bindir}/%{name}
%{_bindir}/%{name}.sh
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1*
