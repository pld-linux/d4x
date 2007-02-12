%define		beta	rc2
Summary:	Downloader for X - ftp/http download manager for X window system
Summary(pl.UTF-8):	Program do pobierania plików poprzez ftp/http dla X, czyli Downloader for X
Name:		d4x
Version:	2.5.0
Release:	0.%{beta}.3
License:	Artistic
Group:		X11/Applications/Networking
Source0:	http://www.krasu.ru/soft/chuchelo/files/%{name}-%{version}%{beta}.tar.gz
# Source0-md5:	73b880b3c4e8a6e05bb88f9eac3e7bb4
Patch0:		%{name}-elif_fix.patch
Patch1:		%{name}-configure_in.patch
Patch2:		%{name}-Makefile.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-configure.patch
Patch5:		%{name}-gtk24.patch
URL:		http://www.krasu.ru/soft/chuchelo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libao-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Obsoletes:	nt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program lets you download files from internet/intranet using FTP
or HTTP protocol. Main features:
- multithreaded design
- convenient user-friendly interface
- automatic resuming after connection breaks
- multiple simultaneous downloads
- recursive FTP and HTTP downloading
- ability to change links in HTML file for offline browsing
- wildcards support for FTP recursing
- filters support for HTTP recursing
- proxy support (FTP and HTTP)
- supports for traffic limitation
- mass downloading function
- FTP search
- build-in scheduler
- and many many other...

%description -l pl.UTF-8
Program pozwalający na pobieranie plików z internetu/intranetu za
pomocą protokołów FTP lub HTTP. Możliwości:
- wielowątkowa budowa
- przyjazny interfejs użytkownika
- automatyczne wznawianie po przerwaniu połączenia
- jednoczesne pobieranie kilku plików
- rekursywne pobieranie
- możliwość zmiany odnośników w plikach HTML do przeglądania offline
- możliwość stosowania znaków wieloznacznych dla FTP
- możliwość stosowania filtrów dla HTTP
- obsługa proxy
- obsługa ograniczenia ruchu
- funkcja zmasowanego pobierania
- wyszukiwanie FTP
- wbudowany harmonogram
- i wiele innych...

%prep
%setup -q -n %{name}-%{version}%{beta}
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I admin -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install share/nt.desktop $RPM_BUILD_ROOT%{_desktopdir}
install share/{*.xpm,*.png} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f DOC/FAQ.gr DOC/FAQ.el
mv -f DOC/README.gr DOC/README.el

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog* TODO PLANS NEWS DOC/{FAQ*,LICENSE,THANKS,TROUBLES,README*}
%lang(de) %doc DOC/{FAQ,README}.de
%lang(es) %doc DOC/{FAQ,README}.es
%lang(fr) %doc DOC/FAQ.fr
%lang(el) %doc DOC/{FAQ,README}.el
%lang(pl) %doc DOC/README.pl
%lang(pt_BR) %doc DOC/README.pt_BR
%lang(ru) %doc DOC/README.ru

%attr(755,root,root) %{_bindir}/nt
%attr(755,root,root) %{_bindir}/d4x
%dir %{_datadir}/d4x
%{_datadir}/d4x/sounds
%{_datadir}/d4x/themes
%{_datadir}/d4x/ftpsearch.xml
%{_mandir}/man1/*
%{_desktopdir}/nt.desktop
%{_pixmapsdir}/*
