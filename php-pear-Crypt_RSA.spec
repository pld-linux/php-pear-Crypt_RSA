%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	RSA
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides RSA-like encryption support
Summary(pl):	%{_pearname} - dostarcza szyfrowania zbli¿onego do RSA
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1.4
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	222a018dc66509d8b56f444a1ea7874d
URL:		http://pear.php.net/package/Crypt_RSA/
BuildRequires:	rpm-php-pearprov >= 4.4.2-10.2
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to use two-key strong cryptography like RSA
with arbitrary key length. It uses one of the following extensions for
math calculations:
- PECL big_int extension version greater than or equal to 1.0.3
- PHP GMP extension
- PHP BCMath extension

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet pozwala na u¿ycie silnej, zbli¿onej do RSA kryptografii z
u¿yciem dwóch kluczy o dowolnej d³ugo¶ci. Wykorzystuje do tego jedno z
poni¿szych rozszerzeñ PHP do obliczeñ matematycznych
- rozszerzenie PECL big_int w wersji co najmniej 1.0.3
- rozszerzenie PHP GMP
- rozszerzenie PHP BCMath

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/{docs,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
