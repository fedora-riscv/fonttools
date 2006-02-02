%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define alphatag 20050624cvs

Name:           fonttools
Version:        2.0
Release:        0.3.%{alphatag}%{?dist}
Summary:        A tool to convert True/OpenType fonts to XML and back

Group:          Development/Tools
License:        BSD
URL:            http://sourceforge.net/projects/fonttools/
Source0:        http://fonttools.sourceforge.net/cvs-snapshots/bzip2/fonttools-2005-03-15.210812.tar.bz2
Patch1:         fonttools-20050315-20050624.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel python-numeric
Requires:   python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")
Requires:       python-numeric


%description
TTX/FontTools is a tool for manipulating TrueType and OpenType fonts. It is
written in Python and has a BSD-style, open-source license. TTX can dump
TrueType and OpenType fonts to an XML-based text format and vice versa.


%prep
%setup -q -n %{name}
%patch1 -p1 -b .20050624

%{__sed} -i.nobang '1 d' Lib/fontTools/ttx.py
%{__chmod} a-x LICENSE.txt


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{python_sitearch}/FontTools/fontTools/ttLib/test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%doc Doc/bugs.txt Doc/ChangeLog.txt Doc/changes.txt Doc/documentation.html
%{python_sitearch}/FontTools.pth
%dir %{python_sitearch}/FontTools
%dir %{python_sitearch}/FontTools/fontTools
%dir %{python_sitearch}/FontTools/fontTools/encodings
%dir %{python_sitearch}/FontTools/fontTools/misc
%dir %{python_sitearch}/FontTools/fontTools/pens
%dir %{python_sitearch}/FontTools/fontTools/ttLib
%dir %{python_sitearch}/FontTools/fontTools/ttLib/tables
%{python_sitearch}/FontTools/*.py
%{python_sitearch}/FontTools/*.pyc
%ghost %{python_sitearch}/FontTools/*.pyo
%{python_sitearch}/FontTools/fontTools/*.py
%{python_sitearch}/FontTools/fontTools/*.pyc
%ghost %{python_sitearch}/FontTools/fontTools/*.pyo
%{python_sitearch}/FontTools/fontTools/*/*.py
%{python_sitearch}/FontTools/fontTools/*/*.pyc
%ghost %{python_sitearch}/FontTools/fontTools/*/*.pyo
%{python_sitearch}/FontTools/fontTools/*/*/*.py
%{python_sitearch}/FontTools/fontTools/*/*/*.pyc
%ghost %{python_sitearch}/FontTools/fontTools/*/*/*.pyo
%{python_sitearch}/FontTools/fontTools/misc/eexecOp.so
%{_bindir}/ttx


%changelog
* Wed Feb 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.3.20050624cvs
- Use upstream snapshots, moving the difference into a patch
- Change alphatag time to the latest change in CVS
- Use %%{python_sitearch} instead of %%{python_sitelib} (for x86_86)
- Use sed instead of a patch to remove shebang

* Sun Jan 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.2.20060103cvs
- Add %%{?dist} tag

* Fri Jan 06 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.1.20060103cvs
- Initial packaging
