from enum import Enum


class MonitorResult(Enum):
    OK = "ok"
    DNS_FAILED = "dns_failed"
    CONNECT_REFUSED = "connect_refused"
    CONNECT_TIMEOUT = "connect_timeout"
    CONNECT_FAILED = "connect_failed"
    TLS_FAILED = "tls_failed"
    TLS_EXPIRING = "tls_expiring"
    STATUS_MISMATCH = "status_mismatch"
    ANSWER_MISMATCH = "answer_mismatch"
    SMTP_REJECTED = "smtp_rejected"
    TARGET_DENIED = "target_denied"
    TIMEOUT = "timeout"
    RULE_MATCHED = "rule_matched"
