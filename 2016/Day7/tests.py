import pytest
from IP import IPAddresses

test_data = [("test1.txt",2)]
test_data2 = [("test2.txt",3)]

@pytest.mark.parametrize("filename,supports_tls",test_data)
def test_supports_tls(filename,supports_tls):
    ips = IPAddresses(filename)
    assert(ips.supports_tls() == supports_tls)

@pytest.mark.parametrize("filename,supports_ssl",test_data2)
def test_supports_ssl(filename,supports_ssl):
    ips = IPAddresses(filename)
    assert(ips.supports_ssl() == supports_ssl)