Summary:	WMfmixer is a simple mixer application for WindowMaker
Summary(pl):	Prosty program do obs³ugi d¼wiêku w WindowMakerze
Name:		wmfmixer
Version:	0.1
Release:	1
License:	GPL
Vendor:		Dimitry Fink <finik@sporu.net>
Group:		X11/Applications/Multimedia
Source0:	http://www.finik.net/files/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.finik.net/software.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_xbindir	%{_prefix}/bin

%description
WMfmixer is a simple dockable program for controlling /dev/mixer
device. It's simplicity is no doubt his good point.

%description -l pl
WMfmixer jest prostym dokowalnym programem do kontroli nad urz±dzeniem
/dev/mixer. Niew±tpliw± zalet± tej aplikacji jest jej prostota.

%prep
%setup -qn %{name}-%{version}

%build
OPTFLAGS="%{rpmcflags}" CC="%{__cc}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xbindir},%{_pixmapsdir},%{_applnkdir}/Multimedia}

install wmfmixer $RPM_BUILD_ROOT%{_xbindir}/wmfmixer
install wmfmixer.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/wmfmixer.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HINTS
%attr (755,root,root)%{_xbindir}/wmfmixer
%{_applnkdir}/Multimedia/wmfmixer.desktop
%{_pixmapsdir}/wmfmixer.xpm
