Name: mythes-ne
Summary: Nepali thesaurus
Version: 1.1
Release: 5%{?dist}
Source0: http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/dictionaries/ne_NP/th_ne_NP_v2.zip
Source1: http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/dictionaries/ne_NP/README_th_ne_NP_v2.txt
Group: Applications/Text
URL: http://data.opentaal.org/opentaalbank/thesaurus
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2
BuildArch: noarch
BuildRequires: mythes-devel
Requires: mythes

%description
Nepali thesaurus.

%prep
%setup -q -c
cp -p %{SOURCE1} README_th_ne_NP_v2.txt

%build
th_gen_idx.pl < th_ne_NP_v2.dat > th_ne_NP_v2.idx

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ne_NP_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_ne_NP_v2.txt
%{_datadir}/mythes/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 16 2010 Caolan McNamara <caolanm@redhat.com> - 1.1-1
- initial version
