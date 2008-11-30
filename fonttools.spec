%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           fonttools
Version:        2.2
Release:        3%{?dist}
Summary:        A tool to convert True/OpenType fonts to XML and back

Group:          Development/Tools
License:        BSD
URL:            http://sourceforge.net/projects/%{name}/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel python-numeric
Requires:       python-numeric

Provides:       ttx = %{version}-%{release}

%description
TTX/FontTools is a tool for manipulating TrueType and OpenType fonts. It is
written in Python and has a BSD-style, open-source license. TTX can dump
TrueType and OpenType fonts to an XML-based text format and vice versa.


%prep
%setup -q

%{__sed} -i.nobang '1 d' Lib/fontTools/ttx.py
%{__chmod} a-x LICENSE.txt


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{python_sitearch}/FontTools/fontTools/ttLib/test
chmod 0755 $RPM_BUILD_ROOT%{python_sitearch}/FontTools/fontTools/misc/eexecOp.so
mkdir -p -m 0755 ${RPM_BUILD_ROOT}%{_mandir}/man1
mv $RPM_BUILD_ROOT/usr/man/man1/ttx.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%doc Doc/ChangeLog.txt Doc/changes.txt Doc/documentation.html
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
%{python_sitearch}/FontTools/fonttools-%{version}-py?.?.egg-info
%{_bindir}/ttx
%{_mandir}/man1/ttx.1.gz



%changelog
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2-3
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2-2
- Rebuild for Python 2.6

* Tue Sep 16 2008 Matt Domsch <mdomsch@fedoraproject.org> - 2.2-1
- update to 2.2, drop upstreamed patch, fix FTBFS BZ#434409

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0-0.12.20060223cvs
- Autorebuild for GCC 4.3

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
