%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define alphatag 20060223cvs

Name:           fonttools
Version:        2.0
Release:        0.11.%{alphatag}%{?dist}
Summary:        A tool to convert True/OpenType fonts to XML and back

Group:          Development/Tools
License:        BSD
URL:            http://sourceforge.net/projects/fonttools/
Source0:        http://fonttools.sourceforge.net/cvs-snapshots/bzip2/fonttools-2006-02-23.085153.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch1:         fonttools-uni5.patch

BuildRequires:  python-devel python-numeric
Requires:       python-numeric

Provides:       ttx

%description
TTX/FontTools is a tool for manipulating TrueType and OpenType fonts. It is
written in Python and has a BSD-style, open-source license. TTX can dump
TrueType and OpenType fonts to an XML-based text format and vice versa.


%prep
%setup -q -n %{name}
%patch1 -p1 -b .uni5

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
%{python_sitearch}/FontTools/*.py*
%{python_sitearch}/FontTools/fontTools/*.py*
%{python_sitearch}/FontTools/fontTools/*/*.py*
%{python_sitearch}/FontTools/fontTools/*/*/*.py*
%{python_sitearch}/FontTools/fontTools/misc/eexecOp.so
%{_bindir}/ttx


%changelog
* Sat Dec 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.11.20060223cvs
- Rebuild for Python 2.5

* Fri Dec 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.10.20060223cvs
- Update the Unicode names file to Unicode 5.0.0

* Thu Nov 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.9.20060223cvs
- Update to newer CVS snapshot dated 2006-02-23
- Cleanup based on latest Python packaging guidelines

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.8.20050624cvs
- De-ghost .pyo files

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.7.20050624cvs
- Rebuild to get into Rawhide

* Mon May 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.6.20050624cvs
- Change specification of ulUnicodeRange1-4 to unsigned long

* Mon Feb 13 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.5.20050624cvs
- Rebuild for Fedora Extras 5

* Thu Feb 02 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.4.20050624cvs
- Provide ttx

* Wed Feb 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.3.20050624cvs
- Use upstream snapshots, moving the difference into a patch
- Change alphatag time to the latest change in CVS
- Use %%{python_sitearch} instead of %%{python_sitelib} (for x86_86)
- Use sed instead of a patch to remove shebang

* Sun Jan 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.2.20060103cvs
- Add %%{?dist} tag

* Fri Jan 06 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.1.20060103cvs
- Initial packaging
