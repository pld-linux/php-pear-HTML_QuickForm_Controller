%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Controller

Summary:	%{_pearname} - add-on to HTML_QuickForm that allows building of multiple forms 
Summary(pl):	%{_pearname} - dodatek do HTML_QuickForm umo�liwiaj�cy budowanie wielu formularzy
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	06cadeca9a7abe41c0af86ba713bd381
URL:		http://pear.php.net/package/HTML_QuickForm_Controller/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is essentially an implementation of a PageController
pattern. 

Architecture:
- Controller class that examines HTTP requests and manages form values
  persistance across requests.
- Page class (subclass of QuickForm) representing a single page of the
  form.
- Business logic is contained in subclasses of Action class.

Cool features:
- Includes several default actions that allows easy building of
  multipage forms.
- Includes usage examples for common usage cases (single-page form,
  wizard tabbed form).

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet jest implementacj� szablonu PageController.

Architektura:
- Klasa Controller badaj�ca zapytania HTTP i zarz�dzaj�ca warto�ciami
  formularza pomi�dzy kolejnymi zapytaniami.
- Klasa Page (podklasa QuickForm) reprezentuj�ca pojedyncz� stron�
  formularza.
- Logika biznesowa zawarta jest w podklasach klasy Action.

Ciekawe cechy:
- Zawiera kilka domy�lnych akcji pozwalaj�cych na �atwe budowanie
  formularzy rozbitych na kilka stron.
- Zawiera gotowe przyk�ady najcz�ciej spotykanych zastosowa�.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Action

install %{_pearname}-%{version}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Action/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Action

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/%{_subclass}
