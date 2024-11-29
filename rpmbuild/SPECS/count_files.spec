Name:           count_files
Version:        1.0
Release:        1%{?dist}
Summary:        Bash script to count files in /etc

License:        GPLv3+
Source0:        count_files.sh

BuildArch:      noarch
Requires: bash

%description
Simple script.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/count_files.sh

%files
/usr/local/bin/count_files.sh

%changelog
* Wed Nov 27 2024 Anatolii <shektoly@gmail.com> - 1.0-1
- Initial package

