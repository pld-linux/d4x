
Summary:	Downloader for X - ftp/http download manager for X window system
Summary(pl):	Program do pobierania plików poprzez ftp/http dla X, czyli Downloader for X
Name:		d4x
Version:	2.4.1
Release:	1
License:	Artistic
Group:		X11/Applications/Networking
Source0:	http://www.krasu.ru/soft/chuchelo/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-elif_fix.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-configure_in.patch
Patch3:		%{name}-Makefile.patch
Patch4:		%{name}-desktop.patch
URL:		http://www.krasu.ru/soft/chuchelo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libao-devel
BuildRequires:	libstdc++-devel
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

%description -l pl
Program pozwalaj±cy na pobieranie plików z internetu/intranetu za
pomoc± protoko³ów FTP lub HTTP Mo¿liwo¶ci:
    - wielow±tkowa budowa
    - przyjazny interfejs u¿ytkownika
    - automatyczne wznawianie po przerwaniu po³±czenia
    - jednoczesne pobieranie kilku plików
    - rekursywne pobieranie
    - mo¿liwo¶æ zmiany odno¶ników w plikach HTML do przegl±dania offline
    - mo¿liwo¶æ stosowania znaków wieloznacznych dla FTP
    - mo¿liwo¶æ stosowania filtrów dla HTTP
    - obs³uga proxy
    - obs³uga ograniczenia ruchu
    - funkcja zmasowanego pobierania
    - wyszukiwanie FTP
    - wbudowany harmonogram
    - i wiele innych...

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I admin
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/applications,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install share/nt.desktop $RPM_BUILD_ROOT%{_datadir}/applications
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
%{_mandir}/man1/*
%{_datadir}/applications/nt.desktop
%{_pixmapsdir}/*
%{_datadir}/d4x/sounds/*
%{_datadir}/d4x/themes/*
%{_datadir}/d4x/ftpsearch.xml
