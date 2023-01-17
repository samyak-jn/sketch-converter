
Name:           sketch-converter
Version:        0.1.0
Release:        1%{?dist}
Summary:        A realtime picture converter that metamorphose real pictures into sketch.
License:        MIT
Url:            https://github.com/samyak-jn/detect
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
	
%description
A realtime picture converter that metamorphose real pictures into sketch.
	
%prep
%autosetup -p1
 
%generate_buildrequires
%pyproject_buildrequires -r
 
%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
 
%files -f %{pyproject_files}
%doc README.md
%doc SECURITY.md
%license LICENSE
%{_bindir}/%{name}
	
%changelog
* Fri Nov 18 2022 <Samyak Jain> <jnsamyak@fedoraproject.org> - 0.1.0-1
- Intial packaging for sketch-converter