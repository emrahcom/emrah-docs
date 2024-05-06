## Critical

### curl and libcurl4

#### CVE-2023-23914

https://access.redhat.com/security/cve/CVE-2023-23914

A flaw was found in the Curl package, where the HSTS mechanism would be ignored
by subsequent transfers when done on the same command line because the state
would not be properly carried.

**RES**: The installed version is `7.88.1-10+deb12u5` which is not affected.

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

**RES**: This package is not installed and it doesn't exist in Debian 12
Bookworm repository. Currently, we provide `sip-jibri` container based on
Debian 12.

### libblas3 and liblapack3

#### CVE-2021-4048

https://access.redhat.com/errata/RHSA-2022:7639

An out-of-bounds read flaw was found in the CLARRV, DLARRV, SLARRV, and ZLARRV
functions in lapack and OpenBLAS. A specially crafted input passed to these
functions could cause an application using lapack to crash or possibly disclose
portions of its memory.

**RES**:

### libdb5.3

#### CVE-2019-8457

https://access.redhat.com/security/cve/CVE-2019-8457

SQLite3 from 3.6.0 to and including 3.27.2 is vulnerable to heap out-of-bound
read in the rtreenode() function when handling invalid rtree tables.

**RES**: Debian repository contains the newer version of this package which is
not vulnerable. The installed version is `5.3.28+dfsg1-0.8` which is based on
`3.28` of upstream.

### libmysofa1

#### CVE-2021-3756

https://github.com/hoene/libmysofa/pull/166/commits/890400ebd092c574707d0c132124f8ff047e20e1

Heap-based Buffer Overflow

**RES**: This was fixed in version `1.2.1`. The installed package is
`1.3.1~dfsg0-1` and it is not vulnerable.

### nodejs and libnode72

#### CVE-2023-32002

https://access.redhat.com/security/cve/CVE-2023-32002

A vulnerability was found in NodeJS. This security issue occurs as the use of
`Module._load()` can bypass the policy mechanism and require modules outside of
the `policy.json` definition for a given module.

**RES**: `libnode72` is not installed. The installed version of `Node.js`
doesn't use this package. The installed Node.js is `v20.11.1` (_released on Feb
13th, 2024_) which has no known security issue.
