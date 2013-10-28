Name: brltty
Version: 4.3dev
Release: 1

Group: System Environment/Daemons
License: GPL
Vendor: The BRLTTY Team
Packager: Dave Mielke <dave@mielke.cc>
URL: http://mielke.cc/brltty/
Source: http://mielke.cc/brltty/releases/%{name}-%{version}.tar.gz

BuildRequires: autoconf >= 2.53
BuildRequires: make
BuildRequires: gcc
BuildRequires: /bin/sh
BuildRequires: /bin/ln
BuildRequires: /usr/bin/ld
BuildRequires: /sbin/ldconfig
BuildRequires: /usr/bin/ranlib
BuildRequires: /usr/bin/ar
BuildRequires: /usr/bin/awk
BuildRequires: /usr/bin/bison
BuildRequires: /usr/bin/install
BuildRequires: glibc-devel
BuildRequires: Pyrex
BuildRequires: tcl
BuildRequires: gcc-java

BuildRoot: %{_tmppath}/%{name}-%{version}-InstallRoot
%define _bindir /bin
%define _sbindir /sbin
%define _libdir /lib
%define _sysconfdir /etc

AutoProv: 1

AutoReq: 1
Requires: /bin/sh

Summary: Braille display driver for Linux/Unix.
%description
BRLTTY is a background process (daemon) which provides access to
the console screen (when in text mode) for a blind person using a
refreshable braille display.  It drives the braille display, and
provides complete screen review functionality.  Some speech capability
has also been incorporated.

Install this package if you use a refreshable braille display.

%package -n brlapi
Version: 0.5.5
Group: Applications/System
License: LGPL

AutoProv: 1

AutoReq: 1

Summary: Appliation Programming Interface for BRLTTY.
%description -n brlapi
This package provides the run-time support for the Application
Programming Interface to BRLTTY.

Install this package if you have an application
which directly accesses a refreshable braille display.

%package -n brlapi-caml
Version: 0.5.5
Group: Applications/System
License: LGPL

AutoProv: 1

AutoReq: 1

Summary: Caml bindings for BrlAPI.
%description -n brlapi-caml
This package provides the Caml bindings for BrlAPI,
which is the Application Programming Interface to BRLTTY.

Install this package if you have a Caml application
which directly accesses a refreshable braille display.

%package -n brlapi-java
Version: 0.5.5
Group: Applications/System
License: LGPL

AutoProv: 1

AutoReq: 1

Summary: Java bindings for BrlAPI.
%description -n brlapi-java
This package provides the Java bindings for BrlAPI,
which is the Application Programming Interface to BRLTTY.

Install this package if you have a Java application
which directly accesses a refreshable braille display.

%package -n brlapi-python
Version: 0.5.5
Group: Applications/System
License: LGPL

AutoProv: 1

AutoReq: 1

Summary: Python bindings for BrlAPI.
%description -n brlapi-python
This package provides the Python bindings for BrlAPI,
which is the Application Programming Interface to BRLTTY.

Install this package if you have a Python application
which directly accesses a refreshable braille display.

%package -n brlapi-tcl
Version: 0.5.5
Group: Applications/System
License: LGPL

AutoProv: 1

AutoReq: 1

Summary: Tcl bindings for BrlAPI.
%description -n brlapi-tcl
This package provides the Tcl bindings for BrlAPI,
which is the Application Programming Interface to BRLTTY.

Install this package if you have a Tcl application
which directly accesses a refreshable braille display.

%package -n brlapi-devel
Version: 0.5.5
Group: Development/System
License: LGPL

AutoProv: 1

AutoReq: 1
Requires: brlapi = 0.5.5

Summary: Headers, static archive, and documentation for BrlAPI.
%description -n brlapi-devel
This package provides the header files, static archive, shared object
linker reference, and reference documentation for BrlAPI (the
Application Programming Interface to BRLTTY).  It enables the
implementation of applications which take direct advantage of a
refreshable braille display in order to present information in ways
which are more appropriate for blind users and/or to provide user
interfaces which are more specifically atuned to their needs.

Install this package if you're developing or maintaining an application
which directly accesses a refreshable braille display.

%prep
# %setup -n %{name}-%{version}
%setup -n brltty-4.3dev

%build
%configure --disable-relocatable-install --with-install-root="${RPM_BUILD_ROOT}" --disable-gpm --without-flite --without-mikropuhe --without-swift --without-theta --without-viavoice --without-libbraille --without-curses --with-braille-driver=-tt,-vr,-xw
make

%install
make install install-documents install-messages
install -m 644 Documents/brltty.conf "${RPM_BUILD_ROOT}%{_sysconfdir}"
%find_lang %{name}

%clean
rm -fr "${RPM_BUILD_ROOT}"

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/brltty
%{_bindir}/brltty-*
%{_bindir}/vstp
%{_libdir}/brltty
%{_sysconfdir}/brltty
%doc %{_mandir}/man1/*
%doc %{_docdir}/*/LICENSE*
%doc %{_docdir}/*/README*
%doc %{_docdir}/*/ChangeLog
%doc %{_docdir}/*/CONTRIBUTORS
%doc %{_docdir}/*/TODO
%doc %{_docdir}/*/brltty.conf
%doc %{_docdir}/*/KeyTables
%doc %{_docdir}/*/Manual-BRLTTY
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/brltty.conf

%files -n brlapi
%defattr(-,root,root)
%{_libdir}/libbrlapi.so.*
%{_bindir}/xbrlapi
%doc %{_docdir}/*/Manual-BrlAPI

%files -n brlapi-caml
/brlapi

%files -n brlapi-java
/usr/share/java/*
/*

%files -n brlapi-python
/usr/lib/python2.7/dist-packages/[bB]rlapi[-.]*

%files -n brlapi-tcl
TCL_PACKAGES_DIRECTORY_NOT_FOUND_BY_CONFIGURE/brlapi-0.5.5/libbrlapi_tcl.so
TCL_PACKAGES_DIRECTORY_NOT_FOUND_BY_CONFIGURE/brlapi-0.5.5/pkgIndex.tcl

%files -n brlapi-devel
%defattr(-,root,root)
%{_libdir}/libbrlapi.a
%{_libdir}/libbrlapi.so
%{_includedir}/brlapi.h
%{_includedir}/brlapi_*.h
%{_includedir}/brltty
%doc %{_mandir}/man3/*
%doc %{_docdir}/*/BrlAPIref

%changelog
* Mon Oct 10 2011 Dave Mielke <dave@mielke.cc> 4.3
+  New options:
      The -F [--speech-fifo=] option has been renamed to -i [--speech-input=].
      The -F [--preferences-file=] option sets the path to the preferences file.
      The -L [--log-file=] brltty option writes timestamped logs to a file.
      The -q [--quiet] xbrlapi option suppresses the displaying of window titles.
      The -r [--reformat-text] ctbtest option joins unindented input lines.
      The log level can now be specified within brltty.conf.
+  New device support:
      A braille driver for BrailComm displays has been added.
      The HandyTech braille driver now supports the Active Braille.
      The Voyager braille driver now supports the part 232 serial adapter.
      The Voyager braille driver now supports the Braille Pen (aka Easy Link).
+  Preferences menu changes:
      The preference selections now apply to the preferences menu itself, too.
      Keyboard key bindings now work correctly within the preferences menu.
      The "Text Style" preference has new settings:
         8-Dot Computer Braille (formerly 8-dot)
         Contracted Braille (formerly 6-dot)
         6-Dot Computer Braille
      The "Expand Current Word" preference has been added.
         It's only visible if "Text Style" is set to "Contracted Braille".
         It can be set to:
            Yes (don't contract the word the cursor is on)
            No (contract the whole line)
      The "Capitalization Mode" preference has been added.
         It's only visible if "Text Style" is set to "Contracted Braille".
         It can be set to:
            No Capitalization
            Use Capital Sign
            Superimpose Dot 7
+  General changes:
      Internationalization support has been improved.
      French and German translations have been added.
      Support for multi-byte local character sets has been improved.
      Horizontal window motions now work correctly with contracted braille.
      The half window left motion no longer can move to a bad location.
      Alert messages no longer disappear unexpectedly.
      The speech FIFO is now created relative to the current working directory.
      Serial flow control is now enabled before device probing.
      The following global variables for use within tables are now predefined:
         tablesDirectory
         tableExtension
         subtableExtension
+  Alva braille driver changes:
      The BC key bindings have been changed significantly in order to add
      more functions and to support the USB640 (which has no smartpad).
      The braille keyboard of the BC Feature Pack is now supported.
+  Baum braille driver changes:
      Updating the text and status cells of the Vario 80 has been fixed.
      The front and command keys of the Vario 80 are now supported.
+  EuroBraille braille driver changes:
      Reading keys is faster and no longer generates spurious input errors.
+  HandyTech braille driver changes:
      Support for the Active Braille has been added.
      The help screen now describes how the keypad keys are named.
+  Papenmeier braille driver changes:
      The initial state of the switches and keys of EL models is detected.
+  Seika braille driver changes:
      The help screen now describes the key layout.
+  TTY braille driver changes:
      A few more key bindings have been defined.
+  Voyager braille driver changes:
      Serial support has been added.
      Bluetooth support has been added.
      Support for the part 232 serial adapter has been added.
      Support for the Braille Pen (aka Easy Link) has been added.
+  XWindow braille driver changes:
      More and less restrictive fonts are supported.
      Hard program exits have been removed.
+  eSpeak speech driver changes:
      The full advertized speech rate range can now be used.
+  FestivalLite speech driver changes:
      The default voice has been changed to kal (from kal16).
+  AtSpi screen driver changes:
      No more annoying warnings when not on an AtSpi widget.
+  BrlAPI fixes:
      ISO-8859-1 is now accepted as a character set when iconv isn't available.
      The autorepeat flags are now handled on a per session basis.
      Commands are now processed when the device is released.
+  WindowEyes BrlAPI driver changes:
      Testing for BrlAPI open errors has been improved.
+  Text table changes:
      A common subtable for the block characters has been added.
      The glyph directive has been added.
      Several alternate fonts for the Latin letters are now defined.
      If a character isn't defined then check for an alternative which is:
         (its Unicode base character, its iconv-defined ASCII equivalent, etc).
      The en_UK text table has been renamed to en_GB (to comply with ISO 3166).
      Updated text tables:
         bo (Tibetan)
         brf: dot 7 is no longer presented
         fr_FR (French France)
         fr-vs (French table used by VisioBraille devices)
         is (Icelandic): updated to the newly adopted standard
+  Contraction table changes:
      If a zero-width character isn't defined then don't show it.
      Updated tables:
         de-kurzschrift (German)
         en-us-g2 (American English)
         es (Spanish)
         fr-abrege (French)
         zh-tw (Taiwanese Chinese)
+  Key table changes:
      A specific key within a set can now be specified by number.
      A key combination can now include specific keys which aren't in set 0.
      Keys which aren't in set 0 can now be mapped to keyboard functions.
      A key set name can now be used to define a hotkey.
      The help text no longer includes hidden hotkeys.
      The help text now handles context-specific hotkeys correctly.
      The note directive now supports the use of variables.
+  Windows changes:
      Serial devices beyond COM9 may now be specified.
      The WindowEyes driver is now copied into the correct installation directory.
+  Build changes:
      Building an exported (not checked out) copy now "knows" its revision number.
      Make support for install/uninstall of /usr/share/doc/brltty has been added.
      The make targets for source archives are now prefixed with "src-".
      The bin-tar, bin-tar-gzip, and bin-tar-bzip2 make targets have been added.
      Support for xz compression of binary and source archives has been added.
      The preferences file has been moved to /var/lib/brltty/brltty.prefs.
      There's now only one preferences file (instead of one per braille driver).
      The preferences file is now text-based (instead of binary).
      The "writable" directory has been moved to /var/run/brltty.
      The "library" directory is now known as the "drivers" directory.
      The "data" directory no longer has a use and has been removed.
      Support for the "gjar" command has been added.

