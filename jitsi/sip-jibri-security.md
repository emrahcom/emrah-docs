## Critical

### curl and libcurl4

#### CVE-2023-23914

https://access.redhat.com/security/cve/CVE-2023-23914

A flaw was found in the Curl package, where the HSTS mechanism would be ignored
by subsequent transfers when done on the same command line because the state
would not be properly carried.

**RES**: Curl is only used to send internal requests to Jibri's internal API. It
is not used to fetch external sites. HSTS (HTTP Strict Transport Security)
mechanism is not needed in our case and therefore this issue is not applicable.

### libaom0

#### CVE-2023-6879

https://access.redhat.com/security/cve/CVE-2023-6879

A heap-based buffer overflow vulnerability was found in AOM. When increasing the
resolution of video frames during a multi-threaded encode, a heap overflow may
occur in `av1_loop_restoration_dealloc()` within `thread_common.c`, leading to a
denial of service or unauthorized reading of memory.

**RES**: This package is not installed and it doesn't exists in Debian 12
Bookworm repository. Currently, we provide `sip-jibri` container based on
Debian 12.

### libblas3

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
not vulnerable. `5.3.28+dfsg1-0.8` which is based on `3.28`.
