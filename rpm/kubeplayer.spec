# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

# Generated by obs-generator version 0.4
#
# Copyright (c) 2010 Robert Riemann <rriemann@physik.hu-berlin.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# norootforbuild


Name:           kubeplayer
License:        GPL
Url:            http://projects.kde.org/projects/playground/multimedia/kubeplayer
Group:          System/GUI/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Multiplatform online video player
Version:        1.2
Release:        1
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?fedora}
BuildRequires:  kdelibs-devel
Requires:       korundum rubygems
%endif

%if 0%{?suse_version}
BuildRequires:  libkde4-devel
Requires:       ruby-kde4 rubygems rubygem-json
%endif


%description
Multiplatform online video player


Author(s):
  Robert Riemann <saloution@googlemail.com>


%prep
%setup -q

%if 0%{?fedora}
# mkdir $RPM_BUILD_ROOT/build
%endif

%build
%if 0%{?suse_version}
  %cmake_kde4 -d build
%endif
%if 0%{?fedora}
  %cmake_kde4
%endif
  %make_jobs

%install
%if 0%{?suse_version}
  %kde4_makeinstall -C build
%endif
%if 0%{?fedora}
  %kde4_makeinstall
%endif
  %suse_update_desktop_file kubeplayer
  %kde_post_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.rdoc
%if 0%{?suse_version}
%{_kde4_applicationsdir}/kubeplayer.desktop
%endif
%if 0%{?fedora}
%{_kde4_datadir}/applications/kde4/kubeplayer.desktop
%endif
%dir %{_kde4_appsdir}/kubeplayer
%{_kde4_appsdir}/kubeplayer/lib
%{_kde4_bindir}/kubeplayer
%{_kde4_iconsdir}/hicolor/*/apps/kubeplayer.png

%changelog
