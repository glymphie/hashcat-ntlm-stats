from hashcat_ntlm_stats.parser.parse import load_file


def test_file_format():
    assert isinstance(load_file("tests/fixtures/user_hashes.sample.ntds"), list)
