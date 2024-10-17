%define oname prawn

Summary:    A fast and nimble PDF generator for Ruby
Name:       rubygem-%{oname}
Version:    0.8.4
Release:    2
Group:      Development/Ruby
License:    Ruby or GPLv2
URL:        https://wiki.github.com/sandal/prawn
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(prawn-core) >= 0.8.4
Requires:   rubygem(prawn-core) < 0.9
Requires:   rubygem(prawn-layout) >= 0.8.4
Requires:   rubygem(prawn-layout) < 0.9
Requires:   rubygem(prawn-security) >= 0.8.4
Requires:   rubygem(prawn-security) < 0.9
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Prawn is a fast, tiny, and nimble PDF generator for Ruby

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 584392
- import rubygem-prawn

