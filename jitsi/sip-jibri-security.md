## Critical

### curl and libcurl4

#### CVE-2023-23914

https://access.redhat.com/security/cve/CVE-2023-23914

A flaw was found in the Curl package, where the HSTS mechanism would be ignored
by subsequent transfers when done on the same command line because the state
would not be properly carried.

**RES**: https://security-tracker.debian.org/tracker/CVE-2023-23914

The installed version is `7.88.1-10+deb12u5` which is not affected.

- Affected versions: `7.77.0` to and including `7.87`
- Not affected versions: < `7.77.0` and >= `7.88.0`

Curl is only used to send internal requests to Jibri's internal API. It is not
used to fetch external sites. HSTS (HTTP Strict Transport Security) mechanism is
not needed in our case.

### libaom0

#### CVE-2023-6879

https://access.redhat.com/security/cve/CVE-2023-6879

A heap-based buffer overflow vulnerability was found in AOM. When increasing the
resolution of video frames during a multi-threaded encode, a heap overflow may
occur in `av1_loop_restoration_dealloc()` within `thread_common.c`, leading to a
denial of service or unauthorized reading of memory.

**RES**: https://security-tracker.debian.org/tracker/CVE-2023-6879

This package is not installed and it doesn't exist in Debian 12 Bookworm
repository. Currently, we provide `sip-jibri` container based on Debian 12.

### libblas3 and liblapack3

#### CVE-2021-4048

https://access.redhat.com/errata/RHSA-2022:7639

An out-of-bounds read flaw was found in the CLARRV, DLARRV, SLARRV, and ZLARRV
functions in lapack and OpenBLAS. A specially crafted input passed to these
functions could cause an application using lapack to crash or possibly disclose
portions of its memory.

**RES**: https://security-tracker.debian.org/tracker/CVE-2021-4048

The installed packages are not vulnerable.

### libdb5.3

#### CVE-2019-8457

https://access.redhat.com/security/cve/CVE-2019-8457

SQLite3 from 3.6.0 to and including 3.27.2 is vulnerable to heap out-of-bound
read in the rtreenode() function when handling invalid rtree tables.

**RES**: https://security-tracker.debian.org/tracker/CVE-2019-8457

Debian repository contains the newer version of this package which is not
vulnerable. The installed version is `5.3.28+dfsg1-0.8` which is based on `3.28`
of upstream.

### libmysofa1

#### CVE-2021-3756

https://github.com/hoene/libmysofa/pull/166/commits/890400ebd092c574707d0c132124f8ff047e20e1

Heap-based Buffer Overflow

**RES**: https://security-tracker.debian.org/tracker/CVE-2021-3756

This was fixed in version `1.2.1`. The installed package is `1.3.1~dfsg0-1` and
it is not vulnerable.

### nodejs and libnode72

#### CVE-2023-32002

https://access.redhat.com/security/cve/CVE-2023-32002

A vulnerability was found in NodeJS. This security issue occurs as the use of
`Module._load()` can bypass the policy mechanism and require modules outside of
the `policy.json` definition for a given module.

**RES**: This package comes from the official Node.js repository.

`libnode72` is not installed. The installed Node.js is `v20.11.1` (_released on
Feb 13th, 2024_) which has no known security issue.

### xserver-common, xserver-xorg-core

#### CVE-2023-6816

https://www.openwall.com/lists/oss-security/2024/01/18/1

Both DeviceFocusEvent and the XIQueryPointer reply contain a bit for each
logical button currently down. Buttons can be arbitrarily mapped to any value up
to 255 but the X.Org Server was only allocating space for the device's number of
buttons, leading to a heap overflow if a bigger value was used.

**RES**: https://security-tracker.debian.org/tracker/CVE-2023-6816

The installed version (`2:21.1.7-3+deb12u7`) is not vulnerable.

### zlib1g

#### CVE-2023-45853

https://www.openwall.com/lists/oss-security/2023/10/20/9

MiniZip in zlib through 1.3 has an integer overflow and resultant heap-based
buffer overflow in zipOpenNewFileInZip4_64 via a long filename, comment, or
extra field.

**RES**: https://security-tracker.debian.org/tracker/CVE-2023-45853

This is not applicable since there is no binary affected by this issue in the
provided container. See
https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1054290 for more details.

## High

### bash CVE-2022-3715

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-3715

### bsdutils CVE-2024-28085

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-28085

### curl CVE-2022-42916

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-42916

### curl CVE-2022-43551

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-43551

### curl CVE-2024-2398

**Not fixed but not applicable**

It works only when an application tells libcurl it wants to allow HTTP/2 server
push, and the amount of received headers for the push surpasses the maximum
allowed limit (1000).

There is no such application in the container and curl is only used for internal
API service.

https://security-tracker.debian.org/tracker/CVE-2024-2398

### e2fsprogs CVE-2022-1304

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-1304

### ffmpeg CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libaom0 CVE-2020-0478

**This package is not installed**

### libavcodec58 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libavcodec58 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libavdevice58 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libavfilter7 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libavformat58 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libavresample4 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libavutil56 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434

### libblkid1 CVE-2024-28085

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-28085

### libc-bin CVE-2024-2961

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-2961

### libc6 CVE-2024-2961

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-2961

### libcaca0 CVE-2021-30498

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2021-30498

### libcaca0 CVE-2021-30499

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2021-30499

### libcap2 CVE-2023-2603

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2023-2603

### libcom-err2 CVE-2022-1304

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-1304

### libcurl4 CVE-2022-42916

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-42916

### libcurl4 CVE-2022-43551

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-43551

### libcurl4 CVE-2024-2398

**Not fixed but not applicable**

It works only when an application tells libcurl it wants to allow HTTP/2 server
push, and the amount of received headers for the push surpasses the maximum
allowed limit (1000).

There is no such application in the container and curl is only used for internal
API service.

https://security-tracker.debian.org/tracker/CVE-2024-2398

### libexpat1 CVE-2023-52425

**Not fixed but not applicable**

It works only when parsing a large token that requires multiple buffer fills to
complete, Expat has to re-parse the token from start numerous times. This
process may trigger excessive resource consumption, leading to a denial of
service.

The service requests the token from known, trusted location (Booking Portal) in
our case. People cannot send a token directly to the service.

It is marked as "moderated" in Red Hat database.

https://security-tracker.debian.org/tracker/CVE-2023-52425
https://access.redhat.com/security/cve/CVE-2023-52425

### libext2fs2 CVE-2022-1304

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-1304

### libgcrypt20 CVE-2021-33560

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2021-33560

### libgdk-pixbuf-2.0-0, libgdk-pixbuf2.0-common CVE-2022-48622

**Not fixed but not applicable**

In GNOME GdkPixbuf (aka gdk-pixbuf) through 2.42.10, the ANI (Windows animated
cursor) decoder encounters heap memory corruption (in `ani_load_chunk` in
io-ani.c) when parsing chunks in a crafted .ani file. A crafted file could allow
an attacker to overwrite heap metadata, leading to a denial of service or code
execution attack.

There is no .ani file or animated cursor in our case.

https://security-tracker.debian.org/tracker/CVE-2022-48622

### libglib2.0-0 CVE-2023-29499

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2023-29499

### libgnutls30 CVE-2024-0553

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-0553

### libgnutls30 CVE-2024-0567

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-0567

### libgssapi-krb5-2, libk5crypto3, libkrb5-3, libkrb5support0 CVE-2024-26462

**Not fixed but not applicable**

Kerberos 5 (aka krb5) 1.21.2 contains a memory leak vulnerability.

This package is installed because of multiple dependencies but Kerberos is no
used in anywhere in SIP-Jibri.

It is marked as "moderated" in Red Hat database.

https://security-tracker.debian.org/tracker/CVE-2024-26462
https://access.redhat.com/security/cve/CVE-2024-26462

### libharfbuzz0b CVE-2023-25193

**Not fixed but not applicable**

A vulnerability was found HarfBuzz. This flaw allows attackers to trigger O(n^2)
growth via consecutive marks during the process of looking back for base glyphs
when attaching marks.

An application prepared by an attacker must be installed inside the container to
exploid this issue.

It is marked as "moderated" in Red Hat database. It is marked as "minor issue"
in Debian database.

https://security-tracker.debian.org/tracker/CVE-2023-25193
https://access.redhat.com/security/cve/CVE-2023-25193

### libimlib2 CVE-2024-25447

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-25447

### libimlib2 CVE-2024-25448

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-25448

### libimlib2 CVE-2024-25450

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-25450

### libldap-2.4-2, libldap-2.5-0 CVE-2023-2953

**Not fixed but not applicable**

A vulnerability was found in openldap. This security flaw causes a null pointer
dereference in `ber_memalloc_x()` function.

This package is installed because of multiple dependencies but `openldap` is not
used anywhere in SIP-Jibri.

https://security-tracker.debian.org/tracker/CVE-2023-2953

### libmount1 CVE-2024-28085

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2024-28085

### libnode72 CVE-2023-30581, CVE-2023-30589, CVE-2023-30590, CVE-2023-32006

**This package is not installed**

### libnode72 CVE-2023-32559, CVE-2024-22019, CVE-2024-27983

**This package is not installed**

### libnss3 CVE-2024-0743

**Not fixed but not applicable**

An unchecked return value in TLS handshake code could have caused a potentially
exploitable crash. This vulnerability affects Firefox < 122, Firefox ESR <
115.9, and Thunderbird < 115.9.

This package is installed because of multiple dependencies but it is not
exploidable since `Firefox` or `Thunderbird` are not installed in SIP-Jibri.

https://security-tracker.debian.org/tracker/CVE-2024-0743

### libopenjp2-7 CVE-2021-3575

**Not fixed but not applicable**

A heap-based buffer overflow was found in openjpeg in `color.c:379:42` in
`sycc420_to_rgb` when decompressing a crafted .j2k file. An attacker could use
this to execute arbitrary code with the permissions of the application compiled
against openjpeg.

There must a crafted application by an attacker inside the container to exploid
it.

It is marked as "medium" in Red Hat database. It is marked as "minor issue" in
Debian database.

https://security-tracker.debian.org/tracker/CVE-2021-3575

### libpam-systemd CVE-2023-50387

**Not fixed but not applicable**

Certain DNSSEC aspects of the DNS protocol (in RFC 4033, 4034, 4035, 6840, and
related RFCs) allow remote attackers to cause a denial of service (CPU
consumption) via one or more DNSSEC responses, aka the "KeyTrap" issue.

DNSSEC is disabled by default in `systemd-resolved` and `systemd-resolved`
doesn't run in the container.

https://security-tracker.debian.org/tracker/CVE-2023-50387

### libpam-systemd CVE-2023-50868

**Not fixed but not applicable**

The Closest Encloser Proof aspect of the DNS protocol (in RFC 5155 when RFC 9276
guidance is skipped) allows remote attackers to cause a denial of service (CPU
consumption for SHA-1 computations) via DNSSEC responses in a random subdomain
attack, aka the "NSEC3" issue.

DNSSEC is disabled by default in `systemd-resolved` and `systemd-resolved`
doesn't run in the container.

https://security-tracker.debian.org/tracker/CVE-2023-50868

### libpostproc55 CVE-2022-48434

**Not vulnerable for the installed version**

https://security-tracker.debian.org/tracker/CVE-2022-48434
