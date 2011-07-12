Name:    	igal2
Version: 	2.0
Release: 	%mkrel 1
License: 	GPLv2
Group:		Text tools
URL:		http://igal.trexler.at/
Source0: 	http://igal.trexler.at/%{name}-%{version}.tar.gz
Patch0:		igal2.patch
Summary: 	Easy and flexible online Image GALlery generator
BuildRoot:	%{_temppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%rename igal

Requires: 	perl
Requires:	ImageMagic

%description
Igal2 is a quick, easy and flexible program meant to help you place your
digital images online.  It generates a pretty good-looking set of HTML
slides even with its default settings -- which can otherwise be easily
changed with a good number of command-line options or by altering igal2's
HTML and CSS template files.


%prep
%setup -q
%patch0 -p1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p  %{buildroot}/%{_libdir}/%{name}
mkdir -p  %{buildroot}/%{_docdir}/%{name}

install -p -m 0755 %{name} %{buildroot}/%{_bindir}
install -p -m 0755 utilities/%{name}.sh %{buildroot}/%{_bindir}
install -p -m 0644 %{name}.1 %{buildroot}/%{_mandir}/man1
install -p -m 0644 README ChangeLog %{buildroot}/%{_docdir}/%{name}
install -p -m 0644 indextemplate2.html slidetemplate2.html tile.png igal2.css directoryline2.html %{buildroot}/%{_libdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/%{name}.sh
%{_libdir}/%{name}/*
%{_mandir}/man1/%{name}.1*
%doc README ChangeLog

